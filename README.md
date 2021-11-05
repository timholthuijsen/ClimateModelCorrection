# ClimateModelCorrection
### Adjusting Contemporary Climate Models using GIS Error Analysis and Machine Learning
This Repository represents the final products of my Climate Model Correction Algorithm.

In the data found in this repository, a general method for climate model correction is developed in the capstone.ipynb file.

The accompanying Paper can also be found in this repo, under the name capstone.pdf

From the climate model adjustment method developed in this repository, a generalized correction algorithm is developed in the ModelMaker.py file. 
For this file, any and all climate model temperature outputs can be given as a NetCDF (.nc) file, and the .py file will return a tailor-made model that reduces your climate model inaccuracy by a significant amount.
The function will also give an indication of how much it reduced your climate model error in terms of RMSE reduction. 

Note that any climate model .nc input given to the ModelMaker.py needs to be in the shape [422,360,180], with the dimensions (time, longitude, latitude).



For further questions about model usage and applicability, email me at timholthuijsen@hotmail.com
