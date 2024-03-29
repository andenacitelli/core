import t
import Fac


class Exp():
    def __init__(self):
        self.__fac = None
        self.__exp = None
        self.__alternative = None

    def parse(self):

        # Fac
        self.__fac = Fac.Fac()
        self.__fac.parse()

        # Use one-token lookahead to decide which production we used
        tokNo = t.tokenizer.get_token()
        if tokNo == t.Tokens.PLUS.value:
            t.tokenizer.skip_token()
            # print("Exp: Consumed `+` token.")
            self.__exp = Exp()
            self.__exp.parse()
            self.__alternative = 2
        elif tokNo == t.Tokens.MINUS.value:
            t.tokenizer.skip_token()
            # print("Exp: Consumed `-` token.")
            self.__exp = Exp()
            self.__exp.parse()
            self.__alternative = 3
        else:
            self.__alternative = 1

        # Successful error code
        return 0

    def exec(self):
        if self.__alternative == 1:
            return int(self.__fac.exec())
        if self.__alternative == 2:
            return int(self.__fac.exec()) + int(self.__exp.exec())
        return int(self.__fac.exec()) - (self.__exp.exec())

    def print(self):
        self.__fac.print()
        if self.__alternative == 2:
            print(" + ", end="")
            self.__exp.print()
        if self.__alternative == 3:
            print(" - ", end="")
            self.__exp.print()