# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Constants
sim_time = 168  # hours
delta_t = 0.01  # hours
sim_steps = int(sim_time / delta_t)
half_life = 22  # hours
dose_interval = 8  # hours
dose_steps = int(dose_interval / delta_t)
absorption_constant = 0.12
serum_volume = 3000  # milliliters
dosage = 100 * 1000  # micrograms
elimination_constant = -np.log(2) / half_life  # inverse hours
mec = 10  # micrograms per milliliter
mtc = 20  # micrograms per milliliter
serum_concentration = [[0, 0]]

# Algorithm
dilantin_in_system = absorption_constant * dosage
for step_index in range(1, sim_steps + 1):
    if step_index % dose_steps == 0:
        dilantin_in_system += absorption_constant * dosage
    
    elimination = elimination_constant * dilantin_in_system
    dilantin_in_system += elimination * delta_t
    serum_concentration.append([step_index, dilantin_in_system / serum_volume])

# Pandas data frame
simulation_df = pd.DataFrame({
    "step": [x[0] for x in serum_concentration],
    "serum": [x[1] for x in serum_concentration],
})
simulation_df["time"] = simulation_df["step"] * delta_t

# Figure
fig, ax = plt.subplots(dpi=120)  # Use dpi to change figure size in notebooks
ax.axhline(mec, color="k", linestyle="--")  # Plots MEC minimum line
ax.axhline(mtc, color="k", linestyle="--")  # Plots MTC maximum line
ax.plot(simulation_df["time"], simulation_df["serum"].values, "-")
ax.text(0, mec + 1, "MEC")
ax.text(0, mtc - 1, "MTC")
ax.set_ylim(bottom=0)
ax.set_xlabel("time (hr)")
ax.set_ylabel(r"serum concentration $(\mu{}g/\mathrm{mL})$");