
import os
import customtkinter as ctk


def main():

    # Constants #
    VERSION = "1.0"
    # Get root directory
    rootdir = os.path.dirname(os.path.dirname(__file__))
    credits_filler = "\n********************************************************\n\n"
    state = {"decipher_running": False}

    root = ctk.CTk()
    root.title("Index of Coincidence Calculator")
    root.geometry("1000x700")
    root.iconbitmap(os.path.join(rootdir, "res", "favicon.ico"))
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    def decipher():
        string=textbox_input.get("1.0", ctk.END).strip().lower()
        textbox_output.configure(state="normal")
        textbox_output.delete("1.0", ctk.END)
        sigma = 0

        string = string.replace(" ", "")

        alphabet = textbox_alphabet.get("1.0", ctk.END).strip()
        alphabet = list(alphabet)

        for letter in alphabet:
            if string.count(letter) <=1:
                IC = 0
            else:
                IC = 26 * ( string.count(letter) / len(string) ) * ( string.count(letter)-1 / len(string)-1 )
                textbox_output.configure(state="normal")
                textbox_output.insert("end", f"{letter} = {IC}\n")
               # print(f"{letter} = {IC}")
            sigma += IC

        textbox_output.insert("end", f"## Sigma = {sigma}\n")
        textbox_output.configure(state="disabled")


    textbox_frame = ctk.CTkFrame(root)
    textbox_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    textbox_frame.grid_columnconfigure(0, weight=1, uniform="textcols")
    textbox_frame.grid_columnconfigure(1, weight=1, uniform="textcols")

   # -- cipher processing -- #

    textbox_input = ctk.CTkTextbox(textbox_frame, font=("Courier New", 12), activate_scrollbars=False)
    textbox_input.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
    textbox_input.configure(height=300, width=300)

    label_input = ctk.CTkLabel(textbox_frame, text="Input:", font=ctk.CTkFont(size=16, weight="bold"))
    label_input.grid(row=0, column=0, padx=20, pady=(10,0))


    btn_input_process = ctk.CTkButton(
        textbox_frame,
        text="Calculate Index of Coincidence",
        command=decipher
    )
    btn_input_process.grid(row=2, column=0, pady=10, columnspan=2)


    textbox_output = ctk.CTkTextbox(textbox_frame, font=("Courier New", 12), activate_scrollbars=False)
    textbox_output.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
    textbox_output.configure(state="disabled")

    label_output = ctk.CTkLabel(textbox_frame, text="Output:", font=ctk.CTkFont(size=16, weight="bold"))
    label_output.grid(row=0, column=1, padx=20, pady=(10,0))


    label_alphabet = ctk.CTkLabel(textbox_frame, text="Alphabet:", font=ctk.CTkFont(size=16, weight="bold"))
    label_alphabet.grid(row=3, column=0, padx=20, pady=(10,0), sticky="nsew",columnspan=2)

    textbox_alphabet = ctk.CTkTextbox(textbox_frame, font=("Courier New", 12), activate_scrollbars=False, height=30, width=200)

    textbox_alphabet.grid(row=4, column=0, padx=20, pady=(0,10), sticky="nsew", columnspan=2)
    textbox_alphabet.insert("1.0", "abcdefghijklmnopqrstuvwxyz")



    def on_closing():
        
        root.withdraw()
        root.quit()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()