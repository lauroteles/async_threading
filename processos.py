import multiprocessing


print(f'inicializando processos : {multiprocessing.current_process().name}')


def faz_algo(valor):
    print(f'Fazendo algo com o valor {valor}')


def main():
    pc = multiprocessing.Process(target=faz_algo,args=(10,),name='Processo filho')

    print(f'Processo filho: {pc.name}')


    pc.start()
    pc.join()


if __name__=='__main__':
    main()


