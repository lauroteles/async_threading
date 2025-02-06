import multiprocessing


def calcular(dado):
    return ((((dado ** 15) * 150) / 2) / 50) /184

def main():
    tamanho_pool = multiprocessing.cpu_count()*2

    pool = multiprocessing.Pool(processes=tamanho_pool)
    entradas = list(range(7))
    saidas = pool.map(calcular, entradas)

    print(f'Saidas : {saidas}')

    pool.close()
    pool.join()


if __name__ == "__main__":
    main()    


