import streamlit as st
from bokeh.plotting import figure

# Sample data
x = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
y1 = [i**2 for i in x]
y2 = [10*i for i in x]

# Creating a new plot
p = figure(
    title='Sample Data Plot',
    x_axis_label='X Axis Label',
    y_axis_label='Y Axis Label')

# Adding a line
p.line(x, y1, legend_label='Line 1', line_width=2, color="navy")

# Adding circles
p.circle(x, y1, size=10, color="navy", alpha=0.5)

# Adding a fill between the line and the x-axis
p.varea(x=x, y1=y1, y2=y2, fill_color="purple", fill_alpha=0.4)

# Adding a second line
p.line(x, y2, legend_label='Line 2', line_width=2, color="orange")

# Adding crosses
p.cross(x, y2, size=10, color="orange", alpha=0.5)

# Displaying the plot
st.bokeh_chart(p, use_container_width=True)
