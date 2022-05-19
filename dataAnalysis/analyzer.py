from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
import statsmodels.api as sm

ytData = pd.read_csv('../webscraper/dataByYear.csv')

