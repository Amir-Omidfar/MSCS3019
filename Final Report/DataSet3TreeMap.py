from data_reader import DataReader
from collections import Counter
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

if __name__ == "__main__":
    df = pd.read_csv("3PublicInterest.csv")
    
    Order = df["Order/Suborder"]
    Genus = df["Genus"]
    Survey = df["Survey "]
   
    df = pd.DataFrame(
        dict(Order=Order, Genus=Genus, Survey=Survey)
    )
    df["All Groups"] = "All Groups" 

    fig = px.treemap(df, path=['All Groups', 'Order', 'Genus',
                                'Survey'])
    fig.update_traces(root_color="aliceblue")
    fig.update_layout(
        treemapcolorway = ["palegreen","steelblue"],
        margin = dict(t=50, l=25, r=25, b=25))
    fig.show() 
    