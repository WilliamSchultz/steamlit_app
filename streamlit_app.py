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

# Create two columns for filters
filter_col1, filter_col2 = st.columns(2)

# Filter for the "rev" column
with filter_col1:
    st.write('### Filter by Revenue:')
    min_rev = st.slider('Min Revenue', min_value=0, max_value=250, value=0)
    max_rev = st.slider('Max Revenue', min_value=0, max_value=250, value=250)

# Filter for the "brand" column
with filter_col2:
    st.write('### Filter by Brand:')
    selected_brands = st.multiselect('Select Brands', df['brand'].unique())

# Apply filters to the dataframe
filtered_df = df[(df['rev'] >= min_rev) & (df['rev'] <= max_rev) & df['brand'].isin(selected_brands)]

# Display the filtered dataframe
st.write(filtered_df)
```

#st.dataframe(df)

