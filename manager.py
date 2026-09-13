import tkinter as tk
from tkinter import *
from tkinter import ttk
from login_window import Login, Registro, Inicio, Cliente, RegistroCliente
from container import Container
from container_clientes import Container_clientes
import os 
import ctypes

try:
    font_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Cocogoose-Pro-Bold-trial.ttf")
    ctypes.windll.gdi32.AddFontResourceExW(font_path, 0x10, 0)
except Exception:
    pass


class Manager(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("SuperMarket")
        try:
            icon = tk.PhotoImage(file="imagenes1/carrito-de-supermercado.png")
            self.iconphoto(True, icon)
        except Exception:
            pass
        self.state("zoomed")
        self.resizable(False, False)
        self.minsize(1100, 650)
        
        self.current_user = None
        self.current_client = None

        self._scale_active = True
        self._scale_x = 1.0
        self._scale_y = 1.0
        self.bind('<Configure>', self.on_resize)
        
        # Make the container fill the whole screen so it triggers resizes on its children
        container = tk.Frame(self, bg="white")
        container.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.main_container = container

        self.frames = {}
        for i in (Inicio, Login, Registro, Cliente, Container, RegistroCliente, Container_clientes ):
            frame = i(container, self)
            self.frames[i] = frame

        self.show_frame(Inicio)

        
        

    def on_resize(self, event):
        if event.widget == self:
            if event.width == 1100 and event.height == 650:
                self._scale_x = 1.0
                self._scale_y = 1.0
            else:
                self._scale_x = event.width / 1100.0
                self._scale_y = event.height / 650.0
            
            def refresh(w):
                if hasattr(w, '_orig_place_kw'):
                    w.place(**w._orig_place_kw)
                
                if hasattr(w, '_orig_img'):
                    from PIL import Image, ImageTk
                    new_w = int(1100 * self._scale_x)
                    new_h = int(650 * self._scale_y)
                    if new_w > 0 and new_h > 0:
                        try:
                            # Use LANCZOS or nearest depending on PIL version, we just use default or LANCZOS
                            resized = w._orig_img.resize((new_w, new_h), Image.LANCZOS)
                            w.image = ImageTk.PhotoImage(resized)
                            w.configure(image=w.image)
                        except Exception:
                            pass
                
                for child in w.winfo_children():
                    refresh(child)
            
            refresh(self.main_container)
            
            # Recargar la grilla del inventario si está inicializado
            try:
                from inventario import Inventario
                if Inventario in self.frames:
                    self.frames[Inventario].cargar_articulos()
            except Exception:
                pass

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

    def logout(self):
        self.current_user = None
        self.current_client = None
        
        try:
            self.frames[Login].username.delete(0, 'end')
            self.frames[Login].password.delete(0, 'end')
        except Exception:
            pass
            
        try:
            self.frames[Cliente].idusercedula.delete(0, 'end')
        except Exception:
            pass
            
        self.show_frame(Inicio)
