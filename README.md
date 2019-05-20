CDS 411 course materials
================

[![](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jkglasbrenner/cds411-course-materials/master)

  - [Topic schedule](#topic-schedule)
  - [Readings](#readings)
  - [Homeworks](#homeworks)
  - [Final project](#final-project)
  - [Resources and links](#resources-and-links)
      - [Datacamp cheat
sheets](#datacamp-cheat-sheets)
      - [Software](#software)
  - [License](#license)

## Topic schedule

| Class | Topic                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     1 | [Course toolbox](https://nbviewer.jupyter.org/github/jkglasbrenner/cds411-course-materials/blob/master/class_notes/class01/class01_slides.pdf)                                                                                                                                                                                                                                                                                                                                                               |
|     2 | [Python fundamentals I](class_notes/class04/python_fundamentals.py)                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|     3 | [Python fundamentals II](https://nbviewer.jupyter.org/github/jkglasbrenner/cds411-course-materials/blob/master/class_notes/class03/class03_slides.pdf)                                                                                                                                                                                                                                                                                                                                                       |
|     4 | [Python for scientific computing I](https://nbviewer.jupyter.org/github/jkglasbrenner/cds411-course-materials/blob/master/class_notes/class04/class04_slides.pdf)                                                                                                                                                                                                                                                                                                                                            |
|     5 | [Python for scientific computing II](https://nbviewer.jupyter.org/github/jkglasbrenner/cds411-course-materials/blob/master/class_notes/class05/class05_notebook.ipynb)<br>[*Demo file:* `scientific_computing_with_numpy.py`](class_notes/class05/scientific_computing_with_numpy.py)                                                                                                                                                                                                                        |
|     6 | [Python for scientific computing III](https://nbviewer.jupyter.org/github/jkglasbrenner/cds411-course-materials/blob/master/class_notes/class06/class06_notebook.ipynb)                                                                                                                                                                                                                                                                                                                                      |
|     7 | [System dynamics models: Growth and decay](https://nbviewer.jupyter.org/github/jkglasbrenner/cds411-course-materials/blob/master/class_notes/class07/class07_notebook.ipynb)                                                                                                                                                                                                                                                                                                                                 |
|     8 | [System dynamics models: Growth and decay II](https://nbviewer.jupyter.org/github/jkglasbrenner/cds411-course-materials/blob/master/class_notes/class08/class08_notebook.ipynb)<br>[*Source file:* `bacteria.py`](class_notes/class08/bacteria.py)                                                                                                                                                                                                                                                           |
|     9 | [System dynamics models: Drug dosage I](https://nbviewer.jupyter.org/github/jkglasbrenner/cds411-course-materials/blob/master/class_notes/class09/class09_notebook.ipynb)<br>[*Source file:* `aspirin.py`](class_notes/class09/aspirin.py)                                                                                                                                                                                                                                                                   |
|    10 | [System dynamics models: Drug dosage II](https://nbviewer.jupyter.org/github/jkglasbrenner/cds411-course-materials/blob/master/class_notes/class10/class10_notebook.ipynb)<br>[*Source file:* `dilantin.py`](class_notes/class10/dilantin.py)                                                                                                                                                                                                                                                                |
|    11 | [System dynamics models: Damped oscillator and bungee jumping I](https://nbviewer.jupyter.org/github/jkglasbrenner/cds411-course-materials/blob/master/class_notes/class11/class11_notebook.ipynb)                                                                                                                                                                                                                                                                                                           |
|    12 | [System dynamics models: Damped oscillator and bungee jumping II](https://nbviewer.jupyter.org/github/jkglasbrenner/cds411-course-materials/blob/master/class_notes/class12/class12_notebook.ipynb)<br>[*Demo notebook:* Interactive undamped oscillator notebook](https://nbviewer.jupyter.org/github/jkglasbrenner/cds411-course-materials/blob/master/class_notes/class12/interactive_undamped_oscillator.ipynb)<br>[*Source file:* `undamped_oscillator.py`](class_notes/class12/undamped_oscillator.py) |
|    13 | [System dynamics models: Damped oscillator and bungee jumping III and shark competition model](https://nbviewer.jupyter.org/github/jkglasbrenner/cds411-course-materials/blob/master/class_notes/class13/class13_notebook.ipynb)<br>[*Source file:* `oscillator.py`](class_notes/class13/oscillator.py)<br>[*Source file:* `bungee.py`](class_notes/class13/bungee.py)<br>[*Source file:* `sharks.py`](class_notes/class13/sharks.py)                                                                        |
|    14 | [Data-driven modeling I](https://nbviewer.jupyter.org/github/jkglasbrenner/cds411-course-materials/blob/master/class_notes/class14/class14_notebook.ipynb)                                                                                                                                                                                                                                                                                                                                                   |
|    15 | [Data-driven modeling II](https://nbviewer.jupyter.org/github/jkglasbrenner/cds411-course-materials/blob/master/class_notes/class15/class15_notebook.ipynb)                                                                                                                                                                                                                                                                                                                                                  |
|    16 | [Data-driven modeling III](https://nbviewer.jupyter.org/github/jkglasbrenner/cds411-course-materials/blob/master/class_notes/class16/class16_notebook.ipynb)<br>[*Source file:* `bootstrap.py`](class_notes/class16/bootstrap.py)                                                                                                                                                                                                                                                                            |
|    17 | [Data-driven modeling IV](https://nbviewer.jupyter.org/github/jkglasbrenner/cds411-course-materials/blob/master/class_notes/class17/class17_notebook.ipynb)                                                                                                                                                                                                                                                                                                                                                  |
|    18 | [Monte Carlo simulations I](https://nbviewer.jupyter.org/github/jkglasbrenner/cds411-course-materials/blob/master/class_notes/class18/class18_notebook.ipynb)<br>[*Practice notebook:* Module 9.1: Quick Review Questions](https://nbviewer.jupyter.org/github/jkglasbrenner/cds411-course-materials/blob/master/class_notes/class18/module_9-1_practice_questions.ipynb)                                                                                                                                    |
|    19 | [Monte Carlo simulations II](https://nbviewer.jupyter.org/github/jkglasbrenner/cds411-course-materials/blob/master/class_notes/class19/class19_notebook.ipynb)<br>[*Source file:* `mc_integration.py`](class_notes/class19/mc_integration.py)                                                                                                                                                                                                                                                                |
|    20 | [Monte Carlo simulations III](https://nbviewer.jupyter.org/github/jkglasbrenner/cds411-course-materials/blob/master/class_notes/class20/class20_notebook.ipynb)                                                                                                                                                                                                                                                                                                                                              |
|    21 | [Cellular automata I: Heat diffusion](https://nbviewer.jupyter.org/github/jkglasbrenner/cds411-course-materials/blob/master/class_notes/heat_diffusion/heat_diffusion_notebook.ipynb)                                                                                                                                                                                                                                                                                                                        |
|    22 | [Cellular automata II: Forest fire](https://nbviewer.jupyter.org/github/jkglasbrenner/cds411-course-materials/blob/master/class_notes/forest_fire/forest_fire_notebook.ipynb)<br>[*Source file:* `forest_fire.py`](class_notes/forest_fire/forest_fire.py)                                                                                                                                                                                                                                                   |
|    23 | [Cellular automata III: Ants](https://nbviewer.jupyter.org/github/jkglasbrenner/cds411-course-materials/blob/master/class_notes/ants/ants_notebook.ipynb)                                                                                                                                                                                                                                                                                                                                                    |
|    24 | [Course wrap-up](https://nbviewer.jupyter.org/github/jkglasbrenner/cds411-course-materials/blob/master/class_notes/wrapup/wrapup_notebook.ipynb)                                                                                                                                                                                                                                                                                                                                                             |

## Readings

| Week | Book                                                                                                                          | Assignment                                                                                                                                                                                                      |
| ---: | :---------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    1 | ![Introduction to Computational Science](img/shiflet_cover.gif)                                                               | Read all of chapters 1.1 and 1.2                                                                                                                                                                                |
|    2 | [![Automate the Boring Stuff with Python by Al Sweigart](img/automate_cover_medium.png)](https://automatetheboringstuff.com/) | **Supplement**<br>Chapters 1 through 8 cover the material in the **Python fundamentals** classes in more depth and with a focus on helping beginners.                                                           |
|    2 | [![Think Python by Allen Downey](img/think_python_medium.png)](http://greenteapress.com/thinkpython/html/index.html)          | **Supplement**<br>Chapters 2, 3, 5, 7, 8, 10, 11, 12, and 14 cover the material in the **Python fundamentals** classes. This book is a reference manual for Python, and covers things at a more advanced level. |
|    3 | [An introduction to Numpy and Scipy by M. Scott Shell](https://engineering.ucsb.edu/~shell/che210d/numpy.pdf)                 | Read from the beginning up until the end of the Statistics section on page 19                                                                                                                                   |
|    4 | ![Introduction to Computational Science](img/shiflet_cover.gif)                                                               | Read all of chapters 2.2 and 2.3                                                                                                                                                                                |
|    5 | ![Introduction to Computational Science](img/shiflet_cover.gif)                                                               | Read all of chapter 2.5                                                                                                                                                                                         |
|    6 | ![Introduction to Computational Science](img/shiflet_cover.gif)                                                               | Read all of chapter 3.2                                                                                                                                                                                         |
|    9 | ![Introduction to Computational Science](img/shiflet_cover.gif)                                                               | Read all of chapters 8.2 and 8.3                                                                                                                                                                                |
|   10 | ![Introduction to Computational Science](img/shiflet_cover.gif)                                                               | Read all of chapter 9.2                                                                                                                                                                                         |
|   11 | ![Introduction to Computational Science](img/shiflet_cover.gif)                                                               | Read all of chapters 9.3 and 9.5                                                                                                                                                                                |
|   12 | ![Introduction to Computational Science](img/shiflet_cover.gif)                                                               | Read all of chapter 10.2                                                                                                                                                                                        |
|   13 | ![Introduction to Computational Science](img/shiflet_cover.gif)                                                               | Read all of chapter 10.3                                                                                                                                                                                        |

## Homeworks

| \# | Description                                                                                        |
| -: | :------------------------------------------------------------------------------------------------- |
|  1 | [**Python fundamentals** and **Python for scientific computing** exercises](homework/homework1.md) |
|  2 | [System dynamics: growth and decay models](homework/homework2.md)                                  |
|  3 | [System dynamics: oscillatory motion models](homework/homework3.md)                                |
|  4 | [Data-driven modeling](homework/homework4.md)                                                      |
|  5 | [Monte Carlo simulations: integration and random number generation](homework/homework5.md)         |
|  6 | [Monte Carlo simulations: random walk](homework/homework6.md)                                      |
|  7 | [Cellular automata simulations](homework/homework7.md)                                             |

## Final project

**Instructions:** [project/final\_project.md](project/final_project.md)

## Resources and links

### Datacamp cheat sheets

[Datacamp](https://datacamp.com) has put together a series of [*Python
for Data Science* cheat
sheets](https://www.datacamp.com/community/data-science-cheatsheets)
that you can use as a quick reference during the class. The most
relevant ones have been downloaded to this repository and are linked
below:

| Cheat sheet                                                                                                                                                     | Description                                   |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------- |
| [![Python for Data Science Cheat Sheet - Jupyter Notebook](img/datacamp-numpy-basics.png)](cheatsheets/datacamp-numpy-basics.pdf)                               | Basics of the Jupyter Notebook                |
| [![Python for Data Science Cheat Sheet - NumPy Basics](img/datacamp-matplotlib-data-visualization.png)](cheatsheets/datacamp-matplotlib-data-visualization.pdf) | NumPy Basics                                  |
| [![Python for Data Science Cheat Sheet - SciPy - Linear Algebra](img/datacamp-scipy-linear-algebra.png)](cheatsheets/datacamp-scipy-linear-algebra.pdf)         | SciPy - Linear Algebra                        |
| [![Python for Data Science Cheat Sheet - Matplotlib](img/datacamp-jupyter-notebook-basics.png)](cheatsheets/datacamp-jupyter-notebook-basics.pdf)               | Data visualization with Matplotlib            |
| [![Python for Data Science Cheat Sheet - Seaborn](img/datacamp-seaborn-data-visualization.png)](cheatsheets/datacamp-seaborn-data-visualization.pdf)            | Data visualization with Seaborn               |
| [![Python for Data Science Cheat Sheet - Importing Data](img/datacamp-importing-data.png)](cheatsheets/datacamp-importing-data.pdf)                             | Importing Data                                |
| [![Python for Data Science Cheat Sheet - Pandas](img/datacamp-pandas-data-wrangling.png)](cheatsheets/datacamp-pandas-data-wranglings.pdf)                      | Data transformation and reshaping with Pandas |
| [![Python for Data Science Cheat Sheet - Scikit-Learn](img/datacamp-scikit-learn.png)](cheatsheets/datacamp-scikit-learn.pdf)                                   | Machine learning with Scikit-Learn            |

### Software

The following software is not required for participating in the course,
but may be useful in your
workflow.

<table>

<thead>

<tr>

<th style="text-align:left;">

Software

</th>

<th style="text-align:left;">

OS

</th>

<th style="text-align:left;">

Description

</th>

</tr>

</thead>

<tbody>

<tr>

<td style="text-align:left;">

[GitKraken<br>![Gitkraken](img/gitkraken-logo.png)](https://www.gitkraken.com/git-client)

</td>

<td style="text-align:left;">

Windows<br>macOS<br>Linux

</td>

<td style="text-align:left;">

A graphical interface for using git. Cross-platform, works with GitHub,
and free to use for educational purposes. Cheatsheets available:

<ul>

<li>

<a href='cheatsheets/gitkraken-cheat-sheet.pdf'>GitKraken cheat
sheet</a>

</li>

<li>

<a href='cheatsheets/gitkraken-for-github-users-cheat-sheet.pdf'>GitKraken
for GitHub users cheat sheet</a>

</li>

</ul>

</td>

</tr>

<tr>

<td style="text-align:left;">

[GitHub Desktop<br>![GitHub
Desktop](img/github-desktop-logo.svg)](https://desktop.github.com)

</td>

<td style="text-align:left;">

Windows<br>macOS

</td>

<td style="text-align:left;">

A graphical interface for interacting with GitHub, built by GitHub. User
documentation from GitHub is
available:

<ul>

<li>

<a href='https://help.github.com/desktop/guides/getting-started-with-github-desktop/'>Getting
Starting with GitHub
Desktop</a>

</li>

<li>

<a href='https://help.github.com/desktop/guides/contributing-to-projects/'>Contributing
to projects with GitHub Desktop</a>

</li>

</ul>

</td>

</tr>

<tr>

<td style="text-align:left;">

[Visual Studio Code<br>![Visual Studio
Code](img/vscode-logo.png)](https://code.visualstudio.com/)

</td>

<td style="text-align:left;">

Windows<br>macOS<br>Linux

</td>

<td style="text-align:left;">

A cross-platform and open-source integrated development environment
(IDE) for programming. Uses a plugin system called Extensions to add
support for different languages and for interfacing with git and GitHub.
At a minimum, you should install the [official extension for
Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
There are also [introductory tutorial videos
available](https://code.visualstudio.com/docs/getstarted/introvideos).

</td>

</tr>

<tr>

<td style="text-align:left;">

[PyCharm<br>![PyCharm](img/pycharm-logo.png)](https://jetbrains.com/pycharm)

</td>

<td style="text-align:left;">

Windows<br>macOS<br>Linux

</td>

<td style="text-align:left;">

A cross-platform integrated development environment (IDE) designed
specifically for programming in Python. Comes with many useful features
enabled. Has a plugin ecosystem, but unlike Visual Studio Code they can
be treated as optional. There are [introductory tutorial videos
available](https://www.jetbrains.com/pycharm/documentation/pycharm-videos.html).
As a current student, you get a free professional license for the editor
if you [fill out and submit this
form](https://www.jetbrains.com/shop/eform/students).

</td>

</tr>

</tbody>

</table>

## License

[![Creative Commons
License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)

Unless otherwise noted, the course materials in this repository are
licensed under a [Creative Commons Attribution-ShareAlike 4.0
International License](http://creativecommons.org/licenses/by-sa/4.0/).
