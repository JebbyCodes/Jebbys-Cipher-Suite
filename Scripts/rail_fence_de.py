# all maths / equations are from:
# https://en.wikipedia.org/wiki/Rail_fence_cipher



## Will come back to
## DO NOT TOUCH, thanks :)

def main():
    from wordfreq import top_n_list
    cipher = "WECRUO ERDSOEERNTNE AIVDAC".replace(" ", "") #input(">>> ")
    rails = 3 # num of rails during encryption    
    period = 2*(rails-1) # the spacing
    length = len(cipher)
    k = int(length / period)
    # Assuming length is a multiple of period and k
    
    text = cipher[0:k] + " " + cipher[k:3*k] + " " + cipher[3*k: len(cipher)]
    newText = text.split(" ")
    print(newText)
    
    


if __name__ == "__main__":
    main()  # only runs if you execute this file directly
            # yeah yeah, we get it already