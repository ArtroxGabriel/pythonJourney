# Mad Libs:
# Concatenação de strings, e.g, "Hello, " + "world!" = "Hello, world!
# Primeiro projeto extremamento basico que funcionara como pseudo hello world :)
def execute():
    phrase = input("Enter a phrase: ")
    standard = f"subscribe to {phrase}"
    #print(standard + phrase)                 # Concatenação
    #print("Subscribe to {}".format(phrase))  # .format() 
    #print(f"Subscribe to {phrase}")          # f-strings

    
    print(standard)