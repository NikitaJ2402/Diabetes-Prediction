import numpy as np 
import pickle 
import streamlit as st 


#loading the saved model
loaded_model=pickle.load(open("D:\Programmes\Python\Jupyter Notebook\diabetes.sav",'rb'))


#creating a function for prpediction

def diabetes_prediction(input_data):

    #changing the input data to numpy array
    input_data_as_numpy_array=np.asarray(input_data)

    #reshape the array as we are predicting for one instance
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0]==0):
        return 'The Person is not Diabetic'
    else:
        return 'The Person is Diabetic'

def main():

    #giving a title
    st.title('Diabetes Prediction Web App')

    #getting the input data from the User

    pregnencies=st.text_input('Number of Pregnencies')
    Glucose=st.text_input('Glucose Level')
    BloodPressure=st.text_input('Blood Pressure Value')
    SkinThickness=st.text_input('Skin Thickness Value')
    Insulin=st.text_input('Insulin Count')
    BMI=st.text_input('BMI Value')
    DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function Value')
    Age=st.text_input('Age of the person')


    #code for prediction
    diagnosis=''

    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diagnosis=diabetes_prediction([pregnencies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])

    st.success(diagnosis)

if __name__ =='__main__':
    main()