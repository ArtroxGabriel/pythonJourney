import os 

def main():
    i = 0

    path = f"../../public/qrcode/"

    for filename in os.listdir(path):
        print(filename)
        my_dest = f"img_{str(i)}.png"
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1

if __name__ == "__main__":
    main()