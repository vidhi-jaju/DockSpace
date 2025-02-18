import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score 
import joblib
import warnings

warnings.filterwarnings('ignore')  # Ignore warnings for cleaner output

# Load dataset
url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
data = pd.read_csv(url)

# Check dataset columns
print("Columns in the dataset:", data.columns)

# Convert 'Sex' column to numerical values (0 for 'female', 1 for 'male')
data['Sex'] = data['Sex'].map({'male': 1, 'female': 0})

# Handle missing values
data['Siblings/Spouses Aboard'] = data['Siblings/Spouses Aboard'].fillna(data['Siblings/Spouses Aboard'].median())
data['Parents/Children Aboard'] = data['Parents/Children Aboard'].fillna(data['Parents/Children Aboard'].median())
data['Fare'] = data['Fare'].fillna(data['Fare'].median())
data['Age'] = data['Age'].fillna(data['Age'].median())  # Handle missing age values

# Define features and target
features = ['Pclass', 'Sex', 'Age', 'Siblings/Spouses Aboard', 'Parents/Children Aboard', 'Fare']
X = data[features]
y = data['Survived']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'titanic_model.pkl')

# Test accuracy
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
