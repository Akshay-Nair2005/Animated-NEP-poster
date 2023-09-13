import tkinter as tk                
from tkinter import font as tkfont  
from homepage import StartPage
from poster import PageOne

class SampleApp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("National Education Policy")
        self.wm_attributes('-fullscreen',True)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (StartPage, PageOne):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


# ------------------------------------------------------------------------------

root     = tk.Tk()
img_file = "splash.gif"
image    = tk.PhotoImage(file=img_file)
w,h      = image.width(), image.height()

screen_width  = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width  / 2) - (w / 2)
y = (screen_height / 2) - (h / 2)

root.overrideredirect(True)
root.geometry(f'{w}x{h}+{int(x)}+{int(y)}')

canvas = tk.Canvas(root, highlightthickness=0)
canvas.create_image(0,0, image=image, anchor='nw')
canvas.pack(expand=1,fill='both')

root.after(2000, root.destroy)

root.mainloop()

# ------------------------------------------------------------------------------


app = SampleApp()
app.mainloop()