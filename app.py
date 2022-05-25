from tkinter import *
from tkinter import filedialog
from  detection import detectionImage
from PIL import Image, ImageTk


def BrowseImage():
    global img
    image_path = filedialog.askopenfilename(initialdir = "/",
                                          title = "Selecciona una imagen",
                                         filetypes=[('PNG Files','*.png'),('Jpg Files', '*.jpg')])
    
    if len(image_path)>0:
        label_file_explorer.configure(text="ruta del archivo "+image_path)
        detectionImage(image_path)
        img = ImageTk.PhotoImage(file="images/output.png")
        b2 = Button(root,image=img) 
        b2.grid(column = 0,row = 3, columnspan = 2, sticky = W+E+N+S, padx = 5, pady = 5)
    else:
        label_file_explorer.configure(text="No seleccionaste ningún archivo")



root = Tk()
root.title("Detención de rostros con OpenCV")


label_file_explorer = Label(root,
                            text = "Abrir imagen",
                            width = 100, height = 4,
                            fg = "blue")
  
      
button_explore = Button(root,
                        text = "Buscar archivo",
                        command = lambda : BrowseImage())
  
button_exit = Button(root,
                     text = "salir",
                     command = exit)



label_file_explorer.grid(column = 0, row = 1, columnspan = 2)
  
button_explore.grid(column = 0, row = 2, columnspan = 2, sticky = W+E, ipady=5)
  


button_exit.grid(column = 1,row = 4, columnspan = 2)



root.mainloop()

