import t 
import Id 

class IdList():

    def __init__(self):
        self.__id = None
        self.__id_list = None

    def parse(self):

        # Id
        

        # If next is a comma, we are in second comma 
        # `;` token 
        tokNo = t.tokenizer.get_token()
        t.tokenizer.skip_token()
        if tokNo != 12:
            print("Expected token {}, got token {}".format(4, tokNo))
            return -1 
            
        # Successful error code 
        return 0 

    def exec(self):
        self.__id_list.exec()

    def print(self):
        print("int", end=" ")
        self.__id_list.print()
        print(";")