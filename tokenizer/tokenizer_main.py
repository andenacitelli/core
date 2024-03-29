import sys
import globals

def main(argv):

    # Open file and handle any errors
    f = open(argv[0], "r")

    # Init file used to track our globals 
    globals.setup(f)

    # Loop and print result until we get to it returning an EOF character
    #print("calling getToken()")
    token = globals.tokenizer.getToken()
    error = (token == -1)
    while token != 33 and token != -1:
        print("{}".format(token), end=" ")
        globals.tokenizer.skipToken()
        token = globals.tokenizer.getToken()
        error = (token == -1)

    if error:
        print("\nERROR: Invalid Token {}".format(token))
    else:
        print("33") # We always exit the loop on an eof; probably a cleaner way, but this works 

    # Close file
    f.close()

if __name__ == "__main__":
    main(sys.argv[1:])