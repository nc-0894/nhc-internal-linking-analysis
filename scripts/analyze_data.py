import pandas as pd
import matplotlib.pyplot as plt

def analyze_data():
    combined_df = pd.read_csv('data/combined_SL_links.csv')
    
    # Print column names to verify
    print("Columns in combined DataFrame:", combined_df.columns)

    # Analysis: Top 10 Most Linked Internal Pages
    if 'Destination_internal' in combined_df.columns:
        top_internal_linked_pages = combined_df['Destination_internal'].value_counts().head(10)
        plt.figure(figsize=(10, 6))
        top_internal_linked_pages.plot(kind='bar')
        plt.title('Top 10 Most Linked Internal Pages')
        plt.xlabel('Page')
        plt.ylabel('Number of Links')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout(pad=2.0)
        plt.savefig('data/top_internal_linked_pages.png', bbox_inches='tight')
        plt.close()

        # Analyze sources for top internal linked pages
        top_internal_sources = combined_df[combined_df['Destination_internal'].isin(top_internal_linked_pages.index)]
        top_internal_sources = top_internal_sources['Source_internal'].value_counts().head(10)
        plt.figure(figsize=(10, 6))
        top_internal_sources.plot(kind='bar')
        plt.title('Top Sources for Top Internal Pages')
        plt.xlabel('Source Page')
        plt.ylabel('Number of Links')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout(pad=2.0)
        plt.savefig('data/top_sources_internal_pages.png', bbox_inches='tight')
        plt.close()
    else:
        print("'Destination_internal' column not found in combined DataFrame.")

    # Analysis: Top 10 Most Linked External Pages
    if 'Destination_external' in combined_df.columns:
        top_external_linked_pages = combined_df['Destination_external'].value_counts().head(10)
        plt.figure(figsize=(10, 6))
        top_external_linked_pages.plot(kind='bar')
        plt.title('Top 10 Most Linked External Pages')
        plt.xlabel('Page')
        plt.ylabel('Number of Links')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout(pad=2.0)
        plt.savefig('data/top_external_linked_pages.png', bbox_inches='tight')
        plt.close()

        # Analyze sources for top external linked pages
        top_external_sources = combined_df[combined_df['Destination_external'].isin(top_external_linked_pages.index)]
        top_external_sources = top_external_sources['Source_external'].value_counts().head(10)
        plt.figure(figsize=(10, 6))
        top_external_sources.plot(kind='bar')
        plt.title('Top Sources for Top External Pages')
        plt.xlabel('Source Page')
        plt.ylabel('Number of Links')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout(pad=2.0)
        plt.savefig('data/top_sources_external_pages.png', bbox_inches='tight')
        plt.close()
    else:
        print("'Destination_external' column not found in combined DataFrame.")

    print("Data analysis complete. Visualizations saved as 'top_internal_linked_pages.png', 'top_external_linked_pages.png', 'top_sources_internal_pages.png', and 'top_sources_external_pages.png'.")

if __name__ == "__main__":
    analyze_data()
