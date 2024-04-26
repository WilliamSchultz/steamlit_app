import pandas as pd
import streamlit as st

df = pd.read_csv('https://github.com/WilliamSchultz/steamlit_app/blob/main/allb.csv?raw=true')

df = df[['domain', 'title', 'category', 'brand', 'url', 'items', 'rev']]

# -- Set page config
#st.set_page_config(page_title='Grips')

# Title the app
#st.header('Grips product analysis')

#app main image
#image = Image.open('F:\DYMO NA App\images\logo.svg.PNG')
#st.image(image,
        #use_column_width=True )

#st.markdown ('##')

#App title

st.title("Grips product analysis")
#st.markdown('##')

#Slidebar filter
#st.sidebar.header("Choose your product")

# Create filters
st.write("## Filter Data")
rev_range = st.select_slider("Select Revenue Range", options=range(0, 301, 50))
selected_brand = st.selectbox("Select Brand", df["brand"].unique())

# Apply filters
filtered_df = df[(df["rev"] >= rev_range) & (df["brand"] == selected_brand)]

# Display filtered data
st.write("## Filtered Data")
st.write(filtered_df)





#st.dataframe(df)

