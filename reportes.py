import sqlite3
from tkinter import *
import tkinter as tk
from ventas import Ventas
from tkinter import ttk, messagebox 
import datetime

class Reportes(ttk.Frame):
    db_name= "database.db"

    def __init__(self, padre):
        super().__init__(padre)
        self.widgets()
        self.ver_ventas_realizadas()
        
    
    def ver_ventas_realizadas(self):
        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("SELECT * FROM ventas")
            ventas = c.fetchall()
            conn.close()
        
            def filtrar_ventas():
                factura_a_buscar = entry_factura.get()
                cliente_a_buscar = entry_cliente.get()
                for item in tree.get_children():
                    tree.delete(item)
                    
                ventas_filtradas = [
                    venta for venta in ventas
                    if (str(venta[0])== factura_a_buscar or not factura_a_buscar) and
                    (venta[1].lower() == cliente_a_buscar.lower() or not cliente_a_buscar)
                ]
                
                for venta in ventas_filtradas:
                    venta = list(venta)
                    venta[3] = "{:,.0f}".format(venta[3])
                    venta[5] = "{:,.0f}".format(venta[5])
                    venta[6] = datetime.datetime.strptime(venta[6], "%Y-%m-%d").strftime("%d-%m-%Y")
                    tree.insert("", "end", values=venta)
                
            labelframe = ttk.LabelFrame(self)
            labelframe.place(x=25, y=40, width=1045, height=60)

            label_ventas_realizadas = ttk.Label(self, text="Ventas Realizadas", font="{Segoe UI} 14 bold")
            label_ventas_realizadas.place(x=450,y=10)
        
            label_factura = ttk.Label(labelframe, text="Numero de factura:", font="{Segoe UI} 14 bold")
            label_factura.place(x=10, y=5)
            
            entry_factura = ttk.Entry(labelframe, font="{Segoe UI} 14 bold")
            entry_factura.place(x=230, y=5, width=200, height=30)
            
            label_cliente = ttk.Label(labelframe, text="Cliente:", font="{Segoe UI} 14 bold")
            label_cliente.place(x=480, y=5)
            
            entry_cliente = ttk.Entry(labelframe, font="{Segoe UI} 14 bold")
            entry_cliente.place(x=620, y=5, width=200, height=30)
            
            btn_filtrar = tk.Button(labelframe, text="Filtrar", font="{Segoe UI} 12 bold", bg="#F2B04A", fg="black", cursor="hand2", command=filtrar_ventas)
            btn_filtrar.place(x=840, y=5)
        
            treeFrame = ttk.Frame(self)
            treeFrame.place(x=20, y=140, width=1060, height=400)
    
            scrol_y = ttk.Scrollbar(treeFrame)
            scrol_y.pack(side=RIGHT, fill=Y)
        
            scrol_x = ttk.Scrollbar(treeFrame, orient=HORIZONTAL)
            scrol_x.pack(side=BOTTOM, fill=X)
        
            tree = ttk.Treeview(treeFrame, columns=("Factura", "Cliente", "Producto", "Precio", "Cantidad", "Total", "Fecha", "Hora"), show="headings")
            tree.pack(expand=True, fill=BOTH)
        
            scrol_y.config(command=tree.yview)
            scrol_x.config(command=tree.xview)
    
            tree.heading("Factura", text="Factura")
            tree.heading("Cliente", text="Cliente")
            tree.heading("Producto", text="Producto")
            tree.heading("Precio", text="Precio")
            tree.heading("Cantidad", text="Cantidad")
            tree.heading("Total", text="Total")
            tree.heading("Fecha", text="Fecha")
            tree.heading("Hora", text="Hora")

            tree.column("Factura", width=60, anchor="center")
            tree.column("Cliente", width=120, anchor="center")
            tree.column("Producto", width=120, anchor="center")
            tree.column("Precio", width=80, anchor="center")
            tree.column("Cantidad", width=80, anchor="center")
            tree.column("Total", width=80, anchor="center")
            tree.column("Fecha", width=80, anchor="center")
            tree.column("Hora", width=80, anchor="center")
    
            for venta in ventas:
                venta = list(venta)
                venta[3] = "{:,.0f}".format(venta[3])
                venta[5] = "{:,.0f}".format(venta[5])
                venta[6] = datetime.datetime.strptime(venta[6], "%Y-%m-%d").strftime("%d-%m-%Y")
                tree.insert("", "end", values=venta)
                
        except sqlite3.Error as e:
            messagebox.showerror("Error", "Error al obtener las ventas", e)
            return
            
    def widgets(self):
        labelframe = tk.LabelFrame(self, font="{Segoe UI} 14 bold", bg="white")
        labelframe.place(x=25, y=40, width=1045, height=60)
        
        lbl_buscar = ttk.Label(labelframe, text="Numero de factura:", font="{Segoe UI} 14 bold")
        lbl_buscar.place(x=10, y=10)
        
        self.entry_buscar = ttk.Entry(labelframe, font="{Segoe UI} 14 bold")
        self.entry_buscar.place(x=200, y=10, width=200, height=30)
        
        lbl_cliente = ttk.Label(labelframe, text="Cliente:", font="{Segoe UI} 14 bold")
        lbl_cliente.place(x=420, y=10)
        
        self.entry_cliente = ttk.Entry(labelframe, font="{Segoe UI} 14 bold")
        self.entry_cliente.place(x=500, y=10, width=250, height=30)
        
        btn_filtrar = tk.Button(labelframe, text="Filtrar", font="{Segoe UI} 12 bold", bg="#F2B04A", fg="black", command=self.ver_ventas_realizadas)
        btn_filtrar.place(x=800, y=5, width=200, height=20)
