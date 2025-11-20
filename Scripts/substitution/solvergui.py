from substitution_de import substitutiondecode, decode
from frequency_analyser import analyse_freq
import tkinter as tk
import threading, string
from tkinter import ttk

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import re, time






def decodethread():
    global labels, entries, mapping, canvas, chartframe

    
    try:
        plaintextwidget.config(foreground="black")
        text = substitutiondecode(ciphertextwidget.get("1.0", tk.END).upper().strip())[0]

        mapping = substitutiondecode(ciphertextwidget.get("1.0", tk.END).upper().strip())[1]

        for label in labels:
                    labeltext = label.cget("text") 
                    if labeltext in mapping:
                            index = labels.index(label)

                            entries[index].delete(0, tk.END) 
                            entries[index].insert(0, mapping[labeltext]) 


    except Exception as e:
            print(e)
            emptymapping = {letter: "" for letter in string.ascii_uppercase}
            text = decode(ciphertextwidget.get("1.0", tk.END), emptymapping)

            for label in labels:
                        labeltext = label.cget("text") 
                        if labeltext in emptymapping:
                                    index = labels.index(label)

                                    entries[index].delete(0, tk.END) 
                                    entries[index].insert(0, emptymapping[labeltext]) 

    plaintextwidget.config(state="normal")
    plaintextwidget.delete("1.0", tk.END)
    plaintextwidget.insert(tk.END, text)
    plaintextwidget.config(state="disabled")

    ciphertextwidget.yview_moveto(0.0)
    plaintextwidget.yview_moveto(0.0)

    actuallymakegraph(ciphertextwidget.get("1.0", tk.END).upper().strip())

    decodebutton["state"] = "disabled"
    time.sleep(0.1)
    decodebutton["state"] = "normal"

def decodecontents():
        threading.Thread(target=decodethread).start()

        text = ciphertextwidget.get("1.0", tk.END).strip()
        ciphertextwidget.delete("1.0", tk.END)
        ciphertextwidget.insert(tk.END, text)

        return "break"

def scroll(*args):
        try:
                ciphertextwidget.yview(*args)
                plaintextwidget.yview(*args)
                plaintextscroll.set(*args)
        except:
                pass

def mousewheel(event):
        delta = int(-1*(event.delta/120))
        ciphertextwidget.yview_scroll(delta, "units")
        plaintextwidget.yview_scroll(delta, "units")
        return "break"

def highlight(event):
        originalselectionwidget = event.widget
        try:
                first = originalselectionwidget.index("sel.first")
                last = originalselectionwidget.index("sel.last")

        except tk.TclError:
                for widget in [ciphertextwidget, plaintextwidget]:
                    widget.tag_remove("sel_txt", "1.0", tk.END)
                return

        for widget in [ciphertextwidget, plaintextwidget]:
                widget.tag_remove("sel_txt", "1.0", tk.END)
                widget.tag_add("sel_txt", first, last)
                widget.tag_config("sel_txt", background=widget.cget("selectbackground"), foreground="white")

def clear(_):
        for widget in [ciphertextwidget, plaintextwidget]:
                widget.tag_remove("sel_txt", "1.0", tk.END)
                widget.tag_remove("sel", "1.0", tk.END)



def updateplaintext(event):
    global entries, labels, mapping

    entry = event.widget
    char = entry.get().strip()
    
    if char.isalpha():
        char = char[0].upper()
    else:
        char = "" 

    entry.delete(0, tk.END)
    entry.insert(0, char)

    index = entries.index(entry)
    labelchar = labels[index]["text"]
    try:
        keys = list(mapping.keys())
    except:
        mapping = {}
        for i in range(26):
            letter = chr(ord("A") + i)
            mapping[letter] = ""

    for key in keys:
        if mapping[key] == char and key != labelchar:
            mapping[key] = ""

    mapping[labelchar] = char

    plaintextwidget.config(state="normal")
    plaintextwidget.delete("1.0", tk.END)
    plaintextwidget.insert(tk.END, decode(ciphertextwidget.get("1.0", tk.END), mapping))
    plaintextwidget.config(state="disabled")

    ciphertextwidget.yview_moveto(0.0)
    plaintextwidget.yview_moveto(0.0)

    actuallymakegraph(ciphertextwidget.get("1.0", tk.END).upper().strip())




def plotfreq(dictionary=None, mode="text"):
    try:
        if mode == "english":
            dictionary = {
                'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75,
                'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78,
                'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
                'P': 1.93, 'B': 1.49, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15,
                'Q': 0.10, 'Z': 0.07
            }

            letters = list(dictionary.keys())
            frequencies = np.array(list(dictionary.values()))
            y_label = "Frequency (%)"
            y_limit = 14
        else:
            letters = list(dictionary.keys()) if dictionary else []
            if letters:
                frequencies = np.array([dictionary[l]["freq"] for l in letters])
            else:
                letters = [""]
                frequencies = np.array([0])
            y_label = "Frequency"
            y_limit = max(frequencies.max(), 1)

        norm = plt.Normalize(frequencies.min(), frequencies.max() if frequencies.max() != 0 else 1)
        colors = plt.cm.RdYlGn_r(norm(frequencies))

        fig = Figure(figsize=(6, 3))
        ax = fig.add_subplot(111)
        bars = ax.bar(letters, frequencies, color=colors)

        ax.set_xlabel("Letters")
        ax.set_ylabel(y_label)
        ax.set_ylim(0, y_limit)
        fig.tight_layout()

        sm = plt.cm.ScalarMappable(cmap="RdYlGn_r", norm=norm)
        sm.set_array([])
        fig.colorbar(sm, ax=ax, label="Frequency Level")

        return fig

    except Exception as e:
        print("plotfreq error:", e)


root = tk.Tk()
root.title("Substitution cipher decoding tool")
root.resizable(False, False)


textframe = tk.Frame(root)
textframe.pack(padx=10, pady=10)

ciphertexttitle = tk.Label(textframe, text="Ciphertext")
ciphertexttitle.grid(row=0, column=0, pady=5)

ciphertextframe = tk.Frame(textframe)
ciphertextframe.grid(row=1, column=0, padx=(10, 7))

ciphertextwidget = tk.Text(ciphertextframe, width=59, height=15, wrap="word")
ciphertextwidget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

root.bind("<Button-1>", clear)


plaintexttitle = tk.Label(textframe, text="Plaintext")
plaintexttitle.grid(row=0, column=1, pady=5)
plaintextframe = tk.Frame(textframe)
plaintextframe.grid(row=1, column=1, padx=(7, 10))

plaintextwidget = tk.Text(plaintextframe, width=59, height=15, state='disabled', wrap="word")
plaintextwidget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

plaintextscroll = tk.Scrollbar(plaintextframe, command=scroll)
plaintextscroll.pack(side=tk.RIGHT, fill=tk.Y)
plaintextwidget.config(yscrollcommand=plaintextscroll.set)
ciphertextwidget.config(yscrollcommand=plaintextscroll.set)


for widget in [ciphertextwidget, plaintextwidget]:
        widget.bind("<<Selection>>", highlight)


ciphertextwidget.bind("<MouseWheel>", mousewheel)
plaintextwidget.bind("<MouseWheel>", mousewheel)




mappingtitle = tk.Label(root, text="Character Mapping")
mappingtitle.pack(pady=(10, 0))

decodebutton = tk.Button(root, text="Autofill Plaintext", command=decodecontents, disabledforeground="black")
decodebutton.place(x=20, y=285)

gridframe = tk.Frame(root)
gridframe.pack(pady=10)

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
entries = []
labels = []

for i in range(len(letters)):
    letter = letters[i]

    label = tk.Label(gridframe, text=letter, width=4, height=2, font=("TkDefaultFont ", 10))
    label.grid(row=1, column=i)
    labels.append(label)

    entry = tk.Entry(gridframe, width=4, justify="center", font=("TkDefaultFont ", 10))
    entry.grid(row=0, column=i, pady=1, ipady=5)
    entry.bind("<KeyRelease>", updateplaintext)
    entries.append(entry)

chartframe = None 
canvas = None
current_mode = "text" 


def cyclethread():
    global current_mode

    if current_mode == "text":
        current_mode = "english"
        actuallymakegraph("ENGLISHFREQ")
    else:
        current_mode = "text"
        text = ciphertextwidget.get("1.0", tk.END).upper().strip()
        actuallymakegraph(text)
    
    backward["state"] = "disabled"
    forward["state"] = "disabled"
    time.sleep(0.1)
    backward["state"] = "normal"
    forward["state"] = "normal"

def cycle():
    threading.Thread(target=cyclethread).start()


def actuallymakegraph(text):
    global canvas, chartframe, graphtitle

    text = re.sub(r"[^A-Z]", "", text)

    if text == "ENGLISHFREQ":
        fig = plotfreq(mode="english")
        titletext = "English Letter Frequency"
    else:
        result = analyse_freq(text)
        fig = plotfreq(result, mode="text")
        titletext = "Ciphertext Frequency Analysis"

    if canvas:
        canvas.get_tk_widget().destroy()
    else:
        graphframe = tk.Frame(root)
        graphframe.pack(anchor="w")

        if 'graphtitle' not in globals() or graphtitle is None:
            graphtitle = tk.Label(graphframe)
            graphtitle.grid(row=0, column=0, pady=(0, 10))

        chartframe = tk.Frame(graphframe, bd=1, relief="sunken", background="white")
        chartframe.grid(row=1, column=0, sticky="w", padx=(20, 20), pady=(0, 20))

        forward.place(x=597 - 180, y=414)
        forward.lift()

        backward.place(x=20 + 180, y=414)
        backward.lift()

    graphtitle.config(text=titletext)

    newcanvas = FigureCanvasTkAgg(fig, master=chartframe)
    newcanvas.draw()
    newcanvas.get_tk_widget().pack()
    canvas = newcanvas


forward = tk.Button(root, text=">", width=2, command=cycle, disabledforeground="black")
backward = tk.Button(root, text="<", width=2, command=cycle, disabledforeground="black")

actuallymakegraph("")


root.mainloop()
