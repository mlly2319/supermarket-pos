from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
try:
    from ventasclientes import Ventasclientes
except ImportError:
    messagebox.showerror(title= "Error", message="No se pudo importar el módulo Ventasclientes")
    raise

class Container_clientes(tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.pack()
        self.place(x=0, y=0, width=1100, height=650)
        self.widgets()
        self.frames = {}
        self.buttons = []
        for i in (Ventasclientes,):
            frame = i(self)
            self.frames[i] = frame
            frame.pack()
            frame
            frame.place(x=0, y=40, width=1100, height=610)
        self.show_frames(Ventasclientes)

    
    def show_frames(self, containercliente):
        frame = self.frames[containercliente]
        frame.tkraise()

    def ventasclientes(self):
        self.show_frames(Ventasclientes)
        
    def cerrar_sesion(self):
        self.controlador.logout()
        
    def widgets(self):
        frame2 = tk.Frame(self, bg="#1A1F17")
        frame2.place(x=0, y=0, width=1100, height=40)

        title = tk.Label(frame2, text="Ventas", font="{Segoe UI} 20 bold", bg="#1A1F17", fg="white")
        title.place(x=500, y=0)

        btn_cerrar = tk.Button(frame2, text="Cerrar sesión", font="{Segoe UI} 14 bold", bg="#871F17", fg="white", cursor="hand2", command=self.cerrar_sesion)
        btn_cerrar.place(x=915, y=0, width=185, height=40)
