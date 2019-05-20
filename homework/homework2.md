Homework 2
================

## Instructions

Obtain the GitHub repository you will use to complete the homework
assignment, which contains the starter Jupyter notebook file
`homework2.ipynb`. The notebook template provides space for you to
answer each question. Your notebook should run without error when you
select **Restart Kernel and Run All
Cells**:

<img src="../img/jupyterlab_restart_kernel_and_run_all.png" style="display: block; margin: auto;" />

When you’re done, save your file, then stage, commit, and push (upload)
it to GitHub, and then follow the instructions in the [How to
submit](#how-to-submit) section.

## Questions

1.  Develop a model for Newton’s Law of Heating and Cooling. This model
    states that the rate of change of the temperature
    ![T](https://latex.codecogs.com/png.latex?T "T") with respect to the
    time ![t](https://latex.codecogs.com/png.latex?t "t") of an object
    is proportional to the difference between the temperatures of an
    object and its surroundings. In your model, use the variable name
    `object_temperature` for the object temperature and
    `external_temperature` for the temperature of the surroundings. For
    the proportionality constant, use `alpha`. Place any functions you
    write in a file named `newton.py`.
    
    1.  Write the model inside a function named `newton_heating_cooling`
        that takes the following inputs:
        
          - Initial object temperature
          - Temperature of surroundings
          - Proportionality constant
        
        The function, upon completion, should return a pandas DataFrame
        of the object temperature as a function of time (“clock time”,
        not just the time steps).
    
    2.  Suppose the object is cold water at ![6\\text{
        }^{\\circ}\\text{C}](https://latex.codecogs.com/png.latex?6%5Ctext%7B%20%7D%5E%7B%5Ccirc%7D%5Ctext%7BC%7D
        "6\\text{ }^{\\circ}\\text{C}") that is placed in a room of
        temperature ![20\\text{
        }^{\\circ}\\text{C}](https://latex.codecogs.com/png.latex?20%5Ctext%7B%20%7D%5E%7B%5Ccirc%7D%5Ctext%7BC%7D
        "20\\text{ }^{\\circ}\\text{C}"). After 1 hour, the temperature
        of the water is ![20\\text{
        }^{\\circ}\\text{C}](https://latex.codecogs.com/png.latex?20%5Ctext%7B%20%7D%5E%7B%5Ccirc%7D%5Ctext%7BC%7D
        "20\\text{ }^{\\circ}\\text{C}"). Modify your simulation to
        allow you to calculate the constant of proportionality.
    
    3.  Using the constant of proportionality you found in part ii, run
        your simulation to figure out how much of the water’s
        temperature changes after 15 minutes.
    
    4.  How long will it take to warm the water to room temperature?
        Create a plot showing the temperature as a function of time as
        it warms to room temperature.

2.  It has been estimated that for the Antarctic fin whale,
    ![r=0.08](https://latex.codecogs.com/png.latex?r%3D0.08 "r=0.08")
    per year,
    ![M=400,000](https://latex.codecogs.com/png.latex?M%3D400%2C000
    "M=400,000") whales, and
    ![P\_0=70,000](https://latex.codecogs.com/png.latex?P_0%3D70%2C000
    "P_0=70,000") whales in 1976. Model this population by starting with
    the constrained growth model we derived in class and save your
    functions in a file named `whales.py`. Then, inside the Jupyter
    notebook, visualize the whale population as a function of time (in
    units of years) using a line plot. Then, revise the model to
    consider harvesting the whales as a percentage of
    ![rM](https://latex.codecogs.com/png.latex?rM "rM"). Give various
    values for this percentage that lead to extinction and other values
    that lead to increases in population. Estimate the **maximum
    sustainable yield**, or the percentage of
    ![rM](https://latex.codecogs.com/png.latex?rM "rM") that gives a
    constant population in the long term.

3.  Develop a two-compartment model for one dose of aspirin, where the
    rate of change of absorption from the stomach to the plasma is
    proportional to the volume of the stomach and to the difference of
    the aspirin concentrations in the stomach and plasma. Check the
    effect of three stomach sizes, 400 milliliters, 500 milliliters, and
    600 milliliters. Plot the original one compartment model and the
    results for the three stomach sizes on the same graph for
    comparison.

4.  In an attempt to quickly raise the drug concentration in a person’s
    body, sometimes doctors give a patient a **loading dose**, which is
    an initial dosage that is much higher than the maintenance dosage. A
    loading dose for Dilantin is three doses — 400 milligrams, 300
    milligrams, and 300 milligrams two hours apart. Twenty-four hours
    after the loading dose, normal dosage of 100 milligrams every eight
    hours begins. Develop a model for this dosage regime. Plot the
    results of the original model and your modified model on the same
    graph and then discuss the following questions:
    
    1.  Is there a risk of breaching the toxicity threshold?
    
    2.  How much sooner does the concentration reach the therapeutic
        range compared to the conventional dosing schedule?

## How to submit

**To lock in your submission time**, export your notebook to PDF and
upload the PDF file to the assignment posting on
Blackboard.

<img src="../img/jupyterlab_export_to_pdf.png" style="display: block; margin: auto;" />

**In addition, be sure to save, commit, and push your final result so
that everything is synchronized to GitHub.** I may want to inspect your
source files directly and run your notebook, so it’s very important that
the files in your homework repository match what I see in the PDF export
uploaded to Blackboard.
