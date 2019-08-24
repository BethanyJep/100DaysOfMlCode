# # Assignment#2:
 
# Problem Statement:
# Step1: Study the Complete File Operations Lectures and Data Analysis Tecniques and Manipulation Lectures 
# (Section #4 and #5 of the Udemy Intern Kit).
 
# 1. Create a single .xlsx file with 10 sheets inside filled with dummy data.
# 2. Read the .xlsx file using pandas
# 3. Export every single sheet of the .xlsx file as a .csv file.
# (The Output should produce 10 .csv files that contains values of each sheet of .xlsx file respectively)
 
 
# Step2: Email the following files to amanda@takenmind.com within the deadline date:

# A. Code File (.py file)

# B. Input File (.xlsx file)
 
# The subject of your Email: <Your Name> - Assignment#2

import numpy as np
import pandas as pd

data  = pd.read_excel("assignments.xlsx")
data.head()