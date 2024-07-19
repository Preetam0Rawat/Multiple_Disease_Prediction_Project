import numpy as np
import pickle 
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('E:/Study Material/College Projects/Multiple_Disease_Prediction/Diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('E:/Study Material/College Projects/Multiple_Disease_Prediction/Heartdisease_model.sav', 'rb'))



# Create Menu Option
with st.sidebar:
    
    
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                        
                           
                           default_index = 0)
    
# Diabetes Prediction Page
if(selected == 'Diabetes Prediction'):

    
    # page title
    st.title('Diabetes Prediction using ML')
    
    col1,col2 = st.columns(2)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', value = 6)
    with col2:
          Glucose = st.text_input('Glucose Level', value = 148)
    with col1:
          BloodPressure = st.text_input('Blood Pressure Value', value = 72)
    with col2:
         SkinThickness = st.text_input('Skin Thickness Value', value = 35)
    with col1:
         Insulin = st.text_input('Insulin Level', value = 0)
    with col2:
         BMI = st.text_input('BMI Value', value = 33.6)
    with col1:
         DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value', 0.627)
    with col2:
        Age = st.text_input('Age of the Person', 50)
    
    diab_diagnosis = ''

     
    #creating button for prediction
    
    if st.button('Diabetes Test Result'):
             if not Pregnancies or not Glucose or not BloodPressure  or not SkinThickness  or not Insulin  or not BMI  or not  DiabetesPedigreeFunction  or not Age:
                st.warning('Please fill out this field before submitting!')
             else:
                 diab_Prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,  BMI, DiabetesPedigreeFunction, Age]])
        
                 if(diab_Prediction[0]==1):
                    diab_diagnosis = 'The Person is Diabetic'
        
                 else:
                    diab_diagnosis = 'The Person is Not Diabetic'
                 st.success(diab_diagnosis)                   
    
    # Heart Disease Prediction Page
if(selected == 'Heart Disease Prediction'):
        
        # page title
        st.title('Heart Disease Prediction using ML')
        
        col1,col2 = st.columns(2)
        with col1:
            age = st.text_input('Age', value= 63)
        with col2:
             sex = st.text_input('Sex', value = 1)
        with col1:
             cp = st.text_input('Chest Pain Types', value = 3)
        with col2:
             trestbps = st.text_input('Resting Blood Pressure', value = 145)
        with col1:
             chol = st.text_input('Serum Cholestrol in mg/dL', value = 233)
        with col2:
             fbs = st.text_input('Fasting Blood sugar > 120 mg/dL', value = 1)
        with col1:
            restecg = st.text_input('Resting Electrocardiographic results', value = 0)
        with col2:
            thalach = st.text_input('Maximum Heart Rate achieved', value = 150)
        with col1:
            exang = st.text_input('Exercise Induced Angina', value = 0)
        with col2:
            oldpeak = st.text_input('ST depression induced by exercise', value = 2.3)
        with col1:
            slope = st.text_input('Slope of the peak exercise ST segment', value = 0)
        with col2:
             ca = st.text_input('Major vessels colored by fluorosopy', value = 0)
        with col1:
             thal = st.text_input('thal: 0 = normal; 1 = fiixed defect; 2 = reverseable defect', value = 1)
             
             heart_diagnosis = ''
             
             #creating button for prediction
             
             if st.button('Heart Disease Test Result'):
                 if not age or not sex or not cp or not trestbps or not chol or not  fbs or not restecg or not thalach or not exang or not oldpeak or not slope or not ca or not thal :
                   st.warning('Please fill out this field before submitting!')
                 else:
                    heart_Prediction = heart_model.predict([[ age, sex, cp, trestbps, chol,  fbs, restecg, thalach,  exang, oldpeak, slope,  ca, thal]])
           
                    if(heart_Prediction[0]==1):
                     heart_diagnosis = 'The Person is having Heart Disease'
                 
                    else:
                     heart_diagnosis = 'The Person does not have any Heart Disease'
                 st.success(heart_diagnosis) 
               
        
        
        
