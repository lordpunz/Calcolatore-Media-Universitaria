from tkinter import *

Voti = []
Cfu = []

def add():
    try:
        voto = float(entry_voto.get())
        cfu = float(entry_cfu.get())
        if (voto>=18) and (voto<=30):
            Voti.append(voto)
            Cfu.append(cfu)
            entry_voto.delete(0, END)
            entry_cfu.delete(0, END)
        else:
            result_label.config(text="Inserisci un voto da 18 a 30")
    except ValueError:
        result_label.config(text="Inserisci valori numerici validi")

def media_uni():
    try:
        Tot = [v * c for v, c in zip(Voti, Cfu)]
        denom = sum(Cfu)
        num = sum(Tot)
        if denom != 0:
            media = num / denom
            result_label.config(text=f"Media: {media:.2f}")
        else:
            result_label.config(text="La somma dei CFU è zero")
    except ZeroDivisionError:
        result_label.config(text="Errore: divisione per zero")

window = Tk()
#window.geometry("420x420")
window.title("Calcolatore media universitaria")
window.config(background="black")

label = Label(master=window, 
              text="Calcolatore media universitaria", 
              font=("Times New Roman", 20, "italic"), 
              background="black", 
              foreground="white")
label.pack(pady=10)

frame = Frame(window, background="black")
frame.pack(pady=10)

entry_voto_label = Label(frame, text="Voto:", background="black", foreground="white")
entry_voto_label.pack(side=LEFT, padx=5)
entry_voto = Entry(frame)
entry_voto.pack(side=LEFT, padx=5)

entry_cfu_label = Label(frame, text="CFU:", background="black", foreground="white")
entry_cfu_label.pack(side=LEFT, padx=5)
entry_cfu = Entry(frame)
entry_cfu.pack(side=LEFT, padx=5)

button2 = Button(window, text="Aggiungi", command=add)
button2.pack(pady=5)

button1 = Button(window, text="Calcola", command=media_uni)
button1.pack(pady=5)

result_label = Label(window, text="", font=("Times New Roman", 15), background="black", foreground="white")
result_label.pack(pady=10)

window.mainloop()
