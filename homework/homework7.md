Homework 7
================
Due: December 7, 2018 @ 11:59pm

## Instructions

[Obtain the GitHub repository](https://classroom.github.com/a/XOALlp1O)
you will use to complete the homework assignment, which contains the
starter Jupyter notebook file `homework7.ipynb`. The notebook template
provides space for you to answer each question. Your notebook should run
without error when you select **Restart Kernel and Run All
Cells**:

<img src="../img/jupyterlab_restart_kernel_and_run_all.png" style="display: block; margin: auto;" />

When you’re done, save your file, then stage, commit, and push (upload)
it to GitHub, and then follow the instructions in the [How to
submit](#how-to-submit) section.

## Questions

### Diffusion simulation

For questions 1 and 2, use the code provided to you in the **heat
diffusion** lecture notebook,
<https://github.com/jkglasbrenner/cds411-course-materials/blob/master/class_notes/heat_diffusion>,
as a starting point.

1.  Starting with diffusion code provided to you, implement the other
    two kinds of boundary conditions described in the chapter, those
    being **absorbing** boundary conditions and **periodic** boundary
    conditions. The **absorbing** boundary condition should assume a
    constant value of ![25\\text{
    }^{\\circ}\\text{C}](https://latex.codecogs.com/png.latex?25%5Ctext%7B%20%7D%5E%7B%5Ccirc%7D%5Ctext%7BC%7D
    "25\\text{ }^{\\circ}\\text{C}") on the boundary. Re-calculate the
    animation for all three boundary conditions and discuss the
    similarities and differences in the output.
    
    When implementing the other boundary conditions, you should do this
    by extending one of the already existing functions in the
    simulation. Your changes should not remove the ability to use the
    other boundary conditions; instead your code should allow the user
    to select any of the three boundary conditions by changing one of
    the inputs to this function.

2.  Instead of using the formula for diffusion in the section “Heat
    Diffusion,” employ the filter in Figure 10.2.13. Thus, to obtain the
    value at a site for time
    ![t+1](https://latex.codecogs.com/png.latex?t%2B1 "t+1"), we add 25%
    of the site’s temperature to the selected site at time
    ![t](https://latex.codecogs.com/png.latex?t "t"), 12.5% to each of
    its north, east, south, and west neighbor cells at time
    ![t](https://latex.codecogs.com/png.latex?t "t"), and 6.25% to each
    of the northeast, southeast, southwest, and northwest corner cells
    at time ![t](https://latex.codecogs.com/png.latex?t "t"). This sum
    is called a **weighted sum** with each nutrition value carrying a
    particular weight as indicated. Revise the model using this
    configuration and then run both unweighted and weighted versions of
    the simulation, creating animations for each and then discussing the
    similarities and differences. For each simulation run, use
    **reflecting** boundary conditions.
    
    Run simulations for three different cases:
    
    1.  Using the same input parameters provided in chapter 10.2 of the
        textbook.
    
    2.  Starting with the chapter 10.2 parameters, change the ambient
        temperature from ![25\\text{
        }^{\\circ}\\text{C}](https://latex.codecogs.com/png.latex?25%5Ctext%7B%20%7D%5E%7B%5Ccirc%7D%5Ctext%7BC%7D
        "25\\text{ }^{\\circ}\\text{C}") to ![10\\text{
        }^{\\circ}\\text{C}](https://latex.codecogs.com/png.latex?10%5Ctext%7B%20%7D%5E%7B%5Ccirc%7D%5Ctext%7BC%7D
        "10\\text{ }^{\\circ}\\text{C}").
    
    3.  Starting with the chapter 10.2 parameters, change the
        temperature for the hot spots from ![50\\text{
        }^{\\circ}\\text{C}](https://latex.codecogs.com/png.latex?50%5Ctext%7B%20%7D%5E%7B%5Ccirc%7D%5Ctext%7BC%7D
        "50\\text{ }^{\\circ}\\text{C}") to ![100\\text{
        }^{\\circ}\\text{C}](https://latex.codecogs.com/png.latex?100%5Ctext%7B%20%7D%5E%7B%5Ccirc%7D%5Ctext%7BC%7D
        "100\\text{ }^{\\circ}\\text{C}").
    
    Close with a couple of remarks discussing how each change affected
    how diffusion propagates in the simulation (consider both the
    changes in input parameters as well as going from an unweighted sum
    to a weighted sum).

### Forest fire simulation

For question 3, use the code provided to you in the **forest fire**
lecture notebook,
<https://github.com/jkglasbrenner/cds411-course-materials/blob/master/class_notes/forest_fire>,
as a starting point.

3.  Revise the fire simulation so that **a tree takes two time steps to
    burn completely instead of one step**. After implementing the
    change, re-run the simulation using the default input parameters
    (see notebook) and generate an animation. Then, reduce `prob_tree`
    by at least 0.1 units and run the simulation a second time (this
    should be separate from the first). Create and watch the animation
    for this run.
    
    After running the simulations, discuss any differences you see
    between these two runs. Then, explain whether this change to the
    model make it more or less likely for the entire forest to burn down
    compared to the original implementation, all else being equal.

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
