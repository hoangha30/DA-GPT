import streamlit as st
import pygwalker as pyg
from pygwalker.api.streamlit import StreamlitRenderer

def main():

    #Set up streamlit interface
    st.set_page_config(
        page_title="📈Interactive_Visualization_Tool📉", page_icon="📈📉", layout="wide"
    )

    st.header("📈Interactive_Visualization_Tool📉")
    st.write("### Welcome ")
    
    #Render pygwalker
    if st.session_state.get('df') is not None:
        pyg_app = StreamlitRenderer(st.session_state.df)
        pyg_app.explorer()

    else:
        st.info("Please upload a dataset to begin")

    

if __name__ == "__main__":
    main()