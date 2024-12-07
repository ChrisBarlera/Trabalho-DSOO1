import PySimpleGUI as sg
from datetime import date as Date


class TelaAdotante:

    def __init__(self) -> None:
        self.__window = None

    def tela_opcoes(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Adotante',size=(20,1), font=titulo)],
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

    
    def pega_dados_adotante(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Insira os dados',size=(20,1), font=titulo)],
            [sg.Text('CPF', size=20, font=botao_font),
             sg.Input('Ex.: 12345678902', size=20, font=('Helvetica', 15), key='cpf')],
            [sg.Text('Nome', size=20, font=botao_font),
             sg.Input('Ex.: Fulaninho', size=20, font=('Helvetica', 15), key='nome')],
            [sg.Text('Data de Nascimento (Formato dd/mm/yyyy)', size=20, font=botao_font),
             sg.Input('Ex.: 13/12/2024', size=20, font=('Helvetica', 15), key='data_nasc')],
            [sg.Text('Endereço completo', size=20, font=botao_font),
             sg.Input('Ex.: Rua Fulano de tal', size=20, font=('Helvetica', 15), key='endereco')],
            [sg.Checkbox(text='Já possui animal?',size=20, font=botao_font, key='possui_animais')],
            [sg.Ok(size=20, font=botao_font)]
        ]
        self.__window = sg.Window('Sistema da ONG', default_element_size=(200,1)).Layout(layout)
        button, values = self.open()
        try:
            values['cpf'] = int(values['cpf'])
            raw_data_nasc = values['data_nasc'].split('/')
            data_dict = {'day': int(raw_data_nasc[0]),
                     'month': int(raw_data_nasc[1]),
                     'year': int(raw_data_nasc[2])}
            values['data_nasc'] = Date(**data_dict)
        except:
            self.mostra_mensagem('Preenchimento inválido dos dados!')
            self.close()
            self.pega_dados_adotante()
        self.close()
        return values

    def mostra_todos_adotantes(self, lista, selecionar=False):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [[sg.Text('Adotantes cadastrados',size=(20,1), font=titulo)]]
        if selecionar:
            for adotante in lista:
                layout.append(self.mostra_adotante(adotante))
                layout.append([sg.Button(f'Selecionar {adotante['cpf']}')])
                layout.append([sg.Text('-------------------------------------------')])
        else:
            for adotante in lista:
                layout.append(self.mostra_adotante(adotante))
                layout.append([sg.Text('-------------------------------------------')])
        self.__window = sg.Window('Sistema da ONG', default_element_size=(200,1)).Layout(layout)
        retorno, values = self.open()
        if selecionar:
            retorno = int(retorno[11::])
        self.close()
        return retorno
    
    def mostra_adotante(self, dados_adotante):
        adotante_layout = [
            [sg.Text(f'CPF: {dados_adotante['cpf']}')],
            [sg.Text(f'Nome: {dados_adotante['nome']}')],
            [sg.Text(f'Data de Nascimento: {dados_adotante['data_nasc']}')],
            [sg.Text(f'Endereço: {dados_adotante['endereco']}')],
            [sg.Text(f'Número habitação: {dados_adotante['habitacao'].numero}')],
            [sg.Text(f'Já possui animais? {dados_adotante['possui_animais']}')]
        ]
        return adotante_layout
    
    def habitacao_ja_cadastrada(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Habitação já cadastrada?',size=(20,1), font=titulo)],
            [
                sg.Button('Sim', size=20, font=botao_font),
                sg.Button('Não', size=20, font=botao_font)
            ],
            [sg.Button('Retornar', size=20, font=botao_font)]
        ]
        self.__window = sg.Window('Sistema da ONG', default_element_size=(200,1)).Layout(layout)
        
        retorno, values = self.open()
        dicionario = {
            'Sim' : 1,
            'Não' : 0
        }
        self.close()
        return dicionario[retorno]
    
    def tbm_trocar_habitacao(self):
        titulo = ('Helvetica', 30)
        botao_font = ('Helvetica', 20)
        layout = [
            [sg.Text('Também trocar habitação?',size=(20,1), font=titulo)],
            [
                sg.Button('Sim', size=20, font=botao_font),
                sg.Button('Não', size=20, font=botao_font)
            ]
        ]
        self.__window = sg.Window('Sistema da ONG', default_element_size=(200,1)).Layout(layout)
        
        retorno, values = self.open()
        dicionario = {
            'Sim' : 1,
            'Não' : 0
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