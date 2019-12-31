from Verbo import Verbo
from functools import partial
import tkinter as tk
import tkinter.ttk as ttk

def btnppoa(x):
    print(actlist)
    if actlist[x] == 1:
        if actlist.count(0) == 1:
            (btnlist[actlist.index(0)])['relief'] = tk.RAISED
            actlist[actlist.index(0)] = 1
        (btnlist[x])["relief"] = tk.SUNKEN
        actlist[x] = 0
    else:
        (btnlist[x])["relief"] = tk.RAISED
        actlist[x] = 1

def cboxmodocheck(eventObject):
    if str(cboxmodo.get()).lower() == "indicativo":
        cboxnome["values"] = ["Presente", "Pretérito Mais-que-perfeito", "Pretérito Perfeito", "Pretérito Imperfeito",
                              "Futuro do Presente", "Futuro do Pretérito", "Pretérito Mais-que-perfeito composto",
                              "Pretérito Perfeito Composto", "Futuro do Presente Composto", "Futuro do Pretérito composto"]
        cboxppd["values"] = ["Eu", "Tu", "Ele", "Nós", "Vós", "Eles"]
    elif str(cboxmodo.get()).lower() == "subjuntivo":
        cboxnome["values"] = ["Presente", "Pretérito Imperfeito", "Futuro", "Pretérito Mais-que-perfeito Composto",
                              "Pretérito Perfeito Composto", "Futuro Composto"]
        cboxppd["values"] = ["Eu", "Tu", "Ele", "Nós", "Vós", "Eles"]
    elif str(cboxmodo.get()).lower() == "imperativo":
        cboxnome["values"] = ["Positivo", "Negativo"]
        cboxppd["values"] = ["Tu", "Ele", "Nós", "Vós", "Eles"]
    elif str(cboxmodo.get()).lower() == "particípio":
        cboxnome["values"] = ["--"]
        cboxppd["values"] = ["Ele", "Ela", "Eles", "Elas"]
    elif str(cboxmodo.get()).lower() == "gerúndio":
        cboxnome["values"] = ["Simples", "Composto"]
        cboxppd["values"] = ["--"]
    else:
        cboxnome["values"] = ["Impessoal", "Pessoal"]
        if str(cboxnome.get()).lower() == "pessoal":
            cboxppd["values"] = ["Eu", "Tu", "Ele", "Nós", "Vós", "Eles"]
        else:
            cboxppd["values"] = ["--"]
    cboxnome.current(0)
    cboxppd.current(0)
def cboxnomecheck(eventObject):
    if str(cboxmodo.get()).lower() == "infinitivo":
        if str(cboxnome.get()).lower() == "impessoal":
            cboxppd["values"] = ["--"]
        else:
            cboxppd["values"] = ["Eu", "Tu", "Ele", "Nós", "Vós", "Eles"]
        cboxppd.current(0)
def cboxcheck():
    cboxnomestr = ""
    for c in range(0, len(cboxnome.get())):
        x = str(cboxnome.get()[c]).lower()
        if x == " ":
            cboxnomestr = cboxnomestr + "-"
        else:
            cboxnomestr = cboxnomestr + x
    print(cboxnomestr)
    #try:
    if str(cboxmodo.get()).lower() == "gerúndio":
        txtaft["text"] = Verbo(str(everbo.get()).lower()).conjugar("gerúndio", str(cboxnome.get()).lower(), 0)
    elif str(cboxmodo.get()).lower() == "particípio:":
        txtaft["text"] = Verbo(str(everbo.get()).lower())
    elif 0 in actlist and not str(cboxcp.get()).lower() == "nenhuma":
            txtaft["text"] = Verbo(str(everbo.get()).lower()).posppoa([str(cboxmodo.get()).lower(), cboxnomestr,
                                                                    ppdlist.index(str(cboxppd.get()).lower())], str(btnlist[actlist.index(0)]["text"]).lower(), str(cboxcp.get()).lower())
    else:
        if str(cboxmodo.get()).lower() == "particípio":
            ["ele", "ela", "eles", "elas"].index(str(cboxppd.get()).lower())
            txtaft["text"] = Verbo(str(everbo.get()).lower()).conjugar(str(cboxmodo.get()).lower(), cboxnomestr,
                                                                       ["ele", "ela", "eles", "elas"].index(str(cboxppd.get()).lower()))
        else:
            txtaft["text"] = Verbo(str(everbo.get()).lower()).conjugar(str(cboxmodo.get()).lower(), cboxnomestr,
                                                                    ppdlist.index(str(cboxppd.get()).lower()))
    # except:
    #     txtaft["text"] = "Uma(s) Opção(ões) não é(são) válida(s)"
    txtaft["text"] = str(txtaft["text"][0]).capitalize() + str(txtaft["text"][1:])

def everbolim(*args):
    if len(everbo.get()) >= 24:
        everbolimsv.set(everbo.get()[:-1])

sizebtppoa = int(113/7)
colorbt = "lightgray"
xbtplace = int(114)
ybtplace = int(378)
ybtplacedif = 400 - ybtplace
arccolor = "saddlebrown"
ppdlist = ["eu", "tu", "ele", "nós", "vós", "eles", "--"]
eleas = ["ele", "ela", "eles", "elas", "--"]

root = tk.Tk()

root.title('Conjugador Verbal')
root.geometry("800x400")
root.resizable(False, False)

txtlist = ['me', 'te', 'o', 'a', 'se', 'lhe', 'nos', 'vos', 'os', 'as', 'lhes', 'mo', 'ma', 'mos', 'mas',
                  'to', 'ta', 'tos', 'tas', 'lho', 'lha', 'lhos', 'lhas', 'no-lo', 'no-la', 'no-los', 'no-las', 'vo-lo',
                  'vo-la', 'vo-los', 'vo-las', 'lhe-lo', 'lhe-la', 'lhe-los', 'lhe-las']
btnlist = []
actlist = []

# Widgets
for c in range(0, 35):
    if c > 9:
        btnlist.append(tk.Button(root, width=sizebtppoa, text=txtlist[c], highlightthickness=0, bd=1, bg=colorbt,
                               activebackground=colorbt, foreground=arccolor, activeforeground=arccolor))
    else:
        btnlist.append(tk.Button(root, width=sizebtppoa, text=txtlist[c], highlightthickness=0, bd=1, bg=colorbt,
                                 activebackground=colorbt, fg="black"))
    btnlist[c].place(x=(xbtplace*(c%7)), y=ybtplace-(ybtplacedif*(4-int(c/7))))
    (btnlist[c])['command'] = partial(btnppoa, c)
    actlist.append(1)

cboxmodo = ttk.Combobox(root)
cboxmodo["values"] = ["Indicativo", "Subjuntivo", "Imperativo", "Gerúndio", "Infinitivo", "Particípio"]
cboxmodo.bind("<<ComboboxSelected>>", cboxmodocheck)
cboxmodo["width"] = 10
cboxmodo.current(0)
cboxmodo["state"] = "readonly"
cboxmodo.place(x=710, y=150)

cboxnome = ttk.Combobox(root)
cboxnome["width"] = 35
cboxnome["values"] = ["Presente", "Pretérito Mais-que-perfeito", "Pretérito Perfeito", "Pretérito Imperfeito",
                              "Futuro do Presente", "Futuro do Pretérito", "Pretérito Mais-que-perfeito composto",
                              "Pretérito Perfeito Composto", "Futuro do Presente Composto", "Futuro do Pretérito composto"]
cboxnome.bind("<<ComboboxSelected>>", cboxnomecheck)
cboxnome.current(0)
cboxnome["state"] = "readonly"
cboxnome.place(x=560, y=200)

everbo = tk.Entry(root, bd=2, width=30)
everbolimsv = tk.StringVar()
everbolimsv.trace("w", everbolim)
everbo["textvariable"] = everbolimsv
everbo.place(x=0, y=0)

cboxppd = ttk.Combobox(root) # ppd = Pronome Pessoal Direto
cboxppd["values"] = ["Eu", "Tu", "Ele", "Nós", "Vós", "Eles"]
cboxppd["width"] = 5
cboxppd.bind("<<ComboboxSelected>>")
cboxppd.current(0)
cboxppd["state"] = "readonly"
cboxppd.place(x=740, y=250)

cboxcp = ttk.Combobox(root, width=7) # cp = Colocação Pronominal
cboxcp["values"] = ["Próclise", "Ênclise", "Mesóclise", "Nenhuma"]
cboxcp.current(3)
cboxcp["state"] = "readonly"
cboxcp.place(x=0, y=260)

btnverbo = tk.Button(root, text="Conjugar", command=cboxcheck)
btnverbo.place(x=0, y=20)

txtaft = tk.Label(root, text="Verbo conjugado", font=("Times New Roman", 18))
txtaft.place(y=150)

root.mainloop()
