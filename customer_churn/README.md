# Customer Churn Prediction

## 📌 Project Overview
This project predicts whether a customer will churn (stop using a service) based on their demographic and service usage data.  
The goal is to help businesses identify customers at risk and take retention actions.

## 📂 Dataset
- File: `data/churn_synthetic.csv`
- Size: 2000 records, 21 columns
- Key features: `tenure`, `InternetService`, `Contract`, `MonthlyCharges`, etc.
- Target: `Churn` (Yes/No)

## 🔎 Data Insights
- Churn rate in dataset: **61%**
- Customers with shorter tenure and higher monthly charges are more likely to churn.

## 🧠 Modeling
We trained and evaluated two models:
- Logistic Regression
- Random Forest Classifier ✅ (best)

**Best Model:** Random Forest  
- Accuracy: ~65%  
- Recall: ~80%  
- ROC AUC: ~0.67  

## 📊 Visualizations
- **ROC Curve** shows Random Forest separates churners better than Logistic Regression.  
- **Confusion Matrix** highlights correct vs misclassified churn predictions.  

## 🚀 Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt

