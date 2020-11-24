
from tabulate import tabulate

import matplotlib.pyplot as plt


def inter_num():
    while True:
        num = input('Введите число: ')
        if num.isdecimal() and int(num) > 0:
            return \
                int(num)
            break
        else:
            print('Вы должны ввести целое число, больше нуля, пропробуте снова')

print ('введите минимальное количество узлов')
N_min = inter_num()
print ('введите максимальное количество узлов')
N_mах = inter_num()
K_eff_rad_1 = {i: 8.91/i for i in range(N_min, N_mах+1)}
K_eff_rad_1_1 = {i: (8.91*1.1)/i for i in range(N_min, N_mах+1)}
K_eff_crk_1 = {i: 0.11*i for i in range(N_min, N_mах+1)}
K_eff_crk_1_1 = {i: (0.11*i)/1.1 for i in range(N_min, N_mах+1)}
columns = ['количество узлов', 'коэффициент эффективности']
print('K_eff_rad_1', tabulate(list(K_eff_rad_1.items()), headers=columns, tablefmt="grid"), sep='\n')
print('K_eff_rad_1_1', tabulate(list(K_eff_rad_1_1.items()), headers=columns, tablefmt="grid"), sep='\n')
print('K_eff_crk_1', tabulate(list(K_eff_crk_1.items()), headers=columns, tablefmt="grid"), sep='\n')
print('K_eff_crk_1_1', tabulate(list(K_eff_crk_1_1.items()), headers=columns, tablefmt="grid"), sep='\n')
plt.subplot(121)
plt.plot(K_eff_rad_1.keys(), K_eff_rad_1.values(), label='радиальная структура')
plt.plot(K_eff_crk_1.keys(), K_eff_crk_1.values(), label='кольцевая структура')
plt.title('коэффициент кривизны 1')
plt.ylabel('коэффициент эффективности')
plt.xlabel('количество узлов')
plt.legend()
plt.grid(True)
plt.subplot(122)
plt.plot(K_eff_rad_1_1.keys(), K_eff_rad_1_1.values(), label='радиальная структура')
plt.plot(K_eff_crk_1_1.keys(), K_eff_crk_1_1.values(), label='кольцеая структура')
plt.title('коэффициент кривизны 1.1')
plt.ylabel('коэффициент эффективности')
plt.xlabel('количество узлов')
plt.legend()
plt.grid(True)
plt.show()