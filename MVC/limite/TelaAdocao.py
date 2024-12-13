import PySimpleGUI as sg
from datetime import date as Date


class TelaAdocao:

    def __init__(self) -> None:
        self.__window = None

    def tela_opcoes(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Adoções',size=(20,1), font=titulo)],
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

    def mostra_todas_adocoes(self, lista, selecionar=False):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [[sg.Text('Adoções cadastradas',size=(20,1), font=titulo)]]
        if selecionar:
            for adocao in lista:
                layout.append(self.mostra_adocao(adocao))
                layout.append([sg.Button(f'Selecionar {adocao['numero_id']}')])
                layout.append([sg.Text('-------------------------------------------')])
        else:
            for adocao in lista:
                layout.append(self.mostra_adocao(adocao))
                layout.append([sg.Text('-------------------------------------------')])
        self.__window = sg.Window('Sistema da ONG', default_element_size=(200,1)).Layout(layout)
        retorno, values = self.open()
        if selecionar:
            retorno = int(retorno[11::])
        self.close()
        return retorno

    def pega_dados_adocao(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Insira os dados',size=(20,1), font=titulo)],
            [sg.Text('ID da adoção', size=20, font=botao_font),
             sg.Input('Ex.: 123', size=20, font=('Helvetica', 15), key='numero_id')],
            [sg.Text('Data de adoção (Formato dd/mm/yyyy)', size=20, font=botao_font),
             sg.Input('Ex.: 13/12/2024', size=20, font=('Helvetica', 15), key='data')],
            [sg.Ok(size=20, font=botao_font)]
        ]
        self.__window = sg.Window('Sistema da ONG', default_element_size=(200,1)).Layout(layout)
        button, values = self.open()
        try:
            values['numero_id'] = int(values['numero_id'])
            raw_data = values['data'].split('/')
            data_dict = {'day': int(raw_data[0]),
                     'month': int(raw_data[1]),
                     'year': int(raw_data[2])}
            values['data'] = Date(**data_dict)
        except:
            self.mostra_mensagem('Preenchimento inválido dos dados!')
            self.close()
            self.pega_dados_adocao()
        self.close()
        return values
    
    def mostra_adocao(self, dados_adocao):
        adocao_layout = [
            [sg.Text(f'ID da adoção: {dados_adocao['numero_id']}')],
            [sg.Text(f'Data: {dados_adocao['data']}')],
            [sg.Text(f'Animal: {dados_adocao['nome_animal']}')],
            [sg.Text(f'Adotante: {dados_adocao['nome_adotante']}')]
        ]
        return adocao_layout

    def ja_tem_adotante(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Adotante já cadastrado?',size=(20,1), font=titulo)],
            [
                sg.Button('Sim', size=20, font=botao_font),
                sg.Button('Não', size=20, font=botao_font)
            ]
        ]
        self.__window = sg.Window('Sistema da ONG', default_element_size=(200,1)).Layout(layout)
        
        retorno, values = self.open()
        dicionario = {
            'Sim' : True,
            'Não' : False
        }
        self.close()
        return dicionario[retorno]
    
    def ja_tem_animal(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Animal já cadastrado?',size=(20,1), font=titulo)],
            [
                sg.Button('Sim', size=20, font=botao_font),
                sg.Button('Não', size=20, font=botao_font)
            ]
        ]
        self.__window = sg.Window('Sistema da ONG', default_element_size=(200,1)).Layout(layout)
        
        retorno, values = self.open()
        dicionario = {
            'Sim' : True,
            'Não' : False
        }
        self.close()
        return dicionario[retorno]
    
    def tbm_trocar_adotante(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Também alterar adotante?',size=(20,1), font=titulo)],
            [
                sg.Button('Sim', size=20, font=botao_font),
                sg.Button('Não', size=20, font=botao_font)
            ]
        ]
        self.__window = sg.Window('Sistema da ONG', default_element_size=(200,1)).Layout(layout)
        
        retorno, values = self.open()
        dicionario = {
            'Sim' : True,
            'Não' : False
        }
        self.close()
        return dicionario[retorno]
    
    def tbm_trocar_animal(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Também alterar animal?',size=(20,1), font=titulo)],
            [
                sg.Button('Sim', size=20, font=botao_font),
                sg.Button('Não', size=20, font=botao_font)
            ]
        ]
        self.__window = sg.Window('Sistema da ONG', default_element_size=(200,1)).Layout(layout)
        
        retorno, values = self.open()
        dicionario = {
            'Sim' : True,
            'Não' : False
        }
        self.close()
        return dicionario[retorno]
    
    def mostra_mensagem(self, mensagem: str, titulo='Mensagem'):
        sg.Popup(titulo, mensagem)

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()