import t
import IdList


class Out():
    def __init__(self):
        self.__id_list = None

    def parse(self):

        # `write` token
        tokNo = t.tokenizer.get_token()
        t.tokenizer.skip_token()
        if tokNo != t.Tokens.WRITE.value:
            print("Id: Expected token {}, got token {}".format(
                t.Tokens.WRITE.value, tokNo))
            return -1
        # print("Out: Consumed `write` token.")

        # IdList
        self.__id_list = IdList.IdList()
        self.__id_list.parse()

        # `;` token
        tokNo = t.tokenizer.get_token()
        t.tokenizer.skip_token()
        if tokNo != t.Tokens.SEMICOLON.value:
            print("Id: Expected token {}, got token {}".format(
                t.Tokens.SEMICOLON.value, tokNo))
            return -1
        # print("Out: Consumed `;` token.")

    def exec(self):
        self.__id_list.print_values(
        )  # Special print function that prints values instead of ids

    def print(self):
        print("write ", end="")
        self.__id_list.print()
        print(";")