import json
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.svm import LinearSVC
from sklearn.model_selection import StratifiedKFold, cross_val_score
import joblib
from sklearn.calibration import CalibratedClassifierCV






# Load the labelled dataset
with open("urbanfix/data/raw/aiml_labelled_samples.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print("Total samples:", len(data))

print("\nFirst 3 samples:")
for sample in data[:3]:
    print(sample)

print("\nLabels:")
labels = [sample["label"] for sample in data]
print(set(labels))



# Separate text and labels
texts = [sample["text"] for sample in data]
labels = [sample["label"] for sample in data]

# Split into training and holdout sets
X_train, X_test, y_train, y_test = train_test_split(
    texts,
    labels,
    test_size=0.20,
    random_state=42,
    stratify=labels
)

print("\nTraining samples:", len(X_train))
print("Holdout samples:", len(X_test))



# Convert text into numerical features using TF-IDF
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    sublinear_tf=True
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

print("\nTF-IDF training shape:", X_train_tfidf.shape)
print("TF-IDF holdout shape:", X_test_tfidf.shape)



# Train the classifier
model = LogisticRegression(max_iter=1000)

model.fit(X_train_tfidf, y_train)

print("\nModel training completed successfully.")



# Predict labels for the holdout set
y_pred = model.predict(X_test_tfidf)

# Evaluate the model
print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))



# Train a Linear SVM classifier
svm_model = LinearSVC()

svm_model.fit(X_train_tfidf, y_train)

# Predict on the holdout set
svm_pred = svm_model.predict(X_test_tfidf)

# Evaluate the Linear SVM model
print("\nLinear SVM Classification Report:")
print(classification_report(y_test, svm_pred, zero_division=0))




# Cross-validation on the available labelled data
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

cv_scores = cross_val_score(
    svm_model,
    X_train_tfidf,
    y_train,
    cv=cv,
    scoring="f1_macro"
)

print("\n5-Fold Cross-Validation Macro F1 Scores:")
print(cv_scores)

print("Mean Cross-Validation Macro F1:", cv_scores.mean())


# Save the trained model and TF-IDF vectorizer
joblib.dump(svm_model, "urbanfix/models/email_classifier.pkl")
joblib.dump(vectorizer, "urbanfix/models/tfidf_vectorizer.pkl")

print("\nModel saved successfully.")
print("Vectorizer saved successfully.")


# Save evaluation results
report = classification_report(
    y_test,
    svm_pred,
    output_dict=True,
    zero_division=0
)

with open("urbanfix/models/evaluation_results.json", "w", encoding="utf-8") as file:
    json.dump(report, file, indent=4)

print("\nEvaluation results saved successfully.")



# Create a calibrated Linear SVM for confidence scoring
calibrated_model = CalibratedClassifierCV(
    estimator=LinearSVC(),
    cv=5,
    method="sigmoid"
)

# Train the calibrated classifier
calibrated_model.fit(X_train_tfidf, y_train)

# Save the calibrated model
joblib.dump(
    calibrated_model,
    "urbanfix/models/calibrated_email_classifier.pkl"
)

print("\nCalibrated classifier trained and saved successfully.")