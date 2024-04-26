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

# Filter for Revenue range
rev_range = st.slider('Select Revenue Range', min_value=0, max_value=30000, step=10, value=(0, 30000))

# Filter for Brand selection
brands = data['Brand'].unique().tolist()
selected_brand = st.selectbox('Select Brand', brands)

# Filtered data based on the selected filters
filtered_data = data[(data['Rev'] >= rev_range[0]) & (data['Rev'] <= rev_range[1])]
if selected_brand:
    filtered_data = filtered_data[filtered_data['Brand'] == selected_brand]

# Display the filtered data in a table
st.write(filtered_data)




#st.dataframe(df)

