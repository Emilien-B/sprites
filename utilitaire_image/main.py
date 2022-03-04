
from PIL import Image, ImageTk
from tkinter import E, HORIZONTAL, filedialog
import tkinter as tk
import time 

def main():
    window = tk.Tk()
    window.title("Utilitaire d'image Galaxia")
    width = 500
    height = 250
    window.geometry(str(width)+"x"+str(height))
    window.minsize(width,height)
    window.maxsize(width,height)
    # logo = ImageTk.PhotoImage(Image.open("logo_thingz.png"))
    image = Image.new('1',(1,1))

    def change_log(a):
        log.configure(text=a)
        
    def calc_size(a):
        global img
        if img.width < img.height:
            width = a
            height = round(int(a)*(img.width/img.height))
        else:
            height = a
            width = round(int(a)*(img.width/img.height))
        res = str(width)+"x"+str(height)
        size.configure(text=res)
    
        return {'width':width,'height':height}



    def file():
        global img
        path = filedialog.askopenfilename(initialdir = "/",title = "Sélectionner une image",filetypes = (("png files","*.png"),("jpg files","*.jpg"),("jpeg files","*.jpeg"),("gif files","*.gif"),("all files","*.*"),))

        name = path.split("/")[len(path.split("/"))-1].split(".")[0]

        img = Image.open(path)
        change_log("Traitement de l'image...")
        try:
            r, g, b, a  = img.split()
        except:
            r, g, b  = img.split()

        img = Image.merge("RGB", (r, g, b))
        global img_original
        img_original = img.quantize(255)
        change_log("Séléctionnez la taille de l'image voulue (l'écran mesure 128 par 160 pixels).")


        button.pack_forget()
        log.pack_forget()

        slider = tk.Scale(window, from_=7, to=min(img.width, img.height), orient=HORIZONTAL, showvalue=0, command=calc_size, length=200)
        slider.pack()
        calc_size(slider.get())
        
        
        def save_image():
            global img
            img = img_original.resize((calc_size(slider.get())['width'],calc_size(slider.get())['height']))
            
            def change_path(a):
                path = filedialog.asksaveasfilename(initialdir = "",title = a)
                if not path.endswith('.bmp'):
                    path = path+'.bmp'
                img.save(path)

            try:
                img.save('/Volumes/GALAXIA/'+name+'.bmp')
                change_log('Image sauvegardée dans la Galaxia !')
            except FileNotFoundError:
                change_path("""La Galaxia n'est pas connectée, choissez un emplacement sur votre ordinateur.""")
            except OSError:
                change_path("""La Galaxia est pleine, choissez un emplacement sur votre ordinateur.""")

        def reload():
            size.pack_forget()
            slider.pack_forget()
            valider.pack_forget()
            quit.pack_forget()
            log.pack_forget()
            button.pack_forget()
            button.pack()
            log.pack()
            size.configure(text="")
            size.pack()
            change_log("Sélectionner une image pour commencer")


        valider = tk.Button(window,text="Sauvegarder l'image",command=save_image)
        valider.pack()
        log.pack()
        quit = tk.Button(window,text="Sélectionner une nouvelle image",command=reload)
        quit.pack()
        


    # tk.Label(window, image=logo).pack()
    tk.Label(window, font=("Arial",12,"bold"), text="""
    Sélectionnez une image pour que ses couleurs soient indexées, 
    qu'elle soit redimensionnée, reformatée et sauvegardée 
    dans la Galaxia (/Volumes/GALAXIA).
    """).pack()

    button = tk.Button(window, text="Sélectionner une image", command=file)
    button.pack()
    log = tk.Label(window, text="Sélectionner une image pour commencer")
    log.pack()
    size = tk.Label(window, text="")
    size.pack()




    """
    file = input().strip()
    img = Image.open(file)
    r, g, b, a = img.split()
    img = Image.merge("RGB", (r, g, b))
    img = img.resize((70,60))
    img = img.quantize(255)
    name = input('Name...')
    img.save("/Volumes/GALAXIA/"+name+'.bmp')"""

    window.mainloop()

if __name__=="__main__":
    main()