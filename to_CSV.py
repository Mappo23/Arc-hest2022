import json
import pandas as pd
import datetime as DT
import numpy as np

filename = 'day1/B_15_40.json'

with open(filename, 'r') as f:
    data = json.load(f)
# interface parameters
parameters = data[:-1]
# remove type column and date from core data
columns = list(data[-2].keys())
# print(columns)
columns.remove('type')
columns.remove('date')

timeformat = lambda x: DT.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')

# create index
index = []
for e in data[:-1] :
    index.append(timeformat(e['date']))

# create DataFrame
df = pd.DataFrame(columns=columns, index=index)

# store data
tmp_res = []
for e in data[:-1]:
    if e['type'] == 'normal':
        s = pd.Series({k: e[k] for k in columns if k in e})

        #print(s.values)
        s = s.drop(['imgW', 'imgH', 'color', 'direction'])

        tmp_res.append(s)


pd.DataFrame(tmp_res).to_csv(filename.split('.')[0] + '.csv')

