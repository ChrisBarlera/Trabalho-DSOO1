from datetime import date as Date
from MVC.entidade.Cachorro import Cachorro, Tamanho_Cachorro
from MVC.entidade.Gato import Gato
from MVC.controle.Controlador_Sistema import Controlador_Sistema
from MVC.entidade.Vacinacao import Vacina

data_vac = Date(2024,12,1)

gatin = Gato(123, 'Gatin', 'siames')
doguin = Cachorro(12,'opa','labrador', Tamanho_Cachorro.GRANDE)

doguin.vacinar(data_vac, Vacina.HEPATITE_INFECCIOSA)

print(doguin.vacinacoes[0])