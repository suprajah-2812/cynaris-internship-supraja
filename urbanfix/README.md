# UrbanFix – AI/ML Email Classification

## Project Overview

UrbanFix is a home-services platform project focused on automating customer-support email classification and routing.

The goal is to classify incoming customer-support emails into the required support categories and provide a confidence score for each prediction.

## Support Categories

The classifier is expected to handle:

1. Complaints
2. Booking Queries
3. Payment Issues
4. Technician Feedback
5. Refunds
6. Escalations

## Project Structure

```text
urbanfix/
├── data/
│   ├── processed/
│   └── raw/
├── models/
├── notebooks/
├── src/
├── tests/
└── README.md

## Checkpoint 1 — Classifier Trained and Evaluated

### Dataset

The provided labelled sample dataset contains 56 text examples across 7 service categories.

The required 2,000 labelled UrbanFix customer-support emails were not available in the provided data pack at the time of implementation.

### Methodology

1. Loaded the labelled JSON dataset.
2. Separated email text and category labels.
3. Used an 80/20 stratified train-holdout split.
4. Converted text into numerical features using TF-IDF.
5. Trained a Logistic Regression baseline.
6. Trained a Linear SVM classifier.
7. Evaluated predictions using precision, recall, F1-score, and macro F1.

### Model Result

The Linear SVM achieved:

- Accuracy: 0.67
- Macro F1: 0.68

The evaluation was performed on a 12-sample holdout set.

### Saved Model Artifacts

- `models/email_classifier.pkl`
- `models/tfidf_vectorizer.pkl`
- `models/evaluation_results.json`

### Dataset Limitation

The checkpoint specifies a 2,000-email labelled dataset and a target macro F1 above 0.82. The available labelled sample dataset contains only 56 examples and uses service-category labels. Therefore, the current result should be considered a baseline/prototype evaluation rather than the final 2,000-email checkpoint result.

## Checkpoint 2 – Routing Logic and Confidence Scoring

### Routing Workflow

The trained text classifier was extended with calibrated confidence scoring and routing logic.

The routing rule is:

- Confidence > 0.85 → `AUTO_ROUTE`
- Confidence <= 0.85 → `HUMAN_QUEUE`

### Implementation

1. Loaded the calibrated email classifier and TF-IDF vectorizer.
2. Generated a predicted category for each email.
3. Calculated the calibrated prediction confidence.
4. Applied the client-defined 0.85 confidence threshold.
5. Automatically routed high-confidence predictions.
6. Sent lower-confidence predictions to the human queue.

### Available Data Evaluation

The available dataset provided only 56 labelled samples, resulting in 12 holdout samples using the existing 80/20 stratified split.

Results:

- Total holdout emails: 12
- Auto-routed: 0
- Human queue: 12
- Auto-route percentage: 0.00%
- Confidence threshold: 0.85

### Checkpoint Limitation

The checkpoint requires testing on 200 holdout emails. The required 2,000 labelled customer-support email dataset was not available in the provided data pack, so a 200-email evaluation could not be performed without inventing or substituting data.

The current routing result therefore represents an evaluation on the available 12-sample holdout set.