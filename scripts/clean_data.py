import pandas as pd

def load_and_clean_data():
    # Load the data files
    inlinks_df = pd.read_excel('data/all_nhc_inlinks.xlsx')
    outlinks_df = pd.read_excel('data/all_nhc_outlinks.xlsx')

    # Remove duplicates
    inlinks_df.drop_duplicates(inplace=True)
    outlinks_df.drop_duplicates(inplace=True)

    # Handle missing values
    inlinks_df.dropna(subset=['Target'], inplace=True)
    outlinks_df.dropna(subset=['Target'], inplace=True)

    # Save cleaned data
    inlinks_df.to_csv('data/cleaned_nhc_inlinks.csv', index=False)
    outlinks_df.to_csv('data/cleaned_nhc_outlinks.csv', index=False)

    print("Data cleaning complete. Cleaned files saved as 'cleaned_nhc_inlinks.xlsx' and 'cleaned_nhc_outlinks.xlsx'.")

if __name__ == "__main__":
    load_and_clean_data()
