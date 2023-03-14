# A super simple python code that uses ydata_profiling to build out a report

import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport

# use ' df = pd.read_csv("FILE_PATH") ' for csv files

df = pd.read_excel("FILE_PATH")
profile = ProfileReport(df,title = "Data Report") # Name this whatever you want
profile.to_file('Report.html') # Point the file to wherever you want it to write


# Thats it. you will get a nice detailed breakdown of your data in the html file.

# Try it out!

