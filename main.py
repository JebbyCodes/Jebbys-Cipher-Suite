import os
import sys
import customtkinter as ctk # type: ignore
from Scripts import atBash_de, caeser_cipher_de, hex_oct_bin_de, bacon_de, affine_de, verify, frequency_analyser, vigenere_de, transposition_de

sys.path.append(os.path.join(os.path.dirname(__file__), "Scripts", "substitution"))
from Scripts.substitution import main_substitution

# Constants #
VERSION = "1.0"
# Get root directory
rootdir = os.path.dirname(__file__)
credits_filler = "\n********************************************************\n\n"

root = ctk.CTk()
root.title("Jebby's Cipher Suite")
root.geometry("500x700")
root.iconbitmap(os.path.join(rootdir, "res", "favicon.ico"))
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Clear Function #
def clear():
    for widget in root.winfo_children():
        widget.destroy()

# Help Function #
def help():
    clear()
    #Help#
    text_help = ctk.CTkTextbox(root, wrap="word")
    text_help.insert("1.0",f"""
                     What is this?
                        >This is a simple Tkinter application to centralise all the created scripts in handy little buttons!
                     """)
    text_help.grid(pady=20)
    text_help.configure(state="disabled")
    init(Exitable=True)

# Credits Function #
def credits():
    clear()
    #Credits#
    text_credits = ctk.CTkTextbox(root, wrap="word")
    
    text_credits.insert("1.0",f"""
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
                                ~~~~~~~~
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
                        ~~~~~~~~
    > wordsegment
        Created by: Grant Jenks
        Licence: Apache Software License (Apache 2.0);
        WordSegment License
        -------------------

        Copyright 2018 Grant Jenks

        Licensed under the Apache License, Version 2.0 (the "License");
        you may not use this file except in compliance with the License.
        You may obtain a copy of the License at

            http://www.apache.org/licenses/LICENSE-2.0

        Unless required by applicable law or agreed to in writing, software
        distributed under the License is distributed on an "AS IS" BASIS,
        WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
        See the License for the specific language governing permissions and
        limitations under the License.
{credits_filler}""")
    text_credits.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    text_credits.configure(state="disabled")
    
    init(True)
    

# Init Function (to main) #
def init(Exitable=False):
    if Exitable:
        btn_exit = ctk.CTkButton(root, text="Exit", command=init)
        btn_exit.grid(pady=10)
        Exitable = False
    else:
        clear()
        # ~~ MAIN ~~ ~~ MAIN ~~  ~~ MAIN ~~  ~~ MAIN ~~  ~~ MAIN ~~  ~~ MAIN ~~ 
        frame_main = ctk.CTkFrame(root)
        frame_main.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        frame_main.grid_columnconfigure(0, weight=1)
        frame_main.grid_columnconfigure(1, weight=1)
        for i in range(1, 9): # number of rows (essentially normal main buttons)
            frame_main.grid_rowconfigure(i, weight=1)

        # Main Buttons #
        btn_help = ctk.CTkButton(frame_main, text="Help", command=help, width=50, height=25)

        btn_credits = ctk.CTkButton(frame_main, text="Credits", command=credits, width=50, height=25)

        btn_atbash = ctk.CTkButton(frame_main, text="AtBash Solver", command=lambda: atBash_de.main(), width=200, height=50, font=ctk.CTkFont(weight="bold"))

        btn_caeser = ctk.CTkButton(frame_main, text="Caeser Cipher Solver", command=lambda: caeser_cipher_de.main(), width=200, height=50, font=ctk.CTkFont(weight="bold"))

        btn_transposition = ctk.CTkButton(frame_main, text="Transposition Cipher Solver", command=lambda: transposition_de.main(), width=200, height=50, font=ctk.CTkFont(weight="bold"))
        btn_transposition._text_label.configure(wraplength = root.winfo_width())

        btn_hexoctbin = ctk.CTkButton(frame_main, text="Hex/Oct/Bin Decoder", command=lambda: hex_oct_bin_de.main(), width=200, height=50, font=ctk.CTkFont(weight="bold"))

        btn_bacon = ctk.CTkButton(frame_main, text="Bacon Cipher Solver", command=lambda: bacon_de.main(), width=200, height=50, font=ctk.CTkFont(weight="bold"))

        btn_substitution = ctk.CTkButton(frame_main, text="Substitution Cipher Solver", command=lambda: main_substitution.main(), width=200, height=50, font=ctk.CTkFont(weight="bold"))

        btn_affine = ctk.CTkButton(frame_main, text="Affine Cipher Solver", command=lambda: affine_de.main(), width=200, height=50, font=ctk.CTkFont(weight="bold"))

        btn_freqanalyse = ctk.CTkButton(frame_main, text="Frequency Analyser", command=lambda: frequency_analyser.main(), width=200, height=50, font=ctk.CTkFont(weight="bold"))

        btn_vigenere = ctk.CTkButton(frame_main, text="Vigenère Cipher Solver",command=lambda: vigenere_de.main(), width=200, height=50, font=ctk.CTkFont(weight="bold"))
        btn_vigenere._text_label.configure(wraplength = root.winfo_width())

        btn_verify = ctk.CTkButton(frame_main, text="Verify", command=lambda: verify.main(), width=200, height=100, fg_color="#3EC385", hover_color="#29845D", font=ctk.CTkFont(size=16, weight="bold"))
        
        # Main Pack #
        btn_help.grid(row=0, column=0, padx=5, pady=10, sticky="ew")
        btn_credits.grid(row=0, column=1, padx=5, pady=10, sticky="ew")

        btn_atbash.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
        btn_vigenere.grid(row=1, column=1, padx=5, pady=10, sticky="nsew")
        btn_caeser.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
        btn_transposition.grid(row=2, column=1, padx=5, pady=10, sticky="nsew")
        btn_hexoctbin.grid(row=3, column=0, columnspan=2, pady=10, sticky="nsew")
        btn_bacon.grid(row=4, column=0, columnspan=2, pady=10, sticky="nsew")
        btn_substitution.grid(row=5, column=0, columnspan=2, pady=10, sticky="nsew")
        btn_affine.grid(row=6, column=0, columnspan=2, pady=10, sticky="nsew")
        btn_freqanalyse.grid(row=7, column=0, columnspan=2, pady=10, sticky="nsew")
        btn_verify.grid(row=8, column=0, columnspan=2, pady=10, sticky="nsew")

        # ~~ END MAIN ~~ ~~ END MAIN ~~  ~~ END MAIN ~~  ~~ END MAIN ~~



init()
def on_closing():    
    root.withdraw()
    root.quit()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()