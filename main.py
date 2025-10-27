import os
import tkinter as tk
import wordfreq
from Scripts import AtBash_de, caeser_cipher_de, hex_oct_bin_de

# Constants #
VERSION = "1.0"
# Get root directory
rootdir = os.path.dirname(__file__)
credits_filler = "\n********************************************************\n"

root = tk.Tk()
root.title("Jebby's Cipher Suite")
root.geometry("750x750")

# Clear Function #
def clear():
    for widget in root.winfo_children():
        widget.destroy()

# Help Function #
def help():
    clear()
    #Help#
    text_help = tk.Label(root, text="What is this?\n\t>This is a simple Tkinter application to centralise all the created scripts in handy little buttons!")
    text_help.pack(pady=20)
    init(Exitable=True)

# Credits Function #
def credits():
    clear()
    #Credits#
    text_credits = tk.Label(root, text=f"MODULES USED:\n\n\t>wordfreq\n\t\tCreated by: Robyn Speer\n\t\tLicence:Apache License, Version 2.0;\n\t\t>>Copyright 2022 Robyn Speer\n\nLicensed under the Apache License, Version 2.0 (the \"License\");\nyou may not use this file except in compliance with the License.\nYou may obtain a copy of the License at\n\thttp://www.apache.org/licenses/LICENSE-2.0\n\nUnless required by applicable law or agreed to in writing, software\ndistributed under the License is distributed on an \"AS IS\" BASIS,\nWITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\nSee the License for the specific language governing permissions and\nlimitations under the License.{credits_filler}")
    text_credits.pack(pady=20)
    init(Exitable=True)
    

# Init Function (to main) #
def init(Exitable=False):
    if Exitable:
        btn_exit = tk.Button(root, text="Exit", command=init)
        btn_exit.pack(pady=10)
        Exitable = False
    else:
        clear()
        # ~~ MAIN ~~ ~~ MAIN ~~  ~~ MAIN ~~  ~~ MAIN ~~  ~~ MAIN ~~  ~~ MAIN ~~ 

        # Main Buttons #
        btn_hello = tk.Button(root, text="Help", command=help)
        btn_atbash = tk.Button(root, text="AtBash Solver", command=lambda: AtBash_de.main())
        btn_caeser = tk.Button(root, text="Caeser Cipher Solver", command=lambda: caeser_cipher_de.main())
        btn_hexoctbin = tk.Button(root, text="Hex/Oct/Bin Decoder", command=lambda: hex_oct_bin_de.main())

        # Main Buttons BOTTOM #
        btn_credits = tk.Button(root, text="Credits", command=credits)

        # Main Pack #
        btn_hello.pack(pady=10)
        btn_atbash.pack(pady=10)
        btn_caeser.pack(pady=10)
        btn_hexoctbin.pack(pady=10)
        btn_credits.pack(pady=10)

        # ~~ END MAIN ~~ ~~ END MAIN ~~  ~~ END MAIN ~~  ~~ END MAIN ~~



init()
root.mainloop()