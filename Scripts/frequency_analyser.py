'''
import numpy as np
import matplotlib

def main():
    # accuracy of percentage frequency (decimal places)
    accuracy = 3
    
    text = input("$frequency_analyser >>> ")
    text = text.upper().strip()
    dictionary = {}

    # Build frequency dictionary
    for letter in text:
        if letter not in dictionary:
            dictionary[letter] = {"freq": 1, "percent": round(1 / len(text), accuracy)}
        else:
            dictionary[letter]["freq"] += 1
            dictionary[letter]["percent"] = round(dictionary[letter]["freq"] / len(text), accuracy)

    # Order dictionary after the loop finishes
    dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1]["freq"], reverse=True))

    return dictionary  


if __name__ == "__main__":
    result = main()
    print(result)

'''

import matplotlib.pyplot as plt
import numpy as np

#The only part AI was used in was to generate the real world frequency data.

def main():

    # accuracy of percentage frequency (decimal places)
    accuracy = 3
        
    text = input("$frequency_analyser >>> ")
    text = text.strip()
    dictionary = {}

    # Build frequency dictionary
    for letter in text:
        if letter not in dictionary:
            dictionary[letter] = {"freq": 1, "percent": round(1 / len(text), accuracy)}
        else:
            dictionary[letter]["freq"] += 1
            dictionary[letter]["percent"] = round(dictionary[letter]["freq"] / len(text), accuracy)

    # Order dictionary after the loop finishes
    dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1]["freq"], reverse=True))

    letters = list(dictionary.keys())

    characters = [
        "A","B","C","D","E","F","G","H","I","J","K","L","M",
        "N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
        " ", ".", ",", "!", "?", "'", "\"", ";", ":", "-", "_", "(", ")", "[", "]", "{", "}", "\n",
        "a","b","c","d","e","f","g","h","i","j","k","l","m",
        "n","o","p","q","r","s","t","u","v","w","x","y","z"
    ]


    real_percentages = np.array([
        8.17, 1.49, 2.78, 4.25, 12.70, 2.23, 2.02, 6.09, 6.97, 0.15, 0.77, 4.03, 2.41,
        6.75, 7.51, 1.93, 0.10, 5.99, 6.33, 9.06, 2.76, 0.98, 2.36, 0.15, 1.97, 0.07,
        18.00, 6.57, 6.14, 0.30, 0.30, 0.25, 0.25, 0.20, 0.20, 0.30, 0.05, 0.05, 0.05,
        0.02, 0.02, 0.01, 0.01, 0.40,
        8.17, 1.49, 2.78, 4.25, 12.70, 2.23, 2.02, 6.09, 6.97, 0.15, 0.77, 4.03, 2.41,
        6.75, 7.51, 1.93, 0.10, 5.99, 6.33, 9.06, 2.76, 0.98, 2.36, 0.15, 1.97, 0.07
    ])


    cipher_percentages = np.array([dictionary.get(l, {}).get("percent", 0) * 100 for l in characters]) #[dictionary.get(l, {}) - fetchs l - otherwise blank, then calls get percent = returns stored value

    # Plotting

    plt.style.use('dark_background')

    fig, ax = plt.subplots(figsize=(15,5)) #width, height
    bar_width = 0.4 #width of each bar
    x = np.arange(len(characters)) #arranges labels for each char on x axis

    ax.bar(x - bar_width/2, real_percentages, bar_width, label="Real-life", color="#4bd3fe") #x offset to left
    ax.bar(x + bar_width/2, cipher_percentages, bar_width, label="Cipher Text", color="#d991fc") #x offset to the right

    ax.set_xticks(x) #set tick pos to x axis
    ax.set_xticklabels(characters, rotation=0) #assigns labels to ticks

    ax.set_xlabel("Character")
    ax.set_ylabel("Percent Occurrence")
    ax.set_title("Character Frequency Analysis")

    ax.legend()
    plt.tight_layout()
    plt.show()

    plt.show()

    #print(dictionary)

if __name__ == "__main__":
    main()