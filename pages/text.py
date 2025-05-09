import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

st.title("Text")

st.write("""
requires: matplotlib
Use fig.text to reference x, y coordinates from 0 to 1.
Use ax.text to reference x, y coordinates from the axis limits.
""")

fig_or_ax = st.selectbox("fig or ax", options=["fig", "ax"])
c1, c2, c3 = st.columns([1,1,10])
x = c1.number_input("x", value=0.5)
y = c2.number_input("y", value=0.5)
s = c3.text_input("s", value="Hello, World!")
c1, c2, c3 = st.columns([1,1,1])
alpha = c1.number_input("alpha", value=1.0, min_value=0.0, max_value=1.0, step=0.1)
backgroundcolor = c2.color_picker("backgroundcolor", value="#ffffff")
#bbox = 
color = c3.color_picker("color", value="#000000")
c1, c2, c3 = st.columns([1,1,1])
fontfamily = c1.selectbox("fontfamily", options=["serif", "sans-serif", "cursive", "fantasy", "monospace"])
fontsize = c2.selectbox("fontsize", options=["xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large"])
fontweight = c3.selectbox("fontweight", options=["ultralight", "light", "normal", "regular", "book", "medium", "roman", "semibold", "demibold", "demi", "bold", "heavy", "extra bold", "black"])
c1, c2, c3 = st.columns([1,1,1])
fontstretch = c1.selectbox("fontstretch", options=["ultra-condensed", "extra-condensed", "condensed", "semi-condensed", "normal", "semi-expanded", "expanded", "extra-expanded", "ultra-expanded"])
fontstyle = c2.selectbox("fontstyle", options=["normal", "italic", "oblique"])
fontvariant = c3.selectbox("fontvariant", options=["normal", "small-caps"])
c1, c2, c3 = st.columns([1,1,1])
ha = c1.selectbox("ha", options=["left", "center", "right"])
va = c2.selectbox("va", options=["baseline", "bottom", "center", "center_baseline", "top"])
rotation = c3.number_input("rotation", value=0.0, min_value=-180.0, max_value=180.0, step=1.0)
c1, c2, c3 = st.columns([1,1,1])
zorder = c3.number_input("zorder", value=0.0, min_value=0.0, max_value=100.0, step=1.0)


fig, ax = plt.subplots(figsize=(2,3))
kwargs = {
    "alpha": alpha,
    "backgroundcolor": backgroundcolor,
    "color": color,
    "fontfamily": fontfamily,
    "fontsize": fontsize,
    "fontweight": fontweight,
    "fontstretch": fontstretch,
    "fontstyle": fontstyle,
    "fontvariant": fontvariant,
    "ha": ha,
    "va": va,
    "rotation": rotation,
    "zorder": zorder,
}
if fig_or_ax == "fig":
    fig.text(x, y, s, **kwargs)
else:
    ax.text(x, y, s, **kwargs)

st.pyplot(fig)

st.divider()

st.markdown("[Official documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html)")