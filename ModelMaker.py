import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

text = input("""Please provide the path to your .nc climate model output file or use the default setup by typing default: """)

"""
Note: This program is still currently under development
"""


print("your nc file is:", text)

if text == 'SudoDebug':
    print("Welcome to debug mode")
    debug = True
elif text == 'default':
    print("You are using the default training set up")
    default = True
else:
    normal = True
    

#Determine data origin based on usage mode
if default == True:
    data = pd.read_csv("MegaTable.csv/")
    

columns_to_use = [
    "ReforecastLon",
    "ReforecastLat",
    "Time",
    "ReforecastTemp",
    "Precipitation",
    "CloudCover",
    "Water","Ice",
    "Land",
    "Shallow Water",
    "Desert"]

target_column = "ModelError"
x_train, x_test, y_train, y_test = train_test_split(
    data[columns_to_use], data[target_column]
)

if len(x_train) == len(y_train):
    print("Train/Test split worked!")
    
def error(prediction, true = y_test):
    "A function to automate error calculation"
    PredictionSubstracted = y_test - prediction
    Totalerror = 0
    for modelerror in PredictionSubstracted:
        addition = (modelerror**2)**0.5
        Totalerror = Totalerror + addition
    RMSE = Totalerror/len(prediction)
    return RMSE    

def ModelMaker(model, x_train = x_train, y_train = y_train,
               x_test = x_test, y_test = y_test, fit = True):
    "A function to automate model making"
    if fit:
        model.fit(x_train,y_train)
    y_predicted = model.predict(x_test)
    RMSE = error(y_predicted)
    print("your ", model, "model yields an RMSE of:", RMSE)
    return RMSE


    
modeltype = input("""What kind of model do you want to use?
                  options: Linear, RandomForest, NeuralNetwork """)
                  
if modeltype.lower() == 'linear':
    linear = True

if linear:
    model = LinearRegression()
    ModelMaker(LinearRegression())
    
ModelMaker(model)   
joblib.dump(model, 'TrainedModel.joblib')