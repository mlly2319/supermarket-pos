from tkinter import ttk
from tkinter import *
import tkinter as tk 
from ventas import Ventas
from inventario import Inventario
from proveedor import Proveedor
from reportes import Reportes
from cliente import Clientes

class Container(tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.place(x=0, y=0, width=1100, height=650)
        self.widgets()
        self.frames = {}
        self.buttons = []
        for i in (Ventas, Inventario, Clientes, Proveedor, Reportes):
            frame = i(self)
            self.frames[i] = frame
            frame.pack()
            frame
            frame.place(x=0, y=40, width=1100, height=610)
        self.show_frames(Ventas)

    def show_frames(self, container):
        frame = self.frames[container]
        frame.tkraise()

    def ventas(self):
        self.show_frames(Ventas)

    def inventario(self):
        self.show_frames(Inventario)
        
    def clientes(self):
        self.show_frames(Clientes)

    def reportes(self):
        self.show_frames(Reportes)

    def proveedor(self):
        self.show_frames(Proveedor)

    def cerrar_sesion(self):
        self.controlador.logout()

    def widgets(self):
        frame2 = tk.Frame(self, bg="#1A1F17")
        frame2.place(x=0, y=0, width=1100, height=40)

        self.btn_ventas = Button(frame2, text="🛒 Ventas", font="{Segoe UI} 14 bold", bg="#871F17", fg="white", command=self.ventas)
        self.btn_ventas.place(x=0, y=0, width=183, height=40)
        
        self.btn_inventario = Button(frame2, text="📦 Inventario", font="{Segoe UI} 14 bold", bg="#871F17", fg="white", command=self.inventario)
        self.btn_inventario.place(x=183, y=0, width=183, height=40)
        
        self.btn_clientes = Button(frame2, text="👥 Clientes", font="{Segoe UI} 14 bold", bg="#871F17", fg="white", command=self.clientes)
        self.btn_clientes.place(x=366, y=0, width=183, height=40)

        self.btn_proveedor = Button(frame2, text="🤝 Proveedores", font="{Segoe UI} 14 bold", bg="#871F17", fg="white", command=self.proveedor)
        self.btn_proveedor.place(x=549, y=0, width=183, height=40)

        self.btn_reportes = Button(frame2, text="📊 Reportes", font="{Segoe UI} 14 bold", bg="#871F17", fg="white", command=self.reportes)
        self.btn_reportes.place(x=732, y=0, width=183, height=40)

        self.btn_cerrar_sesion = Button(frame2, text="🚪 Cerrar sesión", font="{Segoe UI} 14 bold", bg="#871F17", fg="white", command=self.cerrar_sesion)
        self.btn_cerrar_sesion.place(x=915, y=0, width=185, height=40)

        self.buttons = [self.btn_ventas, self.btn_inventario, self.btn_proveedor, self.btn_reportes, self.btn_clientes, self.btn_cerrar_sesion]