import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Insurance Premium Calculator", layout="centered")


@st.cache_resource
def load_model():
    model = joblib.load("insurance_rf_model.pkl")
    model_columns = joblib.load("model_columns.pkl")
    return model, model_columns


def engineer_features(age, diabetes, bp, transplants, chronic, height, weight,
                      allergies, cancer_history, surgeries):
    bmi = weight / ((height / 100) ** 2)

    if bmi < 18.5:
        bmi_category = "Underweight"
    elif bmi < 25:
        bmi_category = "Normal"
    elif bmi < 30:
        bmi_category = "Overweight"
    else:
        bmi_category = "Obese"

    if surgeries == 0:
        surgery_bucket = "0"
    elif surgeries == 1:
        surgery_bucket = "1"
    else:
        surgery_bucket = "2+"

    health_score = (
        3 * chronic
        + 4 * transplants
        + 2 * surgeries
        + 2 * cancer_history
        + 1 * diabetes
        + 1 * bp
    )

    if health_score >= 6:
        risk_category = "High Risk"
    elif health_score >= 3:
        risk_category = "Medium Risk"
    else:
        risk_category = "Low Risk"

    age_surgery = age * surgeries
    bmi_health = bmi * health_score

    input_df = pd.DataFrame([{
        "Age": age,
        "Diabetes": diabetes,
        "BloodPressureProblems": bp,
        "AnyTransplants": transplants,
        "AnyChronicDiseases": chronic,
        "Height": height,
        "Weight": weight,
        "KnownAllergies": allergies,
        "HistoryOfCancerInFamily": cancer_history,
        "NumberOfMajorSurgeries": surgeries,
        "Clean BMI Formula": bmi,
        "BMI Categories": bmi_category,
        "Risk Category": risk_category,
        "Health Score": health_score,
        "Surgery_Bucket": surgery_bucket,
        "Age_Surgery": age_surgery,
        "BMI_Health": bmi_health
    }])

    return input_df, bmi, bmi_category, health_score, risk_category


model, model_columns = load_model()

st.title("Insurance Premium Estimator")
st.write("Enter customer details to estimate insurance premium.")

age = st.number_input("Age", min_value=18, max_value=100, value=30)
diabetes = st.selectbox("Diabetes", ["No", "Yes"])
diabetes = 1 if diabetes == "Yes" else 0

bp = st.selectbox("Blood Pressure Problems", ["No", "Yes"])
bp = 1 if bp == "Yes" else 0

transplants = st.selectbox("Any Transplants", ["No", "Yes"])
transplants = 1 if transplants == "Yes" else 0

chronic = st.selectbox("Any Chronic Diseases", ["No", "Yes"])
chronic = 1 if chronic == "Yes" else 0

height = st.number_input("Height (cm)", min_value=120, max_value=220, value=170)
weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)

allergies = st.selectbox("Known Allergies", ["No", "Yes"])
allergies = 1 if allergies == "Yes" else 0

cancer_history = st.selectbox("History of Cancer in Family", ["No", "Yes"])
cancer_history = 1 if cancer_history == "Yes" else 0

surgeries = int(st.number_input("Number of Major Surgeries", min_value=0, max_value=10, value=0, step=1))

if st.button("Estimate Premium"):
    input_df, bmi, bmi_category, health_score, risk_category = engineer_features(
        age, diabetes, bp, transplants, chronic, height, weight,
        allergies, cancer_history, surgeries
    )

    if bmi > 60:
        st.error("BMI looks unusually high. Please double-check height and weight.")
        st.stop()

    categorical_cols = ["BMI Categories", "Risk Category", "Surgery_Bucket"]
    input_processed = pd.get_dummies(input_df, columns=categorical_cols, drop_first=True)
    input_processed = input_processed.reindex(columns=model_columns, fill_value=0)

    prediction = model.predict(input_processed)[0]

    st.subheader("Estimated Premium")
    st.success(f"Estimated Premium Amount: {prediction:,.0f}")

    if prediction >= 35000:
        st.error("Higher estimated premium profile")
    elif prediction >= 25000:
        st.warning("Moderate estimated premium profile")
    else:
        st.info("Lower estimated premium profile")

    profile_df = pd.DataFrame({
        "Metric": ["BMI", "BMI Category", "Health Score", "Risk Category"],
        "Value": [round(bmi, 2), bmi_category, health_score, risk_category]
    })
    st.write("Derived Profile")
    st.dataframe(profile_df, hide_index=True, use_container_width=True)