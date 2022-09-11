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
    menu2(opcao)


def menu2(opcao) -> None:
    cabecalho()
    if opcao == 1:
        while True:
            query: str = input('Qual assunto deseja pesquisar?  ').lower().strip()
            if query == '' or query == ' ':
                print('Não conseguir entender o que você inseriu. ')
            else:
                pesquisa(query)
    elif opcao == 2:
        print('Saindo do sistema..')
        sleep(2)
        exit()
    else:
        print('Opção inválida. Tente novamente.')
        teste()


def pesquisa(query) -> None:
    while True:
        cabecalho()
        print('1  - VISUALIZAÇÃO DOS TWEETS SOBRE O ASSUNTO INSERIDO\n'
              '2  - ANÁLISE DE SENTIMENTO COM O GRÁFICO WORDCLOUD \n')
        usuario: int = int(input('Informe sua opção: '))
        linha()
        if usuario == 1:
            pesquisa_twitter = Tweets(query)
            print(pesquisa_twitter.query)
            linha()
            conti = int(input('Deseja visualizar o gráfico wordcloud ? 1-Sim ou 2-Não '))
            if conti == 1:
                print('Plotando o gráfico com a nuvem de palavras mais comentado do momento')
                sleep(2)
                pesquisa_twitter.grafico()
                opcao = int(input('Deseja pesquisar outro assunto ou sair do sistema? 1-Sim ou 2-Sair'))
                if opcao == 1:
                    sleep(1)
                    menu2(opcao)
                else:
                    print('Saindo do sistema..')
                    sleep(1)
                    exit()

            elif conti == 2:
                print('Saindo do sistema..')
                exit()
            else:
                print('Opção inválida. Tente novamente. ')
        elif usuario == 2:
            grafico = Tweets(query)
            grafico.grafico()
            opcao = int(input('Deseja pesquisar outro assunto ou sair do sistema? 1-Sim ou 2-Sair'))
            if opcao == 1:
                sleep(1)
                menu2(opcao)
            else:
                print('Saindo do sistema..')
                sleep(1)
                exit()
        else:
            print('Opção inválida. Tente novamente. ')







