import tkinter as tk
from PIL import ImageTk, Image

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        

        # load the image
        bg = ImageTk.PhotoImage(file="tricolor.png")

        # Create a Canvas
        canvas = tk.Canvas(self, width=700, height=3500, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        # Add Image inside the Canvas
        canvas.create_image(0, 0, image=bg, anchor='nw')
        img= ImageTk.PhotoImage(Image.open("emblem3.png"))
        canvas.create_image(580,100,anchor='nw',image=img)
        
        
        # Function to resize the window
        def resize_image(e):
            global image, resized, image2, img, img2, namaste_img
            # open image to resize it
            image = Image.open("tricolor.png")
            #Load an image in the script
            img= ImageTk.PhotoImage(Image.open("emblem3.png"))
            img2 = ImageTk.PhotoImage(Image.open("chakra1.png"))
            namaste_img = ImageTk.PhotoImage(Image.open('namaste_2.png'))

            #Add image to the Canvas Items
            # resize the image with width and height of self
            resized = image.resize((e.width, e.height), Image.LANCZOS)
            image2 = ImageTk.PhotoImage(resized)
            canvas.create_image(0, 0, image=image2, anchor='nw')
            canvas.create_image(620,70,anchor='nw',image=img)
            canvas.create_image(640,360,anchor='nw',image=img2)
            
            a = canvas.create_text(765,490,text="",font=("Times New Roman", 44, 'bold'))
            our_text="NATIONAL EDUCATION POLICY"
            delta=300
            delay=0
            for x in range(len(our_text)+1):
                s=our_text[:x]
                new_text=lambda s=s:canvas.itemconfigure(a, text=s)
                canvas.after(delay,new_text)
                delay +=delta
            
            button = tk.Button(self, image=namaste_img,command=lambda: controller.show_frame("PageOne"), borderwidth=0, bg='#04a91f', activebackground="#04a91f")
            button.place(x=1290, y=750)
          
        # Bind the function to configure the parent window
        self.bind("<Configure>", resize_image)
        
        # create a label to display the image
        label = tk.Label(self, image=bg)
        label.pack()
        
