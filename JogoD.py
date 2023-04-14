import random
from tkinter import *


num = random.randrange(10)


jogo = Tk()
jogo.geometry('300x200')
jogo.title("XBETA")
jogo['bg']='darkblue'

def Processar():
    Resultado = Tk()
    Resultado.geometry('300x200')
    Resultado.title("XBETA")
    Resultado['bg'] = 'darkblue'
    responde = Label(Resultado)
    responde['fg'] = 'white'
    responde['font'] = 'fantasy', '12', 'bold'
    responde['bg'] = 'darkblue'
    reagir = Label(Resultado)
    reagir['font'] = 'fantasy', '50', 'bold'
    reagir['bg'] = 'darkblue'

    Pontos = Label(Resultado)
    Pontos['fg'] = 'white'
    Pontos['font'] = 'fantasy', '12', 'bold'
    Pontos['bg'] = 'darkblue'

    valor = int(random.randrange(2))
    rp = roda.get()
    rp =int(rp)
    pt =0
    if rp == valor:
        responde['text']='Achou'
        reagir['text']='X'
        reagir['fg'] = 'green'
        pt +=10
        Pontos['text']='PONTOS :{}'.format(cont)
    else:
        responde['text'] = ' Não achou '
        reagir['text'] = 'O'
        reagir['fg'] = 'red'
        pt -= 10
        cont = str(pt)
        Pontos['text'] = 'PONTOS :{}'.format(cont)
    responde.pack()
    reagir.pack()
    Pontos.pack()
    Resultado.mainloop()




txt = Label(jogo,pady=12)
txt['text']='ACHE O NUMERO'
txt['fg']='white'
txt['font']='fantasy','12','bold'
txt['bg']='darkblue'

roda = Entry(jogo)
roda['width']=10

roda['fg']='green'
roda['bg']='lightblue'

bt = Button(jogo, command=Processar,pady=12)
bt['text']='Verificar'
bt['fg']='white'
bt['bg']='orange'
bt['width']=12











txt.pack()
roda.pack()
bt.pack()

jogo.mainloop()
