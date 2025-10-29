def main():
    from wordfreq import top_n_list
    from wordsegment import load, segment
    commonwords = top_n_list('en', 100)
    cipher = str(input("$vigenere_de >>> ")).lower()
    answers = {}
    load()
    for keywordIndex in range(len(commonwords)):
        freq = 0
        keyword = commonwords[keywordIndex]
        keywordFit = ""
        plaintext = ""
        keyIndex = 0
        ## have cipher length
        ## have keyword length
        ## need keyword the fit the length of the cipher
        ## once complete just minus the values of the letters from each other

        for let in cipher:
            if let.isalpha():
                letValue = ord(let) - ord('a')
                keyValue = ord(keyword[keyIndex % len(keyword)]) - ord('a')
                value = (letValue - keyValue + 26) % 26 + ord( 'a') # Not sure how, but I guessed this and it was right
                plaintext += chr(value)
                keyIndex += 1


        
    for keyword in commonwords:
        freq = 0
        plaintext = ""
        keyIndex = 0

        for let in cipher:
            if let.isalpha():
                letValue = ord(let) - ord('a')
                keyValue = ord(keyword[keyIndex % len(keyword)]) - ord('a')
                value = (letValue - keyValue + 26) % 26 + ord('a')
                plaintext += chr(value)
                keyIndex += 1
            else:
                plaintext += let

        words = ' '.join(segment(plaintext))


        for word in words.split():
            if word in commonwords:
                freq += 1

        answers.setdefault(freq, []).append(plaintext)

    ## prints mostly likely from the bottom to the top
    for freq in sorted(answers.keys(), reverse=False):
        for text in answers[freq]:
            print(f"{text}")
            
    

if __name__ == "__main__":
    main()
