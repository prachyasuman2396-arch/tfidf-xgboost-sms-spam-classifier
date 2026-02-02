SMS Spam Detection System
TF-IDF + XGBoost | End-to-End NLP Application


🔗 Live Demo:
https://tfidf-xgboost-sms-spam-classifier.onrender.com


🔗 GitHub Repository:
https://github.com/prachyasuman2396-arch/tfidf-xgboost-sms-spam-classifier

 
 
 Project Overview
SMS spam is one of the most common vectors for phishing and financial fraud.
This project implements a production-ready SMS spam detection system using natural language processing, feature engineering, and machine learning, and deploys it as a web application.
The goal was not just to achieve high accuracy, but to:
handle real-world spam patterns
minimize false positives (blocking legitimate messages)
remain explainable and deployable
behave reliably under noisy and adversarial text
 Problem Statement
Given an SMS message, classify it as:
HAM – legitimate message
SPAM – promotional, phishing, or fraudulent message
Challenges:
Highly imbalanced dataset (HAM ≫ SPAM)
Spam messages are short and intentionally obfuscated
Same words appear in both spam and legitimate messages
Accuracy alone is misleading in such scenarios
⚙️ Tech Stack
Python
Scikit-learn
XGBoost
TF-IDF (Word-level & Character-level)
Flask
Gunicorn
Render (Deployment)

 Text Preprocessing (What & Why)
Preprocessing was designed to reduce noise without losing spam signals.

1️ Lowercasing
Ensures consistent representation and reduces vocabulary size.

2️ URL Removal
Spam URLs change frequently and do not generalize well across messages.

3️Special Character Normalization
Removes unnecessary punctuation while preserving meaningful tokens.

4️Whitespace Normalization
Ensures consistent tokenization across messages.
Feature Engineering (Beyond Plain Text)
Text alone often fails to capture spam behavior.
Additional handcrafted features were added to model message style:
Feature	Reason
Message length	Spam often follows length patterns
Presence of numbers	Common in prizes, phone numbers
Presence of “free”	Strong spam indicator
These features improve recall but require careful handling.
Text Vectorization Strategy
 Word-Level TF-IDF
Captures semantic meaning:
win, prize, offer, urgent
 Weak against obfuscated spam (fr33, w1n)
 Character-Level TF-IDF
Captures patterns and obfuscation:
fr33, w1n, $$$, !!!, c@sh
Strong against adversarial spam
Improves recall significantly
Models Evaluated & Observations


**1️Naive Bayes 
Why it underperformed:
Assumes feature independence
Fails with correlated features (TF-IDF + engineered features)
Performs poorly with continuous TF-IDF values
Tends to be overconfident and poorly calibrated
Result:
Low recall on spam and unstable predictions.


**2️Logistic Regression 
Strengths:
Works well with TF-IDF
Interpretable coefficients
Stable baseline
Limitations:
Linear decision boundary
Cannot model complex feature interactions
Struggles with obfuscated spam patterns
Result:
Good precision, but missed non-linear spam cases.


3️**Linear SVM** 
Strengths:
Strong margin-based classifier
Works well for high-dimensional sparse data
Limitations:
No native probability output
Requires calibration
Still linear in nature
Result:
Better than Logistic Regression in some cases, but limited flexibility.


Why XGBoost Was Chosen (Final Model)
XGBoost was selected as the final model because it naturally fits the problem characteristics.
Key Reasons:
✔ Handles Non-Linear Feature Interactions
XGBoost learns interactions between:
word TF-IDF
character TF-IDF
handcrafted features
This is something linear models cannot do.
✔ Robust to Noisy & Adversarial Text
Tree-based splits handle:
obfuscated words
mixed numeric patterns
irregular message structure
Better suited for real-world spam.
✔ Strong Performance on Imbalanced Data
Boosting focuses on hard-to-classify samples, improving spam recall.
✔ Probabilistic Output
Provides confidence scores, enabling:
threshold tuning
safer production decisions
✔ Deployment-Friendly
Fast inference, stable behavior, and predictable performance.


Model Behavior Summary
Model	Precision	Recall	Notes
Naive Bayes	Medium	Low	Assumption mismatch
Logistic Regression	High	Medium	Linear limitation
Linear SVM	High	Medium	No native probabilities
XGBoost	High	High	Best overall balance


Web Application
The trained model is deployed using Flask + Gunicorn and hosted on Render.
Features:
Single SMS input
Real-time prediction
Confidence score
Clean UI


Known Limitations
Feature scaling must be handled carefully
Threshold tuning affects spam vs ham trade-off
Model trained on SMS data only (not email/WhatsApp)

Future Improvements
Feature scaling pipeline
Model monitoring & drift detection
Multi-language spam detection
Explainability dashboards (SHAP)


Author
Prachya Das
B.Tech (CSE – AI & ML)
Aspiring Machine Learning Engineer
