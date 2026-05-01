# We're importing every major library to make sure they all installed correctly
import pandas
import numpy
import matplotlib
import seaborn
import sklearn
import xgboost
import tensorflow
import joblib
import streamlit
import groq

# If we reach this line, everything imported without error
print("✅ All libraries imported successfully!")
print(f"Pandas version: {pandas.__version__}")
print(f"TensorFlow version: {tensorflow.__version__}")
print(f"Scikit-learn version: {sklearn.__version__}")