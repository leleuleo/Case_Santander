import json
from twython import Twython
import pandas as pd
from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d%m%Y")

with open('../parm/twitter_credencias.json', 'r') as file:
    creds = json.load(file)

print(creds)
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

dict_ = {'id': [], 'user': [], 'date': [], 'text': [], 'favorite_count': [], 'retweet_count': [], 'location': []}


def busca_tweets(query_term, max_id, max_iters):
    # Query
    for call in range(0, max_iters):
        query = {'q': query_term,
                 'result_type': 'recent',
                 'count': 100,
                 'max_id': max_id,
                 'tweet_mode': 'extended',
                 'include_entities': False
                 }

        for status in python_tweets.search(**query)['statuses']:
            dict_['id'].append(status['id'])
            dict_['user'].append(status['user']['screen_name'])
            dict_['date'].append([status['created_at']])
            dict_['text'].append(status['full_text'])
            dict_['favorite_count'].append(status['favorite_count'])
            dict_['retweet_count'].append(status['retweet_count'])
            dict_['location'].append(status['user']['location'])
            max_id = status['id']
        # Estrutura do dataframe


busca_tweets("santander_br", "", 2)
df = pd.DataFrame(dict_)
# print(df.to_string())

file_name = '/sistemas/ingestao/stage/twitter_santander-DATREF=' + d1

df.to_csv(file_name, sep='|', index=False)
