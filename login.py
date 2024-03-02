
import customtkinter as ctk
from tkinter import *
import database
from tkinter import messagebox


janela = ctk.CTk()

class Aplication():
    def  __init__(self):
        self.janela=janela
        self.tema()
        self.tela()
        self.tela_login()
        janela.mainloop()
        
        



    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")


    def tela(self):
        janela.geometry("924x520")
        janela.title("Sistema de Login")
        janela.resizable(False,False)
        icon = PhotoImage(file="icon.png")
        janela.wm_iconphoto(True, icon)

    def tela_login(self):    
        # Trabalhando com a imagem
        img = PhotoImage(file="log.png")
        label_img = ctk.CTkLabel(master=janela, image=img, text="",).place(x=15, y=75)


        title_label = ctk.CTkLabel(master=janela, text="Entre na sua Conta para usar\na Plataforma",
            font=("Roboto", 20)).place(x=140, y=10)

        # Frame
        login_frame = ctk.CTkFrame(master=janela, width=400, height=396)
        login_frame.pack(side=RIGHT)


        # Widget dentro da frame de tela login

        label = ctk.CTkLabel(master=login_frame, text="Fabio Barbearia", 
            font=("Roboto", 20)).place(x=15, y=10)

        username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Email", 
        width=300, font=("Roboto", 20)).place(x=25, y=105)
        username_label = ctk.CTkLabel(master=login_frame,text="Email Obrigatório.",
        text_color="green",font=("Roboto", 15)).place(x=25, y=135)


        password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Senha", 
        width=300, font=("Roboto", 20), show="*").place(x=25, y=175)
        password_label = ctk.CTkLabel(master=login_frame,text="Senha Obrigatório.",
        text_color="green",font=("Roboto", 15)).place(x=25, y=205)

        chekbox = ctk.CTkCheckBox(master=login_frame, text="lembrar Email").place(x=25, y=235)  

        def login():
            msg = messagebox.showinfo(title="Estado do login", message="Login realizado com sucesso!")
            pass
        login_button = ctk.CTkButton(master=login_frame, text="Login", width=300, command=login).place(x=25, y=285)

        register_span = ctk.CTkLabel(master=login_frame,text="Não tem uma conta?").place(x=25, y=325)

        def tela_register():
        # Remover tela de login
            login_frame.pack_forget()


        # Criando tela de cadastro
            register_frame = ctk.CTkFrame(master=janela, width=400, height=396)
            register_frame.pack(side=RIGHT)

            label = ctk.CTkLabel(master=register_frame, text="Cadastro de login", 
            font=("Roboto", 20)).place(x=25, y=5)

            username_entry = ctk.CTkEntry(master=register_frame, placeholder_text="E-mail",
            width=300, font=("Roboto", 20)).place(x=25, y=50)
            

            userpassword_entry = ctk.CTkEntry(master=register_frame, placeholder_text="Senha",
            width=300, font=("Roboto", 20, )).place(x=25, y=120)

            userpassword_entry = ctk.CTkEntry(master=register_frame, placeholder_text="Confirme a senha",
            width=300, font=("Roboto", 20, )).place(x=25, y=190)

            def back():
            # removendo frame de cadrastro    
                register_frame.pack_forget()

            # devolvendo o frame de login    
                login_frame.pack(side=RIGHT)

                
            back_button = ctk.CTkButton(master=register_frame, text="Voltar", 
            width=120,fg_color="gray", command=back).place(x=25, y=300)


            def save_user():   
                msg = messagebox.showinfo(title="Estado do cadastro", message="Cadastro realizado\n  com sucesso!")
                pass 
            save_button = ctk.CTkButton(master=register_frame, 
            text="Salvar",fg_color="green", command=save_user, width=175).place(x=150, y=300)



            
        register_button = ctk.CTkButton(master=login_frame, text="Cadastre-se", width=150,
        fg_color="green", hover_color="#2D9334", command=tela_register).place(x=175, y=325)


Aplication()
