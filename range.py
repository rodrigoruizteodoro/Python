import streamlit as st
import pandas as pd

st.title('Streamlit-serch ranges')

DATA_URL=('dataset.csv')

@st.cache
def load_data_byrange(startid,endid):
    data=pd.read_csv(DATA_URL)
    filtered_data_byrange=data[(data['index']>=startid)&(data['index']<=endid)]

    return filtered_data_byrange

startid=st.text_input('Star Index:')
endid=st.text_input('End Index:')
BtnRange=st.button('Serch by range')

if(BtnRange):
    filterbyrange=load_data_byrange(int(startid),int(endid))
    count_row=filterbyrange.shape[0]
    st.write(f"Total Items:{count_row}")

    st.dataframe(filterbyrange)
