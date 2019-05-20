# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


def simulation(
    sim_time=5.0,
    delta_t=0.01,
    mass=0.2,
    spring_constant=10,
    unweighted_length=1.000,
    init_displacement = 0.3,
    method="forward",
):
    gravity_acceleration = -9.81
    sim_steps = int(sim_time / delta_t)
    weight = mass * gravity_acceleration
    weight_displacement = np.abs(mass * gravity_acceleration) / spring_constant
    weighted_length = unweighted_length + weight_displacement
    
    if method == "forward":
        simulation_df = forward_euler(
            spring_constant=spring_constant,
            unweighted_length=unweighted_length,
            weighted_length=weighted_length,
            init_displacement=init_displacement,
            mass=mass,
            weight=weight,
            sim_steps=sim_steps,
            delta_t=delta_t,
        )
        
    elif method == "midpoint":
        simulation_df = midpoint_euler(
            spring_constant=spring_constant,
            unweighted_length=unweighted_length,
            weighted_length=weighted_length,
            init_displacement=init_displacement,
            mass=mass,
            weight=weight,
            sim_steps=sim_steps,
            delta_t=delta_t,
        )
    
    elif method == "leapfrog":
        simulation_df = leapfrog(
            spring_constant=spring_constant,
            unweighted_length=unweighted_length,
            weighted_length=weighted_length,
            init_displacement=init_displacement,
            mass=mass,
            weight=weight,
            sim_steps=sim_steps,
            delta_t=delta_t,
        )
        
    return simulation_df


def forward_euler(
    spring_constant,
    unweighted_length,
    weighted_length,
    init_displacement,
    mass,
    weight,
    sim_steps,
    delta_t,
):
    length = weighted_length + init_displacement
    velocity = 0
    trace = [[0, length, 0]]
    
    for step_index in range(1, sim_steps + 1):
        restoring_spring_force = spring_constant * (length - unweighted_length)
        total_force = restoring_spring_force + weight
        acceleration = total_force / mass
    
        length += -velocity * delta_t
        velocity += delta_t * acceleration
    
        trace.append([step_index, length, velocity])
        
    simulation_df = pd.DataFrame({
        "time": [x[0] * delta_t for x in trace],
        "length": [x[1] for x in trace],
        "velocity": [x[2] for x in trace],
        "method": "forward_euler",
    })
        
    return simulation_df


def midpoint_euler(
    spring_constant,
    unweighted_length,
    weighted_length,
    init_displacement,
    mass,
    weight,
    sim_steps,
    delta_t,
):
    length = weighted_length + init_displacement
    velocity = 0
    trace = [[0, length, 0]]
    
    for step_index in range(1, sim_steps + 1):
        velocity_old = velocity
        acceleration = (spring_constant * (length - unweighted_length) + weight) / mass
        velocity_half_step = velocity_old + acceleration * (delta_t / 2)
        length_half_step = length - velocity_old * (delta_t / 2)
        
        acceleration_half_step = (spring_constant * (length_half_step - unweighted_length) + weight) / mass
        
        velocity += acceleration_half_step * delta_t
        length += -velocity_half_step * delta_t
        trace.append([step_index, length, velocity])
        
    simulation_df = pd.DataFrame({
        "time": [x[0] * delta_t for x in trace],
        "length": [x[1] for x in trace],
        "velocity": [x[2] for x in trace],
        "method": "midpoint_euler",
    })
        
    return simulation_df


def leapfrog(
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
    
    simulation_df = pd.merge(
        pd.DataFrame({
            "time": [x[0] * delta_t for x in trace_length],
            "length": [x[1] for x in trace_length],
            "method": "leapfrog",
        }),
        pd.DataFrame({
            "time": [(x[0] - 0.5) * delta_t for x in trace_velocity],
            "velocity": [x[1] for x in trace_velocity],
            "method": "leapfrog",
        }),
        how="outer",
    )
        
    return simulation_df