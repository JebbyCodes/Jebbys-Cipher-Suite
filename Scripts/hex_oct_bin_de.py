
import os
import customtkinter as ctk
import tkinter as tk
from wordfreq import top_n_list
import configparser

def main():

    # Constants #
    VERSION = "1.0"
    # Get root directory
    rootdir = os.path.dirname(os.path.dirname(__file__))
    credits_filler = "\n********************************************************\n\n"
    CONFIG = configparser.ConfigParser()
    CONFIG.read(os.path.join(rootdir, "config.cfg"))

    root = ctk.CTk()
    root.title("Hex/Oct/Bin Convertor")
    root.geometry("1000x700")
    root.iconbitmap(os.path.join(rootdir, "res", "favicon.ico"))
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    def decipher():
        #print("test")
        commonwords = top_n_list('en', 500000)

        freq = 0
        oldFreq = -1          # allow zero-score results
        #  Hex / Bin / Octo
        # works by converting value in denary then into ascii

        ## Add the text in the string litteral below
        text = textbox_cipher.get("1.0", ctk.END).strip().upper().replace(" ", "")
        noSpaces = text.replace(" ", "")
        backToString = ""
        mostLikely = ""
        if all(let in "0123456789ABCDEF " for let in noSpaces): # yes this works somehow
            result = [noSpaces[i:i+2] for i in range(0, len(noSpaces), 2)]
            decoded = ''.join(chr(int(x, 16)) for x in result).split(" ")
            for word in decoded:
                if word in commonwords:
                    freq += 1
            
     
            if freq > oldFreq:
                mostLikely = decoded
                oldFreq = freq
                freq = 0
                       
     
        if all(let in "01234567 " for let in noSpaces): # yes this works somehow
            result = [noSpaces[i:i+3] for i in range(0, len(noSpaces), 3)]
            decoded = ''.join(chr(int(x, 8)) for x in result).split(" ")
            for word in decoded:
                if word in commonwords:
                    freq += 1

            if freq > oldFreq:
                mostLikely = decoded
                oldFreq = freq
                freq = 0
            
        if all(let in "01 " for let in noSpaces):
            freq = 0
            result = [noSpaces[i:i+8] for i in range(0, len(noSpaces), 8)]
            decoded = ''.join(chr(int(x, 2)) for x in result).split(" ")
            for word in decoded:
                if word in commonwords:
                    freq += 1
            

            if freq > oldFreq:
                mostLikely = decoded
                oldFreq = freq
                freq = 0
        
        
        for x in mostLikely:
            backToString += x + " "
        backToString.strip()

        textbox_plain.configure(state="normal")
        textbox_plain.delete("1.0", ctk.END)
        textbox_plain.insert("1.0", backToString)
        textbox_plain.configure(state="disabled")

    textbox_frame = ctk.CTkFrame(root)
    textbox_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    textbox_frame.grid_columnconfigure(0, weight=1, uniform="textcols")
    textbox_frame.grid_columnconfigure(1, weight=1, uniform="textcols")

    # -- cipher processing -- #

    textbox_cipher = ctk.CTkTextbox(textbox_frame, font=("Courier New", 12), activate_scrollbars=False)
    textbox_cipher.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
    textbox_cipher.configure(height=300, width=300)

    label_cipher = ctk.CTkLabel(textbox_frame, text="Ciphertext:", font=ctk.CTkFont(size=16, weight="bold"))
    label_cipher.grid(row=0, column=0, padx=20, pady=(10,0))

    btn_cipher_process = ctk.CTkButton(textbox_frame, text="Convert Hex/Oct/Bin", command=decipher)
    btn_cipher_process.grid(row=2, column=0, pady=10, columnspan=2)

    def on_enter():
        decipher()
        return "break"
    
    def on_shift_enter():
        pass

    if CONFIG.getboolean("SETTINGS", "QUICK_ENTER", fallback=False):
        textbox_cipher.bind("<Return>", lambda event: on_enter())
        textbox_cipher.bind("<Shift-Return>", lambda event: on_shift_enter())

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







