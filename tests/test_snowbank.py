from snowbank import __version__
from snowbank.main import Memory, Processes


def test_version():
    assert __version__ == '0.1.0'


def test_memory():
    memory = Memory()
    assert memory.size == 0
    memory.size = 1024
    assert memory.size == 1024
    memory.size = 2024
    assert memory.size == 2024
    memory.size = 0
    assert memory.size == 0


def test_processes():
    processes = Processes()
    processes.add_process('name')
    assert len(processes.processes) == 1
    assert processes.processes['name'].is_alive()
    processes.add_process('other')
    assert len(processes.processes) == 2
    assert processes.processes['other'].is_alive()
    processes.remove_process('name')
    assert len(processes.processes) == 1
    processes.remove_all_processes()
    assert len(processes.processes) == 0
