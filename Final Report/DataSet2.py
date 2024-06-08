import chart_studio.plotly as py
import plotly.figure_factory as ff
import pandas as pd


import plotly.graph_objects as go

fig = go.Figure(go.Indicator(
    mode = "number+gauge+delta", value = 220,
    domain = {'x': [0, 1], 'y': [0, 1]},
    delta = {'reference': 280, 'position': "top"},
    title = {'text':"<b>Profit</b><br><span style='color: gray; font-size:0.8em'>U.S. $</span>", 'font': {"size": 14}},
    gauge = {
        'shape': "bullet",
        'axis': {'range': [None, 300]},
        'threshold': {
            'line': {'color': "red", 'width': 2},
            'thickness': 0.75, 'value': 270},
        'bgcolor': "white",
        'steps': [
            {'range': [0, 150], 'color': "cyan"},
            {'range': [150, 250], 'color': "royalblue"}],
        'bar': {'color': "darkblue"}}))
fig.update_layout(height = 250)
fig.show()
"""

if __name__ == "__main__":
    df = pd.read_csv("2Investment.csv")
    order = df["Order/Suborder"]
    genus = df["Genus"]
    current_investment = df["Investment '22 ($M)"]
    projected_investment = df["Projected Investment '23 ($M)"]
    labels = [genus[i]+" "+order[i] for i in range(len(order))]
    ranges = [1.62,3.23,4.90]
    point = 2.45
    performance = [0] #value

    data = []
    for i in range(len(order)):
        new_dict = {}
        new_dict["label"] = labels[i]
        new_dict["sublabel"] = "Million $"
        new_dict["range"] = ranges
        new_dict["performance"] = projected_investment[i]
        new_dict["point"] = point
        data.append(new_dict)
    data = (
    {"label": "Revenue", "sublabel": "US$, in thousands",
    "range": [150, 225, 300], "performance": [220,270], "point": [250]},
    {"label": "Profit", "sublabel": "%", "range": [20, 25, 30],
    "performance": [21, 23], "point": [26]},
    {"label": "Order Size", "sublabel":"US$, average","range": [350, 500, 600],
    "performance": [100,320],"point": [550]},
    {"label": "New Customers", "sublabel": "count", "range": [1400, 2000, 2500],
    "performance": [1000, 1650],"point": [2100]},
    {"label": "Satisfaction", "sublabel": "out of 5","range": [3.5, 4.25, 5],
    "performance": [3.2, 4.7], "point": [4.4]}
    )
    
    data = tuple(data)
    fig = ff.create_bullet(
        data, titles='label', subtitles='sublabel', markers='point',
        measures='performance', ranges='range', orientation='v',
    )
    py.iplot(fig, filename='bullet chart from dict')

"""