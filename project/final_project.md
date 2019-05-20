Final project
================

## Table of contents

  - [Instructions](#instructions)
  - [Selecting your project](#selecting-your-project)
      - [System dynamics projects](#system-dynamics-projects)
      - [Cellular automata projects](#cellular-automata-projects)
      - [Data-driven projects](#data-driven-projects)
  - [Grade](#grade)
  - [Report guidelines](#report-guidelines)
      - [Sections in your Jupyter notebook
        report](#sections-in-your-jupyter-notebook-report)
          - [Analysis of the problem](#analysis-of-the-problem)
          - [Model design and solution](#model-design-and-solution)
          - [Results and conclusions](#results-and-conclusions)
      - [Other considerations](#other-considerations)
      - [Jupyter notebook examples](#jupyter-notebook-examples)
  - [How to submit](#how-to-submit)

## Instructions

For your final project for the course, you will select and implement
either a system dynamics model, a predictive data-driven model, or
cellular automata simulation. A list of project ideas is given below,
but you may propose another project that you find interesting. You will
write a report about your model in a Jupyter notebook that follows the
basic guidelines outlined in chapter 1.2 of your textbook, in particular
pages 10 and 11, see [report guidelines](#report-guidelines) for more
details.

Obtain the GitHub repository you will use to complete the final project,
which contains the starter Jupyter notebook file `final_project.ipynb`.
You are permitted to keep all of your code in the Jupyter notebook if
you like instead of moving code to external files, **but your
implementation must be organized into functions**. If you prefer to keep
the code in a separate `.py` file, that is fine as well. Finally, as
always, your notebook should run without error when you select **Restart
Kernel and Run All Cells**.

<table>

<tbody>

<tr>

<td align="center">

<p>

**Students are not allowed to collaborate in any way on the final
project.** **The code and written analysis you submit for the project
cannot come from or be adapted from a homework assignment, exercise, or
project you completed in another class, nor can it include code you find
online.**

</p>

</td>

</tr>

</tbody>

</table>

## Selecting your project

The lists below are system dynamics and cellular automata projects from
the textbook that are pre-approved and you can choose to do for your
final project. Predictive data-driven model projects require you to
propose a dataset and specify the quantity you want to predict, see the
[data-driven projects](#data-driven-projects) subsection for details.
Other projects in the textbook may be selected, but will require
approval and should be discussed with Dr. Glasbrenner.

**Only two students per system dynamics or cellular automata project
will be allowed. For data-driven projects, only one dataset per student
is permitted. Projects are first come, first serve.**

### System dynamics projects

  - **Projects from module 3.1**: 4, 6, 7

  - **Projects from module 4.2**: 1

  - **Projects from module 4.3**: 3, 4, 16

  - **Projects from module 7.1**: 1 (skipping parts *f*, *h*, and *j*,
    and verification part of *d*)

  - **Projects from module 7.3**: 1

### Cellular automata projects

  - **Projects from module 10.2**: 5, 6, 8

  - **Projects from module 10.3**: 10, 11, 12

  - **Projects from module 14.1**: 2

  - **Projects from module 14.6**: 1

### Data-driven projects

A data-driven project is permissible if it centers around finding the
best predictive model for a publicly available dataset through the use
of model selection techniques. The dataset needs to be large enough to
be interesting, but not so large that analysis cannot be completed in a
reasonable time on a desktop computer. It is okay if you start with a
fairly large dataset but filter it down to a more manageable size prior
to starting up your model building workflow.

**To get approval for a data-driven project, you will need to identify
the dataset you plan to use and specify the quantity you are going to
try and predict.** **The project *cannot* be a data-driven project you
worked on in any way for another class.**

The following is a short list of possible datasets for you to consider:

  - Medicare Provider Utilization and Payment Data:
    <https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/>

  - Chicago Data Portal — Crimes – 2001 to present:
    <https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2>

  - U.S. Department of Education — College Scorecard Dataset:
    <https://collegescorecard.ed.gov/data/>

  - NYC Taxi and Limousine Commission Trip Data:
    <http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml>

  - United States Census Bureau:
    <https://www.census.gov/data/data-tools.html>

  - Climatological Database for the World’s Oceans 1750 – 1850:
    <http://webs.ucm.es/info/cliwoc/>

There are also repositories of datasets and search engines for you to
look through if you are having trouble finding a dataset that interests
you. **Please note that not every dataset you may find is a reasonable
choice for the project**, make sure that you inspect the dataset
contents and discuss your choice with me beforehand.

  - UCI Machine Learning Repository:
    <https://archive.ics.uci.edu/ml/index.php>

  - US Government’s Open Data Site: <https://www.data.gov/>

  - Nature Scientific Data Recommended Data Repositories:
    <https://www.nature.com/sdata/policies/repositories>

  - Google Dataset Search: <https://toolbox.google.com/datasetsearch>

## Grade

Grading criteria for the written submission will be based on
model/simulation correctness, code and Jupyter notebook readability, and
the overall quality in each of the three sections of your report
outlined in the [report guidelines](#report-guidelines).

## Report guidelines

### Sections in your Jupyter notebook report

Your Jupyter notebook report should contain the following sections based
on pages 10 and 11 of your textbook:

#### Analysis of the problem

Here you present the background and context for the model that you are
going to implement. This includes, but is not limited to: What are your
primary scientific questions? What does the model simulate? What
background knowledge do we need to understand the model?

#### Model design and solution

This is where you describe your computational model and show how to
implement it. All important details should be included in this section.
As an example of what to include in this part of the report, review the
way Dr. Glasbrenner writes about the cellular automata simulations in
the lecture notebooks and the examples listed in the [Jupyter notebook
examples](#jupyter-notebook-examples) subsection.

If you are implementing a system dynamics model, be sure to include:

  - A stock/flow diagram of your system dynamics model

  - An explanation of what your parameters mean, and how can they be
    measured via experiment

  - The rate of change equations for each stock

If you are implementing a predictive data-driven model, be sure to
include:

  - Clear instructions for how to download the dataset or, even better,
    code that automates the process

  - A summary of the *data dictionary*, in particular you should explain
    the variables that are relevant to building your model and the
    variable that you are going to try and predict

  - The code you used to clean your dataset and prepare it for model
    building

If you are implementing a cellular automata simulation, be sure to
include:

  - What are the available grid states in the simulation and what are
    the state transition rules?

  - Are there any specific mathematical formulas that you’re making use
    of?

  - What do the input parameters mean, and are there any constraints on
    their values?

Regardless of your model/simulation choice, your Python code should be
explained so that I can follow your logic.

#### Results and conclusions

Here you discuss the outcomes of the model or simulation and interpret
the results. Your writeup should discuss and display representative
outputs from the simulation. This must consist of static visualizations
and, if appropriate, `matplotlib` animations. Regardless of the type of
model or simulation you implement, be sure to address and answer your
scientific questions by interpreting your model’s outputs.

For system dynamics simulations, your discussion and analysis should
include a parameter sweep of your model so that the range of possible
outcomes is well understood. You should prefer to use visualizations
such as line plots to present your results instead of printing tables.
In some instances tables may be appropriate, but if your table has more
than 10 rows, then it’s a good indication that you should probably use a
visualization instead.

For predictive data-driven models, you should present visualizations
that help the reader to better understand the way the data is
distributed in the dataset, i.e. perform a basic exploratory data
analysis. Then when discussing the predictive model itself, your
discussion and analysis should review the different scores you received
for your model and then conclude which model seems to perform best.
Statistical considerations, such as computing the standard error of the
mean of cross-validated scores, should also be included.

For cellular automata simulations, it is not sufficient to just present
animations and nothing else, you need to also present quantitative
trends observed in the simulations. Simulations with stochastic elements
**require** that you re-run the simulation multiple times with the same
inputs to gather statistics for the outputs. If your project is a direct
extension of the simulations from either chapter 10.2 or 10.3, you
should show how your modification changes things from the starting
baseline. Finally, address and answer your scientific questions by
interpreting your model’s outputs.

### Other considerations

  - Your Jupyter notebook report is expected to include Markdown blocks
    in order to create sections in your document and for “as-needed”
    markup, for example bolding and italicizing words, or for formatting
    any code snippets referenced in your discussion.

  - The Jupyter notebook should have a consistent writing style and a
    structure, meaning it should read like a report that you would type
    in a word processor, not like shorthand notes or answers to a
    classroom worksheet. Everything should be written using complete
    sentences.

  - All Python code is to be written and formatted so as to facilitate
    readability.
    
      - While I am not forcing you to use a style guide, you can consult
        the official Python style guide for recommendations:
        <https://www.python.org/dev/peps/pep-0008/>
    
      - An easy option to ensure readability is to use the *Black*
        Python code formatter to automatically restyle your code,
        install with `pip install black` and see the Black documentation
        for details: <https://black.readthedocs.io/en/stable/>

  - Assume that your audience for the report understands basic Python
    and the general concept of scientific modeling, but that they have
    not seen your particular model or scientific questions before. While
    writing, always ask yourself what this hypothetical audience member
    would need to know so that they don’t become lost.

  - The model or simulation is to be coded in Python (assume anyone
    running your code will have a full Anaconda installation available)
    and all included code must run without error.

  - If your model is building on code originally demonstrated in class,
    that is okay, but you must give credit by citing where in the class
    notes the code comes from.

  - Your function names and inputs should match the model or simulation
    you are implementing, i.e. if I implement the bungee jump model I
    shouldn’t have the main function for it named as
    `damped_oscillator`.

### Jupyter notebook examples

There are many quality examples of well-formatted Jupyter notebooks that
are available on the internet. A good example is the book [*Python Data
Science Handbook*](http://shop.oreilly.com/product/0636920034919.do),
which is [available in full on
Github](https://github.com/jakevdp/PythonDataScienceHandbook) and can be
[rendered interactively using
Binder](https://mybinder.org/v2/gh/jakevdp/PythonDataScienceHandbook/master).
Check out the first few sections of Chapter 3:

  - Chapter 3.1:
    <https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.01-Introducing-Pandas-Objects.ipynb>

  - Chapter 3.2:
    <https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.02-Data-Indexing-and-Selection.ipynb>

  - Chapter 3.3:
    <https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.03-Operations-in-Pandas.ipynb>

**If you are implementing a data-driven model, you cannot use any of the
datasets or examples found in this book\!**

## How to submit

**To lock in your submission time**, export your notebook to PDF and
upload the PDF file to the assignment posting on Blackboard. **In
addition, be sure to save, commit, and push your final result so that
everything is synchronized to GitHub.** I may want to inspect your
source files directly and run your notebook, so it’s very important that
the files in your homework repository match what I see in the PDF export
uploaded to Blackboard.

<table>

<tbody>

<tr>

<td align="center">

<p>

**I am unable to accept late submissions and failing to submit your
project by the deadline will result in an automatic zero for the final
project.** **I do not have any flexibility in this, as final grades are
due to the registrar 48 hours after the final exam time slot is over.**

</p>

</td>

</tr>

</tbody>

</table>
