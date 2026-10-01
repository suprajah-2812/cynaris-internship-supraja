import joblib
# import joblib


# Load the trained model and TF-IDF vectorizer
model = joblib.load("urbanfix/models/email_classifier.pkl")
vectorizer = joblib.load("urbanfix/models/tfidf_vectorizer.pkl")

# Example customer-support email
email_text = "My AC is not cooling properly"

# Convert the email into TF-IDF features
email_features = vectorizer.transform([email_text])

# Predict the category
prediction = model.predict(email_features)[0]

# Get prediction confidence
decision_scores = model.decision_function(email_features)

# Convert the decision scores into a confidence-like value
confidence = decision_scores.max()

print("Email:", email_text)
print("Predicted category:", prediction)
print("Confidence score:", round(confidence, 4))



# Load the calibrated classifier and TF-IDF vectorizer
model = joblib.load(
    "urbanfix/models/calibrated_email_classifier.pkl"
)

vectorizer = joblib.load(
    "urbanfix/models/tfidf_vectorizer.pkl"
)

# Confidence threshold from the client requirement
CONFIDENCE_THRESHOLD = 0.85


def classify_and_route(email_text):
    # Convert email text into TF-IDF features
    email_features = vectorizer.transform([email_text])

    # Predict category
    prediction = model.predict(email_features)[0]

    # Get probability for each category
    probabilities = model.predict_proba(email_features)[0]

    # Get the highest probability
    confidence = probabilities.max()

    # Routing decision
    if confidence > CONFIDENCE_THRESHOLD:
        route = "AUTO_ROUTE"
    else:
        route = "HUMAN_QUEUE"

    return prediction, confidence, route


# Test email
email_text = "My AC is not cooling properly"

prediction, confidence, route = classify_and_route(email_text)

print("Email:", email_text)
print("Predicted category:", prediction)
print("Confidence:", round(confidence, 4))
print("Routing decision:", route)