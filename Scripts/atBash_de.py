def main():
    # add text into the string litteral below
    text = input("$atBash_de >>> ")

    def cipher(text):
        result = ""

        for i in range(len(text)):
            char = text[i]
            if char not in alpha:
                continue
            else:
                index1 = alpha.index(char)
                alpha.reverse()
                result += alpha[index1]


        return result

    alpha = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]


    print(cipher(text).upper())

if __name__ == "__main__":
    main()  # only runs if you execute this file directly





