import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # пункт а

    norm1 = np.random.normal(size=100)
    bin_numb = 10 
    plt.ylabel('Частота')
    plt.xlabel('Данные')


    plt.hist(norm1, density=True, bins = bin_numb)
    x = np.linspace(-5.5, 5.5, num=100)
    plt.plot(x, stats.norm.pdf(x, 0, 1))

    print("Среднее = ",np.mean(norm1),"при исходном 0")
    print("Отклонение = ",np.std(norm1),"при исходном 1")

    #пункт б

    g_dispN = 0
    g_dispN1  = 0
    l_dispN = 0
    l_dispN1 = 0
    mseN = 0
    mseN1 = 0

    for i in range(0,150):
        norm2 = np.random.normal(size=20)
        dispN = np.var(norm2,ddof=0)
        dispN1 = np.var(norm2,ddof=1)
        
        if dispN1 > 1: g_dispN1 += 1
        if dispN > 1: g_dispN += 1
        if dispN < 1: l_dispN += 1
        if dispN1 < 1: l_dispN1 += 1
        
        mseN = (mseN+(1-dispN)**2)/(i+1)
        mseN1 = (mseN1+(1-dispN1)**2)/(i+1)

    print('Количество раз когда дисперсия превысила реальную: ', g_dispN)
    print('Количество раз когда исправленная дисперсия превысила реальную: ', g_dispN1)

    print('Количество раз когда дисперсия недооценила реальную: ', l_dispN)
    print('Количество раз когда исправленная дисперсия недооценила реальную: ', l_dispN1)

    print('Средней квадрат ошибки дисперсии', mseN)
    print('Средней квадрат ошибки исправленной дисперсии', mseN1)