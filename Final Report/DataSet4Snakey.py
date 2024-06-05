from data_reader import DataReader
from collections import Counter
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

if __name__ == "__main__":
    #data_reader_set4 = DataReader("Final Report/4DevelopmentStatus.csv")
    df = pd.read_csv("4DevelopmentStatus.csv")
    rows,cols = df.shape
    columns_set_list = []
    all_colors = ["whitesmoke", "limegreen", "orangered", "blue", "purple"]
    color = []
    for column in df.columns[:cols]:
        new_set = set()
        for variable in df[column]:
            new_set.add(variable)
        columns_set_list.append(new_set)
    label = []
    label_dict = {}
    count = 0
    for index,column_set in enumerate(columns_set_list):
        counter_dict = Counter(df[df.columns[index]])
        for item in column_set:
            label.append(item)
            color.append(all_colors[index])
            count+=1
            label_dict[item] = [count-1,counter_dict[item]]
    #print(label[0])
    label[0] = "Not Started"
    label[1] = "Genetic Extraction"
    label[2] = "Fertilisation"
    label[3] = "Embryo Development"
    label_dict["Not Started"][0] = 0
    label_dict["Genetic Extraction"][0] = 1
    label_dict["Fertilisation"][0] = 2
    label_dict["Embryo Development"][0] = 3

    #print("column set list: ", columns_set_list)
    print("df: ", df)
    #print("label dict: ", label_dict)
    #print("_____________________________________*********_____________________________")
    #print("label: " , label)
    source = [label_dict[item][0] for item in df[df.columns[0]]]
    target = [label_dict[item][0] for item in df[df.columns[1]]]
    value = [label_dict[item][1] for item in df[df.columns[1]]]
    for c in range(1,cols-1):
        for item in df[df.columns[c]]:
            source.append(label_dict[item][0])
        for item in df[df.columns[c+1]]:
            target.append(label_dict[item][0])
            value.append(label_dict[item][1])


    fig = go.Figure(data=[go.Sankey(
        node = dict(
        pad = 15,
        thickness = 20,
        line = dict(color = "black", width = 0.5),
        label = label,
        color = color
        ),
        link = dict(
        source = source,
        target = target,
        value = value
    ))])

    fig.update_layout(title_text="Snakey Diagram of Data Set #4 Development Status", font_size=20)
    fig.show()





