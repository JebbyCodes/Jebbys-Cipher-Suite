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
