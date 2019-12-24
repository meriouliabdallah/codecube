import requests
import json
from country_abbrev import country_abbrev

headers = {'Authorization' : 'bda9bac380ac4144b38b939c7751d50e'}

top_headlines_url = 'https://newsapi.org/v2/top-headlines'
everything_news_url = 'https://newsapi.org/v2/everything'
sources_url = 'https://newsapi.org/v2/sources'

# A function that gets top headlines by country


def headlines_country(count):
    headlines_payload = { 'country': country_abbrev[count]}
    response = requests.get(url=top_headlines_url, headers=headers, params=headlines_payload)
    json_output = json.dumps(response.json() , indent=4)
    return json_output
# A  function that searches for topic mentions in the news

def topic_mentions(query):
    response = requests.get(url=everything_news_url,headers=headers,params={'q' : query})
    json_output = json.dumps(response.json() , indent=4)
    return json_output

    
print(headlines_country('Argentina'))
print(topic_mentions('bitcoin'))