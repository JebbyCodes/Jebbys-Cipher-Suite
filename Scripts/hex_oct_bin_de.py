
def main():
    text = input("$hex_oct_bin_de >>> ")
    #  Hex / Bin / Octo
    # works by converting value in denary then into ascii

    valueasd  = 0

    ## Add the text in the string litteral below
    text = """ """.upper().split(" ") 
    groups = [16, 8, 2]

    plainText = ""
    for group in groups:
        for let in text:
            try:
                value = int(let, group)
                plainText += chr(value)
            except ValueError:
                print(f"not in base {group}")
                print()
                break

        print(plainText)
        plainText = ""

if __name__ == "__main__":
    main()  # only runs if you execute this file directly

    

