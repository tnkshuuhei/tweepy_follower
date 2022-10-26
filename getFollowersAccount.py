#Twitter Developer Portalサイトから下記Keyを取得
#AuthenticationをRead&Write以上にする。
#TwitterAPI v2を利用
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

import tweepy
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit = True)

user = input("「@ユーザーID」を入力してください：")

followerIDs = []
for followerID in tweepy.Cursor(api.get_follower_ids, id=user).items():
    followerIDs.append(followerID)

#print(len(followerIDs))
#count = 0
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
    #count +=1
    #print(count)

import pandas as pd
pd.set_option("display.max_rows", 1000)
df = pd.DataFrame(followerDatas).loc[:,["Name","ID","Follow","Follower","TweetCount","Description"]]

#ファイル出力
fileName = input("ファイル名を入力してください：")
df.to_csv(fileName + ".csv")
print("「" + fileName + ".csv」が作成されました。")