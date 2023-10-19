

import numpy as np

data = np.array([3,6,9,12,15])

#Aqui estamos criando um array na memória local com a função np.save()
np.save("Minha_array", data)