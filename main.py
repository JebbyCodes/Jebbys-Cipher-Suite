import os
import sys
import customtkinter as ctk
from Scripts import atBash_de, caeser_cipher_de, hex_oct_bin_de, bacon_de, affine_de, verify, frequency_analyser, vigenere_de, transposition_de, playfair_de

sys.path.append(os.path.join(os.path.dirname(__file__), "Scripts", "substitution"))
from Scripts import playfair_de
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
    text_help.insert("1.0",f"""What is this?
                        \n\t>This is a simple Tkinter application to centralise all the created scripts into handy little buttons!
                     """)
    text_help.grid(pady=20, padx=20, sticky="nsew")
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
                        ~~~~~~~~
    > numpy
        Created by: Travis E. Oliphant et al.
        Licence: BSD 3-Clause License;
        Copyright (c) 2005-2025, NumPy Developers.
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are
    met:

    * Redistributions of source code must retain the above copyright
       notice, this list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above
       copyright notice, this list of conditions and the following
       disclaimer in the documentation and/or other materials provided
       with the distribution.

    * Neither the name of the NumPy Developers nor the names of any
       contributors may be used to endorse or promote products derived
       from this software without specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
    "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
    LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
    A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
    OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
    SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
    LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
    DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
    THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
                        
                    ~~~~~~~~
    > matplotlib
        Created by: John D. Hunter, Michael Droettboom
        Licence: License agreement for matplotlib versions 1.3.0 and later;
    =========================================================

    1. This LICENSE AGREEMENT is between the Matplotlib Development Team
    ("MDT"), and the Individual or Organization ("Licensee") accessing and
    otherwise using matplotlib software in source or binary form and its
    associated documentation.

    2. Subject to the terms and conditions of this License Agreement, MDT
    hereby grants Licensee a nonexclusive, royalty-free, world-wide license
    to reproduce, analyze, test, perform and/or display publicly, prepare
    derivative works, distribute, and otherwise use matplotlib
    alone or in any derivative version, provided, however, that MDT's
    License Agreement and MDT's notice of copyright, i.e., "Copyright (c)
    2012- Matplotlib Development Team; All Rights Reserved" are retained in
    matplotlib  alone or in any derivative version prepared by
    Licensee.

    3. In the event Licensee prepares a derivative work that is based on or
    incorporates matplotlib or any part thereof, and wants to
    make the derivative work available to others as provided herein, then
    Licensee hereby agrees to include in any such work a brief summary of
    the changes made to matplotlib .

    4. MDT is making matplotlib available to Licensee on an "AS
    IS" basis.  MDT MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR
    IMPLIED.  BY WAY OF EXAMPLE, BUT NOT LIMITATION, MDT MAKES NO AND
    DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS
    FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF MATPLOTLIB
    WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.

    5. MDT SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF MATPLOTLIB
    FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR
    LOSS AS A RESULT OF MODIFYING, DISTRIBUTING, OR OTHERWISE USING
    MATPLOTLIB , OR ANY DERIVATIVE THEREOF, EVEN IF ADVISED OF
    THE POSSIBILITY THEREOF.

    6. This License Agreement will automatically terminate upon a material
    breach of its terms and conditions.

    7. Nothing in this License Agreement shall be deemed to create any
    relationship of agency, partnership, or joint venture between MDT and
    Licensee.  This License Agreement does not grant permission to use MDT
    trademarks or trade name in a trademark sense to endorse or promote
    products or services of Licensee, or any third party.

    8. By copying, installing or otherwise using matplotlib ,
    Licensee agrees to be bound by the terms and conditions of this License
    Agreement.

    License agreement for matplotlib versions prior to 1.3.0
    ========================================================

    1. This LICENSE AGREEMENT is between John D. Hunter ("JDH"), and the
    Individual or Organization ("Licensee") accessing and otherwise using
    matplotlib software in source or binary form and its associated
    documentation.

    2. Subject to the terms and conditions of this License Agreement, JDH
    hereby grants Licensee a nonexclusive, royalty-free, world-wide license
    to reproduce, analyze, test, perform and/or display publicly, prepare
    derivative works, distribute, and otherwise use matplotlib
    alone or in any derivative version, provided, however, that JDH's
    License Agreement and JDH's notice of copyright, i.e., "Copyright (c)
    2002-2011 John D. Hunter; All Rights Reserved" are retained in
    matplotlib  alone or in any derivative version prepared by
    Licensee.

    3. In the event Licensee prepares a derivative work that is based on or
    incorporates matplotlib  or any part thereof, and wants to
    make the derivative work available to others as provided herein, then
    Licensee hereby agrees to include in any such work a brief summary of
    the changes made to matplotlib.

    4. JDH is making matplotlib  available to Licensee on an "AS
    IS" basis.  JDH MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR
    IMPLIED.  BY WAY OF EXAMPLE, BUT NOT LIMITATION, JDH MAKES NO AND
    DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS
    FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF MATPLOTLIB
    WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.

    5. JDH SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF MATPLOTLIB
    FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR
    LOSS AS A RESULT OF MODIFYING, DISTRIBUTING, OR OTHERWISE USING
    MATPLOTLIB , OR ANY DERIVATIVE THEREOF, EVEN IF ADVISED OF
    THE POSSIBILITY THEREOF.

    6. This License Agreement will automatically terminate upon a material
    breach of its terms and conditions.

    7. Nothing in this License Agreement shall be deemed to create any
    relationship of agency, partnership, or joint venture between JDH and
    Licensee.  This License Agreement does not grant permission to use JDH
    trademarks or trade name in a trademark sense to endorse or promote
    products or services of Licensee, or any third party.

    8. By copying, installing or otherwise using matplotlib,
    Licensee agrees to be bound by the terms and conditions of this License
    Agreement.
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

        btn_playfair = ctk.CTkButton(frame_main, text="Playfair Cipher Solver",command=lambda: playfair_de.main(), width=200, height=50, font=ctk.CTkFont(weight="bold"))
        btn_playfair._text_label.configure(wraplength = root.winfo_width())

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
        btn_playfair.grid(row=7, column=0, columnspan=2, pady=10, sticky="nsew")
        btn_freqanalyse.grid(row=8, column=0, columnspan=2, pady=10, sticky="nsew")
        btn_verify.grid(row=9, column=0, columnspan=2, pady=10, sticky="nsew")

        # ~~ END MAIN ~~ ~~ END MAIN ~~  ~~ END MAIN ~~  ~~ END MAIN ~~



init()
def on_closing():    
    root.withdraw()
    root.quit()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()