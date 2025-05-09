import streamlit as st

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
c1, c2, c3 = st.columns(3)
#st.page_link("your_app.py", label="Home", icon="🏠")
c1.page_link("pages/text.py", label="text")
c2.page_link("pages/cooler_text.py", label="text with multiple colors")
c3.page_link("pages/arrows.py", label="arrows")

st.markdown("---")

c1, c2, c3 = st.columns(3)
c1.page_link("pages/bar.py", label="bar")
c2.page_link("pages/barh.py", label="barh")
c3.page_link("pages/meh.py", label="meh")

st.markdown("---")

c1, c2, c3 = st.columns(3)
c1.page_link("pages/line.py", label="line")
c2.page_link("pages/scatter.py", label="scatter")
c3.page_link("pages/area.py", label="area")

st.markdown("---")

st.page_link("pages/tricks.py", label="tricks", use_container_width=True)
