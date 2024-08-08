import pandas as pd

def combine_datasets():
    inlinks_df = pd.read_csv('data/cleaned_SL_inlinks.csv')
    outlinks_df = pd.read_csv('data/cleaned_SL_outlinks.csv')

    combined_df = pd.merge(inlinks_df, outlinks_df, left_on='Target', right_on='Target', how='left', suffixes=('_internal', '_external'))
    combined_df.to_csv('data/combined_SL_links.csv', index=False)

    print("Datasets combined and saved as 'combined_SL_links.csv'.")

if __name__ == "__main__":
    combine_datasets()
