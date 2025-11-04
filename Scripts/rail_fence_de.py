# all maths / equations are from:
# https://en.wikipedia.org/wiki/Rail_fence_cipher



## Will come back to
## DO NOT TOUCH, thanks :)

def main():
    from wordfreq import top_n_list
    cipher = input(">>> ").replace(" ", "")
    rails = int(input("Rails: ")) # num of rails during encryption    
    period = 2*(rails-1) # the spacing
    length = len(cipher)
    k = int(length / period)
    # Assuming length is a multiple of period and k
    a,b,c=0,0,0
    answer=""
    text = cipher[0:k] + " " + cipher[k:3*k] + " " + cipher[3*k: len(cipher)]
    newText = text.split(" ")

    while b <= (length/2)-1:
#
        answer+=newText[0][a]
        a+=1
        answer+=newText[1][b]
        b+=1
        answer+=newText[2][c]
        c+=1
        answer+=newText[1][b]
        b+=1
    
    print(answer)


if __name__ == "__main__":
    main()  # only runs if you execute this file directly
            # yeah yeah, we get it already