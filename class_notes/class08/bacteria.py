#!/usr/bin/env python

from typing import Union

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def simulation(p0: float, growth_rate: float, time: float, delta_t: float) -> pd.DataFrame:
    """Simulate the population of a bacterial colony over time.
    
    :param p0: The initial population of the bacterial colony.
    :param growth_rate: The reproduction rate for the bacteria population.
    :param time: Total amount of clock time to run simulation.
    :param delta_t: The size of the time step interval.
    :returns: Simulation history in a data frame
    """
    total_sim_steps = int(time / delta_t)
    population = p0
    trace = [[0, population]]
    
    for step_index in range(1, total_sim_steps + 1):
        population_change = growth_rate * population
        population += population_change * delta_t
        trace.append([step_index, population])

    population_df = pd.DataFrame({
        "step_index": [x[0] for x in trace],
        "population": [x[1] for x in trace],
    })
    population_df["time"] = population_df["step_index"] * delta_t
    
    return population_df


def exact(p0: float, growth_rate: float, time: float, delta_t: float) -> pd.DataFrame:
    """Exact solution for modeling the population of a bacterial colony over time.
    
    :param p0: The initial population of the bacterial colony.
    :param growth_rate: The reproduction rate for the bacteria population.
    :param time: Total amount of clock time to run simulation.
    :param delta_t: Sampling interval for exact solution.
    :returns: Exact solution history in a data frame
    """
    time_array = np.arange(0, time + delta_t, delta_t)
    population = p0 * np.exp(growth_rate * time_array)
    population_df = pd.DataFrame({
        "time": time_array,
        "population": population,
    })
    
    return population_df


def create_plot(x, y, label, style, xlabel="time", ylabel="population"):
    fig, ax = plt.subplots()
    ax.plot(x, y, style, label=label)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    
    return fig, ax


def add_to_plot(ax, x, y, label, style):
    ax.plot(x, y, style, label=label)
    

if __name__ == '__main__':
    final_population = main(0.1, 0.001, 100)
    print(final_population)
