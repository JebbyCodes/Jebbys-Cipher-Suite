def main():
    text = input(">>> ")

    def cipher(text):
        result = ""

        for i in range(len(text)):
            char = text[i]
            index1 = alpha.index(char)
            alpha.reverse()
            result += alpha[index1]


        return result

    alpha = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

    # add text into the string litteral below
    text = """ """.lower()
    print(cipher(text))

if __name__ == "__main__":
    main()  # only runs if you execute this file directly



