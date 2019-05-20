# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


def run(function, number_of_darts, x_min, x_max, y_min, y_max):
    df = throw_darts(number_of_darts, x_min, x_max, y_min, y_max)
    df = label_hits(df, function)
    area_under_curve = estimate_area_under_curve(df, x_min, x_max, y_min, y_max)
    
    return df, area_under_curve


def cubic_function(x, a=1.4, b=0, c=-1.75, d=1.0):
    return a + b * x + c * x**2 + d * x**3


def throw_darts(number_of_darts, x_min, x_max, y_min, y_max):
    return pd.DataFrame({
        "x": np.random.uniform(low=x_min, high=x_max, size=number_of_darts),
        "y": np.random.uniform(low=y_min, high=y_max, size=number_of_darts),
    })


def find_hits(darts_df, function):
    return darts_df["y"] < function(darts_df["x"].values)


def label_hits(darts_df, function):
    df_copy = darts_df.copy()
    df_copy["hit"] = find_hits(df_copy, function)
    
    return df_copy


def estimate_area_under_curve(darts_df, x_min, x_max, y_min, y_max):
    success_fraction = np.sum(darts_df["hit"]) / len(darts_df)
    
    width = x_max - x_min
    height = y_max - y_min
    
    area = width * height
    return area * success_fraction
