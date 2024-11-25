# import PySimpleGUI as sg 
 
# # Very basic window.  Return values as a dictionary 
 
# layout = [ 
#             [sg.Text('Please enter your Name, Address, Phone')], 
#             [sg.Text('Name', size=(15, 1)), sg.InputText('name', key='name')],
#             [sg.Text('Address', size=(15, 1)), sg.InputText('address', key='address')], 
#             [sg.Text('Phone', size=(15, 1)), sg.InputText('phone', key='phone')], 
#             [sg.Submit(), sg.Cancel()] 
#          ] 
 
# window = sg.Window('Simple data entry GUI').Layout(layout) 
 
# button, values = window.Read() 
 
# print(values['name'], values['address'], values['phone'])

class TelaGato:
    def tela_opcoes(self):
        print('\n-------- GATO ----------')
        print('1 - Incluir Gato')
        print('2 - Alterar Gato')
        print('3 - Listar Gatos')
        print('4 - Excluir Gato')
        print('0 - Retornar')
        
        opcao = int(input('Escolha a opção: '))
        return opcao
    
    def pega_dados_gato(self):
        print('\n-------- DADOS GATO ----------')
        numero_chip = int(input('Número do chip: '))
        nome = input('Nome: ')
        raca = input('Raça: ')

        return {'numero_chip': numero_chip, 'nome': nome, 'raca': raca}
    
    def mostra_gato(self, dados_gato):
        print('\nNUMERO DO GATO: ', dados_gato['numero_chip'])
        print('NOME DO GATO: ', dados_gato['nome'])
        print('RACA DO GATO: ', dados_gato['raca'])

    def seleciona_gato(self):
        numero = int(input('\nNúmero do gato para selecionar: '))
        return numero
    
    def mostra_mensagem(self, msg):
        print(msg)