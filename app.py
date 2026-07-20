# ======================================
# Import Required Libraries
# ======================================

import streamlit as st
import pickle
import pandas as pd



# ======================================
# Page Configuration
# ======================================

st.set_page_config(
    page_title="Employee Salary Prediction",
    page_icon="💰",
    layout="centered"
)

# ============================================
# Custom CSS
# ============================================

st.markdown("""
<style>

/* Main App Background */
.stApp{
    background-color:#F4F8FB;
}

/* Header Box */
.header{
    background:linear-gradient(90deg,#1E3A8A,#2563EB);
    padding:25px;
    border-radius:15px;
    text-align:center;
    color:white;
    box-shadow:0px 4px 15px rgba(0,0,0,0.2);
    margin-bottom:25px;
}

/* Description Box */
.description{
    background:#E0F2FE;
    padding:15px;
    border-radius:10px;
    color:#0F172A;
    font-size:17px;
    margin-bottom:20px;
    border-left:6px solid #2563EB;
}

/* Button */
.stButton>button{
    width:100%;
    height:55px;
    background:linear-gradient(90deg,#2563EB,#1D4ED8);
    color:white;
    font-size:18px;
    font-weight:bold;
    border:none;
    border-radius:10px;
}

.stButton>button:hover{
    background:linear-gradient(90deg,#1D4ED8,#1E40AF);
}

/* Prediction Box */
.result{
    background:#DCFCE7;
    padding:20px;
    border-radius:10px;
    border-left:8px solid green;
    text-align:center;
    font-size:24px;
    font-weight:bold;
    color:#14532D;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# ============================================
# Sidebar
# ============================================

st.sidebar.title("📊 Project Information")

st.sidebar.markdown("""

## 💰Salary Prediction App

---

This application predicts an employee's annual salary using Machine Learning.

---

### 📚 Algorithms Used

✅ Linear Regression

✅ Decision Tree Regressor

✅ Random Forest Regressor

---

### 🏆 Best Model

**Linear Regression**

R² Score: **0.9801**

---
""")

st.sidebar.markdown("## 📈 Model Performance")

st.sidebar.table({
    "Model": [
        "Linear Regression",
        "Decision Tree",
        "Random Forest"
    ],
    "R² Score": [
        "0.9801",
        "0.9373",
        "0.9726"
    ]
})



# ======================================
# App Title
# ======================================

st.markdown("""
<div class="header">
    <h2>💰 Employee Salary Prediction System</h2>
    <h4>Machine Learning Regression Project</h4>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("""
<div class="description">
This application predicts an employee's annual salary using a trained Machine Learning model.

Please enter the employee details below and click <b>Predict Salary</b>.
</div>
""", unsafe_allow_html=True)

st.divider()

# ======================================
# Load Saved Files
# ======================================

model = pickle.load(open("salary_prediction_model.pkl", "rb"))

education_encoder = pickle.load(open("education_encoder.pkl", "rb"))

job_role_encoder = pickle.load(open("job_role_encoder.pkl", "rb"))


# ============================================
# User Inputs
# ============================================

st.subheader("📋 Enter Employee Information")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=70,
        value=25
    )

    years_experience = st.number_input(
        "Years of Experience",
        min_value=0,
        max_value=50,
        value=1
    )

    education_level = st.selectbox(
        "Education Level",
        education_encoder.classes_
    )

    job_role = st.selectbox(
        "Job Role",
        job_role_encoder.classes_
    )

with col2:

    city_option = st.selectbox(
        "City Tier",
        [
            "Tier 1 (Metropolitan)",
            "Tier 2 (Urban)",
            "Tier 3 (Small City)"
        ]
    )

    city_tier = {
        "Tier 1 (Metropolitan)": 1,
        "Tier 2 (Urban)": 2,
        "Tier 3 (Small City)": 3
    }[city_option]

    performance_score = st.slider(
        "Performance Score",
        1,
        5,
        3
    )

    num_skills = st.number_input(
        "Number of Skills",
        min_value=1,
        max_value=20,
        value=5
    )

    remote_option = st.selectbox(
        "Remote Work",
        ["No", "Yes"]
    )

    remote_work = 1 if remote_option == "Yes" else 0

st.divider()

# ============================================
# Encode User Inputs
# ============================================

education = education_encoder.transform([education_level])[0]
job = job_role_encoder.transform([job_role])[0]


# ============================================
# Create Input DataFrame
# ============================================

input_data = pd.DataFrame({
    "age": [age],
    "years_experience": [years_experience],
    "education_level": [education],
    "job_role": [job],
    "city_tier": [city_tier],
    "performance_score": [performance_score],
    "num_skills": [num_skills],
    "remote_work": [remote_work]
})

# ============================================
# Predict Salary
# ============================================

if st.button("Predict Salary"):

    prediction = model.predict(input_data)

    st.markdown(f"""
    <div class="result">
    <h3>💰 Prediction Successful!</h3>

    <h4>${prediction[0]:,.2f}</h4>

    <p>Estimated Annual Salary</p>

    </div>
    """, unsafe_allow_html=True)


st.markdown("""
<hr>

<div style="text-align:center; color:gray; font-size:16px;">

💻 <b>Developed by Syeda Faiza Adil</b>

Machine Learning | Streamlit | Scikit-Learn

📧 Built as part of my AI & Machine Learning Learning Journey

✨ "What we learn is never wasted."

</div>
""", unsafe_allow_html=True)



