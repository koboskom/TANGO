import pickle
import xgboost as xgb
import pandas as pd

def video_to_cuts(path_to_indicators, path_shots_data):
  df = pd.read_csv(path_to_indicators, sep='\t')
  df = df.astype(float)
  shots_data = pickle.load(open(path_shots_data, 'rb'))
  df['Frame: '] = df['Frame: '] +1

  data = []
  cuts = pd.DataFrame()
  for i in shots_data:
    frame = i['frames_range'].replace(" ", "").split(",")
    data.append(df.iloc[int(frame[0]):int(frame[1]),:].mean())

  cuts = pd.DataFrame(data)
  cuts = cuts[['Blockiness: ', 'SA: ', 'Blockloss: ', 'Blur: ', 'TA: ',
        'Exposure(bri): ', 'Contrast: ', 'Noise: ', 'Slice: ', 'Flickering:']]
  cuts.columns = ['Blockiness:', 'SA:', 'Blockloss:', 'Blur:', 'TA:',
        'Exposure(bri):', 'Contrast:', 'Noise:', 'Slice:', 'Flickering:']
  return cuts, shots_data

def ugc_dummy(path_to_indicators, path_shots_data):
#  input path to files where shots data are in pickle format
#  returns updated shots_data
# change paths to models to fit your configuration
# uncomment 31/32 to change models 
  cuts,shots_data = video_to_cuts(path_to_indicators, path_shots_data)
  xgb_cl = pickle.load(open("/content/9k_all_set.json", 'rb'))
#   xgb_cl = pickle.load(open("/content/12k_all_set.json", 'rb'))
  for count, value in enumerate(shots_data):
    preds = xgb_cl.predict((cuts[count:count+1]))
    value['ugc'] = int(preds[0])
  return shots_data

print(ugc_dummy("/content/metricsResultsCSV.csv","/content/data.pkl"))
