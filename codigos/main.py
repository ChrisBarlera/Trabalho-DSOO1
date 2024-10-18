from datetime import date as Date
from Animal import Animal
from Gato import Gato
from Cachorro import Cachorro

data_vac = Date(2024,12,1)

gatin = Gato(123, 'Gatin', 'siames')
doguin = Cachorro(12,'opa','labrador','grande')

doguin.vacinar(data_vac,'lepra')

print(doguin.vacinacoes[0].animal.nome)