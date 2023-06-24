from tkinter import *

janela = Tk()
janela.geometry('350x500')








###########################--FUNÇÕES/funcionalidades--################################

#Armazena a expresão para depois mostrar na tela
expressao = ''
#Mostra a expressão na tela 
toda_expressao = StringVar()


#adiciona na expressão os valores e depois mostra na tela 
def adicionar_expressao(string):
    global expressao
    expressao += string
    #passando os valores para a tela
    toda_expressao.set(expressao)


#Calcula o valor da expressão e mostra na tela 
def calcular():
    try:
        resultado = eval(expressao)
        toda_expressao.set(resultado)
    except:
        toda_expressao.set("ERRO!")


# Limpar valor da tela 
def limpar_tela():
    global expressao
    expressao = ""
    toda_expressao.set("")




###########################--Interface grafica-################################



janela.mainloop()
