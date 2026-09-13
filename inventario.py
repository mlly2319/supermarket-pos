from utils import show_toast
import sqlite3 
from tkinter import *
import tkinter as tk 
from tkinter import ttk, messagebox, filedialog
from PIL import Image , ImageTk
import os


class Inventario(ttk.Frame):
    db_name = "database.db"

    def __init__(self, padre):
        super().__init__(padre)
        self.widgets()
        self.articulos_combobox()
        self.cargar_articulos()
        self.timer_articulos = None
        
        self.image_folder = "fotos"
        if not os.path.exists(self.image_folder):
            os.makedirs(self.image_folder)
            

    def widgets(self):
    #====================================================================================================================
        canvas_articulos = ttk.LabelFrame(self, text="Articulos")
        canvas_articulos.place(x=300, y=10, width=800, height=580)
        
        self.canvas = tk.Canvas(canvas_articulos)
        self.scrollbar = tk.Scrollbar(canvas_articulos, orient= "vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        
        self.canvas.create_window((0,0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)        
        
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
    #====================================================================================================================
        Lblframe_buscar = LabelFrame(self, text="Buscar", font="{Segoe UI} 14 bold")
        Lblframe_buscar.place(x=10,y=10, width=280, height=80)
        
        self.comboboxbuscar = ttk.Combobox(Lblframe_buscar, font="{Segoe UI} 14 bold")
        self.comboboxbuscar.place(x=5, y=5, width=260, height=40)
        self.comboboxbuscar.bind("<<ComboboxSelected>>", self.on_combobox_select)
        self.comboboxbuscar.bind("<KeyRelease>", self.filtrar_articulos)
    #====================================================================================================================
        lblframe_seleccion = LabelFrame(self, text="Seleccionado", font="{Segoe UI} 14 bold")
        lblframe_seleccion.place(x=10, y=95, width=280, height=190)
        
        self.label1 = ttk.Label(lblframe_seleccion, text="Articulo:", font="{Segoe UI} 14 bold", wraplength=300)
        self.label1.place(x=5, y=5)
        
        self.label2 = ttk.Label(lblframe_seleccion, text="Precio:", font="{Segoe UI} 14 bold")
        self.label2.place(x=5, y=40)
        
        self.label3 = ttk.Label(lblframe_seleccion, text="Costo:", font="{Segoe UI} 14 bold")
        self.label3.place(x=5, y=70)
        
        self.label4 = ttk.Label(lblframe_seleccion, text="Stock:", font="{Segoe UI} 14 bold")
        self.label4.place(x=5, y=100)
        
        self.label5 = ttk.Label(lblframe_seleccion, text="Estado:", font="{Segoe UI} 14 bold")
        self.label5.place(x=5, y=130)
    #====================================================================================================================
        lblframe_botones = LabelFrame(self, text="Opciones", font="{Segoe UI} 14 bold")
        lblframe_botones.place(x=10, y=290, width=280, height=300)
        
        btn1 = tk.Button(lblframe_botones, text="Agregar", font="{Segoe UI} 14 bold", bg="#F2B04A", fg="black", cursor="hand2", command=self.agregar_articulo) 
        btn1.place(x=40,y=20, width=180, height=40)
        
        btn2 = tk.Button(lblframe_botones, text="Editar", font="{Segoe UI} 14 bold", bg="#F2B04A", fg="black", cursor="hand2", command=self.editar_articulos) 
        btn2.place(x=40,y=70, width=180, height=40)       
        
        btn3 = tk.Button(lblframe_botones, text="Eliminar", font="{Segoe UI} 14 bold", bg="#F2B04A", fg="black", cursor="hand2", command=self.eliminar_articulo)
        btn3.place(x=40, y=120, width=180, height=40)
    
    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            image = Image.open(file_path)
            image = image.resize((200, 200), Image.LANCZOS)
            image_name = os.path.basename(file_path)
            image_save_path = os.path.join(self.image_folder, image_name)
            image.save(image_save_path)
            
            self.image_tk = ImageTk.PhotoImage(image)
            self.product_image = self.image_tk
            self.image_path = image_save_path
            
            img_label = ttk.Label(self.frameimg, image=self.image_tk)
            img_label.place(x=0, y=0, width=200, height=200)
            
    def articulos_combobox(self):
        self.conn = sqlite3.connect("database.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT articulo FROM articulos")
        self.articulos = [row[0] for row in self.cur.fetchall()]
        self.comboboxbuscar['values'] = self.articulos
    
    def agregar_articulo(self):
        top = tk.Toplevel(self)
        top.title("Agregar Articulo")
        top.geometry("750x450+200+50")
        top
        top.resizable(False, False)
        
        top.transient(self.master)
        top.grab_set()
        top.focus_set()
        top.lift()
        
        ttk.Label(top, text="Articulos:", font="{Segoe UI} 14 bold").place(x=20, y=20, width=105 ,height=25)
        entry_articulo = ttk.Entry(top, font="{Segoe UI} 14 bold")
        entry_articulo.place(x=130, y=20, width=240, height=30)
        
        ttk.Label(top, text="Precio:", font="{Segoe UI} 14 bold").place(x=20, y=60, width=105 ,height=25)
        entry_precio = ttk.Entry(top, font="{Segoe UI} 14 bold")
        entry_precio.place(x=130, y=60, width=240, height=30)
        
        ttk.Label(top, text="Costo:", font="{Segoe UI} 14 bold").place(x=20, y=100, width=105 ,height=25)
        entry_costo = ttk.Entry(top, font="{Segoe UI} 14 bold")
        entry_costo.place(x=130, y=100, width=240, height=30)
        
        ttk.Label(top, text="Stock:", font="{Segoe UI} 14 bold").place(x=20, y=140, width=105 ,height=25)
        entry_stock = ttk.Entry(top, font="{Segoe UI} 14 bold")
        entry_stock.place(x=130, y=140, width=240, height=30)
        
        ttk.Label(top, text="Estado:", font="{Segoe UI} 14 bold").place(x=20, y=180, width=105 ,height=25)
        entry_estado = ttk.Entry(top, font="{Segoe UI} 14 bold")
        entry_estado.place(x=130, y=180, width=240, height=30)
        ttk.Label(top, text="Moneda:", font="{Segoe UI} 14 bold").place(x=20, y=220, width=105 ,height=25)
        entry_moneda = ttk.Combobox(top, font="{Segoe UI} 14 bold", values=["$", "€", "Bs"], state="readonly")
        entry_moneda.set("$")
        entry_moneda.place(x=130, y=220, width=240, height=30)

        
        self.frameimg = tk.Frame(top, bg="white", bd=2, relief="solid")
        self.frameimg.place(x=440, y=30, width=200, height=200)
        
        btnimage =tk.Button(top, text= "Cargar imagen", font="{Segoe UI} 14 bold", bg="#F2B04A", fg="black", cursor="hand2", command=self.load_image)
        btnimage.place(x=470, y=260, width=150, height=40)
        
        def guardar():
            articulo = entry_articulo.get()
            precio = entry_precio.get()
            costo = entry_costo.get()
            stock = entry_stock.get()
            estado = entry_estado.get()
            moneda = entry_moneda.get()
            if not articulo or not precio or not costo or not stock or not estado:
                messagebox.showerror("Error", "Todos los campos deben ser completados")
                return
            
            try:
                precio = float(precio)
                costo = float(costo)
                stock = int(stock)
            except ValueError:
                messagebox.showerror("Error", "precio, costo y stock deben ser numeros validos")
                return 
            
            if precio <= 0 or costo <= 0 or stock < 0:
                messagebox.showerror("Error", "El precio y costo deben ser mayores a cero. El stock no puede ser negativo.")
                return
            
            if hasattr(self, 'image_path'):
                image_path = self.image_path
            else:
                image_path = (r"fotos/default.png")
                
            try:
                self.cur.execute("INSERT INTO articulos (articulo, precio, costo, stock, estado, moneda, image_path) VALUES (?, ?, ?, ?, ?, ?, ?)",
                                (articulo, precio, costo, stock, estado, moneda, image_path))
                self.conn.commit()
                show_toast("Exito", "Articulo agregado correctamente")
                top.destroy()
                self.cargar_articulos()
                self.articulos_combobox() 
            except sqlite3.Error as e:
                messagebox.showerror("Error", "Error al agregar el articulo")
                return
                
        tk.Button(top, text="Guardar", font="{Segoe UI} 14 bold", bg="#F2B04A", fg="black", cursor="hand2", command=guardar).place(x=130, y=300, width=115, height=40)
        tk.Button(top, text="Cancelar", font="{Segoe UI} 14 bold", bg="#F2B04A", fg="black", cursor="hand2", command=top.destroy).place(x=255, y=300, width=115, height=40)
        
    def cargar_articulos(self, filtro= None, categoria= None):
        if hasattr(self, '_timer_cargar'):
            self.after_cancel(self._timer_cargar)
        self._timer_cargar = self.after(200, self._cargar_articulos, filtro, categoria)
        
    def _cargar_articulos(self, filtro= None, categoria= None):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
            
        query = "SELECT articulo, precio, moneda, image_path FROM articulos"
        params = []
        
        if filtro:
            query += " WHERE articulo LIKE ?"
            params.append(f'%{filtro}%')
            
        self.cur.execute(query, params)
        articulos = self.cur.fetchall()
        
        self.row = 0
        self.column = 0
        
        for articulo, precio, moneda, image_path in articulos:
            self.mostrar_articulo(articulo, precio, moneda, image_path)
            
        
    def mostrar_articulo(self, articulo, precio, moneda, image_path):
        app = self.winfo_toplevel()
        sx = getattr(app, '_scale_x', 1.0)
        img_size = int(120 * sx)
        font_size = max(10, int(13 * sx))
        wrap_len = int(140 * sx)
        
        article_frame = tk.Frame(self.scrollable_frame, bg="white", bd=2, relief="solid", width=int(160*sx), height=int(260*sx))
        article_frame.pack_propagate(False)
        article_frame.grid(row=self.row, column=self.column, padx=int(15*sx), pady=int(15*sx))
        
        if image_path and os.path.exists(image_path):
            image = Image.open(image_path)
            image = image.resize((img_size, img_size), Image.LANCZOS)
            imagen = ImageTk.PhotoImage(image)
            image_label = tk.Label(article_frame, image=imagen, bg="white")
            image_label.image = imagen
            image_label.pack(expand= True, fill="both")

        name_label = tk.Label(article_frame, text=articulo, anchor="w", wraplength=wrap_len, font=f"{{Segoe UI}} {font_size} bold", bg="white")
        name_label.pack(side="top", fill="x")
        
        precio_label = tk.Label(article_frame, text=f"precio: {precio:.2f} {moneda}", anchor="w", wraplength=wrap_len, font=f"{{Segoe UI}} {font_size} bold", bg="white")
        precio_label.pack(side="bottom", fill="x")
        
        self.column += 1
        canvas_w = 780 * sx
        item_w = int(195 * sx)
        max_cols = max(1, int(canvas_w / item_w)) - 1
        
        if self.column > max_cols:
            self.column = 0
            self.row += 1
    
    def on_combobox_select(self, event):
        self.actualizar_label()
        
    def actualizar_label(self, event=None):
        articulo_seleccionado = self.comboboxbuscar.get()
        
        try:
            self.cur.execute("SELECT articulo, precio, costo, stock, estado FROM articulos WHERE articulo = ?", (articulo_seleccionado,))
            resultado = self.cur.fetchone()
            
            if resultado is not None:
                articulo, precio, costo, stock, estado = resultado
                
                self.label1.config(text=f"Articulo:{articulo}")
                self.label2.config(text=f"Precio:{precio}")
                self.label3.config(text=f"Costo:{costo}")
                self.label4.config(text=f"Stock:{stock}")
                
                self.label5.config(text=f"Estado:{estado}")
                if estado.lower() == "activo":
                    self.label5.config(fg="green")
                elif estado.lower() == "inactivo":
                    self.label5.config(fg="red")
                else:
                    self.label5.config(fg="black")
            else:
                self.label1.config(text="Articulo: No encontrado")
                self.label2.config(text="Precio: N/A")
                self.label3.config(text="Costo: N/A")
                self.label4.config(text="Stock: N/A")
                self.label5.config(text="Estado: N/A")
                
        except sqlite3.Error as e:
            messagebox.showerror("Error", "Error al obtener los datos del articulo")
            return
        
    def filtrar_articulos(self, event):
        if self.timer_articulos:
            self.after_cancel(self.timer_articulos)
        self.timer_articulos = self.after(500, self._filter_articulos)
        
    def _filter_articulos(self):
        typed = self.comboboxbuscar.get()
        
        if typed == '':
            data = self.articulos
        else:
            data = [item for item in self.articulos if typed.lower() in item.lower()]
        
        if data:
            self.comboboxbuscar['values'] = data
            self.comboboxbuscar.event_generate('<Down>')
        else:
            self.comboboxbuscar['values'] = ['No se encontraron resultados']
            self.comboboxbuscar.event_generate('<Down>')
            
        self.cargar_articulos(filtro=typed)
        
    def editar_articulos(self):
        selected_item = self.comboboxbuscar.get()
        
        if not selected_item:
            messagebox.showerror("Error", "Selecciona un articulo para editar")
            return
        
        self.cur.execute("SELECT articulo, precio, costo, stock, estado, image_path FROM articulos WHERE articulo = ?", (selected_item,))
        resultado = self.cur.fetchone()
        
        if not resultado:
            messagebox.showerror("Error", "Articulo no encontrado")
            return
        
        top = tk.Toplevel(self)
        top.title("Editar Articulo")
        top.geometry("750x450+200+50")
        top.resizable(False, False)
        
        top.transient(self.master)
        top.grab_set()
        top.focus_set()
        top.lift()
        
        (articulo, precio, costo, stock, estado, image_path) = resultado
        
        ttk.Label(top, text="Articulo:", font="{Segoe UI} 14 bold").place(x=20, y=20, width=105, height=25)
        entry_articulo = ttk.Entry(top, font="{Segoe UI} 14 bold")
        entry_articulo.place(x=130, y=20, width=240, height=30)
        entry_articulo.insert(0, articulo)
        
        ttk.Label(top, text="Precio:", font="{Segoe UI} 14 bold").place(x=20, y=60, width=105, height=25)
        entry_precio = ttk.Entry(top, font="{Segoe UI} 14 bold")
        entry_precio.place(x=130, y=60, width=240, height=30)
        entry_precio.insert(0, precio)
        
        ttk.Label(top, text="Costo:", font="{Segoe UI} 14 bold").place(x=20, y=100, width=105, height=25)
        entry_costo = ttk.Entry(top, font="{Segoe UI} 14 bold")
        entry_costo.place(x=130, y=100, width=240, height=30)
        entry_costo.insert(0, costo)
        
        ttk.Label(top, text="Stock:", font="{Segoe UI} 14 bold").place(x=20, y=140, width=105, height=25)
        entry_stock = ttk.Entry(top, font="{Segoe UI} 14 bold")
        entry_stock.place(x=130, y=140, width=240, height=30)
        entry_stock.insert(0, stock)
        
        ttk.Label(top, text="Estado:", font="{Segoe UI} 14 bold").place(x=20, y=180, width=105, height=25)
        entry_estado = ttk.Entry(top, font="{Segoe UI} 14 bold")
        entry_estado.place(x=130, y=180, width=240, height=30)
        entry_estado.insert(0, estado)
        
        ttk.Label(top, text="Moneda:", font="{Segoe UI} 14 bold").place(x=20, y=220, width=105, height=25)
        entry_moneda = ttk.Combobox(top, font="{Segoe UI} 14 bold", values=["$", "€", "Bs"], state="readonly")
        try:
            self.cur.execute("SELECT moneda FROM articulos WHERE articulo = ?", (selected_item,))
            row = self.cur.fetchone()
            if row and row[0]:
                entry_moneda.set(row[0])
            else:
                entry_moneda.set("$")
        except:
            entry_moneda.set("$")
        entry_moneda.place(x=130, y=220, width=240, height=30)
        
        self.frameimg = tk.Frame(top, bg="white", bd=2, relief="solid")
        self.frameimg.place(x=440, y=30, width=200, height=200)
        
        if image_path and os.path.exists(image_path):
            image = Image.open(image_path)
            image = image.resize((200, 200), Image.LANCZOS)
            self.product_image = ImageTk.PhotoImage(image)
            self.image_path = image_path
            image_label = ttk.Label(self.frameimg, image=self.product_image)
            image_label.pack(expand=True, fill="both")
            
        btnimagen = tk.Button(top, text="Cargar imagen", font="{Segoe UI} 14 bold", bg="#F2B04A", fg="black", cursor="hand2", command=self.load_image)
        btnimagen.place(x=470, y=260, width=150, height=40)
        
        def guardar():
            nuevo_articulo = entry_articulo.get()
            precio = entry_precio.get()
            costo = entry_costo.get()
            stock = entry_stock.get()
            estado = entry_estado.get()
            moneda = entry_moneda.get()
            
            if not nuevo_articulo or not precio or not costo or not stock or not estado:
                messagebox.showerror("Error", "Todos los campos deben ser completados")
                return 
            
            try:
                precio = float(precio)
                costo = float(costo)
                stock = int(stock)
            except ValueError:
                messagebox.showerror("Error", "Precio, costo y stock deben ser numeros validos")     
                return
                
            if precio <= 0 or costo <= 0 or stock < 0:
                messagebox.showerror("Error", "El precio y costo deben ser mayores a cero. El stock no puede ser negativo.")
                return
                
            if hasattr(self, 'image_path'):
                image_path = self.image_path
            else:
                image_path = (r"fotos/default.png")
                
            self.cur.execute("UPDATE articulos SET articulo = ?, precio = ?, costo = ?, stock = ?, estado = ?, moneda = ?, image_path = ? WHERE articulo = ?",
                            (nuevo_articulo, precio, costo, stock, estado, moneda, image_path, selected_item)) 
            self.conn.commit()
            
            self.articulos_combobox()
            
            self.after(0, lambda: self.cargar_articulos(filtro=nuevo_articulo))
            
            top.destroy()
            show_toast("Exito", "Articulo editado exitosamente")
            
        btn_guardar = tk.Button(top, text="Guardar", font="{Segoe UI} 14 bold", bg="#F2B04A", fg="black", cursor="hand2", command=guardar)
        btn_guardar.place(x=130, y=300, width=115, height=40)
        
        btn_cancelar = tk.Button(top, text="Cancelar", font="{Segoe UI} 14 bold", bg="#F2B04A", fg="black", cursor="hand2", command=top.destroy)
        btn_cancelar.place(x=255, y=300, width=115, height=40)

    def eliminar_articulo(self):
        selected_item = self.comboboxbuscar.get()
    
        if not selected_item:
            messagebox.showerror("Error", "Selecciona un articulo para eliminar")
            return
    
        respuesta = messagebox.askyesno("Confirmar", f"¿Estás seguro de que deseas eliminar el artículo '{selected_item}'?")
        if respuesta:
            try:
                self.cur.execute("DELETE FROM articulos WHERE articulo = ?", (selected_item,))
                self.conn.commit()
                show_toast("Exito", "Articulo eliminado correctamente")
                self.cargar_articulos()
                self.articulos_combobox()
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Error al eliminar el articulo: {e}")
                return 