import streamlit as st
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool
import random

# Function to create random connections between points
def random_connections(x, y):
    connections = list(zip(x, y))
    random.shuffle(connections)
    x, y = zip(*connections)
    return x, y

# Sample data
x = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
y = [i**2 for i in x]

# Randomly connecting the points
x_rand, y_rand = random_connections(x, y)

# Creating a ColumnDataSource
source = ColumnDataSource(data=dict(x=x, y=y))

# Creating a new plot
p = figure(
    title='Enhanced Plot with Tooltips and Area Chart',
    x_axis_label='X Axis Label',
    y_axis_label='Y Axis Label',
    tools="hover",  # Adding hover tool
)

# Adding lines with random connections
p.line(x_rand, y_rand, legend_label='Random Line', line_width=2, color="green")

# Adding circles for the data points with tooltips
p.circle('x', 'y', size=10, color="blue", alpha=0.5, source=source)

# Configuring the hover tool
p.hover.tooltips = [("X", "@x"), ("Y", "@y")]

# Adding an area chart
p.varea(x='x', y1='y', y2=0, color="red", alpha=0.3, source=source)

# Displaying the plot
st.bokeh_chart(p, use_container_width=True)
