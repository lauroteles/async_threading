import multiprocessing


def ping(queue):
    queue.put('Geek')

def pong(queue):
    msg = queue.get()
    print(f'Mensagem recebida: {msg}')

def main():
    queue = multiprocessing.Pipe(True)

    p1 = multiprocessing.Process(target=ping, args=(queue,))
    p2 = multiprocessing.Process(target=pong, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == '__main__':
    main()

    