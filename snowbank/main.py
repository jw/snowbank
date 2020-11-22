import os
from multiprocessing import Process
from time import sleep


def info(name, size):
    print(f"{name}: {size} bytes.")
    print(f" PPID: {os.getppid()}")
    print(f"  PID: {os.getpid()}")


def f(name, size=1024):
    memory = Memory(size)
    info(name, size)
    while True:
        sleep(1)


# todo: add tree of processes
class Processes:

    def __init__(self):
        self.processes = {}

    def add_process(self, name, size=1024):
        p = Process(target=f, args=(name, size))
        self.processes[name] = p
        p.start()

    def remove_process(self, name):
        if name in self.processes:
            self.processes[name].terminate()
            del self.processes[name]

    def remove_all_processes(self):
        for p in self.processes.values():
            p.terminate()
        self.processes = {}


class Memory:

    def __init__(self, size=0):
        self.block = bytearray(size)
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if len(self.block) <= size:
            self.block += bytearray(size - len(self.block))
        else:
            del self.block[size:len(self.block)]
        self.__size = size


if __name__ == '__main__':
    memory = Memory(1024 * 1024)
    print(f"Created first process (PID: {os.getpid()}) consuming {memory.size} bytes.")
    processes = Processes()
    processes.add_process('snowbank-1', 1024 * 1024)
    processes.add_process('snowbank-2', 512)
    processes.add_process('snowbank-3', 1024 * 1024 * 1024 * 3)
    print("Started 3 subprocesses...")
    while True:
        sleep(1)
