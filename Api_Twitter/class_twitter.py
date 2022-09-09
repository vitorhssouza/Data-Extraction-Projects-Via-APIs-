class Tweets:

    def __init__(self, query: str = '') -> None:
        self.__query = query

    @property
    def query(self):
        return self.__query
