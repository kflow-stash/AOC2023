import requests,json, datetime
import pandas as pd
import sqlite3, dotenv,os
dotenv.load_dotenv()

def to_dt(x):
    if not pd.isna(x):
        return datetime.datetime.fromtimestamp(x)
    else:
        return datetime.datetime.fromtimestamp(0)
    

url = os.getenv('LEADERBOARD_URL')

test =requests.get(url,headers={"Cookie":os.getenv('COOKIE')})

json_ = json.loads(test.content)

dfs = []
for member_id, row in json_["members"].items():
    dfs.append( pd.json_normalize(row))


df = pd.concat(dfs,join="outer")
for col in df.columns:
    if "_ts" in col:
        df[col] = df[col].apply(lambda x: to_dt(x))

DATABASE_URL = "./sqlite/AOC2023.db"
sqlite_driver = sqlite3.connect(DATABASE_URL)
df.to_sql("AOCPrivateLeaderboard",sqlite_driver,if_exists='replace',index=False)