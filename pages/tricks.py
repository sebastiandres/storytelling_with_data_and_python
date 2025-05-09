import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

st.title("Tricks")

st.write("""
requires: matplotlib
Use fig.text to reference x, y coordinates from 0 to 1.
Use ax.text to reference x, y coordinates from the axis limits.
""")

st.code("""
ax.spines[["top", "right"]].set_visible(False)
""")


