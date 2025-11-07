

from wordfreq import top_n_list
from frequency_analyser import analyse_freq

# function to decode text using current mapping
def decode(text, mapping):
    decoded = ""
    reversedmapping = {v: k for k, v in mapping.items() if v != ""}
    
    for letter in text:
        if letter.isalpha():
            if letter in reversedmapping:
                decoded += reversedmapping[letter]
            else:
                decoded += "_"
        else:
            decoded += letter

    
            
    return decoded


def substitutiondecode(text):
    mapping = {}
    for i in range(26):
        letter = chr(ord("A") + i)
        mapping[letter] = ""


    newtext = ""   
    for letter in text:
        if letter.isalpha() or letter == " ":
            newtext += letter
            wordlist = newtext.split(" ")


    dictionary = {}
    for word in top_n_list("en", 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
        dictionary.setdefault(len(word), []).append(word)



    def ispossible(pattern):
        words = dictionary.get(len(pattern), [])
        for word in words:
            match = True
            
            for i in range(len(pattern)):
                if pattern[i] != "_":
                    if pattern[i].lower() != word[i].lower():
                        match = False
                        break
            if match:
                return True
            
        return False


    

        

    # OK i know what to do next. when i do a guessy one like WAS and HAS i will then do the kind of thing with __X_ yk like but with the dictionary this time like with each word in wordlist with where the new letter
    # is and if it makes sense in all of them OR MOST OF THEM IN CASE THERE IS LIKE ONE FOREIGN OR MADE UP WORD then ill pass it. but if it doesnt then ill fail it and try with another combination.
    # ^^^^^ SOLUTION

    def checkmapping(wordlist, mapping):
        count = 0
        for word in wordlist:
            if ispossible(decode(word, mapping)) == False:
                count += 1
        
        if count == 0:
            return True
        
        return False
            
    # determine the most common word (almost certainly "the")
    def mostcommon(wordlist, pattern):
        wordcounts = {}
        
        for word in wordlist:
            if len(word) != len(pattern):
                continue
            
            doeswordmatchpattern = True
            for letterinword, letterinpattern in zip(word, pattern):
                if letterinpattern != letterinword and letterinpattern != "_":
                    doeswordmatchpattern = False
                    break
            
            if doeswordmatchpattern:
                if word in wordcounts:
                    wordcounts[word] += 1
                else:
                    wordcounts[word] = 1
        
        mostcommonword = ""
        highestwordcount = 0
        for word, count in wordcounts.items():
            if count > highestwordcount:
                highestwordcount = count
                mostcommonword = word
        
        return mostcommonword


    # remove all instances of a word from the wordlist FUCK i just realised i could just make the list have only one instance of each word at the start and then just use .remove() oh well
    def removedword(wordlist, removeme):
        return [word for word in wordlist if word != removeme]


    the = mostcommon(wordlist, f"__{next(iter(analyse_freq(text)))}")

                
    # assuming the most common word is "the" we can being the letter mapping
    mapping["T"], mapping["H"], mapping["E"] = the[0], the[1], the[2]

    print(the[0], the[1], the[2])
    print(mapping["T"], mapping["H"], mapping["E"])
    

    # remove "the" from wordlist for future 3 letter words to be decoded
    wordlist = removedword(wordlist, the)

    # SECURE mapping for I
    
    it = mostcommon(wordlist, f"_{mapping['T']}")
    # print(f"_{it}_{mapping['T']}")
    # print(wordlist, decode(text, mapping))
    mapping["I"] = it[0]


    # SECURE mapping for A
    wordlist = removedword(wordlist, mapping["I"])
    a = mostcommon(wordlist, f"_")
    mapping["A"] = a[0]

    then = mostcommon(wordlist, f"{mapping['T']}{mapping['H']}{mapping['E']}_")
    mapping["N"] = then[3]

    if checkmapping(wordlist, mapping) == True:
        ____ing = mostcommon(wordlist, f"____{mapping['I']}{mapping['N']}_")
        if mapping["E"] != ____ing[6]:
            mapping["G"] = ____ing[6]


        andvar = mostcommon(wordlist, f"{mapping['A']}{mapping['N']}_")
        mapping["D"] = andvar[2]

        wordlist = removedword(wordlist, f"{mapping['A']}{mapping['T']}")
        wordlist = removedword(wordlist, f"{mapping['A']}{mapping['N']}")

        # for future reference i could try "AM" here instead of "AS"
        asvar = mostcommon(wordlist, f"{mapping['A']}_")
        mapping["S"] = asvar[1]


        if checkmapping(wordlist, mapping) == True:
            has = mostcommon(wordlist, f"_{mapping['A']}{mapping['S']}")
            mapping["H"] = has[0]

            if checkmapping(wordlist, mapping) == True:
                pass
            else:
                mapping["H"] = ""
                mapping["W"] = has[0]
                
        else:
            mapping["S"] = ""
            mapping["M"] = asvar[1]

    else:
        #print("ive gone to here")
        mapping["N"] = ""
        mapping["M"] = then[3]

        if checkmapping(wordlist, mapping) == True:
            pass
        else:
            mapping["M"] = ""
            mapping["Y"] = then[3]

    return [decode(text, mapping), mapping]































