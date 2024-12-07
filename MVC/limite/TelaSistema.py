import PySimpleGUI as sg


class TelaSistema:

    def __init__(self) -> None:
        self.__window = None
        sg.ChangeLookAndFeel('DarkGreen2')

    def tela_opcoes(self):
        self.init_components()
        retorno, values = self.open()
        dicionario = {
            'Animais' : 1,
            'Pessoas' : 2,
            'Adoções' : 3,
            'Doações' : 4,
            'Habitações' : 5,
            'Vacinações' : 6
        }
        self.close()
        return dicionario[retorno]

    def init_components(self):

        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Escolha seu menu:',size=(20,1), font=titulo)],
            [
                sg.Button('Animais', size=20, font=botao_font),
                sg.Button('Pessoas', size=20, font=botao_font),
                sg.Button('Adoções', size=20, font=botao_font)
            ],
            [
                sg.Button('Doações', size=20, font=botao_font),
                sg.Button('Habitações', size=20, font=botao_font),
                sg.Button('Vacinações', size=20, font=botao_font)
            ]
        ]
        self.__window = sg.Window('Sistema da ONG', default_element_size=(200,1)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
