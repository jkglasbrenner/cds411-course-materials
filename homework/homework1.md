Homework 1
================

## Instructions

Obtain the GitHub repository you will use to complete the homework
assignment, which contains the starter Jupyter notebook file
`homework1.ipynb`. The notebook template provides space for you to
answer each question. Your notebook should run without error when you
select **Restart Kernel and Run All
Cells**:

<img src="../img/jupyterlab_restart_kernel_and_run_all.png" style="display: block; margin: auto;" />

When you’re done, save your file, then stage, commit, and push (upload)
it to GitHub, and then follow the instructions in the [How to
submit](#how-to-submit) section.

## Questions

1.  Create variables that are assigned the following values:
    
    1.  A list called `ages` with values 19, 21, 21, and 20.
    
    2.  A list called `names` with three values “Ruth,” “Callixte,” and
        “Talishia.”

2.  Define a function named `sine_compute` that takes `x` as input and
    returns the value of the mathematical expression
    ![3\\sin(x-1)+2](https://latex.codecogs.com/png.latex?3%5Csin%28x-1%29%2B2
    "3\\sin(x-1)+2"). Evaluate `sine_compute` when
    ![x=5](https://latex.codecogs.com/png.latex?x%3D5 "x=5").

3.  Assign 1 to a variable named `d`. Then, in a loop that executes 10
    times, update the value of `d` to be double what it was before the
    previous iteration. Before executing the loop, determine the final
    value by hand so you can check your work (write this out in a
    Markdown block). Then test your code, and type `print(d)` to display
    d’s final value to check your work.

4.  The following code computes a distance and a time for several steps
    in a loop and prints the results:
    
    ``` python
    import math  # only needed if math hasn't been imported yet
    
    dist = 0
    for i in range(1, 8):
        dist += 2.25
        time = (24.5 - math.sqrt(600.25 - 19.6 * dist)) / 9.8
        print("For distance {0}, time = {1}".format(dist, time))
    ```
    
    Copy this code into your notebook and run it to see the output.
    Next, modify the code so that you do not need to initialize `dist`
    with `dist = 0`, but will still get the same results.

5.  Define a function called `ln_compute` that returns the value of the
    mathematical expression
    ![\\ln(3x+2)](https://latex.codecogs.com/png.latex?%5Cln%283x%2B2%29
    "\\ln(3x+2)"). Then, write a loop that creates a variable `k` that
    takes on integer values from 1 through 8. Inside the loop, print the
    value of `k` and `ln_compute(k)` in the style of the `print()`
    statement used in question 4.

6.  Create the following `numpy` arrays and assign them each to a unique
    variable. Only the first exercise can be created manually, the rest
    must use function(s) to generate the sequence (in some instances,
    you may need to generate sequences individually and join them
    afterwards).
    
    1.  Manually create a `numpy` array with the numbers 47, 35, 22, and
        10.
    
    2.  Generate a `numpy` array with the numbers 1 through 12.
    
    3.  Generate a `numpy` array with the numbers 4, 8, 12, 16, …, 84.
    
    4.  Generate a `numpy` array with eleven 3’s followed by eleven 4’s
        followed by twelve 5’s.
    
    5.  Generate a `numpy` array with the numbers 7, 6, 5, …, 1, 19, 2,
        4, 6, 8, …, 30.

7.  The code snippet below generates the `temperatures` matrix:
    
    ``` python
    import numpy as np  # only if numpy hasn't been imported
    
    t = [57, 64, 88, 81, 61, 88, 86, 76, 63, 89, 70, 76]
    temperatures = np.reshape(t, newshape=(3, 4))
    ```
    
    Slice the `numpy` array to return each of the following. Remember,
    Python starts indexing from `0`, meaning row 1 is index 0\!
    
    1.  The element at row 3, column 3.
    
    2.  The element at row 2, column 1.
    
    3.  The entire 3rd row.
    
    4.  The entire 2nd column.
    
    5.  Columns 2 through 4 of rows 1 and 3.

8.  The code snippet below generates the `air_pressure` matrix:
    
    ``` python
    import numpy as np  # only if numpy hasn't been imported
    
    air_pressure = np.ones((5, 5, 3))
    air_pressure[:, :, 1] = 0.99
    air_pressure[:, :, 2] = 0.98
    ```
    
    “Height” is what we call the third index. Slice the `numpy` array to
    return each of the following. Remember, Python starts indexing from
    `0`, meaning row 1 is index 0\!
    
    1.  The element at row 3, column 3 at height 3.
    
    2.  The element at row 4, column 2 at height 1.
    
    3.  The entire 3rd row for all columns and heights.
    
    4.  All rows and columns for the lowest height.
    
    5.  All heights for row 4, columns 2 through 5.

9.  Perform the following vector operations
    
    1.  With one assignment statement, make `my_matrix` be a 2-by-4
        matrix of all zeros.
    
    2.  With one assignment statement, make the first row of `my_matrix`
        be the sequence of positive integers 1, 3, 5, 7.
    
    3.  Return the product of 3 by every element of `my_matrix` without
        changing `my_matrix`.
    
    4.  Return the square root of every element of `my_matrix` without
        changing `my_matrix` (hint, `numpy` has its own version of
        square root).
    
    5.  Add 2 to every element of `my_matrix`, changing the value of
        `my_matrix` to hold those increased numbers.

10. Use list comprehensions to a “list of lists” named `pairs_list`
    containing a column of x-values, which are positive integers from 1
    through 9, and a second column with values of
    ![3\\sqrt{x}](https://latex.codecogs.com/png.latex?3%5Csqrt%7Bx%7D
    "3\\sqrt{x}"), where the ![x](https://latex.codecogs.com/png.latex?x
    "x") is taken from the first column.

11. Create a new file named `rectangle.py` in the same directory as your
    Jupyter notebook. In this file, define a function called
    `circumference` that returns the circumference of a rectangle with
    parameters for length and width, `l` and `w`, respectively. Save the
    file. Then, **in your Jupyter notebook**, import the file you
    created and test the function you just defined by having it return
    the circumference of a rectangle with dimensions 3 and 4.2,
    respectively.

12. Compute the following matrix-vector exercises using `numpy`:
    
    1.  Generate a 4-by-2 matrix `mA`, where the `i - j` element is the
        **sum** of `i` and `j`. For example, after forming `mA`,
        `mA[3, 2]` should be 5, which is 3 + 2.
    
    2.  Generate a 4-by-2 matrix `mO` of all ones.
    
    3.  Give matrix sum of `mA` and `mO`.
    
    4.  Define a one-dimensional array `u` with elements 2 and 7.
    
    5.  Define a one-dimensional array `v` with elements 5 and 3.
    
    6.  Compute the dot product of `u` and `v`.
    
    7.  Generate a 2-by-3 matrix `mB`, where the `i - j` element is the
        **difference** of `i` and `j`, `i - j`.
    
    8.  Give the matrix product of `mA` and `mB`.

13. Use matplotlib to plot the function
    ![e^{\\sin(x)}](https://latex.codecogs.com/png.latex?e%5E%7B%5Csin%28x%29%7D
    "e^{\\sin(x)}") from -3 to 3, where
    ![x](https://latex.codecogs.com/png.latex?x "x") is stepped through
    in increments of 0.1. Label the x axis as `t` and the y axis as
    ![e^{\\sin(x)}](https://latex.codecogs.com/png.latex?e%5E%7B%5Csin%28x%29%7D
    "e^{\\sin(x)}").

14. Load the provided `iris.csv` file into Pandas and write code that
    reproduces the following
    plot:
    
    <img src="../img/hw1_iris_plot.svg" width="80%" style="display: block; margin: auto;" />
    
    **Hint:** For some relevant examples, take a look at
    <https://scipython.com/book/chapter-7-matplotlib/examples/>.

15. Load the provided `gapminder_all.csv` file into Pandas. Determine
    which countries saw the largest increase and the largest decrease in
    life expectancy between 1987 and 1992.

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
