import util
import streamlit as st

st.title("Adult Census Income Prediction")

education_list = [' 10th', ' 11th', ' 12th', ' 1st-4th', ' 5th-6th', ' 7th-8th', ' 9th', ' Assoc-acdm', ' Assoc-voc', ' Bachelors', ' Doctorate', ' HS-grad', ' Masters', ' Preschool', ' Prof-school', ' Some-college']
gender = [' Female', ' Male']
occupation_list = [' Adm-clerical', ' Armed-Forces', ' Craft-repair', ' Exec-managerial', ' Farming-fishing', ' Handlers-cleaners', ' Machine-op-inspct', ' Other-service', ' Priv-house-serv', ' Prof-specialty', ' Protective-serv', ' Sales', ' Tech-support', ' Transport-moving']


a,b,c = st.columns(3)
age = a.number_input("Enter age:")
hours_per_week = b.number_input("Enter hours-per-week:")
sex = c.selectbox("Gender",gender)

j,k = st.columns(2)
occupation = j.selectbox("Occupation",occupation_list)
education = k.selectbox("Education",education_list)

btn = st.button("Predict Salary")


if btn:
    if age==0:
        st.header("Error : Enter age")
    else:
        util.load_saved_artifacts()
        x = util.get_salary(age,hours_per_week,education,occupation,sex)
        if x == '1':
            st.header("Salary is greater than 50K")
        else:
            st.header("Salary is less than 50K")






