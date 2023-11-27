from tkinter import *


# Calculadora
def calculadora(calculos):
    try:
        n1 = float(entry_n1.get())
        n2 = float(entry_n2.get())
        resultado = 0

        if calculos == "+":
            resultado = n1 + n2
        elif calculos == "-":
            resultado = n1 - n2
        elif calculos == "*":
            resultado = n1 * n2
        elif calculos == "/":
            resultado = n1 / n2

        lbl_resultado.config(text=f"{n1} {calculos} {n2} = {resultado}")
    except ValueError:
        lbl_resultado.config(text="Por favor, insira números válidos.")

# Criação da Janela


window = Tk()
window.title("Calculadora")

# Entrada dos numeros
entry_n1 = Entry(window, width=20)
entry_n1.grid(row=0, column=0, padx=10, pady=10)

entry_n2 = Entry(window, width=20)
entry_n2.grid(row=0, column=1, padx=10, pady=10)

# Label para exibir o resulatado
lbl_resultado = Label(window, text="Resultado")
lbl_resultado.grid(row=1, column=0, columnspan=2)

# Botões para as operações
button_soma = Button(window, text="+", command=lambda: calculadora('+'))
button_soma.grid(row=2, column=0, padx=5, pady=0)

button_subtracao = Button(window, text="- ", command=lambda: calculadora('-'))
button_subtracao.grid(row=2, column=1, padx=5, pady=5)

button_multiplicacao = Button(window, text="* ", command=lambda: calculadora('*'))
button_multiplicacao.grid(row=3, column=0, padx=5, pady=5)

button_divisao = Button(window, text="/", command=lambda: calculadora('/'))
button_divisao.grid(row=3, column=1, padx=5, pady=5)
window.mainloop()
