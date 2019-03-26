CONSUMER_KEY = "******************"
CONSUMER_SECRET = "******************"
ACCESS_TOKEN = "******************"
ACCESS_TOKEN_SECRET = "******************"

import tweepy
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit = True)

user = input("「@ユーザー名」を入力してください：")
followerIDs = api.followers_ids(user)

followerDatas = []
for followerID in followerIDs:
    followerData = {}
    data = api.get_user(followerID)
    followerData["Name"] = data.name
    followerData["Follow"] = data.friends_count
    followerData["Follower"] = data.followers_count
    followerData["Description"] = data.description
    followerData["TweetCount"] = data.statuses_count
    followerDatas.append(followerData)
    print(followerData)

import pandas as pd
pd.set_option("display.max_rows", 1000)
df = pd.DataFrame(followerDatas).loc[:,["Name","Follow","Follower","TweetCount","Description"]]

#ファイル出力
fileName = input("ファイル名を入力してください：")
df.to_csv(fileName + ".csv")
print("「" + fileName + ".csv」が作成されました。")