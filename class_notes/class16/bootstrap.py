# -*- coding: utf-8 -*-

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score, RepeatedKFold

filip_csv_path = Path("../../data/nist/filip.csv")
filip_df = pd.read_csv(filip_csv_path)
filip_df_poly = filip_df.copy()

for n in np.arange(2, 16):
    filip_df_poly[f"x**{n}"] = filip_df_poly["x"] ** n

lm = LinearRegression()

independent_var = "y"
dependent_vars = ["x"]

filip_poly_cv_scores = {
    "n": [],
    "mse_trace": [],
    "mse_mean": [],
    "mse_sd": [],
    "r**2_trace": [],
    "r**2_mean": [],
    "r**2_sd": [],
}

for n in range(1, 16):
    if n > 1:
        dependent_vars.append(f"x**{n}")
        
    rkf = RepeatedKFold(
        n_splits=10,
        n_repeats=100,
        random_state=int(np.round(np.random.uniform(0, 2**31), decimals=0)),
    )
    
    # Cross-validated mean-squared error score
    mse_cv_score = cross_val_score(
        lm,
        filip_df_poly[dependent_vars],
        filip_df_poly[independent_var],
        scoring="neg_mean_squared_error",
        cv=rkf,
        n_jobs=-1,  # Use all processors during cross-validation run
    )

    # Cross-validated R**2 score
    r2_cv_score = cross_val_score(
        lm,
        filip_df_poly[dependent_vars],
        filip_df_poly[independent_var],
        scoring="r2",
        cv=rkf,
        n_jobs=-1,  # Use all processors during cross-validation run
    )

    filip_poly_cv_scores["n"].append(n)
    filip_poly_cv_scores["mse_trace"].append(mse_cv_score)
    filip_poly_cv_scores["mse_mean"].append(np.mean(mse_cv_score))
    filip_poly_cv_scores["mse_sd"].append(np.std(mse_cv_score))
    filip_poly_cv_scores["r**2_trace"].append(r2_cv_score)
    filip_poly_cv_scores["r**2_mean"].append(np.mean(r2_cv_score))
    filip_poly_cv_scores["r**2_sd"].append(np.std(r2_cv_score))

# Convert dictionary to data frame
filip_poly_cv_scores_df = pd.DataFrame(filip_poly_cv_scores)

# Distribution of cross-validation scores
filip_cv_scores_dist_df = pd.concat(
    [
        pd.DataFrame(filip_poly_cv_scores_df["mse_trace"].tolist()) \
        .assign(n=[f"{x}" for x in range(1, 16)], score="mse") \
        .melt(id_vars=["n", "score"], value_vars=list(range(1000)),
              var_name="cv_run", value_name="value") \
        .sort_values(["score", "n", "cv_run"]) \
        .reset_index(drop=True),
        pd.DataFrame(filip_poly_cv_scores_df["r**2_trace"].tolist()) \
        .assign(n=[f"{x}" for x in range(1, 16)], score="r**2") \
        .melt(id_vars=["n", "score"], value_vars=list(range(1000)),
              var_name="cv_run", value_name="value") \
        .sort_values(["score", "n", "cv_run"]) \
        .reset_index(drop=True),
    ]
)

bootstrap_results = {
    "n": [],
    "sample": [],
    "mean": [],
}

for n in range(2, 16):
    bootstrap_series = filip_cv_scores_dist_df \
        .query(f"score == 'mse' & n == '{n}'") \
        .sample(frac=1000, replace=True).loc[:, "value"]
    bootstrap_df = pd.DataFrame(bootstrap_series) \
        .assign(sample_id=[f"{x}" for x in range(1000) for _ in range(1000)])
    bootstrap_mean_samples = bootstrap_df \
        .groupby(["sample_id"]) \
        .mean() \
        .loc[:, "value"] \
        .values

    bootstrap_results["n"].extend(1000 * [f"{n}"])
    bootstrap_results["sample"].extend(list(range(1000)))
    bootstrap_results["mean"].extend(bootstrap_mean_samples)

filip_cv_scores_bootstrap_df = pd.DataFrame(bootstrap_results)

filip_mse_ci_95 = filip_cv_scores_bootstrap_df \
    .loc[:, ["n", "mean"]] \
    .groupby(["n"]) \
    .quantile([0.025, 0.975])
filip_mse_ci_95 = filip_mse_ci_95["mean"] \
    .unstack() \
    .reset_index() \
    .rename(columns={0.025: "lower", 0.975: "upper"})

filip_cv_final_df = filip_poly_cv_scores_df.copy().loc[:, ["n", "mse_mean"]].query("n > 1")
filip_cv_final_df["n"] = filip_cv_final_df["n"].astype(str)
filip_cv_final_df = filip_cv_final_df.merge(filip_mse_ci_95, on=["n"])

filip_cv_final_df["yerr_lower"] = np.abs(filip_cv_final_df["mse_mean"] - filip_cv_final_df["lower"])
filip_cv_final_df["yerr_upper"] = np.abs(filip_cv_final_df["mse_mean"] - filip_cv_final_df["upper"])

# Visualize MSE with 95% CI
fig, ax = plt.subplots(dpi=120, figsize=(4, 3))
facet_var, facet_id, facet_label, facet_ylim = ("mse", 0, r"Mean-squared error", (-0.0006, 0.0001))
sns.scatterplot(
    x="n",
    y=f"{facet_var}_mean",
    data=filip_cv_final_df,
    ax=ax,
)
ax.errorbar(
    filip_cv_final_df["n"],
    filip_cv_final_df[f"{facet_var}_mean"],
    yerr=[filip_cv_final_df["yerr_lower"], filip_cv_final_df["yerr_upper"]],
)
ax.set_ylim(facet_ylim)
ax.set_xlabel(r"Polynomial degree")
ax.set_ylabel(facet_label)

fig.tight_layout();