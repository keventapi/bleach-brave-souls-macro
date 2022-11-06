import tkinter as tk
import main

class Main():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("bleach macro")
        self.window.geometry("400x540")
        self.frame = tk.Frame(self.window)
        self.elements = {}
        self.config = {}

    def label_and_check(self, element_name, label, index, kind):
        self.elements[element_name] = tk.Radiobutton(self.window, text=label, value=label, variable=kind,
                                                     command=lambda: self.radio_get(kind, element_name), tristatevalue=0)
        self.elements[element_name].pack()

    def create_elements(self, text, kind):
        for i in range(len(text)):
            self.label_and_check(text[i].replace(' ', '_'), text[i], 0, kind)

    def radio_get(self, key, value, start=False):
        self.config[key] = value
        try:
            if start:
                main.init(self.config)
        except:
            print('use a integer')

    def create_screen(self):
        head1 = tk.Label(self.window, text="bleach brave souls macros: \n")
        head1.pack()
        self.create_elements(['evento de pontos', 'chronicle quest', 'friend coin'], "macro")
        head2 = tk.Label(self.window, text="o que fazer quando acabar com os tickets: \n")
        head2.pack()
        self.create_elements(['comprar', 'pegar da giftbox', 'nada'], "tickets")
        repeticao = tk.Label(self.window, text='repetições:')
        repeticao.pack()
        quantidade = tk.Entry(self.window)
        quantidade.pack()
        iniciar = tk.Button(text="iniciar", command=lambda: self.radio_get('vezes', quantidade.get(), True))
        iniciar.pack()
        self.window.mainloop()


app = Main()
app.create_screen()
