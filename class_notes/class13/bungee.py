# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


def simulation(
    sim_time=60,
    delta_t=0.01,
    mass=80,
    spring_constant=6,
    unweighted_length=30,
    radius=None,
    mode="no_drag",
):
    gravity_acceleration = -9.81
    sim_steps = int(sim_time / delta_t)
    weight = mass * gravity_acceleration
    weight_displacement = np.abs(mass * gravity_acceleration) / spring_constant
    
    if mode == "no_drag":
        simulation_df = no_drag(
            spring_constant=spring_constant,
            unweighted_length=unweighted_length,
            mass=mass,
            weight=weight,
            sim_steps=sim_steps,
            delta_t=delta_t,
        )
    elif mode == "with_drag" and radius:
        simulation_df = with_drag(
            spring_constant=spring_constant,
            unweighted_length=unweighted_length,
            mass=mass,
            weight=weight,
            radius=radius,
            sim_steps=sim_steps,
            delta_t=delta_t,
        )
        
    return simulation_df


def no_drag(
    spring_constant,
    unweighted_length,
    mass,
    weight,
    sim_steps,
    delta_t,
):
    length = 0  # m
    acceleration = weight / mass
    velocity = 0 - acceleration * delta_t / 2
    
    trace_length = [[0, length]]
    trace_velocity = [[0, velocity]]
    
    for step_index in range(1, sim_steps + 1):
        if length > unweighted_length:
            restoring_spring_force = spring_constant * (length - unweighted_length)
            
        else:
            restoring_spring_force = 0

        total_force = restoring_spring_force + weight
        acceleration = total_force / mass

        velocity += delta_t * acceleration
        length += -velocity * delta_t

        trace_length.append([step_index, length])
        trace_velocity.append([step_index, velocity])
    
    simulation_df = make_data_frame(trace_length, trace_velocity, "no drag", delta_t)
        
    return simulation_df


def with_drag(
    spring_constant,
    unweighted_length,
    mass,
    weight,
    radius,
    sim_steps,
    delta_t,
):
    projected_area = np.pi * radius ** 2
    length = 0  # m
    acceleration = weight / mass
    velocity = 0 - acceleration * delta_t / 2
    
    trace_length = [[0, length]]
    trace_velocity = [[0, velocity]]
    
    for step_index in range(1, sim_steps + 1):
        if length > unweighted_length:
            restoring_spring_force = spring_constant * (length - unweighted_length)

        else:
            restoring_spring_force = 0

        air_friction = -0.65 * projected_area * velocity * np.abs(velocity)
        total_force = restoring_spring_force + weight + air_friction
        acceleration = total_force / mass

        velocity += delta_t * acceleration
        length += -velocity * delta_t

        trace_length.append([step_index, length])
        trace_velocity.append([step_index, velocity])
    
    simulation_df = make_data_frame(trace_length, trace_velocity, "with drag", delta_t)
        
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
    