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

# Create filters for 'rev' column (select range) and 'brand' column
rev_range = st.slider("Select revenue range", float(data['rev'].min()), float(data['rev'].max()), (float(data['rev'].min()), float(data['rev'].max())))
selected_brand = st.selectbox("Select brand", data['brand'].unique())

# Apply filters to the data
filtered_data = data[(data['rev'] >= rev_range[0]) & (data['rev'] <= rev_range[1]) & (data['brand'] == selected_brand)]

# Display the filtered data table
st.write(filtered_data)


#st.dataframe(df)

