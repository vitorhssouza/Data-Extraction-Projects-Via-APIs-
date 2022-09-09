from dicionario import chaves_acessos
import tweepy as tw
import pandas as pd



class Tweets:

    def __init__(self, query: str = '') -> None:
        self.__query = query
        cliente = tw.Client(bearer_token=chaves_acessos['bearer_token'],
                            consumer_key=chaves_acessos['consumer_key'],
                            consumer_secret=chaves_acessos['consume_secret'],
                            access_token=chaves_acessos['acess_token'],
                            access_token_secret=chaves_acessos['acess_token_secret'])

        filtro = cliente.search_recent_tweets(query=self.__query, max_results=100)
        dados_tweets = filtro.data
        lista_dados = list()
        for dados in dados_tweets:
            texto = dados.text
            posicao = texto.find(':')
            twitter = texto[posicao + 2:]
            lista_dados.append(twitter)

        df = pd.DataFrame(lista_dados, columns=['Tweets'])
        pd.options.display.max_colwidth = 150

        string = pd.Series(df['Tweets'].values).str.cat(sep=' ')

        caracteres = "#@"

        for i in range(len(caracteres)):
            string = string.replace(caracteres[i], "")
            #print(string)
        self.__tweets = string


    @property
    def query(self):
        return self.__query

    @property
    def tweets(self):
        return self.__tweets
