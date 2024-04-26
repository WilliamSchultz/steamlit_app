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

data = df

# Create filters
with st.sidebar:
    st.write("### Filters")
    rev_range = st.slider("Revenue Range", min_value=0, max_value=500, value=(0, 500))
    selected_brand = st.selectbox("Brand", df['brand'].unique())

# Apply filters to the data
filtered_df = df[(df['rev'] >= rev_range[0]) & (df['rev'] <= rev_range[1]) & (df['brand'] == selected_brand)]

# Display the filtered data
st.write(filtered_df)



#st.dataframe(df)

