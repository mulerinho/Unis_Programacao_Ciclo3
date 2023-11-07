from tkinter import *


class App:
    # Definindo tamanho da janela
    def __init__(self):
        self.window = Tk()
        self.window.title('Calculadora IMC')

        self.window.minsize(width=400, height=400)
        self.window.maxsize(400, 400)
        self.window.configure(background='light gray')
        campo_altura = Label( font=('arial',20, 'bold'), text='Altura')
        campo_altura.pack()
        self.screen_altura = Entry(self.window, font='arial 20 bold', bg='light blue',  width=9)
        self.screen_altura.pack()
        campo_peso = Label(font=('arial', 20, 'bold'), text='Peso')
        campo_peso.pack()
        self.screen_peso = Entry(self.window, font='arial 20 bold', bg='light blue',  width=9)
        self.screen_peso.pack()

        campo_resposta = Label(font=('arial', 20, 'bold'),  text='Seu IMC:')
        campo_resposta.pack()
        self.screen_imc = Entry(self.window, font='arial 20 bold', bg='light blue', width=9)
        self.screen_imc.pack()
        # Entrada de dados


        self.frame = Frame(self.window)
        self.frame.pack()


        self.button_imc = Button(self.frame, bg='light green', text='IMC', font='arial 20 bold', command=self.total)
        self.button_imc.grid(row=0, column=3)

        self.window.mainloop()


# Criando as funcionalidades



    def total(self):
        alt = self.screen_altura.get()
        convert_alt = float(alt)
        self.screen_altura.delete(0,END)
        pes = self.screen_peso.get()
        convert_pes = float(pes)
        self.screen_peso.delete(0,END)
        total = convert_pes / (convert_alt * convert_alt)
        str_convert = str(total)
        size = len(str_convert)
        final_str = str_convert[: size - 14]
        print(final_str)
        self.screen_imc.insert(0,final_str)
        print('Fim')








executando = App()
