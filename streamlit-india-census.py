import streamlit as st
import numpy as np  
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="India Census Data Analysis",layout="wide")

df=pd.read_csv("IndiaCensus.csv")
list_of_states=list(df["State"].unique())
list_of_states.insert(0,"Overall India")

st.sidebar.title("India Census Data Analysis")
selected_state=st.sidebar.selectbox("select the state",list_of_states)
primary=st.sidebar.selectbox("select the primary parameter",(df.columns[6:]))
secondary=st.sidebar.selectbox("select the secondary parameter",(df.columns[6:]))

plot=st.sidebar.button("plot graph")

if plot:
    st.text("you have selected {} as primary parameter and {} as secondary parameter".format(primary,secondary))
    st.text("size represent primary parameter and color represent secondary parameter")
    if selected_state=="Overall India":
        fig = px.scatter_mapbox(
            df,
            lat="Latitude",
            lon="Longitude",
            size=primary,
            color=secondary,
            zoom=4,
            hover_name="State",
            size_max=50,
            mapbox_style="carto-positron",
            color_continuous_scale=[
        (0.0, "blue"),
        (1.0, "yellow")
    ],
            width=800,
            height=800
        )

        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df=df[df["State"]==selected_state]
        fig=px.scatter_mapbox(state_df,lat="Latitude",lon="Longitude",size=primary,color=secondary,zoom=6,hover_name="District",color_continuous_scale=[
        (0.0, "blue"),
        (1.0, "yellow")
    ],size_max=50,mapbox_style="carto-positron",width=800,height=800)
        st.plotly_chart(fig,use_container_width=True)