import qrcode

def encodeQRCode(filename, data):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(f"/media/artroxgabriel/Selene/Adventure/Python/pythonJourney/public/qrcode/{filename}.png")
    return "qrcode gerado"

def main():
    print(f"""
          Vamos codificar um qrcode:
          """)

    data = input("Qual a mensagem voce deseja codificar?\n")
    name = input("Qual o nome do arquivo? ")
    print(encodeQRCode(name, data))



if __name__ == "__main__":
    main()