import PySimpleGUI as sg


class TelaSistema:

    def __init__(self) -> None:
        self.__window = None

    def tela_opcoes(self):
        self.init_components()
        button, opcao = self.open()
        # print('\n-------- Sistema para ONG de adoção de animais ---------')
        # print('1 - Animais')
        # print('2 - Pessoas')
        # print('3 - Adoções')
        # print('4 - Doações')
        # print('5 - Habitações')
        # print('6 - Vacinações')
        # print('0 - Finalizar sistema')
        # opcao = int(input('Escolha a opção: '))
        return opcao

    def init_components(self):
        sg.ChangeLookAndFeel('DarkGreen2')
        layout = [
            [sg.Text('Um texto')]
        ]
        self.__window = sg.Window('Sistema da ONG', default_element_size=(40,1)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
