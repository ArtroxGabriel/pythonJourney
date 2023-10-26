import time


def countdown():
    contagem = int(input("Digite o tempo, em segundos: "))

    while contagem:
        mins, secs = divmod(contagem, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        contagem -= 1
    
    print("buuum")

countdown()