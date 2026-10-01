import json
import joblib
from routing import classify_and_route

from sklearn.model_selection import train_test_split

from routing import classify_and_route


# Load the labelled dataset
with open(
    "urbanfix/data/raw/aiml_labelled_samples.json",
    "r",
    encoding="utf-8"
) as file:
    data = json.load(file)

# Extract text and labels
texts = [sample["text"] for sample in data]
labels = [sample["label"] for sample in data]

# Recreate the same 80/20 stratified split used during training
X_train, X_test, y_train, y_test = train_test_split(
    texts,
    labels,
    test_size=0.20,
    random_state=42,
    stratify=labels
)

auto_route_count = 0
human_queue_count = 0

print("Routing Test Results")
print("=" * 50)

for email in X_test:
    prediction, confidence, route = classify_and_route(email)

    print(f"\nEmail: {email}")
    print(f"Predicted category: {prediction}")
    print(f"Confidence: {confidence:.4f}")
    print(f"Routing decision: {route}")

    if route == "AUTO_ROUTE":
        auto_route_count += 1
    else:
        human_queue_count += 1

total = len(X_test)
auto_route_percentage = (auto_route_count / total) * 100

print("\n" + "=" * 50)
print("Summary")
print("=" * 50)
print("Total holdout emails:", total)
print("Auto-routed:", auto_route_count)
print("Human queue:", human_queue_count)
print(f"Auto-route percentage: {auto_route_percentage:.2f}%")

# Save routing evaluation results
routing_results = {
    "confidence_threshold": 0.85,
    "total_holdout_emails": total,
    "auto_routed": auto_route_count,
    "human_queue": human_queue_count,
    "auto_route_percentage": auto_route_percentage
}

with open(
    "urbanfix/models/routing_evaluation.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(routing_results, file, indent=4)

print("\nRouting evaluation results saved successfully.")