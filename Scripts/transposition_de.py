import os
import sys
import customtkinter as ctk

def main():
    pass

    # Constants #
    VERSION = "1.0"
    # Get root directory
    rootdir = os.path.dirname(os.path.dirname(__file__))
    credits_filler = "\n********************************************************\n\n"

    root = ctk.CTk()
    root.title("Transposition Cipher Solver")
    root.geometry("400x700")
    root.iconbitmap(os.path.join(rootdir, "res", "favicon.ico"))
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Clear Function #
    def clear():
        for widget in root.winfo_children():
            widget.destroy()


            

    root.mainloop()

if __name__ == "__main__":
    main()