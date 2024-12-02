import PySimpleGUI as sg


class TelaAnimal:

    def __init__(self) -> None:
        self.__window = None
        sg.ChangeLookAndFeel('DarkGreen2')

    def tela_opcoes(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Animais',size=(20,1), font=titulo)],
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
    
    def decide_tipo_animal(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Escolha o tipo:',size=(20,1), font=titulo)],
            [
                sg.Button('Gato', size=20, font=botao_font),
                sg.Button('Cachorro', size=20, font=botao_font)
            ]
        ]
        self.__window = sg.Window('Sistema da ONG', default_element_size=(200,1)).Layout(layout)
        
        retorno, values = self.open()
        dicionario = {
            'Gato' : 1,
            'Cachorro' : 2
        }
        self.close()
        return dicionario[retorno]

    def mostra_animal_especifico(self, dados_animal):
        print('NOME DO ANIMAL:', dados_animal['nome'])
        print('NÚMERO DO ANIMAL:', dados_animal['numero'])
        print('ESPECIE DO ANIMAL:', dados_animal['especie'])

    def decide_mostra_tipo(self):
        print('\n-------- TIPO ANIMAL ----------')
        print('Temos as seguintes listas:')
        print('1 - Gato')
        print('2 - Cachorro')
        print('3 - Todos')
        opcao = int(input('Escolha a opção: '))
        return opcao
    
    def seleciona_animal(self):
        cpf = int(input('\nCPF do animal para selecionar: '))
        return cpf

    def mostra_mensagem(self, mensagem: str, titulo='Mensagem'):
        sg.Popup(titulo, mensagem)

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()
