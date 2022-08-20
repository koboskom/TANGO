# modelowanie dla 9k rekordow 

# for index, row in df.iterrows():
#   if row['Tag:']=='X':
#     df = df.drop(index)
#   elif row["Noise:"]==0 and row['Tag:'] =='U':
#     df = df.drop(index)
#   elif row["Blockloss:"]>=0.9 and row['Tag:'] =='P':
#     df = df.drop(index)
#   elif row["Blockloss:"]<=-1 and row['Tag:'] =='U':
#     df = df.drop(index)
param_grid = {
    "max_depth": [10],
    "scale_pos_weight": [1.2],
    "learning_rate": [0.22],
    "reg_lambda": [0.5],
    "colsample_bytree": [0.7],
    "gamma": [0.3],
}

# modelowanie dla 12k rekordow

# for index, row in df.iterrows():
#   if row['Tag:']=='X':
#     df = df.drop(index)
#   elif row["Noise:"]==0 and row['Tag:'] =='U':
#     df = df.drop(index)
#   elif row["Blockloss:"]<=-1 and row['Tag:'] =='U':
#     df = df.drop(index)
param_grid = {
    "max_depth": [10],
    "scale_pos_weight": [0.7],
    "learning_rate": [0.12],
    "reg_lambda": [0.7],
    "colsample_bytree": [0.9],
    "gamma": [0.3],
}
