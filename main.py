import os
import tkinter as tk
import wordfreq
import customtkinter as ctk
from Scripts import AtBash_de, caeser_cipher_de, hex_oct_bin_de, bacon_de, substitution_de, affine_de, verify

# Constants #
VERSION = "1.0"
# Get root directory
rootdir = os.path.dirname(__file__)
credits_filler = "\n********************************************************\n\n"

root = ctk.CTk()
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
    text_help = ctk.CTkLabel(root, text="What is this?\n\t>This is a simple Tkinter application to centralise all the created scripts in handy little buttons!")
    text_help.pack(pady=20)
    init(Exitable=True)

# Credits Function #
def credits():
    clear()
    #Credits#
    text_credits = ctk.CTkLabel(root, text=f"""
CREDITS:
MODULES USED:

    > wordfreq
        Created by: Robyn Speer
        Licence: Apache License, Version 2.0;
        Copyright 2022 Robyn Speer

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at:
    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

    > customtkinter
        Created by: Tom Schimansky
        Licence: MIT License (Creative Commons Zero v1.0 Universal);
        MIT License

MIT License

Copyright (c) 2023 Tom Schimansky

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
{credits_filler}""")
    text_credits.pack(pady=20)
    init(Exitable=True)
    

# Init Function (to main) #
def init(Exitable=False):
    if Exitable:
        btn_exit = ctk.CTkButton(root, text="Exit", command=init)
        btn_exit.pack(pady=10)
        Exitable = False
    else:
        clear()
        # ~~ MAIN ~~ ~~ MAIN ~~  ~~ MAIN ~~  ~~ MAIN ~~  ~~ MAIN ~~  ~~ MAIN ~~ 

        # Main Buttons #
        btn_hello = ctk.CTkButton(root, text="Help", command=help)
        btn_atbash = ctk.CTkButton(root, text="AtBash Solver", command=lambda: AtBash_de.main())
        btn_caeser = ctk.CTkButton(root, text="Caeser Cipher Solver", command=lambda: caeser_cipher_de.main())
        btn_hexoctbin = ctk.CTkButton(root, text="Hex/Oct/Bin Decoder", command=lambda: hex_oct_bin_de.main())
        btn_bacon = ctk.CTkButton(root, text="Bacon Cipher Solver", command=lambda: bacon_de.main())
        btn_substitution = ctk.CTkButton(root, text="Substitution Cipher Solver", command=lambda: substitution_de.main())
        btn_affine = ctk.CTkButton(root, text="Affine Cipher Solver", command=lambda: affine_de.main())

        # Main Buttons BOTTOM #
        btn_verify = ctk.CTkButton(root, text="Verify", command=lambda: verify.main())
        btn_credits = ctk.CTkButton(root, text="Credits", command=credits)

        # Main Pack #
        btn_hello.pack(pady=10)
        btn_atbash.pack(pady=10)
        btn_caeser.pack(pady=10)
        btn_hexoctbin.pack(pady=10)
        btn_bacon.pack(pady=10)
        btn_substitution.pack(pady=10)
        btn_affine.pack(pady=10)

        btn_verify.pack(pady=10)
        btn_credits.pack(pady=10)

        # ~~ END MAIN ~~ ~~ END MAIN ~~  ~~ END MAIN ~~  ~~ END MAIN ~~



init()
root.mainloop()