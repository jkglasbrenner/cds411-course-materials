# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


def simulation(
    sim_time=5.0,
    delta_t=0.01,
    bts_population_initial=15,
    bts_birth_fraction=1,
    bts_death_constant=0.20,
    wts_population_initial=20,
    wts_birth_fraction=1,
    wts_death_constant=0.27,
):
    sim_steps = int(sim_time / delta_t)
    wts = wts_population_initial
    bts = bts_population_initial
    
    trace = [[0, wts, bts]]
    
    for step_index in range(1, sim_steps + 1):
        wts_rate_of_change = wts_birth_fraction * wts - wts_death_constant * wts * bts
        bts_rate_of_change = bts_birth_fraction * bts - bts_death_constant * wts * bts
        
        wts += wts_rate_of_change * delta_t
        bts += bts_rate_of_change * delta_t

        trace.append([step_index, wts, bts])
    
    simulation_df = make_data_frame(trace, delta_t)
        
    return simulation_df


def make_data_frame(trace, delta_t):
    return pd.DataFrame({
            "time": [x[0] * delta_t for x in trace],
            "wts": [x[1] for x in trace],
            "bts": [x[2] for x in trace],
        })
    