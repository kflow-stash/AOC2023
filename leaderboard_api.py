import requests,json, datetime
import pandas as pd
import sqlite3, dotenv,os,pytz,math
dotenv.load_dotenv()

def to_dt(x):
    if not pd.isna(x):
        return datetime.datetime.fromtimestamp(x)
    else:
        return datetime.datetime.fromtimestamp(0)
    
day1 = datetime.datetime.strptime("11/30/2023","%m/%d/%Y")

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

df.set_index("name",inplace=True)

time_df = df[[x for x in df.columns if "get_star_ts" in x]].stack().reset_index().rename(columns={"level_1":"description",0:"time_of_completion"})
time_df["problem"] = time_df["description"].apply(lambda x: ".".join(x.split(".")[1:3]))

time_df = time_df[time_df["time_of_completion"]>(datetime.datetime.now() - datetime.timedelta(days=30))].copy()
time_df["time_of_completion"] = time_df["time_of_completion"].dt.tz_localize("America/Denver").dt.tz_convert('America/New_York').dt.tz_localize(None)

star_df = df[[x for x in df.columns if "star_index" in x]].stack().reset_index().rename(columns={"level_1":"description",0:"star_index"})
star_df["problem"] = star_df["description"].apply(lambda x: ".".join(x.split(".")[1:3]))

merge_df = time_df[["name","problem","time_of_completion"]].merge(star_df[["name","problem","star_index"]],on=["name","problem"]).sort_values(["name","problem"]).reset_index(drop=True)

merge_df["day"] = merge_df["problem"].apply(lambda x: day1+ datetime.timedelta(days=int(x.split(".")[0])))
merge_df["solve_minutes"] = (merge_df["time_of_completion"] - merge_df["day"]).dt.total_seconds()/60
merge_df["problem_part"] = merge_df["problem"].apply(lambda x: int(x.split(".")[1]))

merge_df["solve_minutes2"] = (merge_df["time_of_completion"] - merge_df["time_of_completion"].shift()).dt.total_seconds()/60
merge_df["solve_minutes"].mask(merge_df["problem_part"]==2,merge_df["solve_minutes2"],inplace=True)

merge_df.drop(columns=["solve_minutes2"],inplace=True)

t1 = datetime.datetime.strptime("12/1/2023","%m/%d/%Y")
eastern_now = datetime.datetime.now(pytz.timezone("America/New_York")).replace(tzinfo=None)
total_hours = math.ceil((eastern_now - t1).total_seconds()/(60*60))

users=pd.DataFrame(data=merge_df["name"].unique(),columns=["name"])
dfs=[]
for t in range(total_hours):
    thresh = t1+datetime.timedelta(hours=t)
    trunc_df = merge_df[merge_df["time_of_completion"]<thresh][["name","problem"]].groupby("name").count().reset_index()
    trunc_df = users.merge(trunc_df,on="name",how="left").fillna(0)
    trunc_df["trunc_time"] = thresh
    trunc_df["lag_index"]=t
    dfs.append(trunc_df)
    
lag_df = pd.concat(dfs,ignore_index=True).sort_values(["trunc_time","problem"],ascending=[True,False]).reset_index(drop=True)

DATABASE_URL = "./sqlite/AOC2023.db"
sqlite_driver = sqlite3.connect(DATABASE_URL)
merge_df.to_sql("AOCPrivateLeaderboard",sqlite_driver,if_exists='replace',index=False)
lag_df.to_sql("AOCPrivateLeaderboard_lagged",sqlite_driver,if_exists='replace',index=False)