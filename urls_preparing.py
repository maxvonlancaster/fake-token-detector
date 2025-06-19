import pandas as pd
import ast

# 1. Load the raw URLs dataset
df_urls = pd.read_csv('data/urls.csv')

# 2. Parse the 'addresses' column from string to Python list
def parse_address(addr_str):
    try:
        addr_dict = ast.literal_eval(addr_str)
        all_addr = []
        for addr in addr_dict.values():
            all_addr.extend(addr)
        return all_addr
    except (ValueError, SyntaxError):
        return []

df_urls['parsed_addresses'] = df_urls['addresses'].apply(parse_address)

# 3. Explode the DataFrame so each row has one address
df_exploded = df_urls.explode('parsed_addresses').rename(columns={'parsed_addresses' : 'address'})

# 4. Drop rows where address is null or empty
df_exploded = df_exploded[df_exploded['address'].notna() & (df_exploded['address'] != '')]

# 5. Remove duplicate addresses, keeping the first occurrence
df_exploded = df_exploded.drop_duplicates(subset=['address'])

# 6. (Optional) Reset index after cleaning
df_exploded = df_exploded.reset_index(drop=True)

# 7. Save the cleaned URLs dataset
cleaned_path = 'data/urls_cleaned.csv'
df_exploded.to_csv(cleaned_path, index=False)

# 8. Display basic info
print("Exploded DataFrame shape:", df_exploded.shape)
print(df_exploded[['address', 'name', 'category', 'subcategory']].head())

# Provide path to the cleaned file for downstream merging
print(f"Cleaned dateset saved to: {cleaned_path}")