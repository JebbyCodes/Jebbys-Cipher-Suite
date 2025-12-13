
import os
import customtkinter as ctk
import tkinter as tk
import threading
import configparser

def main():

    # Constants #
    VERSION = "1.0"
    # Get root directory
    rootdir = os.path.dirname(os.path.dirname(__file__))
    credits_filler = "\n********************************************************\n\n"
    state = {"decipher_running": False, "isKey": False}
    CONFIG = configparser.ConfigParser()
    CONFIG.read(os.path.join(rootdir, "config.cfg"))

    root = ctk.CTk()
    root.title("Playfair Cipher Solver")
    root.geometry("1000x700")
    root.iconbitmap(os.path.join(rootdir, "res", "favicon.ico"))
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)


    def decipher():
        if state["isKey"]:
            state["decipher_running"] = True

            threading.Thread(target=processing).start()
            txt = textbox_cipher.get("1.0", ctk.END).strip()
            key = textbox_key.get("1.0", ctk.END).strip()

            def create_playfair_square(phrase):
                #Generate the Playfair square for the given phrase.
                phrase = phrase.replace('J', 'I').upper()
                alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

                full_key = phrase + alphabet
                full_key = "".join(dict.fromkeys(full_key))  # Remove duplicates

                grid = [[full_key[i + j] for j in range(5)] for i in range(0, 25, 5)]
                return grid


            def find_location(grid, char):
                #Return (row, col) of char in the grid.
                char = char.replace('J', 'I')
                for i in range(5):
                    for j in range(5):
                        if grid[i][j] == char:
                            return i, j
                return None


            def playfair_decrypt(txt: str, key: str) -> str:
                txt = txt.replace("J", "I").upper()
                playfair_square = create_playfair_square(key)
                message = ''

                # Process digraphs
                for i in range(0, len(txt), 2):
                    digraph = txt[i:i+2]
                    row1, col1 = find_location(playfair_square, digraph[0])
                    row2, col2 = find_location(playfair_square, digraph[1])

                    if row1 == row2:  # Same row - move left
                        sub1 = playfair_square[row1][(col1 - 1) % 5]
                        sub2 = playfair_square[row2][(col2 - 1) % 5]

                    elif col1 == col2:  # Same column - move up
                        sub1 = playfair_square[(row1 - 1) % 5][col1]
                        sub2 = playfair_square[(row2 - 1) % 5][col2]

                    else:  # Rectangle swap
                        sub1 = playfair_square[row1][col2]
                        sub2 = playfair_square[row2][col1]

                    message += sub1 + sub2

                # Clean up inserted X's
                # TODO: MAKE THIS USERINPUT BASED
                i = 0
                while i < len(message) - 2:
                    if message[i] == message[i+2] and message[i+1] == 'X':
                        message = message[:i+1] + message[i+2:]
                    i += 1

                if message.endswith("X"):
                    message = message[:-1]

                    #return plaintext
                textbox_plain.configure(state="normal")
                textbox_plain.delete("1.0", ctk.END)
                textbox_plain.insert("1.0", message)
                state["decipher_running"] = False
                textbox_key.configure(state="normal")

            playfair_decrypt(txt, key)


        else:
            state["decipher_running"] = False
            textbox_processing.configure(state="normal")
            #textbox_processing.delete("1.0", "end")
            textbox_processing.insert("1.0", "\nERROR: BRUTEFORCE METHOD NOT VIABLE")
            textbox_processing.configure(state="disabled")

        

    textbox_frame = ctk.CTkFrame(root)
    textbox_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    textbox_frame.grid_columnconfigure(0, weight=1, uniform="textcols")
    textbox_frame.grid_columnconfigure(1, weight=1, uniform="textcols")

    # -- cipher processing -- #
    #decipher_thread = threading.Thread(target=decipher)
    

    textbox_cipher = ctk.CTkTextbox(textbox_frame, font=("Courier New", 12), activate_scrollbars=False)
    textbox_cipher.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
    textbox_cipher.configure(height=300, width=300)

    label_cipher = ctk.CTkLabel(textbox_frame, text="Ciphertext:", font=ctk.CTkFont(size=16, weight="bold"))
    label_cipher.grid(row=0, column=0, padx=20, pady=(10,0))

    def start_decipher():
        threading.Thread(target=decipher).start()

    btn_cipher_process = ctk.CTkButton(
        textbox_frame,
        text="Process Playfair Cipher",
        command=start_decipher
    )
    btn_cipher_process.grid(row=2, column=0, pady=10)

    # -- key processing -- #
    textbox_key = ctk.CTkTextbox(textbox_frame, font=("Courier New", 12), activate_scrollbars=False, height=30, width=200)

    def on_enter():
        start_decipher()
        return "break"

    textbox_key = ctk.CTkTextbox(textbox_frame, font=("Courier New", 12), activate_scrollbars=False, height=30, width=200)

    if CONFIG.getboolean("SETTINGS", "QUICK_ENTER", fallback=False):
        textbox_key.bind("<Return>", lambda event: on_enter())

    def setKey():
        if switch_key_var.get() == "on":
            state["isKey"] = True
            textbox_key.grid(row=3, column=1, pady=10)
            #print("Key input enabled")
        else:
            state["isKey"] = False
            textbox_key.grid_forget()
            #print("Key input disabled")

    switch_key_var = tk.StringVar(value="off")

    switch_key = ctk.CTkSwitch(textbox_frame, text="Input a key?", command=setKey, variable=switch_key_var, onvalue="on", offvalue="off")
    switch_key.grid(row=2, column=1, pady=10)
    # -- END key processing END -- #

    # -- END cipher processing END -- #

    def update_highlight_plain(event):
        """Highlight selected text in both textboxes."""
        original = event.widget
        try:
            first = original.index("sel.first")
            last = original.index("sel.last")
        except tk.TclError:
            for w in [textbox_cipher, textbox_plain]:
                w.tag_remove("sel_txt", "1.0", ctk.END)
            return

        for w in [textbox_cipher, textbox_plain]:
            w.tag_remove("sel_txt", "1.0", ctk.END)
            w.tag_add("sel_txt", first, last)
            w.tag_config("sel_txt", background="#007ACC", foreground="white")

    textbox_cipher.bind("<<Selection>>", update_highlight_plain) # we want it to go both ways


    def sync_scroll(event=None):
        first, last = textbox_cipher.yview()
        textbox_plain.yview_moveto(first)
        return "break"  # prevent recursive event

    # -- plain processing -- #

    textbox_plain = ctk.CTkTextbox(textbox_frame, font=("Courier New", 12), activate_scrollbars=False)
    textbox_plain.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
    textbox_plain.bind("<<Selection>>", update_highlight_plain) # we want it to go both ways

    label_plain = ctk.CTkLabel(textbox_frame, text="Plaintext:", font=ctk.CTkFont(size=16, weight="bold"))
    label_plain.grid(row=0, column=1, padx=20, pady=(10,0))

    # -- END plain processing END -- #

    # -- General Processing -- #
    textbox_processing = ctk.CTkTextbox(textbox_frame, font=("Courier New", 24), activate_scrollbars=False)
    textbox_processing.grid(row=5, columnspan=2, padx=10, sticky="nsew")
    textbox_processing.configure(state="normal")
    textbox_processing.insert("1.0", "NOT RUNNING")
    textbox_processing.configure(state="disabled")

    def processing():
        while state["decipher_running"]:
            textbox_processing.configure(state="normal")
            textbox_processing.delete("1.0", "end")
            textbox_processing.insert("1.0", "RUNNING |")
                
            textbox_processing.delete("1.0", "end")
            textbox_processing.insert("1.0", "RUNNING /")
                
            textbox_processing.delete("1.0", "end")
            textbox_processing.insert("1.0", "RUNNING -")
                
            textbox_processing.delete("1.0", "end")
            textbox_processing.insert("1.0", "RUNNING \\")
                
            textbox_processing.delete("1.0", "end")
            textbox_processing.insert("1.0", "RUNNING |")
            
            textbox_processing.delete("1.0", "end")
            textbox_processing.insert("1.0", "RUNNING /")
                
            textbox_processing.delete("1.0", "end")
            textbox_processing.insert("1.0", "RUNNING -")
                
            textbox_processing.delete("1.0", "end")
            textbox_processing.insert("1.0", "RUNNING \\")
                
            textbox_processing.delete("1.0", "end")
            textbox_processing.configure(state="disabled")
                

    # -- Sync scrolling -- #
    scroll_shared = ctk.CTkScrollbar(textbox_frame)
    scroll_shared.grid(row=1, column=2, sticky="ns", pady=20)

    def sync_scroll(*args):
        #Handle scrollbar or mousewheel scrolls.
        textbox_cipher.yview(*args)
        textbox_plain.yview(*args)
        return "break"

    def on_cipher_scroll(first, last):
        #Sync cipher scroll updates to shared scrollbar.
        scroll_shared.set(first, last)
        textbox_plain.yview_moveto(first)

    def on_plain_scroll(first, last):
        #Sync plain scroll updates to shared scrollbar.
        scroll_shared.set(first, last)
        textbox_cipher.yview_moveto(first)

    textbox_cipher.configure(yscrollcommand=on_cipher_scroll)
    textbox_plain.configure(yscrollcommand=on_plain_scroll)
    scroll_shared.configure(command=sync_scroll)

    textbox_plain.configure(state="disabled")
    

    # -- END Sync scrolling END -- #
    def on_closing():
        
        root.withdraw()
        root.quit()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()


if __name__ == "__main__":
    main()  # only runs if you execute this file directly





