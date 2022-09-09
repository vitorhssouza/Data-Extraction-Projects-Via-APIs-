from Api_Twitter.class_twitter import Tweets
from time import sleep


def linha(tamanho: int = 90) -> None:
    print(tamanho * '=')


def cabecalho():
    linha()
    print('ANÁLISE DE SENTIMENTO DE TWEETS'.center(90))
    linha()


def teste() -> None:
    """Interface gráfica do usuário """
    cabecalho()
    print('1  - PESQUISA NO TWITTER\n'
          '2  - SAIR DO SISTEMA\n')
    opcao: int = int(input('Informe sua opção: '))
    escolha(opcao)


def escolha(opcao) -> None:
    if opcao == 1:
        cabecalho()
        while True:
            query: str = input('Qual assunto deseja pesquisar?  ').lower().strip()
            if query == '' or query == ' ':
                print('Não conseguir entender o que você inseriu. ')
            else:
                break
        cabecalho()
        print('1  - VISUALIZAÇÃO DOS TWEETS SOBRE O ASSUNTO INSERIDO\n'
              '2  - ANÁLISE DE SENTIMENTO COM O GRÁFICO WORDCLOUD \n')
        usuario: int = int(input('Informe sua opção: '))
        if opcao == 1:
            pesquisa = Tweets(query)
            print(pesquisa.tweets)







