import PySimpleGUI as sg
from datetime import date as Date


class TelaPessoa:
    def __init__(self) -> None:
        self.__window = None

    def tela_opcoes(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Pessoas',size=(20,1), font=titulo)],
            [
                sg.Button('Incluir', size=20, font=botao_font),
                sg.Button('Alterar', size=20, font=botao_font),
                sg.Button('Listar', size=20, font=botao_font),
                sg.Button('Excluir', size=20, font=botao_font)
            ],
            [sg.Button('Retornar', size=20, font=botao_font)]
        ]
        self.__window = sg.Window('Sistema da ONG', default_element_size=(200,1)).Layout(layout)
        
        retorno, values = self.open()
        dicionario = {
            'Incluir' : 1,
            'Alterar' : 2,
            'Listar' : 3,
            'Excluir' : 4,
            'Retornar' : 0
        }
        self.close()
        return dicionario[retorno]

    def decide_tipo_pessoa(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Escolha o tipo:',size=(20,1), font=titulo)],
            [
                sg.Button('Doador', size=20, font=botao_font),
                sg.Button('Adotante', size=20, font=botao_font)
            ]
        ]
        self.__window = sg.Window('Sistema da ONG', default_element_size=(200,1)).Layout(layout)
        
        retorno, values = self.open()
        dicionario = {
            'Doador' : 1,
            'Adotante' : 2
        }
        self.close()
        return dicionario[retorno]

    def decide_mostra_tipo(self):
        print('\n-------- TIPO PESSOA ----------')
        print('Temos as seguintes listas:')
        print('1 - Doador')
        print('2 - Adotante')
        print('3 - Todos')

        opcao = int(input('Escolha a opção: '))
        return opcao

    def mostra_mensagem(self, mensagem: str, titulo='Mensagem'):
        sg.Popup(titulo, mensagem)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
