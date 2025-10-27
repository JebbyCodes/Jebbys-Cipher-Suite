#  Hex / Bin / Octo
# works by converting value in denary then into ascii

valueasd  = 0

text = """48 65 78 61 64 65 63 69 6d 61 6c 20 6e 75 6d 65 72 61 6c 73 20 61 72 65 20 77 69 64 65 6c 79 20 75 73 65 64 20 62 79 20 63 6f 6d 70 75 74 65 72 20 73 79 73 74 65 6d 20 64 65 73 69 67 6e 65 72 73 20 61 6e 64 20 70 72 6f 67 72 61 6d 6d 65 72 73 2e 20 41 73 20 65 61 63 68 20 68 65 78 61 64 65 63 69 6d 61 6c 20 64 69 67 69 74 20 72 65 70 72 65 73 65 6e 74 73 20 66 6f 75 72 20 62 69 6e 61 72 79 20 64 69 67 69 74 73 20 28 62 69 74 73 29 2c 20 69 74 20 61 6c 6c 6f 77 73 20 61 20 6d 6f 72 65 20 68 75 6d 61 6e 2d 66 72 69 65 6e 64 6c 79 20 72 65 70 72 65 73 65 6e 74 61 74 69 6f 6e 20 6f 66 20 62 69 6e 61 72 79 2d 63 6f 64 65 64 20 76 61 6c 75 65 73 2e""".upper().split(" ")
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


    
