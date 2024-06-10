import moduleA as ma
print(ma.say_hi('Gal'))

import pandas as pd
import seaborn as sns
import streamlit as st

st.write("""
# My first app
Hello *world!*
""")

st.date_input('Enter a Date: ')

df = sns.load_dataset('dowjones')
df = df.set_index('Date')
st.line_chart(df)




