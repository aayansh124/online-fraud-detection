---
title: Online Fraud Detection
emoji: 🔥
colorFrom: purple
colorTo: pink
sdk: gradio
sdk_version: 6.14.0
python_version: '3.13'
app_file: app.py
pinned: false
license: mit
short_description: ML based online fraud transaction detection system
---
# Online Fraud Detection System

A Machine Learning based web application that detects fraudulent online transactions using transaction behavior patterns and engineered financial features.

The project uses a trained **Random Forest Classifier** with an interactive **Gradio Web Interface** for real-time fraud prediction.

---

# 🚀 Project Overview

Online transaction fraud has become one of the biggest challenges in digital banking systems.  
This project aims to detect suspicious transactions by analyzing:

- Transaction amount
- Sender and receiver balances
- Balance changes
- Transaction timing
- Transfer behavior patterns

The system predicts whether a transaction is:

- ✅ Normal Transaction
- 🚨 Fraudulent Transaction

---

# 🧠 Machine Learning Workflow

The project follows a complete Machine Learning pipeline:

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Training
6. Model Comparison
7. Best Model Selection
8. Deployment using Gradio

---

# 📂 Dataset Features

| Feature | Description |
|---|---|
| `step` | Unit of time where 1 step = 1 hour |
| `type` | Type of transaction |
| `amount` | Transaction amount |
| `oldbalanceOrg` | Sender balance before transaction |
| `newbalanceOrig` | Sender balance after transaction |
| `oldbalanceDest` | Receiver balance before transaction |
| `newbalanceDest` | Receiver balance after transaction |
| `isFraud` | Target variable (0 = Normal, 1 = Fraud) |

---

# ⚙️ Feature Engineering

Additional smart features were created to improve fraud detection accuracy.


| Derived Feature | Derived From | Purpose |
|---|---|---|
| `hour` | `step` | Extract actual transaction hour |
| `is_night` | `hour` | Detect nighttime transactions |
| `amount_ratio` | `amount`, `oldbalanceOrg` | Measure transaction size relative to sender balance |
| `sender_balance_change` | `oldbalanceOrg`, `newbalanceOrig` | Calculate money deducted from sender |
| `receiver_balance_change` | `oldbalanceDest`, `newbalanceDest` | Calculate money added to receiver |
| `sender_balance_zero` | `newbalanceOrig` | Detect emptied sender accounts |
| `receiver_balance_zero` | `newbalanceDest` | Detect suspicious receiver accounts |

---
# 📊 Model Performance Comparison

Different Machine Learning algorithms were trained and evaluated using:

- Accuracy Score
- Precision
- Recall
- F1-Score
- Confusion Matrix

---
# 📈 Final Model Comparison Table

| Model | Accuracy | Fraud Recall | Fraud Precision | F1-Score | Overall Performance |
|---|---|---|---|---|---|
| Logistic Regression | 99.96% | 0.77 | 0.99 | 0.87 | Good Baseline Model |
| Decision Tree | 99.96% | 1.00 | 0.81 | 0.89 | High Recall but Overfitting Risk |
| Random Forest | 99.998% | 1.00 | 0.99 | 0.99 | Best Balanced Model |
| XGBoost | 99.999% | 1.00 | 1.00 | 1.00 | Highest Performance |

---
