import pandas as pd

def load_and_clean_data():
    inlinks_df = pd.read_csv('data/SL_inlinks.csv')
    outlinks_df = pd.read_csv('data/SL_outlinks.csv')

    # Clean the data by removing duplicates and dropping rows with missing targets
    inlinks_df.drop_duplicates(inplace=True)
    outlinks_df.drop_duplicates(inplace=True)

    inlinks_df.dropna(subset=['Target'], inplace=True)
    outlinks_df.dropna(subset=['Target'], inplace=True)

    inlinks_df.to_csv('data/cleaned_SL_inlinks.csv', index=False)
    outlinks_df.to_csv('data/cleaned_SL_outlinks.csv', index=False)

    print("Data cleaning complete. Cleaned files saved as 'cleaned_SL_inlinks.csv' and 'cleaned_SL_outlinks.csv'.")

if __name__ == "__main__":
    load_and_clean_data()
