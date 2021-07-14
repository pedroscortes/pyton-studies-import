import plotly.graph_objects as go

age=[18, 25, 30, 40]
avg_wage=[800, 5000, 7500, 21000]
population=[300, 1000, 250, 150],

fig = go.Figure(data=[go.Scatter(
    x="age", y="avg_wage",
    mode='markers',
    marker=dict(
        color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)',
               'rgb(44, 160, 101)', 'rgb(255, 65, 54)'],
        opacity=[1, 0.8, 0.6, 0.4],
        size="population",
    )
)])

fig.show()