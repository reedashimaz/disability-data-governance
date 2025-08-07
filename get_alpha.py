import pandas as pd
import numpy as np
import krippendorff

def prep(file, coder):
    df = pd.read_csv(file)
    df = df[['Code', 'Quote']].copy()
    df['Code'] = df['Code'].astype(str).str.strip()
    df['Quote'] = df['Quote'].astype(str).str.strip()
    df['Coder'] = coder
    return df

print(prep('KBT_MZC.csv', 'MZC'))