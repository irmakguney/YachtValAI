import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Veri ykle
df = pd.read_csv('/Users/irmakguney/YachtValAI/data/yachts_processed.csv')

# Features ve target
X = df[['age']]   # Ek feature eklemek istersen buraya ekle
y = df['price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Modeli kaydet
joblib.dump(model, '/Users/irmakguney/YachtValAI/models/yacht_price_model.pkl')
print("Model trained and saved to models/yacht_price_model.pkl")

