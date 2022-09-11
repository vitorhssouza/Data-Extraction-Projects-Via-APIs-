from dicionario import chaves_acessos
import tweepy as tw
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


class Tweets:

    def __init__(self, nome: str = '') -> None:
        self.__nome = nome
        cliente = tw.Client(bearer_token=chaves_acessos['bearer_token'],
                            consumer_key=chaves_acessos['consumer_key'],
                            consumer_secret=chaves_acessos['consume_secret'],
                            access_token=chaves_acessos['acess_token'],
                            access_token_secret=chaves_acessos['acess_token_secret'])

        filtro = cliente.search_recent_tweets(query=self.__nome, max_results=100)
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
        self.__query = string

    @property
    def nome(self):
        return self.__nome

    @property
    def query(self):
        return self.__query

    def grafico(self):
        stopwords = set(STOPWORDS)
        stopwords.update(
            ["Eleicoes2022", "Eleições2022", "RT", "por", "de", 'dar', 'pois', 'em', 'um', 'da', 'ser', 'aqui', 'vou',
             'dos', 'ter', 'não', 'ao', 'sou', 'seu', 'à', 'n', 'se', 'esse', 'uma', 'mais', 'ele', 'fazendo', 'você',
             'pode', 'essa', 'é', 'mas', 'segue', 'pra', 'isso', 'vez', 'para', 'muito', 'pelo', 'pela', 'são', 'na',
             'vamos', 'https', 't', 'co', 'c', 'New', 'eu', 'seis', 'retweets', 'ano', 'pessoa', 'likes', 'vai', 'que',
             'ou', 'anos', '7dias', 'tirou', 'tem', 'q', '0', 'O', 'e', 'os', 'assim', 'só', 'mesmo', 'tá', 'pro',
             'votar',
             'pessoas', 'vc', 'eleições2022', 'HTTPS:', 'https:'])

        wordcloud = WordCloud(width=1600, stopwords=stopwords, height=800, max_font_size=200, max_words=20,
                              collocations=False,
                              background_color='white').generate(self.__query)

        plt.figure(figsize=(40, 30))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        return plt.show()
