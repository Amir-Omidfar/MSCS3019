import pandas as pd
import plotly.express as px
df = pd.read_csv('data.csv')
Family = df["Family"]
Order = df["Order"]
English_Name = df["English Name"]
Category = df["Category"]
Scientific_Name = df["Scientific Name"]

Family = ["Family: "+x for x in Family ]
Order = ["Order: "+x for x in Order]
Category = ["Category: "+x for x in Category]
Scientific_Name = ["Scientific Name: "+x for x in Scientific_Name]
#English_Name = ["Name: "+x for x in English_Name]
df = pd.DataFrame(
    dict(Family=Family, Order=Order, English_Name=English_Name, 
         Category=Category, Scientific_Name = Scientific_Name)
)
df["All Groups"] = "All Groups" 

fig = px.treemap(df, path=['All Groups', 'Family', 'Order',
                            'Category', 'Scientific_Name'])
fig.update_traces(root_color="aliceblue")
fig.update_layout(
    treemapcolorway = ["palegreen","steelblue"],
    margin = dict(t=50, l=25, r=25, b=25))
fig.show()