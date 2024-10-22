from datetime import date as Date
from entidade.Cachorro import Cachorro, Tamanho_Cachorro
from entidade.Gato import Gato
from controle.Controlador_Sistema import Controlador_Sistema
from entidade.Vacinacao import Vacina

data_vac = Date(2024,12,1)

gatin = Gato(123, 'Gatin', 'siames')
doguin = Cachorro(12,'opa','labrador', Tamanho_Cachorro.GRANDE)

doguin.vacinar(data_vac, Vacina.HEPATITE_INFECCIOSA)

print(doguin.vacinacoes[0])