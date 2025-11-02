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
    root.geometry("1000x700")
    root.iconbitmap(os.path.join(rootdir, "res", "favicon.ico"))
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Clear Function #
    def clear():
        for widget in root.winfo_children():
            widget.destroy()

    textbox_frame = ctk.CTkFrame(root)
    textbox_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    textbox_frame.grid_columnconfigure(0, weight=1, uniform="textcols")
    textbox_frame.grid_columnconfigure(1, weight=1, uniform="textcols")

    label_cipher = ctk.CTkLabel(textbox_frame, text="Ciphertext:", font=ctk.CTkFont(size=16, weight="bold"))
    label_cipher.grid(row=0, column=0, padx=20, pady=(10,0))

    label_plain = ctk.CTkLabel(textbox_frame, text="Plaintext:", font=ctk.CTkFont(size=16, weight="bold"))
    label_plain.grid(row=0, column=1, padx=20, pady=(10,0))

    textbox_cipher = ctk.CTkTextbox(textbox_frame, font=("Courier New", 12))
    textbox_cipher.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
    textbox_cipher.configure(height=300, width=300)

    def update_plain(event=None):
        text = textbox_cipher.get("1.0", ctk.END).strip()
        textbox_plain.configure(state="normal")  # enable temporarily
        textbox_plain.delete("1.0", ctk.END)     # clear old content
        textbox_plain.insert("1.0", text)        # copy new text
        textbox_plain.configure(state="disabled")  # disable again

    textbox_cipher.bind("<KeyRelease>", update_plain)

    textbox_plain = ctk.CTkTextbox(textbox_frame, font=("Courier New", 12))
    textbox_plain.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
    textbox_cipher.configure(height=300, width=300)
    textbox_plain.configure(state="disabled")


    root.mainloop()

if __name__ == "__main__":
    main()