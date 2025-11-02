# all maths / equations are from:
# https://en.wikipedia.org/wiki/Rail_fence_cipher

def main():
    from wordfreq import top_n_list
    cipher = "WECRUO ERDSOEERNTNE AIVDAC" #input(">>> ")
    rails = 3 # num of rails during encryption    
    period = 2*(rails-1) # the spacing
    length = len(cipher)
    k = length / period
    # Assuming length is a multiple of period and k
    
    print(length, k)
    



if __name__ == "__main__":
    main()  # only runs if you execute this file directly
            # yeah yeah, we get it already