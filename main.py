from logging import config
import os
import sys
import customtkinter as ctk
import tkinter as tk
import configparser
import shutil
from Scripts import atBash_de, caeser_cipher_de, hex_oct_bin_de, bacon_de, affine_de, verify, frequency_analyser, vigenere_de, transposition_de, playfair_de, ioc, beaufort_de

sys.path.append(os.path.join(os.path.dirname(__file__), "Scripts", "substitution"))
from Scripts import playfair_de
from Scripts.substitution import main_substitution

# Constants #
VERSION = "1.0"
# Get root directory
rootdir = os.path.dirname(__file__)
credits_filler = "\n********************************************************\n\n"
CONFIG = configparser.ConfigParser()

if not os.path.exists("config.cfg"):
    shutil.copy("config.default.cfg", "config.cfg")

CONFIG.read(os.path.join(rootdir, "config.cfg"))

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
    
    with open(os.path.join(rootdir, "THIRD_PARTY_LICENCES.txt"), "r", encoding="utf-8") as f:
        credits_raw = f.read()

    text_credits.insert("1.0", credits_raw)
        
    text_credits.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    text_credits.configure(state="disabled")
    
    init(True)

def settings():
    clear()

    frame_settings = ctk.CTkFrame(root)
    frame_settings.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    frame_settings.grid_columnconfigure(0, weight=1)

    #Settings#
    btn_help = ctk.CTkButton(frame_settings, text="Help", command=help, width=100, height=25)
    btn_help.grid(row=0, column=0, padx=5, pady=10)

    label_settings = ctk.CTkLabel(frame_settings, text="Settings:", font=ctk.CTkFont(size=20, weight="bold"))
    label_settings.grid(row=1, column=0, padx=5, pady=10)

    # Quick Enter Setting #
    def QUICK_ENTER():
        if "SETTINGS" not in CONFIG:
            CONFIG.add_section("SETTINGS")

        CONFIG["SETTINGS"]["QUICK_ENTER"] = "ON" if var_QUICK_ENTER.get() else "OFF"

        with open(os.path.join(rootdir, "config.cfg"), "w") as f:
            CONFIG.write(f)

    var_QUICK_ENTER = ctk.BooleanVar()

    switch_QUICK_ENTER = ctk.CTkSwitch(
        frame_settings,
        text="Quick Enter",
        variable=var_QUICK_ENTER,
        command=QUICK_ENTER
    )
    switch_QUICK_ENTER.grid(row=2, column=0, padx=5, pady=10)



    def sync_settings():
        CONFIG.read(os.path.join(rootdir, "config.cfg"))

        enabled = CONFIG.getboolean("SETTINGS", "QUICK_ENTER", fallback=False)
        var_QUICK_ENTER.set(enabled)
    sync_settings()

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

        btn_credits = ctk.CTkButton(frame_main, text="Credits", command=credits, width=50, height=25)

        btn_settings = ctk.CTkButton(frame_main, text="Settings", command=settings, width=50, height=25)

        btn_atbash = ctk.CTkButton(frame_main, text="AtBash Solver", command=lambda: atBash_de.main(), width=200, height=50, font=ctk.CTkFont(weight="bold"))

        btn_caeser = ctk.CTkButton(frame_main, text="Caeser Cipher Solver", command=lambda: caeser_cipher_de.main(), width=200, height=50, font=ctk.CTkFont(weight="bold"))

        btn_transposition = ctk.CTkButton(frame_main, text="Transposition Cipher Solver", command=lambda: transposition_de.main(), width=200, height=50, font=ctk.CTkFont(weight="bold"))
        btn_transposition._text_label.configure(wraplength = root.winfo_width())

        btn_hexoctbin = ctk.CTkButton(frame_main, text="Hex/Oct/Bin Decoder", command=lambda: hex_oct_bin_de.main(), width=200, height=50, font=ctk.CTkFont(weight="bold"))

        btn_bacon = ctk.CTkButton(frame_main, text="Bacon Cipher Solver", command=lambda: bacon_de.main(), width=200, height=50, font=ctk.CTkFont(weight="bold"))

        btn_substitution = ctk.CTkButton(frame_main, text="Substitution Cipher Solver", command=lambda: main_substitution.main(), width=200, height=50, font=ctk.CTkFont(weight="bold"))

        btn_affine = ctk.CTkButton(frame_main, text="Affine Cipher Solver", command=lambda: affine_de.main(), width=200, height=50, font=ctk.CTkFont(weight="bold"))

        btn_freqanalyse = ctk.CTkButton(frame_main, text="Frequency Analyser", command=lambda: frequency_analyser.main(), width=200, height=50, font=ctk.CTkFont(weight="bold"), fg_color="#C33E78", hover_color="#852B52")

        btn_ioc = ctk.CTkButton(frame_main, text="Index of Coincidence Calculator", command=lambda: ioc.main(), width=200, height=50, font=ctk.CTkFont(weight="bold"), fg_color="#C33E78", hover_color="#852B52")

        btn_vigenere = ctk.CTkButton(frame_main, text="Vigenère Cipher Solver",command=lambda: vigenere_de.main(), width=200, height=50, font=ctk.CTkFont(weight="bold"))
        btn_vigenere._text_label.configure(wraplength = root.winfo_width())

        btn_beaufort = ctk.CTkButton(frame_main, text="Beaufort Cipher Solver",command=lambda: beaufort_de.main(), width=200, height=50, font=ctk.CTkFont(weight="bold"))
        btn_beaufort._text_label.configure(wraplength = root.winfo_width())

        btn_playfair = ctk.CTkButton(frame_main, text="Playfair Cipher Solver",command=lambda: playfair_de.main(), width=200, height=50, font=ctk.CTkFont(weight="bold"))
        btn_playfair._text_label.configure(wraplength = root.winfo_width())

        btn_verify = ctk.CTkButton(frame_main, text="Verify", command=lambda: verify.main(), width=200, height=100, fg_color="#3EC385", hover_color="#29845D", font=ctk.CTkFont(size=16, weight="bold"))
        
        # Main Pack #
        btn_credits.grid(row=0, column=1, padx=5, pady=10, sticky="ew")
        btn_settings.grid(row=0, column=0, padx=5, pady=10, sticky="ew")

        btn_atbash.grid(row=3, column=1, padx=5, pady=10, sticky="nsew")
        btn_vigenere.grid(row=1, column=1, padx=5, pady=10, sticky="nsew")
        btn_beaufort.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
        btn_caeser.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
        btn_transposition.grid(row=2, column=1, padx=5, pady=10, sticky="nsew")
        btn_hexoctbin.grid(row=3, column=0, pady=10, sticky="nsew")
        btn_bacon.grid(row=4, column=0, columnspan=2, pady=10, sticky="nsew")
        btn_substitution.grid(row=5, column=0, columnspan=2, pady=10, sticky="nsew")
        btn_affine.grid(row=6, column=0, columnspan=2, pady=10, sticky="nsew")
        btn_playfair.grid(row=7, column=0, columnspan=2, pady=10, sticky="nsew")
        btn_freqanalyse.grid(row=8, column=0, columnspan=1, pady=10, padx=5, sticky="nsew")
        btn_ioc.grid(row=8, column=1, columnspan=1, pady=10, padx=5, sticky="nsew")
        btn_verify.grid(row=9, column=0, columnspan=2, pady=10, sticky="nsew")

        # ~~ END MAIN ~~ ~~ END MAIN ~~  ~~ END MAIN ~~  ~~ END MAIN ~~



init()
def on_closing():    
    root.withdraw()
    root.quit()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()