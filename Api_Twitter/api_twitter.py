import pandas as pd
import tweepy as tw
from wordcloud import WordCloud, STOPWORDS
from dicionario import chaves_acessos

# Adicionando as chave de acesso a variaveis

consumer_key = 'ktfNkSHV9ahnx8eDziqnpXJhk'
consume_secret = '02U3R6Ax2CKQZrgqoEZ0Xi5EevPYJCjXYJe2lnwflFNXFhVauw'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAO8QgwEAAAAAC%2BukDvFoxJVCR2F7ja3oD86wdWA%3DLi34PZA7KPgEtTLMX0tHTGuEhr8c0YhCCnaLWIILQFmkUQB5Pr'
acess_token = '1566146727371018245-ItmgajWDH5i8QFChLXHDglkwkXXyVC'
acess_token_secret = 'S7dJlXB76gdyoZiL57hTzbbtDm7Mwsv2Q8zcQDuiR0OhD'

cliente = tw.Client(bearer_token=chaves_acessos['bearer_token'],
                    consumer_key=chaves_acessos['consumer_key'],
                    consumer_secret=chaves_acessos['consume_secret'],
                    access_token=chaves_acessos['acess_token'],
                    access_token_secret=chaves_acessos['acess_token_secret'])

star = '2022-09-07T16:20:01Z'
end = '2022-09-07T16:21:01Z'

teste = cliente.search_recent_tweets(query='Iphone 14', max_results=100, start_time=star, end_time=end)
dados = teste.data

print(dados)
