import pandas as pd

def load_data():
    inlinks_df = pd.read_csv('data/SL_inlinks.csv')
    outlinks_df = pd.read_csv('data/SL_outlinks.csv')
    
    print("Inlinks DataFrame loaded with shape:", inlinks_df.shape)
    print("Outlinks DataFrame loaded with shape:", outlinks_df.shape)
    
    return inlinks_df, outlinks_df

if __name__ == "__main__":
    inlinks_df, outlinks_df = load_data()
