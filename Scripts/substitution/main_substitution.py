import os
import threading
import string
import customtkinter as ctk
import tkinter as tk
from substitution_de import decode, substitutiondecode


def main():
    # Initialize globals
    global labels, entries, mapping
    labels = []
    entries = []
    mapping = {letter: "" for letter in string.ascii_uppercase}
    rootdir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

    # -------------------- Functions --------------------

    def decodethread():
        """Run substitutiondecode in background thread."""
        global mapping

        try:
            plaintextwidget.configure(state="normal")

            ciphertext = ciphertextwidget.get("1.0", ctk.END).upper().strip()
            text, mapping = substitutiondecode(ciphertext)

            # Update entry boxes with mapping
            for label, entry in zip(labels, entries):
                char = mapping.get(label.cget("text"), "")
                entry.delete(0, ctk.END)
                entry.insert(0, char)

        except Exception:
            # fallback to default decode if substitutiondecode fails
            emptymapping = {letter: "" for letter in string.ascii_uppercase}
            text = decode(ciphertextwidget.get("1.0", ctk.END), emptymapping)
            for label, entry in zip(labels, entries):
                entry.delete(0, ctk.END)
                entry.insert(0, "")

        plaintextwidget.delete("1.0", ctk.END)
        plaintextwidget.insert(ctk.END, text)
        plaintextwidget.configure(state="disabled")

        ciphertextwidget.yview_moveto(0.0)
        plaintextwidget.yview_moveto(0.0)

    def decodecontents():
        """Start decoding in thread."""
        threading.Thread(target=decodethread, daemon=True).start()
        text = ciphertextwidget.get("1.0", ctk.END).strip()
        ciphertextwidget.delete("1.0", ctk.END)
        ciphertextwidget.insert(ctk.END, text)
        return "break"

    # Scroll both textboxes when scrollbar moves
    def sync_scroll(*args):
        ciphertextwidget.yview(*args)
        plaintextwidget.yview(*args)


    def mousewheel(event):
        """Scroll both boxes together."""
        delta = int(-1 * (event.delta / 120))
        ciphertextwidget.yview_scroll(delta, "units")
        plaintextwidget.yview_scroll(delta, "units")
        return "break"

    def highlight(event):
        """Highlight selected text in both textboxes."""
        original = event.widget
        try:
            first = original.index("sel.first")
            last = original.index("sel.last")
        except tk.TclError:
            for w in [ciphertextwidget, plaintextwidget]:
                w.tag_remove("sel_txt", "1.0", ctk.END)
            return

        for w in [ciphertextwidget, plaintextwidget]:
            w.tag_remove("sel_txt", "1.0", ctk.END)
            w.tag_add("sel_txt", first, last)
            w.tag_config("sel_txt", background="#007ACC", foreground="white")

    def clear(_):
        """Remove selection highlight."""
        for w in [ciphertextwidget, plaintextwidget]:
            w.tag_remove("sel_txt", "1.0", ctk.END)
            w.tag_remove("sel", "1.0", ctk.END)

    def updateplaintext(index):
        """Update plaintext dynamically when mapping entry changes."""
        global mapping

        entry = entries[index]  # now 'index' comes from lambda
        text = entry.get().strip()
        char = text[0].upper() if text and text[0].isalpha() else ""

        entry.delete(0, "end")
        entry.insert(0, char)

        labelchar = labels[index].cget("text")

        # Prevent duplicate mappings
        for key in mapping:
            if mapping[key] == char and key != labelchar:
                mapping[key] = ""
        mapping[labelchar] = char

        # Refresh all entries
        for lbl, ent in zip(labels, entries):
            ent.delete(0, "end")
            ent.insert(0, mapping.get(lbl.cget("text"), ""))

        # Update plaintext box
        plaintextwidget.configure(state="normal")
        plaintextwidget.delete("1.0", ctk.END)
        plaintextwidget.insert(ctk.END, decode(ciphertextwidget.get("1.0", ctk.END), mapping))
        plaintextwidget.configure(state="disabled")

        # Reset scroll
        ciphertextwidget.yview_moveto(0.0)
        plaintextwidget.yview_moveto(0.0)

    # -------------------- UI --------------------

    ctk.set_appearance_mode("dark")   # or "light"
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Substitution Cipher Decoder")
    try:
        root.iconbitmap(os.path.join(rootdir, "res", "favicon.ico"))
    except Exception:
        pass
    root.resizable(False, False)

    textframe = ctk.CTkFrame(root)
    textframe.pack(padx=10, pady=10)

    # Ciphertext
    ctk.CTkLabel(textframe, text="Ciphertext").grid(row=0, column=0, pady=5)
    ciphertextframe = ctk.CTkFrame(textframe)
    ciphertextframe.grid(row=1, column=0, padx=(10, 7))
    ciphertextwidget = ctk.CTkTextbox(ciphertextframe, width=500, height=250, wrap="word", font=("Courier New", 12), activate_scrollbars=False)
    ciphertextwidget.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)

    # Plaintext
    ctk.CTkLabel(textframe, text="Plaintext").grid(row=0, column=1, pady=5)
    plaintextframe = ctk.CTkFrame(textframe)
    plaintextframe.grid(row=1, column=1, padx=(7, 10))
    plaintextwidget = ctk.CTkTextbox(plaintextframe, width=500, height=250, wrap="word", state="disabled", font=("Courier New", 12), activate_scrollbars=False)
    plaintextwidget.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)

    # Shared scrollbar
    plaintextscroll = ctk.CTkScrollbar(plaintextframe, command=sync_scroll)
    plaintextscroll.pack(side=ctk.RIGHT, fill=ctk.Y)
    plaintextwidget.configure(yscrollcommand=lambda f, l: plaintextscroll.set(float(f), float(l)))
    ciphertextwidget.configure(yscrollcommand=lambda f, l: plaintextscroll.set(float(f), float(l)))
    plaintextscroll.configure(command=sync_scroll)

    # Bindings
    root.bind("<Button-1>", clear)
    ciphertextwidget.bind("<MouseWheel>", mousewheel)
    plaintextwidget.bind("<MouseWheel>", mousewheel)
    ciphertextwidget.bind("<<Selection>>", highlight)
    plaintextwidget.bind("<<Selection>>", highlight)

    # Decode button
    decodebutton = ctk.CTkButton(root, text="Partially Decode Substitution", command=decodecontents)
    decodebutton.pack(pady=(5, 5))

    # Mapping section
    ctk.CTkLabel(root, text="Character Mapping").pack(pady=(5, 0))
    gridframe = ctk.CTkFrame(root)
    gridframe.pack(pady=10)

    for i, letter in enumerate(string.ascii_uppercase):
        label = ctk.CTkLabel(gridframe, text=letter, width=40)
        label.grid(row=1, column=i, padx=1)
        labels.append(label)

        entry = ctk.CTkEntry(gridframe, width=40, justify="center")
        entry.grid(row=0, column=i, padx=1, pady=(0, 3))
        entry.bind("<KeyRelease>", lambda e, idx=i: updateplaintext(idx))
        entries.append(entry)

    root.mainloop()


if __name__ == "__main__":
    main()
