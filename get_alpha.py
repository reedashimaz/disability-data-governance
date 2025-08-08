import pandas as pd
import numpy as np
import krippendorff

def prep_dataframe(file, coder):
    df = pd.read_csv(file)
    df = df[['Code', 'Quote']].copy()
    df['Code'] = df['Code'].astype(str).str.strip()
    df['Quote'] = df['Quote'].astype(str).str.strip()
    df['Coder'] = coder
    return df

def get_alpha(mzc_codes, rsh_codes):
    mzc_df = prep_dataframe(mzc_codes, 'MZC')
    rsh_df = prep_dataframe(rsh_codes, 'RSH')
    df = pd.concat([mzc_df, rsh_df], ignore_index=True)
    coders = df['Coder'].unique()
    quotes = df['Quote'].unique()
    codes = df['Code'].unique()
    # List of all quote and code pairs
    pairs = [(q, c) for q in quotes for c in codes]
    matrix = []
    for coder in coders:
        row = []
        for quote, code in pairs:
            applied = (
                not df[
                    (df.Coder == coder) &
                    (df.Quote == quote) &
                    (df.Code == code)
                ].empty
            )
            row.append(1 if applied else 0)
        matrix.append(row)
    matrix = np.array(matrix)

    alpha = krippendorff.alpha(matrix, level_of_measurement='nominal')
    print(f"Overall Krippendorff's alpha: {alpha:.3f}")
    return alpha

if __name__ == "__main__":
    get_alpha("MZC_codes.csv", "RSH_codes.csv")


