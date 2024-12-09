from datetime import date as Date
import PySimpleGUI as sg


class TelaVacinacao:

    def __init__(self) -> None:
        self.__window = None

    def tela_opcoes(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Vacinação',size=(20,1), font=titulo)],
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
    
    def pega_dados_vacinacao(self):
        print('\n-------- DADOS VACINAÇÃO ----------')
        raw_data_nasc = input('Data da Vacinação (Formato dd/mm/yyyy): ').split('/')
        data_dict = {'day': int(raw_data_nasc[0]),
                     'month': int(raw_data_nasc[1]),
                     'year': int(raw_data_nasc[2])}
        data = Date(**data_dict)
        print('Vacina 1: Raiva')
        print('Vacina 2: Leptospirose')
        print('Vacina 3: Hepatite Infecciosa')
        vacina = int(input('Escolha uma vacina: '))
        return {'data': data, 'vacina': vacina}
    
    def mostra_vacinacao(self, dados_vacinacao):
        mapa_vacinas = {
            1: 'Raiva',
            2: 'Leptospirose',
            3: 'Hepatite Infecciosa'
        }
        print('\nDATA DA VACINAÇÃO: ', dados_vacinacao['data'])
        print('NOME DA VACINA: ', mapa_vacinas[dados_vacinacao['vacina']])

    def seleciona_vacinacao(self):
        numero = int(input('\nNúmero da vacinação para selecionar: '))
        return numero

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

    def mostra_mensagem(self, mensagem: str, titulo='Mensagem'):
        sg.Popup(titulo, mensagem)

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()