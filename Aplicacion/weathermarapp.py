#Andrea Llavel. Aplicacion Hackathon 2022.
#Agua de Mar como beneficio de la salud.¿Cuando se cosecha?Verificar el clima para navegar
import tkinter as tk    #tkinter es una libreria del lenguaje Python y funciona para la creacion 
#y el desarrollo de aplicaciones de escritorio.
from tkinter import *   #esta libreria facilita el posicionamiento y desarrollo de una interfaz graficacon Python.
import requests       #realiza solicitudes HTTP cuando se esta desarrollando el lado del servidor de una pagina web
import PIL.Image      #Es una libreria gratuita que permite la edicion de imagenes directamente desde Python.
import PIL.ImageTk    #Soporta una variedad de formatos: como GIF, JPG,JPEG y PNG
    
def mostrar_respuesta(clima):                    #Mostrar el clima
    try:
        nombre_ciudad  = clima["name"]
        desc = clima["weather"][0]["description"]
        temp = clima["main"]["temp"]
        
        ciudad["text"] = nombre_ciudad
        temperatura["text"] = str(int(temp)) + "°C"
        descripcion["text"] = desc
    except:
        ciudad["text"] = "Error"
#Openweathermap:es un servicio en linea que proporciona datos y pronosticos meteorologicos.        
def clima_JSON(ciudad):                        #Realizar un Json
    try:
        API_Key = "Deben loguearse en la pagina,asi se les otorga un API_key de usuario"                 #Obtener API_Key
        URL = "https://...."      #Loguearse en la pagina
        parametros = {"APPID": API_Key, "q": ciudad, "units": "metric","lang":"es"}
        response = requests.get(URL, params = parametros)            #respuesta desde el servidor
        clima=response.json()
        mostrar_respuesta(clima)
    except:
        print("Error")
      
        print(clima["name"])
        print(clima["weather"][0]["description"])
        print(clima["main"]["temp"])      
               
ventana = Tk()
ventana.geometry("1100x1200")            #Dar tamaño a la imagen de fondo
img_marcito1 = PIL.Image.open('marcito1.jpg')          #Insertar imagen
img_marcito1 = PIL.ImageTk.PhotoImage(img_marcito1)
lbl_marcito1 = tk.Label(image=img_marcito1)
lbl_marcito1.image = img_marcito1
lbl_marcito1.place(relx=0, rely=0, relheight=1, relwidth=1)

frm_componentes = tk.Frame(bg='white', bd=3)
frm_componentes.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.75, anchor='n')
#Colocar un boton para insertar ciudad
frm_componentes = tk.Button(text='BUSCAR CIUDAD', bg='black', fg='white',font=('Arial', 15))
frm_componentes.place(relx=0.3, rely=0.1, relheight=0.5, relwidth=0.3, anchor='e') 

frm_componentes = tk.Button(bg='black', fg='white',font=('Arial', 15))
frm_componentes.place(relx=0.3, rely=0.1, relheight=0.2, relwidth=0.5, anchor='sw')
#Presentacion de nuestro nombre de Equipo
frm_componentes = tk.Button(text='ENCRYPTED CODE',bg='black', fg='white',font=('Arial', 15))
frm_componentes.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.75, anchor='nw',)
#Tarea asignada por el profesor Osvaldo Giordanini
frm_componentes = tk.Button(text='HACKATHON 2022-CLIMA-SALUD',bg='black', fg='fuchsia',font=('Arial', 12))
frm_componentes.place(relx=0.4, rely=0.1, relheight=0.1, relwidth=0.85, anchor='sw',)
#Idea a mostrar
frm_componentes = tk.Button(text='BENEFICIOS PARA LA SALUD',bg='black', fg='fuchsia',font=('Arial', 9))
frm_componentes.place(relx=0.4, rely=0.1, relheight=0.1, relwidth=0.20, anchor='center',)

texto_ciudad = Entry(ventana, font = ("Arial", 20, "normal"),justify= "center")
texto_ciudad.pack(padx = 30, pady = 30)

obtener_clima = Button(ventana, text= "Verificar Clima para *Cosechar Agua de Mar*", font = ("Arial", 22, "normal"), command = lambda: clima_JSON(texto_ciudad.get()))
obtener_clima.pack()

ciudad = Label( font = ("Arial", 20, "normal"))
ciudad.pack(padx= 20, pady= 20)
temperatura = Label(font = ("Arial", 40, "normal"))
temperatura.pack(padx= 10, pady= 10)
descripcion = Label(font = ("Arial", 20, "normal"))
descripcion.pack(padx= 30, pady= 30)

ventana.mainloop()
