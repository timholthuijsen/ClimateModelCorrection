import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor
import joblib
from DataProcessing import CSVWriter

text = input("""Please provide the path to your .nc climate model output file or use the default setup by typing default: """)

"""
Note: This program is still currently under development
"""


print("your nc file is:", text)

debug = False
default = False
normal = False

if text == 'SudoDebug':
    print("Welcome to debug mode")
    debug = True
elif text == 'default':
    print("You are using the default training set up")
    default = True
else:
    normal = True
    
    

#Determine data origin based on usage mode
if default:
    data = pd.read_csv("MegaTable.csv/")
    
#If someone gives their own custom .nc filetype, we convert it to the required format:
if normal:
    #We use our new DataProcessing function to transform the .nc data
    try:
        CSVWriter(Data = text)
        #if it worked, we use this data
        data = pd.read_csv("CustomTable.csv/")
    #if it doesn't work
    except:
        print("""Your data needs to be inserted into the MegaTable.csv training set.
          An automatic implementation for this is on its way and will be available
          in this function soon. If you already want to use this function,
          simply put your climate temperature data into the MegaTable.csv and
          use the 'default' implementation.""")
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
                  
linear = False
neural = False
forest = False
                  
if modeltype.lower() == 'linear':
    linear = True
    
if modeltype.lower() == 'randomforest':
    neural = True
    
if modeltype.lower() == 'neuralnetwork':
    forest = True

if linear:
    print('training your model. This may take a while.')
    model = LinearRegression().fit(x_train,y_train)
    ModelMaker(model, fit=False)
    
if neural:
    print('training your model. This may take a while.')
    model= MLPRegressor(max_iter = 500).fit(x_train,y_train)
    ModelMaker(model, fit=False)
    
if forest:
    print('training your model. This may take a while.')
    model=RandomForestRegressor().fit(x_train,y_train)
    ModelMaker(model, fit=False)
      
joblib.dump(model, 'TrainedModel.joblib')