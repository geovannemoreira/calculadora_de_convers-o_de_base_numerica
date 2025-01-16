# bibliotecas importadas
import tkinter
from tkinter import *
from tkinter import ttk

# Cores
cor_0 = "#444466"  # Preta
cor_1 = "#feffff"  # branca / white
cor_2 = "#6f9fbd"  # azul
cor_3 = "#38576b"  # valor
cor_4 = "#403d3d"  # letra
cor_5 = "#e89613"    # laranja

# Janela principal
janela = Tk()
janela.title('')
janela.geometry("400x310")
janela.configure(bg=cor_1)

style = ttk.Style()
style.theme_use('clam')
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=190)

# Dividir a janela em 2 frames

frame_cima = Frame(janela,width=400, height=60, bg=cor_1, pady=0, padx=0)
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela,width=400, height=300, bg=cor_1, pady=12, padx=20)
frame_baixo.grid(row=2, column=0, sticky=NW)

# Configurando frame cima
app_nome = Label(frame_cima, text="Conversor de base númerica", relief=FLAT, anchor='center', font=('System 20'), bg=cor_2, fg=cor_1)
app_nome.place(x=10, y=15)

# Configurando frame baixo
bases = ['Binário', 'Octal', 'Decimal', 'Hexadecimal']

combo = ttk.Combobox(frame_baixo, width=12, justify=CENTER, font=('Ivy 12 bold'))
combo['values'] = (bases)
combo.place(x=35, y=10)

entry_valor = Entry(frame_baixo, width=9, justify='center', font=('',13), highlightthickness=1, relief='solid')
entry_valor.place(x=160, y=10)

# Função para converter
botao_de_converter = Button(frame_baixo, text="CONVERTER", relief=RAISED, overrelief=RIDGE, font=('Ivy 8'), bg=cor_1, fg=cor_4)
botao_de_converter.place(x=247, y=10)

# Resultado
## Binário
label_binario = Label(frame_baixo, text="BINÁRIO", width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg=cor_5, fg=cor_1)
label_binario.place(x=35, y=60)
label_binario = Label(frame_baixo, text="", width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=cor_4)
label_binario.place(x=170, y=60)
## Octal
label_octal = Label(frame_baixo, text="OCTAL", width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg=cor_5, fg=cor_1)
label_octal.place(x=35, y=100)
label_octal = Label(frame_baixo, text="", width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=cor_4)
label_octal.place(x=170, y=100)
## Decimal
label_decimal = Label(frame_baixo, text="DECIMAL", width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg=cor_5, fg=cor_1)
label_decimal.place(x=35, y=140)
label_decimal = Label(frame_baixo, text="", width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=cor_4)
label_decimal.place(x=170, y=140)
## Hexadecimal
label_hexadecimal = Label(frame_baixo, text="HEXADECIMAL", width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg=cor_5, fg=cor_1)
label_hexadecimal.place(x=35, y=180)
label_hexadecimal = Label(frame_baixo, text="", width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=cor_4)
label_hexadecimal.place(x=170, y=180)








janela.mainloop()