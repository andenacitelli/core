import t
import Comp


class Cond():
    def __init__(self):
        self.__value = None  # Needs to be available so other classes can see what this eval'd to
        self.__comp = None
        self.__cond1 = None
        self.__cond2 = None
        self.__alternative = None

    def parse(self):

        # Use one-token lookahead to see which alternative it is
        tokNo = t.tokenizer.get_token()
        if tokNo == t.Tokens.OPEN_PAREN.value:
            self.__comp = Comp.Comp()
            self.__comp.parse()
            self.__alternative = 1
        elif tokNo == t.Tokens.EXCLAMATION_POINT.value:
            t.tokenizer.skip_token()  # Consume exclamation point
            self.__comp = Comp.Comp()
            self.__comp.parse()
            self.__alternative = 2
        elif tokNo == t.Tokens.OPEN_BRACKET.value:
            t.tokenizer.skip_token()  # Consume open bracket
            # print("Comd: Consumed `[` token.")
            self.__cond1 = Cond()
            self.__cond1.parse()
            tokNo = t.tokenizer.get_token()
            if tokNo == t.Tokens.DOUBLE_AND.value:
                self.__alternative = 3
            elif tokNo == t.Tokens.DOUBLE_OR.value:
                self.__alternative = 4
            else:
                print(
                    "Cond: Invalid Token {} between Cond expressions!".format(
                        tokNo))
                return -1
            t.tokenizer.skip_token()  # Skip the && or ||
            self.__cond2 = Cond()
            self.__cond2.parse()
            tokNo = t.tokenizer.get_token()  # Check and consume closed bracket
            t.tokenizer.skip_token()
            if tokNo != t.Tokens.CLOSED_BRACKET.value:
                print("Cond: Expected token {}, got token {}".format(
                    t.Tokens.CLOSED_BRACKET.value, tokNo))
                return -1
            # print("Cond: Consumed `]` token.")
        else:
            print("Cond: No productions are valid!")
            return -1

        # Successful error code
        return 0

    def exec(self):
        if self.__alternative == 1:
            self.__comp.exec()
            self.__value = self.__comp.get_value()
            return self.__value
        elif self.__alternative == 2:
            self.__comp.exec()
            self.__value = not self.__comp.get_value()
            return self.__value
        elif self.__alternative == 3:
            self.__cond1.exec()
            self.__cond2.exec()
            self.__value = self.__cond1.get_value() and self.__cond2.get_value(
            )  # pylint: disable=no-member
            return self.__value
        else:
            self.__cond1.exec()
            self.__cond2.exec()
            self.__value = self.__cond1.get_value() or self.__cond2.get_value()  # pylint: disable=no-member
            return self.__value

    def print(self):
        if self.__alternative == 1:
            self.__comp.print()
        elif self.__alternative == 2:
            print("!", end="")
            self.__comp.print()
        elif self.__alternative == 3:
            print("[", end="")
            self.__cond1.print()
            print(" && ", end="")
            self.__cond2.print()
            print("]", end="")
        else:
            print("[", end="")
            self.__cond1.print()
            print(" || ", end="")
            self.__cond2.print()
            print("]", end="")

    def get_value(self):
        return self.__value