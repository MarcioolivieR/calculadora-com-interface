import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Funções
def soma(a, b): return a + b
def subtracao(a, b): return a - b
def multiplicacao(a, b): return a * b
def divisao(a, b): return "Erro: divisão por zero!" if b == 0 else a / b
def potencia(a, b): return a ** b
def raiz_quadrada(a): return "Erro: número negativo!" if a < 0 else a ** 0.5
def fatorial(n):
    if n < 0: return "Erro: número negativo!"
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
def media(*args): return sum(args) / len(args) if args else "Erro: sem números"
def maior(*args): return max(args) if args else "Erro: sem números"
def menor(*args): return min(args) if args else "Erro: sem números"

# Janela principal
root = tk.Tk()
root.title("Calculadora Avançada")
root.geometry("400x450")

# Widgets 
label_op = ttk.Label(root, text="Escolha a operação:")
label_op.pack(pady=5)

operacoes = [
    "Soma", "Subtração", "Multiplicação", "Divisão",
    "Potência", "Raiz Quadrada", "Fatorial",
    "Média", "Maior", "Menor"
]
combo_op = ttk.Combobox(root, values=operacoes, state="readonly")
combo_op.pack(pady=5)

label_num1 = ttk.Label(root, text="Número 1:")
label_num1.pack()
entry_num1 = ttk.Entry(root)
entry_num1.pack()

label_num2 = ttk.Label(root, text="Número 2 (ou mais, separados por espaço):")
label_num2.pack()
entry_num2 = ttk.Entry(root)
entry_num2.pack()

resultado_label = ttk.Label(root, text="Resultado aparecerá aqui", font=("Arial", 12))
resultado_label.pack(pady=15)

# Função principal 
def calcular():
    op = combo_op.get()
    try:
        a = float(entry_num1.get())
    except ValueError:
        messagebox.showerror("Erro", "Número 1 inválido")
        return

    b_input = entry_num2.get().strip()

    try:
        if op in {"Soma", "Subtração", "Multiplicação", "Divisão", "Potência"}:
            b = float(b_input)
            r = {
                "Soma": soma(a, b),
                "Subtração": subtracao(a, b),
                "Multiplicação": multiplicacao(a, b),
                "Divisão": divisao(a, b),
                "Potência": potencia(a, b)
            }[op]

        elif op == "Raiz Quadrada":
            r = raiz_quadrada(a)

        elif op == "Fatorial":
            r = fatorial(int(a))

        elif op in {"Média", "Maior", "Menor"}:
            lista = [float(x) for x in (str(a) + " " + b_input).split()]
            r = {
                "Média": media(*lista),
                "Maior": maior(*lista),
                "Menor": menor(*lista)
            }[op]

        else:
            r = "Operação inválida"

        resultado_label.config(text=f"Resultado: {r}")

    except Exception as e:
        resultado_label.config(text=f"Erro: {e}")

# Botão
btn = ttk.Button(root, text="Calcular", command=calcular)
btn.pack(pady=10)

# Iniciar GUI
root.mainloop()
