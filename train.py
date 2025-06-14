import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

# Load data
df = pd.read_csv('housing.csv')

# Drop rows with missing values
df = df.dropna()


X = df[['longitude', 'latitude', 'total_rooms', 'total_bedrooms', 'population', 'households']]
y = df['median_house_value']

y = y.clip(lower=0)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


model = LinearRegression()
model.fit(X_train_scaled, y_train)


joblib.dump(model, 'model.pkl')
joblib.dump(scaler, 'scaler.pkl')

print(" Model and scaler saved successfully.")
