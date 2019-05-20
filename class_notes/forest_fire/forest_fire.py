# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib import animation, rc
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import pandas as pd


def forest_fire_simulation(
    number_time_steps, n, prob_tree, prob_burning, prob_immune, prob_lightning, number_burning_trees=0,
):
    """Run temperature diffusion simulation.
    
    Parameters
    ----------
    number_time_steps : int
        Sets the number of time steps over which to run a simulation.

    n : int
        Number of rows and columns in the grid

    prob_tree : float
        Probability to initialize a cell with a tree

    prob_burning : float
        Probability that a tree starts on fire
    
    prob_immune : float
        Probability that a tree will not catch fire from a neighboring cell
        
    prob_lightning : flaot
        Probability that lightning will strike a tree during each simulation
        step.
        
    number_burning_trees : int
        Number of trees to randomly set on fire at start of simulation.

    Returns
    -------
    simulation_history : list
        The forest grid as a function of time during the forest fire simulation.
    """
    # Initialize forest according to parameters
    forest = init_forest(n, prob_tree, prob_burning, number_burning_trees)

    # Initialize record keeper for the simulation history
    simulation_history = [[0, forest.copy()]]

    # Run simulation for specified number of time steps
    for nstep in np.arange(number_time_steps):
        sweep(forest, prob_immune, prob_lightning, nstep, simulation_history)

    return simulation_history


def init_forest(n, prob_tree, prob_burning, number_burning_trees=0):
    """Initialize an n ⨉ n grid of trees in a forest.
    
    Parameters
    ----------
    n : int
        Number of rows and columns in the grid

    prob_tree : float
        Probability to initialize a cell with a tree

    prob_burning : float
        Probability that a tree starts on fire
        
    number_burning_trees : int
        Number of trees to randomly set on fire at start of simulation.

    Returns
    -------
    forest : np.array
        Grid of integers defining the forest
    """
    forest = np.zeros(shape=(n, n), dtype=np.int)

    tree_cells = np.random.uniform(low=0, high=1, size=(n, n)) < prob_tree
    number_trees = np.prod(forest[tree_cells].shape)

    is_burning = np.random.uniform(low=0, high=1, size=number_trees) < prob_burning
    burning_cells = tree_cells.copy()
    np.place(burning_cells, tree_cells, is_burning)

    forest[tree_cells] = 1
    forest[burning_cells] = 2
    
    if number_burning_trees > 0:
        forest = burn_random_tree(forest, number_burning_trees)

    return forest


def visualize_grid(grid, fig_width=6, fig_height=6, dpi=120):
    """Visualize a 2D numpy array using a heatmap.

    Parameters
    ----------
    grid : np.array
        A two-dimensional array representing the cellular automata grid
    
    fig_width : float
        Figure width in inches
        
    fig_height : float
        Figure height in inches
        
    Returns
    -------
    fig, ax : tuple of plt.figure and plt.subplot
        Matplotlib figure and subplot axis objects
        
    .. _colormaps: https://matplotlib.org/examples/color/colormaps_reference.html 
    """
    # grid dimensions
    m, n = grid.shape

    # create matplotlib figure and subplot objects
    fig, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=dpi)

    # Define a custom color map, with 0 being black, 1 being tab:blue, and
    # 2 being tab:orange
    cmap = LinearSegmentedColormap.from_list(
        "forestfire", ["black", "tab:blue", "tab:orange"]
    )

    # imshow visualizes array as a two-dimensionl uniform grid
    im = ax.imshow(grid, cmap=cmap, interpolation="nearest", vmin=0, vmax=2)

    # find the starting and ending coordinates for heatmap for creating
    # grid lines
    xticks_start, xticks_end = ax.get_xlim()
    yticks_start, yticks_end = ax.get_ylim()

    # separate grid cells by white lines
    ax.xaxis.set_ticks(np.linspace(xticks_start, xticks_end, n + 1), minor=False)
    ax.yaxis.set_ticks(np.linspace(yticks_start, yticks_end, m + 1), minor=False)
    ax.axes.grid(True, linestyle="-", linewidth=1, color="white", which="major")

    # we don't need ticks and tick labels because we have grid lines
    ax.tick_params(labelbottom=False, labelleft=False, bottom=False, left=False)

    # Return matplotlib figure and subplot objects
    return fig, ax


def boundary_condition(forest, condition="periodic"):
    """Setup ghost cells for boundary condition.
    
    Parameters
    ----------
    forest : np.array
        Grid of integers defining the forest
        
    condition : str, optional
        The boundary condition to use when creating ghost cells.
    """
    if condition == "periodic":
        extended_forest = np.pad(array=forest, pad_width=(1, 1), mode="wrap")

    else:
        raise ValueError("{0} is not a valid boundary condition".format(condition))

    return extended_forest


def get_neighbors(extended_forest, ghost_width=(1, 1), neighborhood="von_neumann"):
    """Get the cellular state of each site's neighbors in a single sweep.
    
    Paramters
    ---------
    extended_forest : np.array
        Grid of integers defining the forest with ghost cells
        
    ghost_width : array-like
        A number pair that specifies how many rows and columns make up the
        ghost cell region
        
    neighborhood : str, optional
        Determines which cells will be counted as neighbors
        
    Returns
    -------
    forest_with_neighbors : np.array
        Grid of integers of the state of each cell's neighbors in the forest
    """
    m_extended, n_extended = extended_forest.shape
    m, n = (m_extended - ghost_width[0], n_extended - ghost_width[1])

    if neighborhood == "von_neumann":
        forest_with_neighbors = np.array(
            [
                np.roll(extended_forest, shift=(0, 1), axis=(1, 0))[
                    ghost_width[0] : m, ghost_width[1] : n
                ],
                np.roll(extended_forest, shift=(1, 0), axis=(1, 0))[
                    ghost_width[0] : m, ghost_width[1] : n
                ],
                np.roll(extended_forest, shift=(-1, 0), axis=(1, 0))[
                    ghost_width[0] : m, ghost_width[1] : n
                ],
                np.roll(extended_forest, shift=(0, -1), axis=(1, 0))[
                    ghost_width[0] : m, ghost_width[1] : n
                ],
            ]
        )

    else:
        raise ValueError("{0} is not a valid type of neighborhood".format(condition))

    return forest_with_neighbors


def spread(forest, forest_neighbors, prob_immune, prob_lightning):
    """Update cell states using random number generator and transition rules.
    
    Parameters
    ----------
    forest : np.array
        Grid of integers defining the forest

    forest_neighbors : np.array
        Grid of integers of the state of each cell's neighbors in the forest
        
    prob_immune : float
        Probability that a tree will not catch fire from a neighboring cell
        
    prob_lightning : flaot
        Probability that lightning will strike a tree during each simulation
        step.
        
    Returns
    -------
    forest_update : np.array
        Grid of integers that specifies the updated forest after the latest
        time step.
    """
    # Get number of neighbors per cell and x,y dimensions
    num_neighbors, m, n = forest_neighbors.shape

    # Use copy of forest to help prevent premature updating of cellular states.
    forest_update = forest.copy()

    # Find the tree cells and burning cells
    tree_cells = forest_update == 1
    old_burning_cells = forest_update == 2

    # Compute the probability that a lightning strike causes a fire.
    prob_lightning_fire = prob_lightning * (1 - prob_immune)

    # Boolean condition: which cells have a burning neighbor?
    cells_with_burning_neighbors = np.any(forest_neighbors == 2, axis=0)

    # Boolean condition: Which of the cells with burning neighbors has a tree
    # state
    trees_with_burning_neighbors = np.logical_and(
        tree_cells, cells_with_burning_neighbors
    )
    number_trees_with_burning_neighbors = np.sum(trees_with_burning_neighbors)

    # Generate a random number to determine how the fire spreads:
    is_burning = (
        np.random.uniform(low=0, high=1, size=number_trees_with_burning_neighbors)
        >= prob_immune
    )

    # Create an array and fill it with the False boolean, then use np.place()
    # with trees_with_burning_neighbors to label the sites that will burn
    trees_catching_fire = np.full(fill_value=False, shape=(m, n), dtype=np.bool)
    np.place(trees_catching_fire, trees_with_burning_neighbors, is_burning)

    # Next, we test if lightning strikes and causes a fire.
    # Remove the trees from our list that will already catch fire this round
    tree_cells[trees_catching_fire] = False
    number_remaining_trees = np.sum(tree_cells)

    # Check if each tree cell gets hit by lightning AND starts a fire
    is_burning = (
        np.random.uniform(low=0, high=1, size=number_remaining_trees)
        < prob_lightning_fire
    )
    trees_burned_by_lightning = np.full(fill_value=False, shape=(m, n), dtype=np.bool)

    # Use np.place() to mark the cells with trees burned by lightning for
    # update
    np.place(trees_burned_by_lightning, tree_cells, is_burning)

    # Combine burning trees from spreading and lightning into one list
    new_burning_cells = np.logical_or(trees_catching_fire, trees_burned_by_lightning)

    # Update states
    # Replace trees that burned in the previous round with an empty square
    forest_update[old_burning_cells] = 0

    # Use combined list of trees to burn during the next time step to update
    # their state:
    forest_update[new_burning_cells] = 2

    return forest_update


def sweep(forest, prob_immune, prob_lightning, nstep, simulation_history):
    """Sweep over grid and update state of forest.
    
    Parameters
    ----------
    forest : np.array
        Grid of integers defining the forest

    prob_immune : float
        Probability that a tree will not catch fire from a neighboring cell
        
    prob_lightning : flaot
        Probability that lightning will strike a tree during each simulation
        step.

    nstep : int
        Sets the number of time steps over which to run a simulation.

    simulation_history : list
        Time-step history for the simulation's run.
    """
    extended_forest = boundary_condition(forest)
    forest_neighbors = get_neighbors(extended_forest)
    forest_update = spread(forest, forest_neighbors, prob_immune, prob_lightning)
    forest[:, :] = forest_update
    simulation_history.append([nstep, forest_update])


def ca_animation(simulation_history, fig_width=6, fig_height=6, dpi=120):
    """Animate the cellular automata simulation using Matplotlib.

    Parameters
    ----------
    simulation_history : list
        Time-step history for the simulation's run.
    
    cmap : str, optional
        Color scheme for the heatmap scale, see colormaps_ reference.
        
    fig_width : float, optional
        Figure width in inches
        
    fig_height : float, optional
        Figure height in inches
        
    Returns
    -------
    anim : matplotlib.animation.FuncAnimation
        Animated object for the simulation run.
        
    .. _colormaps: https://matplotlib.org/examples/color/colormaps_reference.html 
    """
    # grid dimensions
    m, n = simulation_history[0][1].shape

    # create matplotlib figure and subplot objects
    fig, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=dpi)

    # imshow visualizes array as a two-dimensionl uniform grid
    cmap = LinearSegmentedColormap.from_list(
        "forestfire", ["black", "tab:blue", "tab:orange"]
    )
    im = ax.imshow(
        simulation_history[0][1], cmap=cmap, interpolation="nearest", vmin=0, vmax=2
    )

    # find the starting and ending coordinates for heatmap for creating
    # grid lines
    xticks_start, xticks_end = ax.get_xlim()
    yticks_start, yticks_end = ax.get_ylim()

    # separate grid cells by white lines
    ax.xaxis.set_ticks(np.linspace(xticks_start, xticks_end, n + 1), minor=False)
    ax.yaxis.set_ticks(np.linspace(yticks_start, yticks_end, m + 1), minor=False)
    ax.axes.grid(True, linestyle="-", linewidth=1, color="white", which="major")

    # we don't need ticks and tick labels because we have grid lines
    ax.tick_params(labelbottom=False, labelleft=False, bottom=False, left=False)

    # Initialization function, clears out the data on the im object
    def init():
        im.set_array(np.array([[]]))
        return (im,)

    # Animation function. Input i is the frame number of the animation, and is
    # to be used for referencing how the data changes over time
    def animate(i):
        # Get the simulation history at time step i and set as the underlying
        # data for the im object
        forest_i = simulation_history[i][1]
        im.set_array(forest_i)

        return (im,)

    # Suppress static matplotlib window
    plt.close()

    # Use animation.FuncAnimation to put the animation together.
    # frames controls the number of frames in the movie.
    # interval controls the delay in milliseconds inbetween each frame
    # blit optimizes the animation size by only storing the changes between
    # frames instead of as a series of full plots
    anim = animation.FuncAnimation(
        fig=fig,
        func=animate,
        frames=len(simulation_history),
        init_func=init,
        interval=100,
        blit=True,
    )

    return anim


def burn_random_tree(forest, number_burning_trees):
    """Randomly set a number of trees on fire.
    
    Parameters
    ----------
    forest : np.array
        Grid of integers defining the forest
        
    number_burning_trees : int
        Number of trees to randomly set on fire.

    Returns
    -------
    forest_update : np.array
        Updated forest grid.
    """
    # Get x,y dimensions of forest
    m, n = forest.shape

    # Use copy of forest to help prevent premature updating of cellular states.
    forest_update = forest.copy()

    # Find and count the tree cells
    tree_cells = forest == 1
    number_trees = tree_cells.sum()
    
    # Randomly set trees on fire
    tree_selector = np.array(number_burning_trees * [True] + (number_trees - number_burning_trees) * [False])
    np.random.shuffle(tree_selector)
    
    # Set chosen trees on fire
    trees_to_burn = np.zeros(shape=(m, n), dtype=np.bool)
    np.place(trees_to_burn, tree_cells, tree_selector)
    forest_update[trees_to_burn] = 2

    return forest_update


def make_trace_data_frame(trace):
    trace_array = np.array([simarray[1] for simarray in trace])
    nsteps_idx, grid_x_idx, grid_y_idx = np.indices(trace_array.shape)
    trace_df = pd.DataFrame({
        "nstep": nsteps_idx.flatten(),
        "x": grid_x_idx.flatten(),
        "y": grid_y_idx.flatten(),
        "state": trace_array.flatten(),
    })
    
    return trace_df


def count_states_over_time(trace_df, n):
    return trace_df \
        .groupby("nstep") \
        .apply(
            func=lambda x: pd.Series([len(x[x["state"] == 0]), len(x[x["state"] == 1]), len(x[x["state"] == 2])],
                                     index=["nempty", "ntrees", "nburning"])) \
        .reset_index() \
        .melt(id_vars=["nstep"], var_name="state", value_name="count") \
        .assign(fraction=lambda x: x["count"] / (n * n))