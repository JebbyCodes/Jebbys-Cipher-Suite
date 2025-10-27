def main():
    text = input("$Caeser_de >>> ")

    def cipher(text):
        text = text.lower()
        for shift in range(26):
            result = ""
            for char in text:
                if 'a' <= char <= 'z':
                    result += chr((ord(char) - 97 - shift) % 26 + 97)
                else:
                    result += char
            print(result)

    text = """HELLO""".lower()
    cipher(text)

if __name__ == "__main__":
    main()  # only runs if you execute this file directly