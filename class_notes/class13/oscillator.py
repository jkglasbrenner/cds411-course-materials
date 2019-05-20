# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


def simulation(
    sim_time=5.0,
    delta_t=0.01,
    mass=0.2,
    spring_constant=10,
    unweighted_length=1.000,
    init_displacement=0.3,
    radius=None,
    mode="undamped",
):
    gravity_acceleration = -9.81
    sim_steps = int(sim_time / delta_t)
    weight = mass * gravity_acceleration
    weight_displacement = np.abs(mass * gravity_acceleration) / spring_constant
    weighted_length = unweighted_length + weight_displacement
    
    if mode == "undamped":
        simulation_df = undamped(
            spring_constant=spring_constant,
            unweighted_length=unweighted_length,
            weighted_length=weighted_length,
            init_displacement=init_displacement,
            mass=mass,
            weight=weight,
            sim_steps=sim_steps,
            delta_t=delta_t,
        )
    elif mode == "damped" and radius:
        simulation_df = damped(
            spring_constant=spring_constant,
            unweighted_length=unweighted_length,
            weighted_length=weighted_length,
            init_displacement=init_displacement,
            mass=mass,
            weight=weight,
            radius=radius,
            sim_steps=sim_steps,
            delta_t=delta_t,
        )
        
    return simulation_df


def undamped(
    spring_constant,
    unweighted_length,
    weighted_length,
    init_displacement,
    mass,
    weight,
    sim_steps,
    delta_t,
):
    length = weighted_length + init_displacement  # m
    acceleration = (spring_constant * (length - unweighted_length) + weight) / mass
    velocity = 0 - acceleration * delta_t / 2
    
    trace_length = [[0, length]]
    trace_velocity = [[0, velocity]]
    
    for step_index in range(1, sim_steps + 1):
        restoring_spring_force = spring_constant * (length - unweighted_length)
        total_force = restoring_spring_force + weight
        acceleration = total_force / mass

        velocity += delta_t * acceleration
        length += -velocity * delta_t

        trace_length.append([step_index, length])
        trace_velocity.append([step_index, velocity])
    
    simulation_df = make_data_frame(trace_length, trace_velocity, "undamped", delta_t)
        
    return simulation_df


def damped(
    spring_constant,
    unweighted_length,
    weighted_length,
    init_displacement,
    mass,
    weight,
    radius,
    sim_steps,
    delta_t,
):
    projected_area = np.pi * radius ** 2
    length = weighted_length + init_displacement  # m
    acceleration = (spring_constant * (length - unweighted_length) + weight) / mass
    velocity = 0 - acceleration * delta_t / 2
    
    trace_length = [[0, length]]
    trace_velocity = [[0, velocity]]
    
    for step_index in range(1, sim_steps + 1):
        restoring_spring_force = spring_constant * (length - unweighted_length)
        air_friction = -0.65 * projected_area * velocity * np.abs(velocity)
        total_force = restoring_spring_force + weight + air_friction
        acceleration = total_force / mass

        velocity += delta_t * acceleration
        length += -velocity * delta_t

        trace_length.append([step_index, length])
        trace_velocity.append([step_index, velocity])
    
    simulation_df = make_data_frame(trace_length, trace_velocity, "damped", delta_t)
        
    return simulation_df


def make_data_frame(trace_length, trace_velocity, mode, delta_t):
    return pd.merge(
        pd.DataFrame({
            "time": [x[0] * delta_t for x in trace_length],
            "length": [x[1] for x in trace_length],
            "mode": mode,
        }),
        pd.DataFrame({
            "time": [(x[0] - 0.5) * delta_t for x in trace_velocity],
            "velocity": [x[1] for x in trace_velocity],
            "mode": mode,
        }),
        how="outer",
    )
    