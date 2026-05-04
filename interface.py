import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from organizador import organizar, simular_organizar

janela = tk.Tk()
janela.title("Organizador de Arquivos")
janela.geometry("600x400")

pasta_selecionada = tk.StringVar()

def escolher_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        pasta_selecionada.set(pasta)
        area_log.delete("1.0", "end")
        area_log.insert("end", f"Pasta selecionada: {pasta}\n")

def ao_simular():
    texto, contagem = simular_organizar(pasta_selecionada.get())
    area_log.delete("1.0", "end")
    area_log.insert("end", texto)
    btn_organizar.config(state="normal")

def ao_organizar():
    reposta = messagebox.askyesno("Confirmar", "Deseja organizar os arquivos?")
    if reposta:
        organizar(pasta_selecionada.get())
        area_log.insert("end", "\nOrganização concluída.")

btn_simular = tk.Button(janela, text="Simular", width=20, command=ao_simular)
btn_simular.pack(pady=10)

btn_escolher = tk.Button(janela, text="Escolher Pasta", width=20, command=escolher_pasta)
btn_escolher.pack(pady=5)

btn_organizar = tk.Button(janela, text="Organizar", width=20, command=ao_organizar, state="disabled")
btn_organizar.pack(pady=5)

frame_log = tk.Frame(janela)
frame_log.pack(pady=10)

scrollbar = tk.Scrollbar(frame_log)
scrollbar.pack(side="right", fill="y")

area_log = tk.Text(frame_log, height=15, width=70, yscrollcommand=scrollbar.set)
area_log.pack(side="left")

scrollbar.config(command=area_log.yview)   

rodape = tk.Label(janela, text="Desenvolvido por Allan Lopes - versão 1.0.0", fg="gray", font=("Arial", 8))
rodape.pack(side="bottom", pady=5)

janela.mainloop()