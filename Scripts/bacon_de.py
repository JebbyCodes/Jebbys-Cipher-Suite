def main():
    text  = str(input("$bacon_de >>> ")).lower().split(" ")
    cipher(text)

def cipher(text):
    plaintext=""
    for let in text:
        total = 0
        for value in range(len(let)):
            char=let[value]

            if char == "b":
                total += 2**(5-(value+1))


        plaintext += chr(total+65)

    print(plaintext)

if __name__ == "__main__":
    main()
