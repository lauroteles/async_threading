import threading
import time

def main():
    threads = [threading.Thread(target=contar, args=('elefante',10)),
               threading.Thread(target=contar, args=('buraco',8)),
               threading.Thread(target=contar, args=('dinheiro',15)),
               threading.Thread(target=contar, args=('pato',23)),
                                         ]



    [th.start() for th in threads]
    
    print('Pode fazer outra coisa enquanto a thread executa')
    print('Geek University' * 10)   

    [th.join() for th in threads]
    
    return print('Threads foi finalizada')



def contar(o_que,numero):
    for n in range(1, numero + 1):
        print(f'{n} {o_que}')
        time.sleep(1)



if __name__ == "__main__":
    main()



import os

num_cores = os.cpu_count()
print('Número de cores:', num_cores)	
