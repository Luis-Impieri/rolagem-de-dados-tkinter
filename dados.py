import tkinter as tk
import random

def rolagem(event):
    D = int(faces.get())
    mod = int(modificador.get())
    vant = vantagem.get()

    if D not in {4, 6, 8, 10, 12, 20, 100}:
        result.set("Número inválido de faces no dado")
    else: 
        resultado = random.randint(1, D) + mod

        if vant == "V":
            resultvant = max(resultado, resultado)
            result.set(str(resultvant))
        elif vant == "D":
            resultdesv = min(resultado, resultado)
            result.set(str(resultdesv))
        elif vant == "N":
            result.set(str(resultado))
        else:
            result.set("Erro na vantagem")

root = tk.Tk()
root.geometry("400x600")  
root.title("Rolagem de dados")  

faces = tk.StringVar()
modificador = tk.StringVar()
vantagem = tk.StringVar()
result = tk.StringVar()


faces_label = tk.Label(root, text="Insira o número de faces do dado:", font="lucida 15")
faces_label.grid(row=0, column=0, columnspan=4)

modificador_label = tk.Label(root, text="Insira o modificador:", font="lucida 15")
modificador_label.grid(row=2, column=0, columnspan=4)

vantagem_label = tk.Label(root, text="Insira a vantagem (V, D, N):", font="lucida 15")
vantagem_label.grid(row=4, column=0, columnspan=4)


faces_bot = tk.Entry(root, textvar=faces, font="lucida 20 bold")
faces_bot.grid(row=1, column=0, columnspan=4)

modificador_bot = tk.Entry(root, textvar=modificador, font="lucida 20 bold")
modificador_bot.grid(row=3, column=0, columnspan=4)

vant_bot = tk.Entry(root, textvar=vantagem, font="lucida 20 bold")
vant_bot.grid(row=5, column=0, columnspan=4)


result_label = tk.Label(root, textvar=result, font="lucida 20 bold")
result_label.grid(row=6, column=0, columnspan=4)


rolar = tk.Button(root, text="Rolar", font='lucida 15 bold')
rolar.bind("<Button-1>", rolagem)
rolar.grid(row=7, column=0, columnspan=4)

root.mainloop()