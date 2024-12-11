import PySimpleGUI as sg


class TelaAnimal:

    def __init__(self) -> None:
        self.__window = None

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

    def mostra_todos_animais(self, lista, selecionar=False):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [[sg.Text('Animais cadastrados',size=(20,1), font=titulo)]]
        if selecionar:
            for animal in lista:
                layout.append(self.mostra_animal(animal))
                layout.append([sg.Button(f'Selecionar {animal['numero_chip']}')])
                layout.append([sg.Text('-------------------------------------------')])
        else:
            for animal in lista:
                layout.append(self.mostra_animal(animal))
                layout.append([sg.Text('-------------------------------------------')])
        self.__window = sg.Window('Sistema da ONG', default_element_size=(200,1)).Layout(layout)
        retorno, values = self.open()
        if selecionar:
            retorno = int(retorno[11::])
        self.close()
        return retorno

    def mostra_animal(self, dados_animal):
        animal_layout = [
            [sg.Text(f'Nome: {dados_animal['nome']}')],
            [sg.Text(f'Espécie: {dados_animal['especie']}')],
            [sg.Text(f'Número: {dados_animal['numero_chip']}')]
        ]
        return animal_layout

    def mostra_mensagem(self, mensagem: str, titulo='Mensagem'):
        sg.Popup(titulo, mensagem)

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()
