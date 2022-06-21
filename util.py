import json
import pickle
import numpy as np

data_columns = None
model = None

def get_salary(age,hours_per_week,education,occupation,sex):
    try:
        education_index = data_columns.index(education)
        occupation_index = data_columns.index(occupation)
        sex_index = data_columns.index(sex)
    except:
        education_index = -1
        occupation_index = -1
        sex_index = -1
    x = np.zeros((len(data_columns)))
    x[0] = age
    x[1] = hours_per_week

    if education_index >= 0:
        x[education_index] = 1
    if occupation_index >= 0:
        x[occupation_index] = 1
    if sex_index >= 0:
        x[sex_index] = 1

    return model.predict([x])[0]

def load_saved_artifacts():
    global data_columns
    global model
    with open("./input_columns.json",'r') as f:
        data_columns = json.load(f)['data_columns']

    with open("./adult_salary_prediction.pickle",'rb') as f:
        model = pickle.load(f)

