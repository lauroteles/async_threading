import datetime
import math

import multiprocessing
from concurrent.futures import ProcessPoolExecutor



def main():
    qtd_cores = multiprocessing.cpu_count()
    print(f"Quantidade de cores: {qtd_cores}")

    
    inicio = datetime.datetime.now()


    with ProcessPoolExecutor(max_workers=qtd_cores) as executor:
        for i in range (1, qtd_cores, + 1):

            ini = 50_000_000  * qtd_cores * (i - 1) / qtd_cores
            fim = 50_000_000 * i / qtd_cores
            print(f"Thread {i} - ini: {ini} - fim: {fim}")

            executor.submit(computar, fim, ini)

    tempo = datetime.datetime.now() - inicio
    print(f"Tempo de execução: {tempo.total_seconds():.2f} segundos")


def computar(fim,inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))

if __name__ == "__main__":
    main()        



''' Tempo de execução: 0.78 segundos '''