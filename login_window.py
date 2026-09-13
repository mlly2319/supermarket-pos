import sqlite3
from tkinter import *
import tkinter as tk 
from tkinter import ttk, messagebox
from container import Container
from PIL import Image, ImageTk
from container_clientes import Container_clientes
import hashlib

class Inicio(tk.Frame):
    
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.pack()
        self.place(x=0, y=0, width=1110, height=650)
        self.widgets()
        
    def control1(self):
        self.controlador.show_frame(Login)
        
    def control2(self):
        self.controlador.show_frame(Cliente)
    
    def widgets(self):
        fondo = tk.Frame(self, bg="white")
        fondo.pack(fill="both", expand=True)
        fondo.place(x=0, y=0, width=1100, height=650)
        
        self.bg_image_orig = Image.open("imagenes1/imagen1.jpg")
        self.bg_image = self.bg_image_orig.resize((1100, 650))
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = ttk.Label(fondo, image=self.bg_image)
        self.bg_label._orig_img = self.bg_image_orig
        self.bg_label.place(x=0, y=0, width=1100, height=650)
        
        frame1 = tk.Frame(self, bg="white", bd=2, relief="solid")
        frame1.place(x=110, y=200, width=330, height=330)
        
        self.logo1_image = Image.open("imagenes1/btnusuarios1.png")
        self.logo1_image = self.logo1_image.resize((100, 100))
        self.logo1_image = ImageTk.PhotoImage(self.logo1_image)
        self.logo1_label = tk.Label(frame1, image=self.logo1_image, bg="white")
        self.logo1_label.place(x=130, y=30)
        
        title = tk.Label(fondo, text="SUPERMARKET", font=("CocogooseProTrial Bold", 45), bg="white", fg="black")
        title.place(x=350, y=0)
        
        title1= tk.Label(frame1, text="Ingresar como:", font="{Segoe UI} 14 bold", bg="white")
        title1.place(x=40, y=130)
        
        btn1 = tk.Button(frame1, text=" Administrador", font="{Segoe UI} 14 bold", bg="#F2B04A", fg="black", cursor="hand2", command=self.control1)
        btn1.place(x=60,y=190, width=200, height=40)
        
        btn2 = tk.Button(frame1, text="Cliente", font="{Segoe UI} 14 bold", bg="#F2B04A", fg="black", cursor="hand2", command=self.control2)
        btn2.place(x=60,y=250, width=200, height=40)



class Login(tk.Frame):
    db_name = "database.db"

    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.pack()
        self.place(x=0, y=0, width=1110, height=650)
        self.controlador = controlador
        self.widgets()
        
    def validacion(self, user, pas):
        return len(user) > 0 and len(pas) > 0
    
    def login(self):
        user = self.username.get()
        pas = self.password.get()
        
        if self.validacion(user, pas):
            pas_hashed = hashlib.sha256(pas.encode()).hexdigest()
            consulta = "SELECT * FROM usuarios WHERE username = ? AND password = ?"
            parametros = (user, pas_hashed)
            
            try:
                with sqlite3.connect(self.db_name) as conn:
                    cursor = conn.cursor()
                    cursor.execute(consulta, parametros) 
                    result = cursor.fetchall()
                    
                    if result:
                        self.controlador.current_user = user
                        self.control1()
                    else:
                        self.username.delete(0, "end")
                        self.password.delete(0,"end")
                        messagebox.showerror(title= "Error", message="Usuario y/o clave incorrecta")
            except sqlite3.Error as e:
                messagebox.showerror(title="Error", message="No se conecto a la base de datos: {}".format(e))
                return
        else:
            messagebox.showerror(title="Error", message="Llene todas las casillas")
            return
            
    def control1(self):
        self.controlador.show_frame(Container)
        
    def control2(self):
        self.controlador.show_frame(Registro)
        
    def control3(self):
        self.controlador.show_frame(Inicio)
    
    def widgets(self):
        fondo = tk.Frame(self, bg="white")
        fondo.pack()
        fondo.place(x=0, y=0, width=1100, height=650)
        
        self.bg_image_orig = Image.open("imagenes1/imagen1.jpg")
        self.bg_image = self.bg_image_orig.resize((1100, 650))
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = ttk.Label(fondo, image=self.bg_image)
        self.bg_label._orig_img = self.bg_image_orig
        self.bg_label.place(x=0, y=0, width=1100, height=650)
        
        frame1 = tk.Frame(self, bg="white", bd=2, relief="solid")
        frame1.place(x=110, y=200, width=330, height=330)
        
        title = tk.Label(fondo, text="SUPERMARKET", font=("CocogooseProTrial Bold", 45), bg="white", fg="#1A1F17")
        title.place(x=350, y=0)
        
        title1= tk.Label(frame1, text="Login", font="{Segoe UI} 14 bold", bg="white")
        title1.place(x=40, y=10)
        
        user= tk.Label(frame1, text="Usuario", font="{Segoe UI} 14 bold", bg="white")
        user.place(x=20, y=60)
        self.username = ttk.Entry(frame1, font="{Segoe UI} 14 bold")
        self.username.place(x=20, y=90, width=280, height=30)
        
        pas = tk.Label(frame1, text="Clave", font="{Segoe UI} 14 bold", bg="white")
        pas.place(x=20, y=130)
        self.password = ttk.Entry(frame1,show="*",font="{Segoe UI} 14 bold")
        self.password.place(x=20, y=160, width=280, height=30)
        
        btn1 = tk.Button(frame1, text="Iniciar", font="{Segoe UI} 14 bold", bg="#F2B04A", fg="black", cursor="hand2", command=self.login)
        btn1.place(x=60,y=200, width=200, height=30)
        
        btn2 = tk.Button(frame1, text="Registrar", font="{Segoe UI} 14 bold", bg="#F2B04A", fg="black", cursor="hand2", command=self.control2)
        btn2.place(x=60,y=240, width=200, height=30)
        
        btn3 = tk.Button(frame1, text="Regresar", font="{Segoe UI} 14 bold", bg="#F2B04A", fg="black", cursor="hand2", command=self.control3)
        btn3.place(x=60,y=280, width=200, height=30)
        
def cargar_clave_admin():
    try:
        with open(".env", "r") as f:
            for linea in f:
                linea = linea.strip()
                if linea.startswith("CLAVE_ADMIN="):
                    return linea.split("=", 1)[1]
    except FileNotFoundError:
        pass
    return "1234"
            
class Registro(tk.Frame):
    db_name = "database.db"

    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.pack()
        self.place(x=0, y=0, width=1110, height=650)
        self.controlador = controlador
        self.widgets()
        
    def validacion(self, user, pas):
        return len(user) > 0 and len(pas) > 0
    
    def eje_consulta(self, consulta, parametros=()):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(consulta, parametros)
                conn.commit()
        except sqlite3.Error as e:
            messagebox.showerror(title="Error", message="Error al ejecutar la consulta:{} ".format(e))
            return
            
    def registro(self):
        user = self.username.get()
        pas = self.password.get()
        key = self.key.get()
        if self.validacion(user, pas):
            if len(pas) < 6:
                messagebox.showinfo(title="Error", message="clave demasiado corta")
                self.username.delete(0,'end')
                self.password.delete(0,'end')
            else:
                if key == cargar_clave_admin():
                    pas_hashed = hashlib.sha256(pas.encode()).hexdigest()
                    consulta = "INSERT INTO usuarios VALUES (?,?,?)"
                    parametros =(None, user, pas_hashed)
                    self.eje_consulta(consulta, parametros)
                    messagebox.showinfo(title="Registro", message="Usuario registrado exitosamente.")
                    self.control2()
                else:
                    messagebox.showerror(title="Registro", message="Error al ingresar el codigo de registro")
                    return
        else:
            messagebox.showerror(title="Error", message="Llene sus datos")
            return
            
    def control1(self):
        self.controlador.show_frame(Registro)
        
    def control2(self):
        self.controlador.show_frame(Login)
            
    def widgets(self):
        fondo = tk.Frame(self, bg="white")
        fondo.pack()
        fondo.place(x=0, y=0, width=1100, height=650)
        
        self.bg_image_orig = Image.open("imagenes1/imagen1.jpg")
        self.bg_image = self.bg_image_orig.resize((1100, 650))
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = ttk.Label(fondo, image=self.bg_image)
        self.bg_label._orig_img = self.bg_image_orig
        self.bg_label.place(x=0, y=0, width=1100, height=650)
        
        frame1 = tk.Frame(self, bg="white", bd=2, relief="solid")
        frame1.place(x=110, y=150, width=330, height=430)
        
        title = tk.Label(fondo, text="SUPERMARKET", font=("CocogooseProTrial Bold", 45), bg="white", fg="#1A1F17")
        title.place(x=350, y=0)
        
        title1= tk.Label(frame1, text="Registrarse", font="{Segoe UI} 14 bold", bg="white")
        title1.place(x=40, y=10)
        
        user= tk.Label(frame1, text="Usuario", font="{Segoe UI} 14 bold", bg="white")
        user.place(x=20, y=60)
        self.username = ttk.Entry(frame1, font="{Segoe UI} 14 bold")
        self.username.place(x=20, y=90, width=280, height=30)
        
        pas = tk.Label(frame1, text="Clave", font="{Segoe UI} 14 bold", bg="white")
        pas.place(x=20, y=130)
        self.password = ttk.Entry(frame1,show="*",font="{Segoe UI} 14 bold")
        self.password.place(x=20, y=160, width=280, height=30)
        
        key = tk.Label(frame1, text="Codigo de Registro", font="{Segoe UI} 14 bold", bg="white")
        key.place(x=20, y=200)
        self.key= ttk.Entry(frame1,show="*",font="{Segoe UI} 14 bold")
        self.key.place(x=20, y=230, width=280, height=30)
        
        btn4 = tk.Button(frame1, text="Registrar", font="{Segoe UI} 14 bold", bg="#F2B04A", fg="black", cursor="hand2", command=self.registro)
        btn4.place(x=60,y=280, width=200, height=30)
        
        btn5 = tk.Button(frame1, text="Regresar", font="{Segoe UI} 14 bold", bg="#F2B04A", fg="black", cursor="hand2", command=self.control2)
        btn5.place(x=60,y=320, width=200, height=30)
        
class Cliente(tk.Frame):
    db_name= "database.db"
    
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.pack()
        self.place(x=0, y=0, width=1110, height=650)
        self.controlador = controlador
        self.widgets()
        
    def validacion(self, iduser):
        return len(iduser) > 0 
    
    def Cliente(self):
        iduser = self.idusercedula.get()
        
        if self.validacion(iduser):
            consulta = "SELECT * FROM clientes WHERE idusercedula = ?"
            parametros = (iduser,)
            
            try:
                with sqlite3.connect(self.db_name) as conn:
                    cursor = conn.cursor()
                    cursor.execute(consulta, parametros)
                    result = cursor.fetchall()
                    
                    if result:
                        self.controlador.current_client_name = f"{result[0][1]} {result[0][2]}"
                        self.control1()
                    else:
                        self.idusercedula.delete(0, "end")
                        messagebox.showerror(title= "Error", message="Cedula incorrecta")
                        return
                    
            except sqlite3.Error as e:
                messagebox.showerror(title="Error", message="No se conecto a la base de datos: {}".format(e))
                return
        else:
            messagebox.showerror(title="Error", message="Llene la casilla")
            return
            
        
    def control1(self):
        self.controlador.show_frame(Container_clientes)
        
    def control2(self):
        self.controlador.show_frame(RegistroCliente)
        
    def control3(self):
        self.controlador.show_frame(Inicio)
        
    def widgets(self):
        fondo = tk.Frame(self, bg="white")
        fondo.pack()
        fondo.place(x=0, y=0, width=1100, height=650)
        
        self.bg_image_orig = Image.open("imagenes1/imagen1.jpg")
        self.bg_image = self.bg_image_orig.resize((1100, 650))
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = ttk.Label(fondo, image=self.bg_image)
        self.bg_label._orig_img = self.bg_image_orig
        self.bg_label.place(x=0, y=0, width=1100, height=650)
        
        frame1 = tk.Frame(self, bg="white", bd=2, relief="solid")
        frame1.place(x=110, y=150, width=330, height=330)
        
        title = tk.Label(fondo, text="SUPERMARKET", font=("CocogooseProTrial Bold", 45), bg="white", fg="#1A1F17")
        title.place(x=350, y=0)
        
        title1= tk.Label(frame1, text="Cliente", font="{Segoe UI} 14 bold", bg="white")
        title1.place(x=40, y=20)
        
        iduser= tk.Label(frame1, text="Cedula de identidad", font="{Segoe UI} 14 bold", bg="white")
        iduser.place(x=20, y=70)
        self.idusercedula = ttk.Entry(frame1, font="{Segoe UI} 14 bold")
        self.idusercedula.place(x=20, y=100, width=280, height=30)
        
        btn6 = tk.Button(frame1, text="Acceder", font="{Segoe UI} 14 bold", bg="#F2B04A", fg="black", cursor="hand2", command=self.Cliente)
        btn6.place(x=60,y=150, width=200, height=30)
        
        btn7 = tk.Button(frame1, text="Registrar", font="{Segoe UI} 14 bold", bg="#F2B04A", fg="black", cursor="hand2", command=self.control2)
        btn7.place(x=60,y=200, width=200, height=30)
        
        btn8 = tk.Button(frame1, text="Regresar", font="{Segoe UI} 14 bold", bg="#F2B04A", fg="black", cursor="hand2", command=self.control3)
        btn8.place(x=60, y=240, width=200, height=30)

        
class RegistroCliente(tk.Frame):
    db_name= "database.db"

    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.pack()
        self.place(x=0, y=0, width=1110, height=650)
        self.controlador = controlador
        self.widgets()

    
    def validacion(self, user, last, iduser):
            return len(user) > 0 and len(last) > 0 and len(iduser) > 0
        
    def eje_consulta(self, consulta, parametros=()):
            try:
                with sqlite3.connect(self.db_name) as conn:
                    cursor = conn.cursor()
                    cursor.execute(consulta, parametros)
                    conn.commit()
            except sqlite3.Error as e:
                messagebox.showerror(title="Error", message="Error al ejecutar la consulta:{} ".format(e))
                return
                
    def registrocliente(self):
            user = self.username.get()
            last = self.lastname.get()
            iduser = self.idusercedula.get()
            
            if not iduser.isdigit():
                messagebox.showerror(title="Error", message="La cedula debe contener solo numeros")
                self.idusercedula.delete(0, 'end')
                return
            
            if self.validacion(user, last, iduser):
                if len(iduser) < 6 :
                    messagebox.showinfo(title="Error", message="La cedula debe tener almenos 6 dígitos")
                    self.idusercedula.delete(0, 'end')
                    return
                if not all([user,last,iduser]):
                    messagebox.showerror(title="Error", message="Todos los campos son obligatorios")
                    self.username.delete(0,'end')
                    self.lastname.delete(0,'end')
                    self.idusercedula.delete(0,'end')
                    return
        
                if self.validacion(user, last, iduser):
                    consulta = "INSERT INTO clientes (idusercedula, username, lastname) VALUES (?,?,?)"
                    parametros =(iduser, user, last)
                    self.eje_consulta(consulta, parametros)
                    messagebox.showinfo(title="Registro", message="Usuario registrado con éxito")
                    self.username.delete(0,'end')
                    self.lastname.delete(0,'end')
                    self.idusercedula.delete(0,'end')
                else:
                    messagebox.showerror(title="Registro", message="Error al registrar usuario")
                    return
            else:
                messagebox.showerror(title="Error", message="Llene sus datos")
                return
            
    def control1(self):
        self.controlador.show_frame(RegistroCliente)
        
    def control2(self):
        self.controlador.show_frame(Cliente)

    def widgets(self):
        fondo = tk.Frame(self, bg="white")
        fondo.pack()
        fondo.place(x=0, y=0, width=1100, height=650)
        
        self.bg_image_orig = Image.open("imagenes1/imagen1.jpg")
        self.bg_image = self.bg_image_orig.resize((1100, 650))
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = ttk.Label(fondo, image=self.bg_image)
        self.bg_label._orig_img = self.bg_image_orig
        self.bg_label.place(x=0, y=0, width=1100, height=650)
        
        frame1 = tk.Frame(self, bg="white", bd=2, relief="solid")
        frame1.place(x=110, y=150, width=330, height=430)
        
        title = tk.Label(fondo, text="SUPERMARKET", font=("CocogooseProTrial Bold", 45), bg="white", fg="#1A1F17")
        title.place(x=350, y=0)
        
        title1= tk.Label(frame1, text="Registrarse", font="{Segoe UI} 14 bold", bg="white")
        title1.place(x=40, y=10)
        
        user= tk.Label(frame1, text="Nombre", font="{Segoe UI} 14 bold", bg="white")
        user.place(x=20, y=50)
        self.username = ttk.Entry(frame1, font="{Segoe UI} 14 bold")
        self.username.place(x=20, y=90, width=280, height=30)
        
        last = tk.Label(frame1, text="Apellido", font="{Segoe UI} 14 bold", bg="white")
        last.place(x=20, y=130)
        self.lastname = ttk.Entry(frame1,font="{Segoe UI} 14 bold")
        self.lastname.place(x=20, y=170, width=280, height=30)
        
        iduser = tk.Label(frame1, text="Cedula de identidad", font="{Segoe UI} 14 bold", bg="white")
        iduser.place(x=20, y=220)
        self.idusercedula= ttk.Entry(frame1,font="{Segoe UI} 14 bold")
        self.idusercedula.place(x=20, y=250, width=280, height=30)
        
        btn9 = tk.Button(frame1, text="Registrar", font="{Segoe UI} 14 bold", bg="#F2B04A", fg="black", cursor="hand2", command=self.registrocliente)
        btn9.place(x=40,y=300, width=250, height=30)
        
        btn10 = tk.Button(frame1, text="Regresar", font="{Segoe UI} 14 bold", bg="#F2B04A", fg="black", cursor="hand2", command=self.control2)
        btn10.place(x=40,y=350, width=250, height=30)