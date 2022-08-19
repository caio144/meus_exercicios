from tkinter import *
from turtle import color

window = Tk()
window.geometry("500x300")
window.title("Janelinha")
window.configure(background="purple")

texto=Label(
        window, 
        text="Olá Mundo!!!",
        font=(
            "Times New Roman", 18, "bold"
        ),
        background="purple"
    )

texto.place(
    x = 40,
    y = 40,
    width = 300,
    height= 30
)

entrada = Entry(
    window,
    font=(
    "Timens New Roman", 18 , "bold"
    ),
    background="purple"
)

entrada.place(
    x = 80,
    y = 80,
    width = 300,
    height= 30
)

botao = Button(
    window,
    text= "Clique Aqui"
)

botao.place(
    x= 125,
    y = 135,
    width="80",
    height="50",
)










window.mainloop()


