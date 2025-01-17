import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as ex


data = pd.read_csv("heart.csv")

print(data.head())
print(data.dtypes)
print(data.info())
print(data.shape())
print(data.describe())
print(data.nunique())
print(data.isnull().sum())


# EDA Analysis



