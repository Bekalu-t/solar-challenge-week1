import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    """Load and combine cleaned datasets from Benin, Sierra Leone, and Togo."""
    benin_df = pd.read_csv('data/benin-malanville.csv')
    sierra_leone_df = pd.read_csv('data/sierraleone-bumbuna.csv')
    togo_df = pd.read_csv('data/togo-dapaong_qc.csv')

    benin_df['Country'] = 'Benin'
    sierra_leone_df['Country'] = 'Sierra Leone'
    togo_df['Country'] = 'Togo'

    df_combined = pd.concat([benin_df, sierra_leone_df, togo_df], ignore_index=True)
    df_combined['Timestamp'] = pd.to_datetime(df_combined['Timestamp'])
    return df_combined

def plot_boxplot(df, metric, countries):
    """Generate a boxplot for the specified metric and countries."""
    plt.figure(figsize=(8, 5))
    sns.set_style('darkgrid')
    df_filtered = df[df['Country'].isin(countries)]
    sns.boxplot(x='Country', y=metric, data=df_filtered, palette='Set3')
    plt.title(f'{metric} by Country')
    plt.xlabel('Country')
    plt.ylabel(f'{metric} (W/m²)')
    return plt.gcf()