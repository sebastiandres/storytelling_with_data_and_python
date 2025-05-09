import streamlit as st
import matplotlib.pyplot as plt
from highlight_text import ax_text, fig_text

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

st.title("Text with multiple colors")

st.write("""
requires: matplotlib, highlight_text  
Use highlight_text.fig_text to use figure coordinates (from 0 to 1).  
Use highlight_text.ax_text to use axis coordinates (from the axis limits - depends on the xlims and ylims).  

How to use multiple colors?  
Create highlight_textprops, a list of text property dictionaries: 
each dictionary defines the properties of the text to be colored (all regular matplotlib text properties are supported).

Each text to be colored is defined between <>.
""")

# Define the text to be colored.
colors = ["blue", "green", "red"]
highlight_textprops = [
    {"color": colors[0], 'fontweight': 'bold', "fontsize":20, "alpha": 0.5},
    {"color": colors[1], 'fontweight': 'bold', "backgroundcolor": "lightgrey", 'rotation': 45, "ha": "center", "va": "center"},
    {"color": colors[2], 'fontweight': 'bold', "bbox":dict(boxstyle='square,pad=0.2', color='black')}
]

fig_or_ax = st.selectbox("Method", options=["fig_text", "ax_text"])

c1, c2, c3 = st.columns([1,1,10])
x = c1.number_input("x", value=0.5)
y = c2.number_input("y", value=0.5)
default_text = "The iris dataset contains 3 species:\n<setosa>, <versicolor>, and  < virginica >"
text = c3.text_input("text", value=default_text)

c1, c2, c3 = st.columns([1,1,1])
c1.write("First colored text")
c1.code(highlight_textprops[0], wrap_lines=True)
c2.write("Second colored text")
c2.code(highlight_textprops[1], wrap_lines=True)
c3.write("Third colored text")
c3.code(highlight_textprops[2], wrap_lines=True)

fig, ax = plt.subplots(figsize=(2,3))


fig, ax = plt.subplots(layout="tight")

if fig_or_ax == "fig_text":
    method = fig_text
else:
    method = ax_text

# Some arbitrary lims, to show that the text is centered.
ax.set_xlim(-1, 2)
ax.set_ylim(0, 3)

# Actual plotting.
method(
x=x, y=y, s=text,
fontsize=10, 
color='black',
ha='center',
va='center',
highlight_textprops=highlight_textprops,
)


st.pyplot(fig)

st.divider()

st.markdown("[Official documentation](https://github.com/znstrider/highlight_text)")