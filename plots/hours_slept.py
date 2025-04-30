
import plotly.express as plt
import pandas as pd


df = pd.read_csv('../york/sleep.csv')
print(df)


title = 'Sleeping Habits'
fig = plt.bar(df, x='Month', y='Hours', title=title)

fig.update_layout(
    font_family="Monospace",
    font_color="black",
    title_font_family="Monospace",
    title_font_color="black",
    title=dict(text=title, font=dict(size=32), automargin=True)
)

fig.show()


from plotly.offline import plot
import plotly.graph_objs as go

fig = go.Figure()
scatter = go.Bar(df)
fig.add_trace(scatter)
plt_div = plot(fig, output_type='div')