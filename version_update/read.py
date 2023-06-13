## xgboost version 1.7.5

## to load model 
import pickle
import xgboost as xgb
xgb_cl = pickle.load(open("/content/12k_all_set.json", 'rb'))

## model usage 
xgb_cl.predict(...)