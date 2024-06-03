import pandas as pd
import plotly.express as px

class DataReader:
    def __init__(self,file):
        self.df = pd.read_csv(file)
        self.


