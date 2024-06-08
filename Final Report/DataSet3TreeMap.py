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
    Survey = ["Ranking: "+ str(x) for x in Survey]
    
    values =     [3,2,4,1,1,3,2,2,4,5]
    pop_colors = [3,2,4,1,1,3,2,2,4,5]
    df = pd.DataFrame(
        dict(Order=Order, Genus=Genus, Survey=Survey,ColorRanks =pop_colors )
    )
    df["All Groups"] = "All Groups" 
    
    fig = px.treemap(df, path=[px.Constant('All Groups'), 'Order', 'Genus','Survey'],
                     values=values, color="ColorRanks",
                     color_continuous_scale='viridis')

    fig.update_layout(
        #treemapcolorway = ["steelblue"],
        margin = dict(t=50, l=25, r=25, b=25),
        font = dict(family="Arial", size=50))
    fig.show() 
    '''
    1 2 3 4 5
    5 4 3 2 1
    
    '''