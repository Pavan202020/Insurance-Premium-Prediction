Insurance Premium Prediction

## Live Demo
- Tableau Dashboard: https://public.tableau.com/app/profile/pavan.kumar3701/viz/InsurancePremiumPredictionDashboard/SummaryStatisticsDashboard?publish=yes

🚀 Project Overview

This project builds an end-to-end machine learning solution to predict insurance premiums based on customer demographics and health-related attributes. It combines data analysis, statistical validation, machine learning, and deployment into an interactive web application.

🎯 Objective
Identify key factors influencing insurance premiums
Build a predictive model for premium estimation
Deploy the model as a user-friendly web-based calculator
📊 Dataset
~986 records
Features include:
Age
BMI (derived from height & weight)
Chronic diseases
Surgeries
Transplants
Family medical history
Target:
Insurance Premium Price
🔍 Exploratory Data Analysis (EDA)

Performed univariate and bivariate analysis to understand relationships.

Key Insights:
Premium increases significantly with age
Customers with multiple surgeries or transplants have higher premiums
Health-related features show non-linear relationships with premiums
📐 Feature Engineering

Created derived and interaction features to improve model performance:

Examples:
BMI = Weight / Height²
Health Score (weighted combination of medical factors)
Age × Surgeries interaction
BMI × Health Score interaction
🧪 Hypothesis Testing

Statistical tests (t-tests) were used to validate feature importance:

Surgeries → statistically significant impact on premium
Diabetes → statistically significant but lower practical impact
🤖 Model Building
Models Evaluated:
Linear Regression (baseline)
Random Forest
Gradient Boosting
Performance Comparison:
Model	R² Score	RMSE
Linear Regression	~0.59	~3885
Random Forest	~0.78	~2844
Gradient Boosting	~0.75	~3000
🏆 Final Model Selection

Random Forest was selected because:

Captures non-linear relationships
Handles feature interactions automatically
Achieved the highest R² and lowest RMSE
📉 Residual Diagnostics
Residuals centered around zero → no major bias
Some heteroskedasticity observed
Model performs well overall but struggles slightly with extreme cases
💡 Key Business Insights
Age is the strongest driver of premium pricing
Major medical events (transplants, surgeries) significantly increase premiums
Combined health conditions amplify risk more than individual factors
🌐 Deployment (Streamlit App)

An interactive web application was built using Streamlit:

Features:
User-friendly input interface
Real-time premium estimation
Derived profile display (BMI, risk category, health score)
Premium risk interpretation (low / medium / high)
⚙️ How to Run the App Locally
# Clone the repo
git clone <your-repo-link>

# Navigate to project folder
cd Insurance-Premium-Prediction

# Create virtual environment
python -m venv venv

# Activate environment
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
📁 Project Structure
├── app.py                      # Streamlit application
├── insurance_rf_model.pkl      # Trained Random Forest model
├── model_columns.pkl           # Feature schema
├── requirements.txt
├── README.md
├── notebooks/
│   └── model_training.ipynb
🔧 Tech Stack
Python
Pandas, NumPy
Scikit-learn
Streamlit
Matplotlib / Seaborn (EDA)
Tableau (dashboarding)
🚀 Future Improvements
Hyperparameter tuning using GridSearchCV
Try advanced models (XGBoost, LightGBM)
Deploy as REST API using Flask
Cloud deployment (Streamlit Cloud / AWS)
🧠 Key Learnings
Importance of feature engineering in improving model performance
Difference between statistical significance and practical impact
Handling non-linear relationships using tree-based models
End-to-end ML pipeline from EDA to deployment

Insurance Pricing Calculator .png
Risk Factors Analysis Dashboard.png
Premium Pricing Dashboard.png

👤 Author

Pavan Kumar