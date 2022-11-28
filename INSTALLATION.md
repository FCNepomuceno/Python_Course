# Installation

## Day 1

During the course we will work with [Google Collaboratory](https://colab.research.google.com). You will only need a web browser and Google account (e.g. GMail account).


However, some exercises we will have to be run on your local machine, therefore you will need an installation of **Python**, **VS Code** and **a couple of Python libraries** (numpy, pandas, jupyter, seaborn). 

Try to install these before the course. In case you have any problems, let me know in the beginning of the course.

### Windows

1. Install [a recent version of Python](https://apps.microsoft.com/store/detail/python-39/9P7QFQMJRFP7) from the Windows app store.

2. Install [VS Code](https://apps.microsoft.com/store/detail/visual-studio-code/XP9KHM4BK9FZ7Q) from the Windows app store.

3. Get a terminal (`cmd.exe`), change directory (`cd`) into a folder you have write access (like 'Documents' or a New Folder) to and create a new environment `venv` by running:

```
python -m venv venv
```

and then activate it by running on a command line

```
venv\Scripts\activate
```

4. Install packages into your environment

```
python -m pip install numpy pandas jupyter seaborn
```

If you run into problems with missing admin privileges, you might still be able to install Python and VS Code with `conda` distribution, see https://www.anaconda.com/products/distribution.

For help regarding the virtual environments, see https://realpython.com/python-virtual-environments-a-primer/.

### MacOS / Linux

1. Linux and MacOS contain a distribution of Python. Type `python3` into the command line to verify that.

2. You should install VS Code from the app store or https://code.visualstudio.com/download.

3. Create a new environment `venv` by typing into the terminal:

```
python3 -m venv venv
```

and then activate it by running on a command line

```
source venv/bin/activate
```

4. Install packages into your environment:

```
python -m pip install numpy pandas jupyter seaborn openpyxl requests
```

### Verify the installation

To verify your installation, download and run [test_python.py](test_python.py) on your terminal (`cmd.exe`)

```
python test_python.py
```

that should return `Great installation, thank you!` and no errors.
