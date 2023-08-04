import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.title("Resources:")
st.sidebar.info(
    """
    - GitHub repository: [streamlit_flood](https://github.com/keanteng/streamlit_flood)
    - Data sources: [Flood Data](https://www.water.gov.my/)
    """
)

st.sidebar.title("Created By:")
st.sidebar.info(
    """
  Khor Kean Teng | Intern, DGA, JPS, Bank Negara Malaysia | [GitHub](https://github.com/keanteng) | [LinkedIn](https://www.linkedin.com/in/khorkeanteng/)
    """
)

# Customize page title
st.title("👋Welcome")

st.markdown(
    """
    This is a multipage app that uses [Streamlit](https://streamlit.io) to visualize flood incidents in Malaysia from 2015 - 2022. In this app you can find different pages that visualize the data in different ways. 
    The data for the chart is obtained from the annual report published by the Department of Irrigation and Drainage Malaysia (JPS). The app is also powered by some feature develop by 
    [mapaction/flood mapping tool](https://github.com/mapaction/flood-mapping-tool) and [opengeos/streamlit-geospatial](https://github.com/opengeos/streamlit-geospatial) that make use of 
    Google Earth Engine funtionality. 
    """
)

st.info("👈 Check out my Git repository for installation instruction")

st.header("Documentation")

markdown = """
## A. Flood Mapping Tool
## B. Workflow
"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
