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
rev_range = st.slider('Select revenue range', min_value=df['rev'].min(), max_value=df['rev'].max(), value=(df['rev'].min(), df['rev'].max()))
selected_brand = st.selectbox('Select brand', df['brand'].unique())

# Apply filters to the data
filtered_df = df[(df['rev'] >= rev_range[0]) & (df['rev'] <= rev_range[1])]
if selected_brand:
    filtered_df = filtered_df[filtered_df['brand'] == selected_brand]

# Display the filtered data
st.write(filtered_df)




#st.dataframe(df)

