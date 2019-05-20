# coding: utf-8

import matplotlib.pyplot as plt
import pandas as pd

# Constants
sim_time = 8  # hours
delta_t = 0.01  # hours
sim_steps = int(sim_time / delta_t)
half_life = 3.2  # hours
plasma_volume = 3000  # milliliters
initial_aspirin_in_plasma = 2 * 325 * 1000  # micrograms
elimination_constant = -np.log(2) / half_life  # inverse hours
mec = 150  # micrograms
mtc = 350  # micrograms
plasma_concentration = [[0, initial_aspirin_in_plasma / plasma_volume]]

# Algorithm
aspirin_in_plasma = initial_aspirin_in_plasma
for step_index in range(1, sim_steps + 1):
    elimination = elimination_constant * aspirin_in_plasma
    aspirin_in_plasma += elimination * delta_t
    plasma_concentration.append([step_index, aspirin_in_plasma / plasma_volume])

simulation_df = pd.DataFrame({
    "step": [x[0] for x in plasma_concentration],
    "plasma": [x[1] for x in plasma_concentration],
})
simulation_df["time"] = simulation_df["step"] * delta_t

# Figure
fig, ax = plt.subplots(dpi=120)  # Use dpi to change figure size in notebooks
ax.axhline(mec, color="k", linestyle="--")  # Plots MEC minimum line
ax.axhline(mtc, color="k", linestyle="--")  # Plots MTC maximum line
ax.plot(simulation_df["time"], simulation_df["plasma"].values, "-")
ax.text(7.5, mec + 10, "MEC")
ax.text(7.5, mtc - 20, "MTC")
ax.set_ylim(bottom=0)
ax.set_xlabel("time (hr)")
ax.set_ylabel(r"plasma concentration $(\mu{}g/\mathrm{mL})$")
