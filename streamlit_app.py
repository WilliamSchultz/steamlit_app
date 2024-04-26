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

# Create a slider filter for the "rev" column
rev_min = st.slider("Minimum Revenue", min_value=df["rev"].min(), max_value=df["rev"].max())
rev_max = st.slider("Maximum Revenue", min_value=df["rev"].min(), max_value=df["rev"].max())

# Create a selectbox filter for the "brand" column
selected_brand = st.selectbox("Select Brand", df["brand"].unique())

# Filter the data based on user selections
filtered_df = df[(df["rev"] >= rev_min) & (df["rev"] <= rev_max) & (df["brand"] == selected_brand)]

# Display the filtered data in a table
st.write(filtered_df)




#st.dataframe(df)

