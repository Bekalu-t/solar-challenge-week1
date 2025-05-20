import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.utils import load_data, plot_boxplot
import streamlit as st
import pandas as pd

# Set page title
st.title("Solar Potential Dashboard: Cross-Country Comparison")

# Load data
df = load_data()

# Widget to select countries
all_countries = ['Benin', 'Sierra Leone', 'Togo']
selected_countries = st.multiselect(
    "Select Countries to Compare",
    options=all_countries,
    default=all_countries
)

# Ensure at least one country is selected
if not selected_countries:
    st.warning("Please select at least one country.")
else:
    # Boxplot for GHI
    st.subheader("GHI Comparison")
    fig = plot_boxplot(df, 'GHI', selected_countries)
    st.pyplot(fig)

    # Top regions table (mean GHI)
    st.subheader("Top Regions by Average GHI")
    avg_ghi = df[df['Country'].isin(selected_countries)].groupby('Country')['GHI'].mean().sort_values(ascending=False)
    top_regions = avg_ghi.reset_index()
    top_regions.columns = ['Country', 'Average GHI (W/m²)']
    top_regions['Average GHI (W/m²)'] = top_regions['Average GHI (W/m²)'].round(2)
    st.dataframe(top_regions, use_container_width=True)