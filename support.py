import pdb
from urllib import response, request
import pandas as pd
import json

with request.urlopen('https://github.com/robocorp/inhuman-insurance-inc/raw/main/RS_198.json') as f:
    data = json.load(f)

df = pd.DataFrame(rec for rec in data['value'])
pdb.set_trace()
