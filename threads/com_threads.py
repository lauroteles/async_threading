import time
import colorama

from threading import Thread,RLock
from queue import Queue

def gerados_de_dados(queue):
    for i in range(5):
        time.sleep(1)
        queue.put(i)
        print(colorama.Fore.CYAN + f'Dados produzidos: {i}',flush=True)
        time.sleep(2)
        queue.put(i)

def consumidor_de_dados(queue):
    while queue.qsize() > 0:
        dado = queue.get()
        print(colorama.Fore.GREEN + f'Dados consumidos: {dado * 3}',flush=True)
        time.sleep(5)
        queue.task_done()

if __name__ == "__main__":

    print(colorama.Fore.YELLOW + 'Iniciando a aplicação')
    queue = Queue()
    th1 = Thread(target=gerados_de_dados,args=(queue,))
    th2 = Thread(target=consumidor_de_dados,args=(queue,))

    th1.start()
    th1.join()

    th2.start()
    th2.join()        