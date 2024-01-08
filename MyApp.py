import streamlit as st
st.set_page_config(page_title='Dogs')
st.header("Dogs images")
col1,col2=st.columns(2)
with col1:
  st.subheader("PUPPY")
  st.image("./puppy.jpeg",caption="Puppy",width=300,use_column_width=True)
  st.write("Puppies are cute")
with col2:
  st.subheader("Twin Dogs")
  st.image("./twindogs.jpeg",caption="Twin Cats",width=300,use_column_width=True)
  st.write("Twin Dogs are cute")
