
#accuracy of percentage frequency (d.p.)
accuracy = 3

def analyse_freq(text):
          text = text.upper().strip()
          dictionary = {}

          for letter in text:
                    if letter not in dictionary:
                              #create a nested dictionary for character frequency and percent
                              dictionary[letter] = {"freq": 1, "percent": round(1 / len(text), accuracy)}
                    else:
                              #increases frequency and updates percent
                              dictionary[letter]["freq"] += 1
                              dictionary[letter]["percent"] = round(dictionary[letter]["freq"] / len(text), accuracy)

          #order dictionary based on frequency of letters
          dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1]["freq"], reverse=True))

          return dictionary
