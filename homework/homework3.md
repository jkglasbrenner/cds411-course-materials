Homework 3
================

## Instructions

Obtain the GitHub repository you will use to complete the homework
assignment, which contains the starter Jupyter notebook file
`homework3.ipynb`. The notebook template provides space for you to
answer each question. Your notebook should run without error when you
select **Restart Kernel and Run All
Cells**:

<img src="../img/jupyterlab_restart_kernel_and_run_all.png" style="display: block; margin: auto;" />

When you’re done, save your file, then stage, commit, and push (upload)
it to GitHub, and then follow the instructions in the [How to
submit](#how-to-submit) section.

## Questions

Use the leapfrog integration method when implementing the models in both
questions.

1.  Revise the [model of the motion of a **damped**
    spring](https://github.com/jkglasbrenner/cds411-course-materials/blob/master/class_notes/class15/oscillator.py)
    to account for air friction using Stoke’s friction instead of
    Newtonian friction. The formula for Stoke’s friction is
    
      
    ![F=bv](https://latex.codecogs.com/png.latex?F%3Dbv "F=bv")  
    
    where ![b](https://latex.codecogs.com/png.latex?b "b") is a constant
    and ![v](https://latex.codecogs.com/png.latex?v "v") is the velocity
    of the object. Implement your revised model in a function named
    `simulation` and save it in a file named `stokes.py`.
    
    After implementing the revised model, import it and choose
    parameters that fulfill the following
    relationship:
    
      
    ![b^{2}\>4k^{2}](https://latex.codecogs.com/png.latex?b%5E%7B2%7D%3E4k%5E%7B2%7D
    "b^{2}\>4k^{2}")  
    
    where ![k](https://latex.codecogs.com/png.latex?k "k") is the spring
    constant. Plot the length and velocity of the system as a function
    of time to confirm that the system is **overdamped**, meaning that
    oscillation is damped out.
    
    Then, choose parameters that fulfill the opposite
    condition:
    
      
    ![b^{2}\<4k^{2}](https://latex.codecogs.com/png.latex?b%5E%7B2%7D%3C4k%5E%7B2%7D
    "b^{2}\<4k^{2}")  
    
    Again, plot the length and velocity of the system as a function of
    time and confirm that the system is **underdamped**, meaning that
    the system does show oscillatory behavior.

2.  The restoring force for a nonlinear *hard* spring
    is:
    
      
    ![k(x-x\_{0})\\left\[1+a^{2}(x-x\_{0})^{2}\\right\]](https://latex.codecogs.com/png.latex?k%28x-x_%7B0%7D%29%5Cleft%5B1%2Ba%5E%7B2%7D%28x-x_%7B0%7D%29%5E%7B2%7D%5Cright%5D
    "k(x-x_{0})\\left[1+a^{2}(x-x_{0})^{2}\\right]")  
    
    where ![k](https://latex.codecogs.com/png.latex?k "k") is the spring
    constant, ![x](https://latex.codecogs.com/png.latex?x "x") is the
    spring length,
    ![x\_{0}](https://latex.codecogs.com/png.latex?x_%7B0%7D "x_{0}") is
    the equilibrium spring length, and
    ![a](https://latex.codecogs.com/png.latex?a "a") is a small
    constant. Similarly, the restoring force for a nonlinear *soft*
    spring
    is:
    
      
    ![k(x-x\_{0})\\left\[1-a^{2}(x-x\_{0})^{2}\\right\]](https://latex.codecogs.com/png.latex?k%28x-x_%7B0%7D%29%5Cleft%5B1-a%5E%7B2%7D%28x-x_%7B0%7D%29%5E%7B2%7D%5Cright%5D
    "k(x-x_{0})\\left[1-a^{2}(x-x_{0})^{2}\\right]")  
    
    Extend the [**undamped** model of the motion of a
    spring](https://github.com/jkglasbrenner/cds411-course-materials/blob/master/class_notes/class15/oscillator.py)
    by implementing both types of nonlinear springs. Place your revised
    model in a function named `simulation` and save it in a file named
    `nonlinear.py`. It should be possible using the function inputs for
    `simulation` to specify whether the model will use the standard
    linear spring based on Hooke’s Law, or one of the two nonlinear
    springs.
    
    After implementing the revised model, import it and choose three
    different values of ![a](https://latex.codecogs.com/png.latex?a "a")
    (remember, ![a](https://latex.codecogs.com/png.latex?a "a") is
    supposed to be small, meaning
    ![a\\ll{}1](https://latex.codecogs.com/png.latex?a%5Cll%7B%7D1
    "a\\ll{}1")). For the rest of the model parameters, use the default
    values shown in class for the undamped oscillator. Then, for each of
    those values of ![a](https://latex.codecogs.com/png.latex?a "a"),
    simulate the linear spring, the nonlinear hard spring, and the
    nonlinear soft spring and create plots of the length and velocity of
    the system as a function of time. Ensure that the plots allow the
    reader to easily compare and contrast the model behavior and better
    understand how adding a nonlinear term affects the idealized
    behavior of the linear spring.

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
