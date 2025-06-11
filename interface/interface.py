import tkinter as tk
from tkinter import ttk, messagebox
from banco.crud_pessoa import inserir_pessoa, listar_pessoas, deletar_pessoa, alterar_pessoa
from banco.crud_animal import inserir_animal, listar_animais, alterar_animal, deletar_animal
from banco.crud_vacina import inserir_vacina, listar_vacinas, alterar_vacina, deletar_vacina
from moldes.Pessoa import Pessoa
from moldes.Animal import Animal
from moldes.Vacina import Vacina

def iniciar_interface():
    root = tk.Tk()
    root.title("CARTEIRA DE VACINACAO ANIMAL")
    root.geometry("800x200")

    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # aba de pessoa
    aba_pessoa = tk.Frame(notebook)
    notebook.add(aba_pessoa, text="Pessoa")
    aba_pessoa.columnconfigure(0, weight=1)
    aba_pessoa.columnconfigure(1, weight=1)

    form_frame = tk.Frame(aba_pessoa, padx=10, pady=10)
    form_frame.grid(row=0, column=0, sticky="nsew")

    tk.Label(form_frame, text="Nome:").grid(row=0, column=0, sticky="w")
    entry_nome = tk.Entry(form_frame, width=40)
    entry_nome.grid(row=0, column=1)

    tk.Label(form_frame, text="Email:").grid(row=1, column=0, sticky="w")
    entry_email = tk.Entry(form_frame, width=40)
    entry_email.grid(row=1, column=1)

    tk.Label(form_frame, text="Senha:").grid(row=2, column=0, sticky="w")
    entry_senha = tk.Entry(form_frame, show="*", width=40)
    entry_senha.grid(row=2, column=1)

    tk.Label(form_frame, text="ID para alterar/excluir:").grid(row=3, column=0, sticky="w")
    entry_id_pessoa = tk.Entry(form_frame, width=20)
    entry_id_pessoa.grid(row=3, column=1, sticky="w")

    button_frame = tk.Frame(form_frame, pady=10)
    button_frame.grid(row=4, column=0, columnspan=2)

    def adicionar_pessoa():
        nome = entry_nome.get()
        email = entry_email.get()
        senha = entry_senha.get()
        if nome and email and senha:
            pessoa = Pessoa(nome, email, senha)
            inserir_pessoa(pessoa)
            listar_pessoas_ui()
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos!")

    def alterar_pessoa_ui():
        id_str = entry_id_pessoa.get()
        nome = entry_nome.get()
        email = entry_email.get()
        senha = entry_senha.get()
        if id_str.isdigit() and nome and email and senha:
            pessoa = Pessoa(nome, email, senha, int(id_str))
            alterar_pessoa(pessoa)
            listar_pessoas_ui()
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos e informe o ID corretamente!")

    def excluir_pessoa_ui():
        id_str = entry_id_pessoa.get()
        if id_str.isdigit():
            deletar_pessoa(int(id_str))
            listar_pessoas_ui()
        else:
            messagebox.showwarning("Erro", "Informe um ID válido para excluir.")

    def listar_pessoas_ui():
        frame_listagem = tk.Frame(aba_pessoa, padx=10, pady=10, relief=tk.GROOVE, borderwidth=2)
        frame_listagem.grid(row=0, column=1, sticky="nsew")
        tk.Label(frame_listagem, text="Lista de Pessoas:", font=("Arial", 10, "bold")).pack(anchor='w')
        for widget in frame_listagem.winfo_children()[1:]:
            widget.destroy()
        pessoas = listar_pessoas()
        for p in pessoas:
            tk.Label(frame_listagem, text=f"ID {p[0]}: {p[1]} ({p[2]})").pack(anchor='w')

    tk.Button(button_frame, text="Listar", command=listar_pessoas_ui, width=10).grid(row=0, column=0, padx=5)
    tk.Button(button_frame, text="Adicionar", command=adicionar_pessoa, width=10).grid(row=0, column=1, padx=5)
    tk.Button(button_frame, text="Alterar", command=alterar_pessoa_ui, width=10).grid(row=0, column=2, padx=5)
    tk.Button(button_frame, text="Excluir", command=excluir_pessoa_ui, width=10).grid(row=0, column=3, padx=5)


    # aba de animal
    aba_animal = tk.Frame(notebook)
    notebook.add(aba_animal, text="Animal")
    aba_animal.columnconfigure(0, weight=1)
    aba_animal.columnconfigure(1, weight=1)

    form_animal = tk.Frame(aba_animal, padx=10, pady=10)
    form_animal.grid(row=0, column=0, sticky="nsew")

    tk.Label(form_animal, text="Nome:").grid(row=0, column=0, sticky="w")
    entry_nome_animal = tk.Entry(form_animal, width=40)
    entry_nome_animal.grid(row=0, column=1)

    tk.Label(form_animal, text="Idade:").grid(row=1, column=0, sticky="w")
    entry_idade_animal = tk.Entry(form_animal, width=40)
    entry_idade_animal.grid(row=1, column=1)

    tk.Label(form_animal, text="Espécie:").grid(row=2, column=0, sticky="w")
    entry_especie_animal = tk.Entry(form_animal, width=40)
    entry_especie_animal.grid(row=2, column=1)

    tk.Label(form_animal, text="Raça:").grid(row=3, column=0, sticky="w")
    entry_raca_animal = tk.Entry(form_animal, width=40)
    entry_raca_animal.grid(row=3, column=1)

    tk.Label(form_animal, text="Pessoa ID:").grid(row=4, column=0, sticky="w")
    entry_pessoa_id_animal = tk.Entry(form_animal, width=40)
    entry_pessoa_id_animal.grid(row=4, column=1)

    tk.Label(form_animal, text="ID para alterar/excluir:").grid(row=5, column=0, sticky="w")
    entry_id_animal = tk.Entry(form_animal, width=20)
    entry_id_animal.grid(row=5, column=1, sticky="w")

    button_animal = tk.Frame(form_animal, pady=10)
    button_animal.grid(row=6, column=0, columnspan=2)

    def adicionar_animal():
        nome = entry_nome_animal.get()
        idade = entry_idade_animal.get()
        especie = entry_especie_animal.get()
        raca = entry_raca_animal.get()
        pessoa_id = entry_pessoa_id_animal.get()
        if nome and idade and especie and raca and pessoa_id:
            animal = Animal(nome, int(idade), especie, raca, int(pessoa_id))
            inserir_animal(animal)
            listar_animais_ui()
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos!")

    def alterar_animal_ui():
        id_str = entry_id_animal.get()
        nome = entry_nome_animal.get()
        idade = entry_idade_animal.get()
        especie = entry_especie_animal.get()
        raca = entry_raca_animal.get()
        pessoa_id = entry_pessoa_id_animal.get()
        if id_str.isdigit() and nome and idade and especie and raca and pessoa_id:
            animal = Animal(nome, int(idade), especie, raca, int(pessoa_id), int(id_str))
            alterar_animal(animal)
            listar_animais_ui()
        else:
            messagebox.showwarning("Erro", "Preencha os campos corretamente!")

    def excluir_animal_ui():
        id_str = entry_id_animal.get()
        if id_str.isdigit():
            deletar_animal(int(id_str))
            listar_animais_ui()
        else:
            messagebox.showwarning("Erro", "Informe um ID válido para excluir.")

    def listar_animais_ui():
        frame_listagem_animal = tk.Frame(aba_animal, padx=10, pady=10, relief=tk.GROOVE, borderwidth=2)
        frame_listagem_animal.grid(row=0, column=1, sticky="nsew")
        tk.Label(frame_listagem_animal, text="Lista de Animais:", font=("Arial", 10, "bold")).pack(anchor='w')
        for widget in frame_listagem_animal.winfo_children()[1:]:
            widget.destroy()
        animais = listar_animais()
        for a in animais:
            tk.Label(frame_listagem_animal, text=f"ID {a[0]}: {a[1]}, {a[2]} anos - {a[3]} ({a[4]}) | Pessoa ID {a[5]}").pack(anchor='w')

    tk.Button(button_animal, text="Listar", command=listar_animais_ui, width=10).grid(row=0, column=0, padx=5)
    tk.Button(button_animal, text="Adicionar", command=adicionar_animal, width=10).grid(row=0, column=1, padx=5)
    tk.Button(button_animal, text="Alterar", command=alterar_animal_ui, width=10).grid(row=0, column=2, padx=5)
    tk.Button(button_animal, text="Excluir", command=excluir_animal_ui, width=10).grid(row=0, column=3, padx=5)

    # aba de vacina
    aba_vacina = tk.Frame(notebook)
    notebook.add(aba_vacina, text="Vacina")
    aba_vacina.columnconfigure(0, weight=1)
    aba_vacina.columnconfigure(1, weight=1)

    form_vacina = tk.Frame(aba_vacina, padx=10, pady=10)
    form_vacina.grid(row=0, column=0, sticky="nsew")

    tk.Label(form_vacina, text="Nome da Vacina:").grid(row=0, column=0, sticky="w")
    entry_nome_vacina = tk.Entry(form_vacina, width=40)
    entry_nome_vacina.grid(row=0, column=1)

    tk.Label(form_vacina, text="Dose:").grid(row=1, column=0, sticky="w")
    entry_dose_vacina = tk.Entry(form_vacina, width=40)
    entry_dose_vacina.grid(row=1, column=1)

    tk.Label(form_vacina, text="Data:").grid(row=2, column=0, sticky="w")
    entry_data_vacina = tk.Entry(form_vacina, width=40)
    entry_data_vacina.grid(row=2, column=1)

    tk.Label(form_vacina, text="Animal ID:").grid(row=3, column=0, sticky="w")
    entry_animal_id_vacina = tk.Entry(form_vacina, width=40)
    entry_animal_id_vacina.grid(row=3, column=1)

    tk.Label(form_vacina, text="ID para alterar/excluir:").grid(row=4, column=0, sticky="w")
    entry_id_vacina = tk.Entry(form_vacina, width=20)
    entry_id_vacina.grid(row=4, column=1, sticky="w")

    button_vacina = tk.Frame(form_vacina, pady=10)
    button_vacina.grid(row=5, column=0, columnspan=2)

    def adicionar_vacina():
        nome = entry_nome_vacina.get()
        dose = entry_dose_vacina.get()
        data = entry_data_vacina.get()
        animal_id = entry_animal_id_vacina.get()
        if nome and dose and data and animal_id:
            vacina = Vacina(nome, int(dose), data, int(animal_id))
            inserir_vacina(vacina)
            listar_vacinas_ui()
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos da vacina!")

    def alterar_vacina_ui():
        id_str = entry_id_vacina.get()
        nome = entry_nome_vacina.get()
        dose = entry_dose_vacina.get()
        data = entry_data_vacina.get()
        animal_id = entry_animal_id_vacina.get()
        if id_str.isdigit() and nome and dose and data and animal_id:
            vacina = Vacina(nome, int(dose), data, int(animal_id), int(id_str))
            alterar_vacina(vacina)
            listar_vacinas_ui()
        else:
            messagebox.showwarning("Erro", "Preencha os campos corretamente!")

    def excluir_vacina_ui():
        id_str = entry_id_vacina.get()
        if id_str.isdigit():
            deletar_vacina(int(id_str))
            listar_vacinas_ui()
        else:
            messagebox.showwarning("Erro", "Informe um ID válido para excluir.")

    def listar_vacinas_ui():
        frame_listagem_vacina = tk.Frame(aba_vacina, padx=10, pady=10, relief=tk.GROOVE, borderwidth=2)
        frame_listagem_vacina.grid(row=0, column=1, sticky="nsew")
        tk.Label(frame_listagem_vacina, text="Lista de Vacinas:", font=("Arial", 10, "bold")).pack(anchor='w')
        for widget in frame_listagem_vacina.winfo_children()[1:]:
            widget.destroy()
        vacinas = listar_vacinas()
        for v in vacinas:
            tk.Label(frame_listagem_vacina, text=f"ID {v[0]}: {v[1]} - Dose {v[2]}, Data: {v[3]} | Animal ID {v[4]}").pack(anchor='w')

    tk.Button(button_vacina, text="Listar", command=listar_vacinas_ui, width=10).grid(row=0, column=0, padx=5)
    tk.Button(button_vacina, text="Adicionar", command=adicionar_vacina, width=10).grid(row=0, column=1, padx=5)
    tk.Button(button_vacina, text="Alterar", command=alterar_vacina_ui, width=10).grid(row=0, column=2, padx=5)
    tk.Button(button_vacina, text="Excluir", command=excluir_vacina_ui, width=10).grid(row=0, column=3, padx=5)


    root.mainloop()
