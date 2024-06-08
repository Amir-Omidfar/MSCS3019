import plotly.express as px



data=[[3.00,1.00,2.50,3.00,4.00,5.00], 
      [2.75,0.67,0.87,0.75,2.00,1.75],
      [2.92,0.89,1.96,2.25,3.34,3.92]]
fig = px.imshow(data,
                labels=dict(x="Dinosaurs Orders", y="Investment Analysis Categories", color="Final Score"),
                x=['Carnosaur', 'Ornithopod', 'Sauropod', 'Ceratopsian', 'Stegosaur','Theropod'],
                y=['Survey Ranks', 'Investment Shortcoming', 'Investment Potential'], 
                color_continuous_scale='viridis'
               )
fig.update_xaxes(side="top")
fig.update_layout(
    font = dict(family="Arial", size=40))



fig.show()


		





