import plotly.plotly as py
from plotly.graph_objs import *

if __name__ == "__main__":
    df = pd.read_csv("2Investment.csv")
    order = df["Order/Suborder"]
    genus = df["Genus"]
    current_investment = df["Investment '22 ($M)"]
    projected_investment = df["Projected Investment '23 ($M)"]

trace3 = {
  "uid": "7838af2e-4ea3-4aa6-bfe6-b76bbcca20e5", 
  "mode": "lines+markers+text", 
  "name": "ARP3", 
  "type": "scatter", 
  "x": [1, 2, 3], 
  "y": [2, 3, 3], 
  "marker": {"size": 20}, 
  "text": ["2", "3", "3"]
}
data = Data([trace1, trace2, trace3])
layout = {
  "title": {"text": "Bump chart"}, 
  "xaxis": {
    "type": "linear", 
    "range": [0.5, 3.2], 
    "autorange": True
  }, 
  "yaxis": {
    "type": "linear", 
    "range": [-0.6, 3.5], 
    "autorange": True
  }, 
  "autosize": True
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)

    