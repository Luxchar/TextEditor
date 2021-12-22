from tkinter import *
from tkinter import font
from tkinter import filedialog

fen= Tk()
fen.title('Nouveau Fichier - Editeur de Texte') # on modifie le titre de la fenêtre
fen.geometry("1200x800") # on modifie la taille de la fenêtre
"""
#creer selectionner pour que la variable existe et que ça ne plante pas
global selectionner
selectionner = False"""

def nouveau_fichier():
    text.delete('1.0',END)
    fen.title('Nouveau Fichier - Editeur de Texte')
    statut.config(text='Nouveau Fichier       ')

def ouvrir_fichier():
    text.delete('1.0',END)
    fichier_texte = filedialog.askopenfilename(initialdir='C:', title='ouvrir fichier',filetypes = (("Text Files","*.txt"),('HTML Files','*.html'),('Python Files','*.py'),('All Files', '*.*')))

    fichier_texte=open(fichier_texte,'r')
    a = fichier_texte.read()
    #ajouter le fichier a l'éditeur
    Text.insert(END, a)
    #fermer le fichier
    fichier_texte.close()

def sauvegarder():
    s=(text.get(1.0,END))
    with open("fichier.txt",'w') as f:
        f.write(str(s))
        f.close()
"""
def copier(e):
    global selectionner
    if Text.selection_get():
        #recupérer le texte sélectionné
        selectionner = Text.selection_get()

def couper(e):
    global selectionner
    if Text.selection_get():
        #recupérer le texte sélectionné
        selectionner = Text.selection_get()
        #supprimer le texte sélectionné
        Text.delete('sel.first','sel.last') 

def coller(e):
    if Text.selection_get():
        position = Text.index(INSERT)
        Text.insert(position, selectionner)
"""
"""
#pas fait
def sauvegarder_comme():
    global text
    global inputtext

    fen2 = Tk()
    fen2.title("Nom du fichier")
    fen2.geometry('400x200')

    # création de la textbox
    inputtext = Text(fen2,height = 5,width = 50)
    inputtext.pack()
    
    # création du bouton
    printButton = Button(fen2,text = "Confirmer", command = sauvegarder_comme)
    printButton.pack()

    s=(text.get(1.0,END))
    f = open(str(inputtext),'w')
    f.write(str(s))
    f.close()
"""

def sauvegarder_comme():
    fichier_texte = filedialog.asksaveasfilename(initialdir='C:', title='sauvegarder fichier',filetypes = (("Text Files","*.txt"),('HTML Files','*.html'),('Python Files','*.py'),('All Files', '*.*')))
    if fichier_texte:
        nom = fichier_texte
        nom = nom.replace("C:","")
        fen.title(f'{nom} - Editeur de Texte')

#fond de la fen
screen = Frame(fen)
screen.pack(pady=5)

#scrollbar
text_scroll = Scrollbar(screen)
text_scroll.pack(side=RIGHT, fill = Y)

#champ pr écrire
text = Text(screen, width = 250, height = 40, font=('Arial',13),selectbackground = 'black', selectforeground='white', undo=True, yscrollcommand= text_scroll.set)
text.pack()

#pour que la scrollbar marche
text_scroll.config(command=text.yview)

#petit menu
menu = Menu(fen)
fen.config(menu=menu)

#'fichier'
menu_fichier = Menu(menu, tearoff=False)
menu.add_cascade(label="Fichier", menu=menu_fichier)
menu_fichier.add_command(label='Nouveau', command=nouveau_fichier)
menu_fichier.add_command(label='Ouvrir', command=ouvrir_fichier)
menu_fichier.add_command(label='Sauvegarder', command=sauvegarder)
menu_fichier.add_command(label='Sauvegarder comme', command=sauvegarder_comme)
menu_fichier.add_separator()
menu_fichier.add_command(label='Quitter', command=fen.quit)

"""
#'editer'
menu_editer = Menu(menu, tearoff=False)
menu.add_cascade(label="Editer", menu=menu_editer)
menu_editer.add_command(label='Copier',command=lambda: copier(False))
menu_editer.add_command(label='Couper', command=lambda: couper(False))
menu_editer.add_command(label='Coller', command=lambda: coller(False))
menu_editer.add_command(label='Après')
"""

#bar de stat en bas
statut = Label(fen, text='Pret        ', anchor=E)
statut.pack(fill=X, side=BOTTOM, ipady=5)

fen.mainloop()