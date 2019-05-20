Homework 5
================

## Instructions

Obtain the GitHub repository you will use to complete the homework
assignment, which contains the starter Jupyter notebook file
`homework5.ipynb`. The notebook template provides space for you to
answer each question. Your notebook should run without error when you
select **Restart Kernel and Run All
Cells**:

<img src="../img/jupyterlab_restart_kernel_and_run_all.png" style="display: block; margin: auto;" />

When you’re done, save your file, then stage, commit, and push (upload)
it to GitHub, and then follow the instructions in the [How to
submit](#how-to-submit) section.

## Questions

### Monte Carlo integration

For questions 1 and 2, do the following:

<table>

<tbody>

<tr>

<td>

**a.** Starting with the Monte Carlo functions demoed in the class 21
notes,
<https://github.com/jkglasbrenner/cds411-course-materials/blob/master/class_notes/class21>,
modify the function so that it can compute the value of the requested
quantity. You should be able to specify the number of darts used in the
computation.

**b.** Run the function defined in Part a 10,000 times, computing the
mean of the results.

**c.** Use resampling to compute the standard error of the mean. Review
the code under the **Activity** header in the class 21 notes for a
refresher.

**d.** Visualize the distribution of values obtained in Part b. Your
figure should also plot a line representing the mean value and the upper
and lower bounds for the standard error of the mean.

</td>

</tr>

</tbody>

</table>

1.  An estimate of ![\\pi](https://latex.codecogs.com/png.latex?%5Cpi
    "\\pi"). The area of a circle is ![\\pi
    r^{2}](https://latex.codecogs.com/png.latex?%5Cpi%20r%5E%7B2%7D
    "\\pi r^{2}"), where ![r](https://latex.codecogs.com/png.latex?r
    "r") is the radius. The equation of a circle of radius
    ![r](https://latex.codecogs.com/png.latex?r "r") with center at the
    origin is
    ![x^{2}+y^{2}=r^{2}](https://latex.codecogs.com/png.latex?x%5E%7B2%7D%2By%5E%7B2%7D%3Dr%5E%7B2%7D
    "x^{2}+y^{2}=r^{2}"). Use a circle of radius 1. Consider the quarter
    of the circle in the first quadrant with ![0 \\leq x
    \\leq 1](https://latex.codecogs.com/png.latex?0%20%5Cleq%20x%20%5Cleq%201
    "0 \\leq x \\leq 1") and ![0 \\leq y
    \\leq 1](https://latex.codecogs.com/png.latex?0%20%5Cleq%20y%20%5Cleq%201
    "0 \\leq y \\leq 1"), and multiply your result by 4.

2.  An estimate of the volume of a sphere of radius 1 whose equation is
    ![x^{2}+y^{2}+z^{2}\\leq{}1](https://latex.codecogs.com/png.latex?x%5E%7B2%7D%2By%5E%7B2%7D%2Bz%5E%7B2%7D%5Cleq%7B%7D1
    "x^{2}+y^{2}+z^{2}\\leq{}1"). Consider the portion of the sphere
    with ![x
    \\geq 0](https://latex.codecogs.com/png.latex?x%20%5Cgeq%200
    "x \\geq 0"), ![y
    \\geq 0](https://latex.codecogs.com/png.latex?y%20%5Cgeq%200
    "y \\geq 0"), and ![z
    \\geq 0](https://latex.codecogs.com/png.latex?z%20%5Cgeq%200
    "z \\geq 0"); and multiply your result by 8. In the case of three
    dimensions, a point has three coordinates ![(x, y,
    z)](https://latex.codecogs.com/png.latex?%28x%2C%20y%2C%20z%29
    "(x, y, z)"). Notice that Monte Carlo integration is useful for
    dimensions beyond two.

### Random number sampling

For question 3, use the methods discussed in the chapter 9.3 of the
textbook chapter and in the
[class 21](https://github.com/jkglasbrenner/cds411-course-materials/blob/master/class_notes/class21)
and
[class 22](https://github.com/jkglasbrenner/cds411-course-materials/blob/master/class_notes/class22)
lecture notes.

3.  This question develops code for the rejection method with the
    probability density function ![f(x)=2\\pi\\sin(4\\pi
    x)](https://latex.codecogs.com/png.latex?f%28x%29%3D2%5Cpi%5Csin%284%5Cpi%20x%29
    "f(x)=2\\pi\\sin(4\\pi x)").
    
    1.  Define a Python function to represent the formula
        ![f(x)=2\\pi\\sin(4\\pi
        x)](https://latex.codecogs.com/png.latex?f%28x%29%3D2%5Cpi%5Csin%284%5Cpi%20x%29
        "f(x)=2\\pi\\sin(4\\pi x)"). For an example, see
        `cubic_function` defined in the `mc_integration.py` file:
        <https://github.com/jkglasbrenner/cds411-course-materials/blob/master/class_notes/class21/mc_integration.py>
    
    2.  Plot ![f(x)](https://latex.codecogs.com/png.latex?f%28x%29
        "f(x)") from 0.0 to 2.5, see Figure 9.3.12 in the textbook.
    
    3.  Assign to variable `rand` a uniform number from 0.0 to 0.25, the
        interval of interest in Figure 9.3.12.
    
    4.  Define a Python function called `rejection_method()` with no
        arguments that will return a random number using the rejection
        method. The algorithm for the rejection method is as follows:
        
          - If
            ![f(\\texttt{rand})](https://latex.codecogs.com/png.latex?f%28%5Ctexttt%7Brand%7D%29
            "f(\\texttt{rand})") is greater than a uniform random number
            from 0 to
            ![2\\pi\\sin(4\\pi/8)=2\\pi\\sin(\\pi/2)=2\\pi](https://latex.codecogs.com/png.latex?2%5Cpi%5Csin%284%5Cpi%2F8%29%3D2%5Cpi%5Csin%28%5Cpi%2F2%29%3D2%5Cpi
            "2\\pi\\sin(4\\pi/8)=2\\pi\\sin(\\pi/2)=2\\pi"), which is
            the maximum value of
            ![f(x)](https://latex.codecogs.com/png.latex?f%28x%29
            "f(x)"), return `rand`.
        
          - If the condition is false, we reject `rand` and search for
            another candidate.
        
        Implement this algorithm using a `while` loop in Python, such
        that you exit the loop only after a candidate that passes the
        test is found.
    
    5.  Use the function you built in the previous step to generate a
        list of 1000 random numbers from 0.0 to 0.25 sampled from the
        probability density function ![f(x)=2\\pi\\sin(4\\pi
        x)](https://latex.codecogs.com/png.latex?f%28x%29%3D2%5Cpi%5Csin%284%5Cpi%20x%29
        "f(x)=2\\pi\\sin(4\\pi x)") using the rejection method.
    
    6.  Display a histogram of these values.

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
