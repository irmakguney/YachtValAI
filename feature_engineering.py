import pandas as pd

def process_features(input_csv, output_csv):
    # CSVyi oku
    df = pd.read_csv(input_csv)
    
    # rnek feature: ya
    df['age'] = 2025 - df['year'].astype(int)
    
    # Fiyat float yap, Python 3.13 uyumlu
    df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)
    
    # lenmi CSVyi kaydet
    df.to_csv(output_csv, index=False)
    print(f"Features processed and saved to {output_csv}")

if __name__ == "__main__":
    process_features('../data/yachts_raw.csv', '../data/yachts_processed.csv')

