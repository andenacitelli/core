import t
import Cond
import StmtSeq


class If():
    def __init__(self):
        self.__c = None
        self.__ss1 = None
        self.__ss2 = None
        self.__alternative = None

    def parse(self):

        # `if` token
        tokNo = t.tokenizer.get_token()
        t.tokenizer.skip_token()
        if tokNo != t.Tokens.IF.value:
            print("If: Expected token {}, got token {}".format(
                t.tokenizer.IF.value, tokNo))
            return -1
        print("IF: Consumed `if` token.")

        # Parse Condition
        self.__c = Cond.Cond()
        self.__c.parse()

        # `then` token
        tokNo = t.tokenizer.get_token()
        t.tokenizer.skip_token()
        if tokNo != t.Tokens.THEN.value:
            print("If: Expected token {}, got token {}".format(
                t.tokenizer.THEN.value, tokNo))
            return -1
        print("IF: Consumed `then` token.")

        # `stmtseq` token
        self.__ss1 = StmtSeq.StmtSeq()
        self.__ss1.parse()

        # If we're at an "end", it means there's no `else` and that we should get out
        tokNo = t.tokenizer.get_token()
        t.tokenizer.skip_token()
        if tokNo == t.Tokens.END.value:
            self.__alternative = 1
            return 0

        # Otherwise, we're at an else
        if tokNo != t.Tokens.ELSE.value:
            print("If: Expected token {}, got token {}".format(
                t.tokenizer.ELSE.value, tokNo))
            return -1
        print("IF: Consumed `else` token.")

        # `stmtseq` token
        self.__alternative = 2
        self.__ss2 = StmtSeq.StmtSeq()
        self.__ss2.parse()

        # `end` token
        tokNo = t.tokenizer.get_token()
        t.tokenizer.skip_token()
        if tokNo != t.Tokens.END.value:
            print("If: Expected token {}, got token {}".format(
                t.tokenizer.END.value, tokNo))
            return -1
        print("IF: Consumed `end` token.")

    def exec(self):
        if self.__c.is_true:
            return
        if self.__alternative == 1:
            self.__ss1.exec()
        else:
            self.__ss2.exec()

    def print(self, indentation):
        print(" " * indentation, end="")
        print("if ")
        self.__c.print(indentation + 4)
        print(" then ")
        self.__ss1.print(indentation + 4)
        if self.__alternative == 2:
            print(" else ")
            self.__ss2.print(indentation + 4)
        print(" end")