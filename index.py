import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("train.csv")  # Make sure train.csv is in the same folder

# ===== Data Cleaning =====
# Check null values
print("Missing values before cleaning:\n", df.isnull().sum())

# Fill missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop(columns=['Cabin'], inplace=True)  # Too many missing values

# Remove duplicates
df.drop_duplicates(inplace=True)

# Summary statistics
print("\nDataset Summary:\n", df.describe())

# ===== Professional Plot Settings =====
sns.set_theme(style="whitegrid", palette="Set2")  # Nice clean look

def plot_fullsize(title, plot_func):
    """Wrapper to create full-screen, professional-looking plots."""
    plt.figure(figsize=(12, 8))
    plot_func()
    plt.title(title, fontsize=18, fontweight='bold')
    plt.xlabel(plt.gca().get_xlabel(), fontsize=14)
    plt.ylabel(plt.gca().get_ylabel(), fontsize=14)
    plt.tight_layout()
    plt.show()

# ===== Visualizations =====

# Survival count
plot_fullsize("Survival Count", lambda: sns.countplot(x='Survived', data=df))

# Survival by Gender
plot_fullsize("Survival by Gender", lambda: sns.countplot(x='Sex', hue='Survived', data=df))

# AgeDistribution
plot_fullsize("Age Distribution", lambda: sns.histplot(df['Age'], kde=True, bins=30))

# Class vsSurvival
plot_fullsize("Class vs Survival", lambda: sns.countplot(x='Pclass', hue='Survived', data=df))
