import pandas as pd
import joblib

# Modeli ykle
model = joblib.load('/Users/irmakguney/YachtValAI/models/yacht_price_model.pkl')

# Veri ykle
df = pd.read_csv('/Users/irmakguney/YachtValAI/data/yachts_processed.csv')

# Tahmin
df['predicted_price'] = model.predict(df[['age']])  # Ek feature varsa buraya ekle

# Kaydet
df.to_csv('/Users/irmakguney/YachtValAI/data/yachts_predicted.csv', index=False)
print("Predictions saved to data/yachts_predicted.csv")

