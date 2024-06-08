import plotly.graph_objects as go

labels = ['Not Started','Genetic Extraction','Fertilisation','Embryo Development']
values = [10,40,20,30]
colors = ["lightgrey","mediumturquoise","lightgreen","yellowgreen"]
fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                             insidetextorientation='radial',marker=dict(colors=colors),
                             title="Dinosaurs Development Status Proportional Percentage Pie Graph"
                             )])
fig.update_layout(
    font = dict(family="Arial", size=35))

fig.show()