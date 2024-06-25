import asyncio
from twscrape import API

async def retrieve_tweets(api, q, limit):
    return [tweet async for tweet in api.search(q, limit=limit)]

def write_to_csv(tweets, since, until):
    with open(f'tweets_camclim_{since}_{until}.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # Write CSV header
        csvfile.write("Date{¨¨}Id{¨¨}RawContent{¨¨}ReplyCount{¨¨}RetweetCount{¨¨}LikeCount{¨¨}QuoteCount{¨¨}" +
                      "Username{¨¨}UserCreated{¨¨}FollowersCount{¨¨}FriendsCount{¨¨}" +
                      "StatusesCount{¨¨}FavouritesCount{¨¨}ListedCount{¨¨}MediaCount{¨¨}Location{¨¨}" +
                      "Verified{¨¨}Blue{¨¨}BlueType{¨¨}RawDescription\n")

        # Write tweets to CSV
        for tweet in tweets:
            csvfile.write(str(tweet.date).replace('\n', ' ') + "{¨¨}" +
                          str(tweet.id_str).replace('\n', ' ') + "{¨¨}" +
                          str(tweet.rawContent).replace('\n', ' ') + "{¨¨}" +
                          str(tweet.replyCount).replace('\n', ' ') + "{¨¨}" +
                          str(tweet.retweetCount).replace('\n', ' ') + "{¨¨}" +
                          str(tweet.likeCount).replace('\n', ' ') + "{¨¨}" +
                          str(tweet.quoteCount).replace('\n', ' ') + "{¨¨}" +
                          str(tweet.user.username).replace('\n', ' ') + "{¨¨}" +
                          str(tweet.user.created).replace('\n', ' ') + "{¨¨}" +
                          str(tweet.user.followersCount).replace('\n', ' ') + "{¨¨}" +
                          str(tweet.user.friendsCount).replace('\n', ' ') + "{¨¨}" +
                          str(tweet.user.statusesCount).replace('\n', ' ') + "{¨¨}" +
                          str(tweet.user.favouritesCount).replace('\n', ' ') + "{¨¨}" +
                          str(tweet.user.listedCount).replace('\n', ' ') + "{¨¨}" +
                          str(tweet.user.mediaCount).replace('\n', ' ') + "{¨¨}" +
                          'loc:'+str(tweet.user.location).replace('\n', ' ') + "{¨¨}" +
                          str(tweet.user.verified).replace('\n', ' ') + "{¨¨}" +
                          str(tweet.user.blue).replace('\n', ' ') + "{¨¨}" +
                          str(tweet.user.blueType).replace('\n', ' ') + "{¨¨}" +
                          'des:' + str(tweet.user.rawDescription).replace('\n', ' ') + "\n")

async def main(since, until):
    api = API()

    q = f"cambio climatico since:{since} until:{until} lang:es"
    limit = 1000

    # Gather tweets asynchronously
    tweets = await retrieve_tweets(api, q, limit)
    # Write tweets synchronously
    write_to_csv(tweets, since, until)

if __name__ == "__main__":
    for i in range(18,30,1):
        print('Retrieving: ','2024-03-'+('0' if i < 10 else '')+str(i), '2024-03-'+('0' if i+1 < 10 else '')+str(i+1))
        asyncio.run(main('2024-03-'+('0' if i < 10 else '')+str(i), '2024-03-'+('0' if i+1 < 10 else '')+str(i+1)))
