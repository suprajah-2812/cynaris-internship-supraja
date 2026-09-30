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