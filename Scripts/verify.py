import os
import tkinter as tk
from tkinter import ttk

def main():
    # Constants #
    VERSION = "1.0"
    # Get root directory
    rootdir = os.path.dirname(__file__)
    credits_filler = "\n********************************************************\n"
    state = {
        "plaintext": "",
        "ciphertext": "",
        "entered_plaintext": False,
        "entered_ciphertext": False
    }

    root = tk.Tk()
    root.title("Verfication Suite")
    root.geometry("750x750")

    # Clear Function #
    def clear():
        for widget in root.winfo_children():
            widget.destroy()


    # Init Function (to main) #
    def init(Exitable=False):
        if Exitable:
            btn_exit = tk.Button(root, text="Exit", command=init)
            btn_exit.pack(pady=10)
            Exitable = False
        else:

            def enter_plaintext():
                state["plaintext"] = entry_plaintext.get("1.0", tk.END).strip()
                state["entered_plaintext"] = True
                btn_plaintext.config(text="✅ PLAINTEXT ENTERED")
                if state["entered_plaintext"] and state["entered_ciphertext"]:
                    tools()
                #print(plaintext)

            def enter_ciphertext():
                state["ciphertext"] = entry_ciphertext.get("1.0", tk.END).strip()
                state["entered_ciphertext"] = True
                btn_ciphertext.config(text="✅ CIPHERTEXT ENTERED")
                if state["entered_plaintext"] and state["entered_ciphertext"]:
                    tools()
                #print(ciphertext)

            def tools():
                # lowercase #
                def lowercase():
                    entry_plaintext.delete("1.0", tk.END)
                    entry_ciphertext.delete("1.0", tk.END)
                    entry_plaintext.insert("1.0", state["plaintext"].lower())
                    entry_ciphertext.insert("1.0", state["ciphertext"].lower())

                def uppercase():
                    entry_plaintext.delete("1.0", tk.END)
                    entry_ciphertext.delete("1.0", tk.END)
                    entry_plaintext.insert("1.0", state["plaintext"].upper())
                    entry_ciphertext.insert("1.0", state["ciphertext"].upper())

                def lencheck():
                    if len(state["plaintext"]) == len(state["ciphertext"]):
                        print("Lengths Match!")
                    else:
                        print("Lengths Do Not Match!")

                btn_lowercase = tk.Button(root, text=".lower()", command=lambda: lowercase())
                btn_lowercase.pack(pady=10)

                btn_uppercase = tk.Button(root, text=".upper()", command=lambda: uppercase())
                btn_uppercase.pack(pady=10)

                btn_lencheck = tk.Button(root, text="Length Check", command=lambda: lencheck())
                btn_lencheck.pack(pady=10)
                #   #

            clear()
            # ~~ MAIN ~~ ~~ MAIN ~~  ~~ MAIN ~~  ~~ MAIN ~~  ~~ MAIN ~~  ~~ MAIN ~~ 

            entry_plaintext = tk.Text(root, height=15)
            btn_plaintext = tk.Button(root, text="ENTER PLAINTEXT", command=enter_plaintext)

            entry_ciphertext = tk.Text(root, height=15)
            btn_ciphertext = tk.Button(root, text="ENTER CIPHERTEXT", command=enter_ciphertext)

            # MAIN PACK #
            entry_plaintext.pack(padx=10, pady=10, expand=False)
            btn_plaintext.pack(pady=10)

            entry_ciphertext.pack(padx=10, pady=10, expand=False)
            btn_ciphertext.pack(pady=10)

            # ~~ END MAIN ~~ ~~ END MAIN ~~  ~~ END MAIN ~~  ~~ END MAIN ~~

        

    init()
    root.mainloop()

if __name__ == "__main__":
    main()  # only runs if you execute this file directly