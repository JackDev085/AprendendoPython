import numpy as np

#Com a função np.empty() podemos gerar um array com números em notação científica,
#representando algo muito próximo de zero, porém não zero absoluto
data = np.empty((3,4))
print(data)
'''
[[2.12199579e-314 0.00000000e+000 2.12199579e-314 1.03721032e-309]
 [8.34402697e-308 0.00000000e+000 0.00000000e+000 0.00000000e+000]
 [7.56575361e-307 1.37962388e-306 4.66839075e-313 1.11253693e-308]]
'''