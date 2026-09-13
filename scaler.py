from tkinter import ttk
import tkinter as tk

_orig_place = tk.Widget.place

def hooked_place(self, cnf={}, **kw):
    kwargs = cnf.copy()
    kwargs.update(kw)
    if not hasattr(self, '_orig_place_kw'):
        self._orig_place_kw = kwargs.copy()
    
    app = self.winfo_toplevel()
    if getattr(app, '_scale_active', False):
        sx = getattr(app, '_scale_x', 1.0)
        sy = getattr(app, '_scale_y', 1.0)
        new_kw = {}
        for k, v in kwargs.items():
            if k in ('x', 'width'):
                new_kw[k] = int(float(v) * sx)
            elif k in ('y', 'height'):
                new_kw[k] = int(float(v) * sy)
            else:
                new_kw[k] = v
                
        try:
            font = self.cget('font')
            if font and not hasattr(self, '_orig_font'):
                self._orig_font = font
            orig_font = getattr(self, '_orig_font', None)
            if orig_font:
                import re
                m = re.match(r'^(.*?)\s+(\d+)(.*)$', str(orig_font))
                if m:
                    new_size = max(8, int(int(m.group(2)) * min(sx, sy)))
                    self.configure(font=f"{m.group(1)} {new_size}{m.group(3)}")
        except Exception:
            pass
        _orig_place(self, **new_kw)
    else:
        _orig_place(self, **kwargs)

tk.Widget.place = hooked_place

