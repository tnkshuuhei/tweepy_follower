CONSUMER_KEY = "1vJb727lQTjybAyQ4MqGYjss4"
CONSUMER_SECRET = "SYshDqqjAVK5sgaPsfizHQmGheNnQxRP0s6GlMIb98imYPFvSE"
ACCESS_TOKEN = "1482836345986826242-594q3iMdw8A6lnZsa157yoUTdyRzQX"
ACCESS_TOKEN_SECRET = "tP9yxqAuGaAOgVadjJXqdFBj1dRDaE16AQLlhawx6PbTX"

import tweepy
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit = True)

#user = input("「@ユーザー名」を入力してください：")
#followerIDs = api.get_follower_ids(id="tech_comi")
#print(len(followerIDs))
followerIDs = []
for followerID in tweepy.Cursor(api.get_follower_ids, id="_shutanaka").items():
    followerIDs.append(followerID)

print(len(followerIDs))
count = 0
followerDatas = []
for followerID in followerIDs:
    followerData = {}
    data = api.get_user(user_id=followerID)
    followerData["Name"] = data.name
    followerData["ID"] = followerID
    followerData["Follow"] = data.friends_count
    followerData["Follower"] = data.followers_count
    followerData["Description"] = data.description
    followerData["TweetCount"] = data.statuses_count
    followerDatas.append(followerData)
    count +=1
    print(count)

import pandas as pd
pd.set_option("display.max_rows", 1000)
df = pd.DataFrame(followerDatas).loc[:,["Name","ID","Follow","Follower","TweetCount","Description"]]

#ファイル出力
fileName = input("ファイル名を入力してください：")
df.to_csv(fileName + ".csv")
print("「" + fileName + ".csv」が作成されました。")
