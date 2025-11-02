""""
thanks too this stack overflow person:
https://stackoverflow.com/questions/10133194/reverse-modulus-operator
I could solve it
"""


def main():
    from wordfreq import top_n_list
    string = input("$affine_de >>> ").upper()
    iterations = int(input("How hard do you want to bruteforce your text\n>> "))
    list1 = top_n_list('en', 50)

    commonwords = [x.upper() for x in list1]

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for a in range(iterations):
        for b in range(iterations):
            count = 0
            try:
                inversB = pow(b, -1, 26)
            except ValueError:
                continue

            decrypted = ""
            for letter in string:
                if letter.isalpha():
                    y = alphabet.index(letter)
                    x = (inversB * (y - a)) % 26
                    decrypted += alphabet[x]
                else:
                    decrypted += letter


            for word in decrypted.split(" "):
                if word in commonwords:
                    count += 1
            if any(word in decrypted for word in commonwords) and count > 0:
                print(f"{a},{b} -> {decrypted}, {count}")


if __name__ == "__main__":
    main()  # only runs if you execute this file directly