import sqlite3 
from tkinter import *
import tkinter as tk 
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class Clientes(ttk.Frame):
    db_name = "database.db"

    def __init__(self, padre):
        super().__init__(padre)
        self.widgets()
        self.cargar_registros()

    def widgets(self):
        self.labelframe = ttk.LabelFrame(self, text="Clientes")
        self.labelframe.place(x=20, y=20, width=260, height=560)
        
        lblnombre = ttk.Label(self.labelframe, text="Nombre: ", font="{Segoe UI} 14 bold")
        lblnombre.place(x=10, y=20)
        self.nombre = ttk.Entry(self.labelframe, font="{Segoe UI} 14 bold")
        self.nombre.place(x=10, y=50, width=220, height=40)
        
        lblcedula = ttk.Label(self.labelframe, text="Cédula: ", font="{Segoe UI} 14 bold")
        lblcedula.place(x=10, y=100)
        self.cedula = ttk.Entry(self.labelframe, font="{Segoe UI} 14 bold")
        self.cedula.place(x=10, y=130, width=220, height=40)
        
        lblcelular = ttk.Label(self.labelframe, text="Celular: ", font="{Segoe UI} 14 bold")
        lblcelular.place(x=10, y=180)
        self.celular = ttk.Entry(self.labelframe, font="{Segoe UI} 14 bold")
        self.celular.place(x=10, y=210, width=220, height=40)
        
        lbldireccion = ttk.Label(self.labelframe, text="Dirección: ", font="{Segoe UI} 14 bold")
        lbldireccion.place(x=10, y=260)
        self.direccion = ttk.Entry(self.labelframe, font="{Segoe UI} 14 bold")
        self.direccion.place(x=10, y=290, width=220, height=40)
        
        lblcorreo = ttk.Label(self.labelframe, text="Correo: ", font="{Segoe UI} 14 bold")
        lblcorreo.place(x=10, y=340)
        self.correo = ttk.Entry(self.labelframe, font="{Segoe UI} 14 bold")
        self.correo.place(x=10, y=370, width=220, height=40)
        
        btn1 = tk.Button(self.labelframe, text="Ingresar", font="{Segoe UI} 14 bold", bg="#F2B04A", fg="black", cursor="hand2", command=self.registrar)
        btn1.place(x=10, y=420, width=220, height=30)
        
        btn2 = tk.Button(self.labelframe, text="Modificar", font="{Segoe UI} 14 bold", bg="#F2B04A", fg="black", cursor="hand2", command=self.modificar)
        btn2.place(x=10, y=460, width=220, height=30)
        
        btn3 = tk.Button(self.labelframe, text="Eliminar", font="{Segoe UI} 14 bold", bg="#F2B04A", fg="black", cursor="hand2", command=self.eliminar)
        btn3.place(x=10, y=500, width=220, height=30)
        
        treFrame = Frame(self)
        treFrame.place(x=290, y=20, width=790, height=560)
        
        scrol_y = ttk.Scrollbar(treFrame)
        scrol_y.pack(side=RIGHT, fill=Y)
        
        scrol_x = ttk.Scrollbar(treFrame, orient=HORIZONTAL)
        scrol_x.pack(side=BOTTOM, fill=X)
        
        self.tre = ttk.Treeview(treFrame, yscrollcommand=scrol_y.set, xscrollcommand=scrol_x.set, height=40,
                                columns=("ID", "Nombre", "Cédula", "Celular", "Dirección", "Correo"), show="headings")
        self.tre.pack(expand=True, fill=BOTH)
        
        scrol_y.config(command=self.tre.yview)
        scrol_x.config(command=self.tre.xview)
        
        self.tre.heading("ID", text="ID")
        self.tre.heading("Nombre", text="Nombre")
        self.tre.heading("Cédula", text="Cédula")
        self.tre.heading("Celular", text="Celular")
        self.tre.heading("Dirección", text="Dirección")
        self.tre.heading("Correo", text="Correo")
        
        self.tre.column("ID", width=50, anchor="center")
        self.tre.column("Nombre", width=150, anchor="center")
        self.tre.column("Cédula", width=120, anchor="center")
        self.tre.column("Celular", width=120, anchor="center")
        self.tre.column("Dirección", width=200, anchor="center")
        self.tre.column("Correo", width=200, anchor="center")
    
    def validar_campos(self):
        if not self.nombre.get() or not self.cedula.get() or not self.celular.get() or not self.direccion.get() or not self.correo.get():
            messagebox.showerror("Error", "Todos los campos son requeridos")
            return False
        return True
    
    def registrar(self):
        if not self.validar_campos():
            return
        
        nombre = self.nombre.get()
        cedula = self.cedula.get()
        celular = self.celular.get()
        direccion = self.direccion.get()
        correo = self.correo.get()
        
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO cliente (nombre, cedula, celular, direccion, correo) VALUES (?, ?, ?, ?, ?)",
                        (nombre, cedula, celular, direccion, correo))
            conn.commit()
            conn.close()
            messagebox.showinfo("Exito", "Cliente registrado correctamente.")
            self.limpiar_campos
            self.limpiar_treeview()
            self.cargar_registros()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"No se pudo registrar el cliente: {e}")
            return
            
    def cargar_registros(self):
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM cliente")
            rows = cursor.fetchall()
            for row in rows:
                self.tre.insert("", "end", values=row)
            conn.close()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"No se pudo cargar los registros: {e}")
            return
            
    def limpiar_treeview(self):
        for item in self.tre.get_children():
            self.tre.delete(item)
            
    def limpiar_campos(self):
        self.nombre.delete(0, END)
        self.cedula.delete(0, END)
        self.celular.delete(0, END)
        self.direccion.delete(0, END)
        self.correo.delete(0, END)
        
    def modificar(self):
        if not self.tre.selection():
            messagebox.showerror("Error", "Por favor seleccione un cliente para modificar.")
            return
        
        item = self.tre.selection()[0]
        id_cliente = self.tre.item(item, "values")[0]
        
        nombre_actual = self.tre.item(item, "values")[1]
        cedula_actual = self.tre.item(item, "values")[2]
        celular_actual = self.tre.item(item, "values")[3]
        direccion_actual = self.tre.item(item, "values")[4]
        correo_actual = self.tre.item(item, "values")[5]
        
        top_modificar = Toplevel(self)
        top_modificar.title("Modificar cliente")
        top_modificar.geometry("400x400+400+50")
        top_modificar
        top_modificar.resizable(False, False)
        top_modificar.transient(self.master)
        top_modificar.grab_set()
        top_modificar.focus_set()
        top_modificar.lift()
        
        self.logo1_image = Image.open("imagenes1/registrar1.png")
        self.logo1_image=self.logo1_image.resize((80, 80), Image.LANCZOS)
        self.logo1_image = ImageTk.PhotoImage(self.logo1_image)
        self.logo1_label = ttk.Label(top_modificar, image=self.logo1_image)
        self.logo1_label.place(x=150, y=10)
        
        nombre_label = ttk.Label(top_modificar, text="Nombre: ", font="{Segoe UI} 14 bold")
        nombre_label.place(x=10, y=110)
        nombre_nuevo = ttk.Entry(top_modificar, font="{Segoe UI} 14 bold")
        nombre_nuevo.insert(0, nombre_actual)
        nombre_nuevo.place(x=110, y=110, width=250, height=30)
        
        cedula_label= ttk.Label(top_modificar, text="Cédula: ", font="{Segoe UI} 14 bold")
        cedula_label.place(x=10, y=150)
        cedula_nuevo = ttk.Entry(top_modificar, font="{Segoe UI} 14 bold")
        cedula_nuevo.insert(0, cedula_actual)
        cedula_nuevo.place(x=110, y=150, width=250, height=30)
        
        celular_label = ttk.Label(top_modificar, text="Celular: ", font="{Segoe UI} 14 bold")
        celular_label.place(x=10, y=190)
        celular_nuevo = ttk.Entry(top_modificar, font="{Segoe UI} 14 bold")
        celular_nuevo.insert(0, celular_actual)
        celular_nuevo.place(x=110, y=190, width=250, height=30)
        
        direccion_label = ttk.Label(top_modificar, text="Dirección: ", font="{Segoe UI} 14 bold")
        direccion_label.place(x=10, y=230)
        direccion_nuevo = ttk.Entry(top_modificar, font="{Segoe UI} 14 bold")
        direccion_nuevo.insert(0, direccion_actual)
        direccion_nuevo.place(x=110, y=230, width=250, height=30)
        
        correo_label = ttk.Label(top_modificar, text="Correo: ", font="{Segoe UI} 14 bold")
        correo_label.place(x=10, y=270)
        correo_nuevo = ttk.Entry(top_modificar, font="{Segoe UI} 14 bold")
        correo_nuevo.insert(0, correo_actual)
        correo_nuevo.place(x=110, y=270, width=250, height=30)
        
        def guardar_modificiones():
            nuevo_nombre = nombre_nuevo.get()
            nueva_cedula = cedula_nuevo.get()
            nuevo_celular = celular_nuevo.get()
            nueva_direccion = direccion_nuevo.get()
            nuevo_correo = correo_nuevo.get()
            
            try:
                conn = sqlite3.connect(self.db_name)
                cursor = conn.cursor()
                cursor.execute("""UPDATE cliente SET nombre = ?, cedula = ?, celular = ?, direccion = ?, correo = ? WHERE id = ?""",
                            (nuevo_nombre, nueva_cedula, nuevo_celular, nueva_direccion, nuevo_correo, id_cliente))
                conn.commit()
                conn.close()
                messagebox.showinfo("Exito", "Cliente modificado correctamente.")
                self.limpiar_treeview()
                self.cargar_registros()
                top_modificar.destroy()
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"No se pudo modificar el cliente: {e}")
                return
            
        btn_guardar = tk.Button(top_modificar, text="Guardar Cambios", font="{Segoe UI} 14 bold", bg="#F2B04A", fg="black", cursor="hand2", command=guardar_modificiones)
        btn_guardar.place(x=50, y= 320, width=250, height=40)
        
    def eliminar(self):
            if not self.tre.selection():
                messagebox.showerror("Error", "Por favor seleccione un proveedor para eliminar.")
                return
    
            item = self.tre.selection()[0]
            id_proveedor = self.tre.item(item, "values")[0]
            nombre_proveedor = self.tre.item(item, "values")[1]
    
            respuesta = messagebox.askyesno("Confirmar", f"¿Seguro que desea eliminar al proveedor '{nombre_proveedor}'?")
            if not respuesta:
                return
    
            try:
                conn = sqlite3.connect(self.db_name)
                cursor = conn.cursor()
                cursor.execute("DELETE FROM proveedores WHERE id = ?", (id_proveedor,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Exito", "Proveedor eliminado correctamente.")
                self.limpiar_treeview()
                self.cargar_registros()
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"No se pudo eliminar el proveedor: {e}")
                return