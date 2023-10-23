# Mad Libs:
# Concatenação de strings, e.g, "Hello, " + "world!" = "Hello, world!
# Primeiro projeto extremamento basico que funcionara como pseudo hello world :)
def execute():
    standard = "subscribe to "
    phrase = input("Enter a youtube channel to subscribe to: ")
    print(standard + phrase)                 # Concatenação
    print("Subscribe to {}".format(phrase))  # .format() 
    print(f"Subscribe to {phrase}")          # f-strings