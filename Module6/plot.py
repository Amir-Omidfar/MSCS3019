import plotly.express as px
import pandas as pd

data = {
    "category": ["species", "subspecies","subspecies","subspecies","subspecies",
                 "species",
                 "species", "subspecies","subspecies","subspecies","subspecies","subspecies"],
    "English Name":["Common Ostrich", "", "", "", "",
                    "Somali Ostrich",
                    "Greater Rhea", "", "", "", "", ""],
    "Scientific Name":["Struthio camelus", "Struthio camelus camelus","Struthio camelus syriacus",
                       "Struthio camelus massaicus","Struthio camelus australis", "Struthio molybdophanes",
                        "Rhea americana", "Rhea americana araneipes", "Rhea americana americana", "Rhea americana nobilis",
                         "Rhea americana albescens", "Rhea americana intermedia" ],
    "Order": ["Struthioniformes Struthionidae (Ostriches)",
              "Struthioniformes","Struthioniformes","Struthioniformes",
              "Struthioniformes","Struthioniformes","Rheiformes","Rheiformes","Rheiformes","Rheiformes","Rheiformes","Rheiformes"],
    "Family": ["","Struthionidae (Ostriches)","Struthionidae (Ostriches)","Struthionidae (Ostriches)","Struthionidae (Ostriches)"
               ,"Struthionidae (Ostriches)","Rheidae (Rheas)","Rheidae (Rheas)","Rheidae (Rheas)","Rheidae (Rheas)","Rheidae (Rheas)","Rheidae (Rheas)"]
}


Category = ["species", "subspecies","subspecies","subspecies","subspecies",
                 "species",
                 "species", "subspecies","subspecies","subspecies","subspecies","subspecies"]
English_Name = ["Common Ostrich", "None", "None", "None", "None",
                    "Somali Ostrich",
                    "Greater Rhea", "None", "None", "None", "None", "None"]
Scientific_Name = ["Struthio camelus", "Struthio camelus camelus","Struthio camelus syriacus",
                       "Struthio camelus massaicus","Struthio camelus australis", "Struthio molybdophanes",
                        "Rhea americana", "Rhea americana araneipes", "Rhea americana americana", "Rhea americana nobilis",
                         "Rhea americana albescens", "Rhea americana intermedia" ]

Order = ["Struthioniformes Struthionidae (Ostriches)",
              "Struthioniformes","Struthioniformes","Struthioniformes",
              "Struthioniformes","Struthioniformes","Rheiformes","Rheiformes","Rheiformes","Rheiformes","Rheiformes","Rheiformes"]

Family = ["None", "Struthionidae (Ostriches)","Struthionidae (Ostriches)","Struthionidae (Ostriches)","Struthionidae (Ostriches)"
               ,"Struthionidae (Ostriches)","Rheidae (Rheas)","Rheidae (Rheas)","Rheidae (Rheas)","Rheidae (Rheas)","Rheidae (Rheas)","Rheidae (Rheas)"]




df = pd.DataFrame(
    dict(Family=Family, Order=Order, English_Name=English_Name, Scientific_Name=Scientific_Name, Category=Category)
)
df["All Ostriches"] = "All Ostriches" # in order to have a single root node
print(df)
fig = px.icicle(df, path=['All Ostriches', 'Category', 'English_Name', 'Order'])
fig.update_traces(root_color='lightgrey')
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()