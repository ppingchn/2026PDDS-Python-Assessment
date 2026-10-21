# 2026PDDS-Python-Assessment
This repository is create to evaluate the python coding capability from the student in Programming for Data-Driven System Course at National Tsing Hua University

# Noted for Student
Please fork this repository to your git repo by
```bash
git fork https://github.com/ppingchn/2026PDDS-Python-Assessment.git
```
And after that enjoy your python practice.

# Student Instructions

## Setup

Open a terminal in the repository root and install the required library:

```bash
python -m pip install -r requirements.txt
```

## Submit Your Solutions

Complete the Python list question in `python_list_src` and the pandas question in
`pandas_src`. You may rename the starter files, but each folder must contain
exactly one Python submission file. Do not add extra `.py` files to either folder.

Keep the required variable names from the questions because the testbenches use
them to check your results.

## Run the Testbenches

Run these commands from the repository root:

```bash
python -m unittest testbench.tb_list
python -m unittest testbench.tb_pd
```

