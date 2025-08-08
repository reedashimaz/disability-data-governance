import pandas as pd
mzc_files = ['KBT_MZC.csv', 'LPA_MZC.csv', 'SSSK_MZC.csv']
rsh_files = ['KBT_RSH.csv', 'LPA_RSH.csv', 'SSSK_RSH.csv']
def merge(file_list, output_file):
    df_all = []
    for file in file_list:
        df = pd.read_csv(file)
        df_all.append(df)
    merged = pd.concat(df_all, ignore_index=True)
    merged.to_csv(output_file, index=False)

merge(mzc_files, 'MZH_codes.csv')
merge(rsh_files, 'RSH_codes.csv')