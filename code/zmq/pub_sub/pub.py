from time import sleep
from itertools import count
import zmq

from proto import ADDR

# from proto import FRONTEND_ADDR
# pub_sock.connect(FRONTEND_ADDR)

def pub():
    context = zmq.Context()
    pub_sock = context.socket(zmq.PUB)
    pub_sock.bind(ADDR)
    for i in count(0):
        pub_sock.send(str(i))
        sleep(2)


if __name__ == '__main__':
    pub()
