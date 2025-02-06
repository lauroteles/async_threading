import multiprocessing


def depositar(saldo, lock):
    with lock:
        for  _ in range(10000):
            saldo.value += 1

def sacar(saldo,lock):
    with lock:
        for _  in range(10000):
            saldo.value = saldo.value - 1

def realizar_transacoes(saldo,lock):
    pc1 = multiprocessing.Process(target=depositar,args=(saldo,lock))
    pc2 = multiprocessing.Process(target=sacar,args=(saldo,lock))

    pc1.start()
    pc2.start()

    pc1.join()
    pc2.join()


if __name__=='__main__':
    saldo = multiprocessing.Value('i', 100)

    lock = multiprocessing.RLock()
    print(f'Saldo antes das transações: {saldo.value}')

    for _ in range(10):
        realizar_transacoes(saldo,lock)

    print(f'Saldo após as transações: {saldo.value}')
