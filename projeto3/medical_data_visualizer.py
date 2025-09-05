import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1 Read the dataset into a DataFrame
df = pd.read_csv('medical_examination.csv')

# 2 Calculate BMI and create a new column 'overweight' (1 = overweight, 0 = not overweight)
BMI = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = (BMI > 25).astype(int)

# 3 Normalize cholesterol and glucose (1 = good, 0 = normal/bad)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4 Function to draw categorical plot
def draw_cat_plot():
    # 5 Reshape data so we can count each variable by cardio
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )

    # 6 Group and count by cardio, variable, and value
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    # 7 e 8 Create a bar plot with cardio as column split
    fig = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
    ).fig

    # 9 Save the figure and return it
    fig.savefig('catplot.png')
    return fig


# 10 Function to draw heat map
def draw_heat_map():
    # 11 Clean the data (remove outliers and wrong values)
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &  # valid blood pressure
        (df['height'] >= df['height'].quantile(0.025)) &  # remove very small height
        (df['height'] <= df['height'].quantile(0.975)) &  # remove very large height
        (df['weight'] >= df['weight'].quantile(0.025)) &  # remove very low weight
        (df['weight'] <= df['weight'].quantile(0.975))    # remove very high weight
    ]

    # 12 Calculate correlation matrix
    corr = df_heat.corr()

    # 13 Create a mask for the upper triangle (to avoid duplicate values)
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14 Create matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 8))

    # 15 Draw the heatmap with annotations
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5},
        ax=ax
    )

    # 16 Save the figure and return it
    fig.savefig('heatmap.png')
    return fig
