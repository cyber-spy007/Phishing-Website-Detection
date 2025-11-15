import pickle
from features import extract_features


# Load model
with open('model.pkl', 'rb') as f:
model = pickle.load(f)


print("Phishing URL Detection System")
url = input("Enter URL: ")


features = extract_features(url)
pred = model.predict([features])[0]


if pred == 1:
print("⚠️ Phishing URL Detected!")
else:
print("✔️ Legitimate URL")
