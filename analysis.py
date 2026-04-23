# ============================================
# Biological Data Analysis — Python & Pandas
# Author: Victoria Djana
# Description: Exploratory analysis of a
# fictional proteomics dataset
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# ── 1. LOAD DATA ──
df = pd.read_csv("data/proteomics_example.csv", index_col=0)
print(f"Dataset loaded: {df.shape[0]} proteins × {df.shape[1]} samples")

# ── 2. DATA CLEANING ──
# Check missing values
missing = df.isnull().sum()
print(f"\​​​​​​​​​​​​​​​​
