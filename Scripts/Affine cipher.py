## thanks too this stack overflow person:
## https://stackoverflow.com/questions/10133194/reverse-modulus-operator
## I could solve it

string = input("Input your string to decrypt\n>> ").upper()
iterations = int(input("How hard do you want to bruteforce your text\n>> "))

commonwords = [
    "THE", "BE", "TO", "OF", "AND",  "IN", "THAT", "HAVE",
    "IT", "FOR", "NOT", "ON", "WITH", "HE", "AS", "YOU", "DO", "AT",
    "THIS", "BUT", "HIS", "BY", "FROM", "THEY", "WE", "SAY", "HER", "SHE",
    "OR", "AN", "WILL", "MY", "ONE", "ALL", "WOULD", "THERE", "THEIR", "WHAT",
    "SO", "UP", "OUT", "IF", "ABOUT", "WHO", "GET", "WHICH", "GO", "ME",
    "WHEN", "MAKE", "CAN", "LIKE", "TIME", "NO", "JUST", "HIM", "KNOW", "TAKE",
    "PEOPLE", "INTO", "YEAR", "YOUR", "GOOD", "SOME", "COULD", "THEM", "SEE", "OTHER",
    "THAN", "THEN", "NOW", "LOOK", "ONLY", "COME", "ITS", "OVER", "THINK", "ALSO",
    "BACK", "AFTER", "USE", "TWO", "HOW", "OUR", "WORK", "FIRST", "WELL", "WAY",
    "EVEN", "NEW", "WANT", "BECAUSE", "ANY", "THESE", "GIVE", "DAY", "MOST", "US"
]
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


