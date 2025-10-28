from substitution_de import substitutiondecode, decode
import tkinter as tk
import threading
from tkinter import ttk





def decodethread():
          global labels, entries, mapping
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
                  plaintextwidget.config(foreground="red")
                  text = f"SOMETHING WENT WRONG:\n{e}"

          plaintextwidget.config(state="normal")
          plaintextwidget.delete("1.0", tk.END)
          plaintextwidget.insert(tk.END, text)
          plaintextwidget.config(state="disabled")

          ciphertextwidget.yview_moveto(0.0)
          plaintextwidget.yview_moveto(0.0)

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

          keys = list(mapping.keys())
          for i in range(len(keys)):
                    key = keys[i]
                    value = mapping[key]

                    if value == char and key != labelchar:
                              mapping[key] = ""

          
          mapping[labelchar] = char

          for label in labels:
                              labeltext = label.cget("text") 
                              if labeltext in mapping:
                                        index = labels.index(label)

                                        entries[index].delete(0, tk.END) 
                                        entries[index].insert(0, mapping[labeltext]) 

          plaintextwidget.config(state="normal")
          plaintextwidget.delete("1.0", tk.END)
          plaintextwidget.insert(tk.END, decode(ciphertextwidget.get("1.0", tk.END), mapping))
          plaintextwidget.config(state="disabled")

          ciphertextwidget.yview_moveto(0.0)
          plaintextwidget.yview_moveto(0.0)



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

decodebutton = tk.Button(root, text="Partially decode substitution", command=decodecontents)
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



root.mainloop()
