import streamlit as st
import numpy as np
import pandas as pd 
from sklearn.ensemble import RandomForestRegressor 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
# from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
import plotly.graph_objects as go
import pickle
import joblib

st.title('Predicting Energy Consumption')
st.header('CAISO Energy Market')
st.sidebar.title('Energy Consumption Of SDGE By The Hour')