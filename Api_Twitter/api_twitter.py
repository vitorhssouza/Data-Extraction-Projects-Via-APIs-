import pandas as pd
import tweepy as tw
from wordcloud import WordCloud, STOPWORDS
from dicionario import chaves_acessos

# Adicionando as chave de acesso a variaveis

cliente = tw.Client(bearer_token=chaves_acessos['bearer_token'],
                    consumer_key=chaves_acessos['consumer_key'],
                    consumer_secret=chaves_acessos['consume_secret'],
                    access_token=chaves_acessos['acess_token'],
                    access_token_secret=chaves_acessos['acess_token_secret'])

star = '2022-09-07T16:20:01Z'
end = '2022-09-07T16:21:01Z'

#t = tw.Place()

teste = cliente.search_recent_tweets(query='Iphone 14', max_results=100, start_time=star, end_time=end)
dados = teste.data


print(teste)
