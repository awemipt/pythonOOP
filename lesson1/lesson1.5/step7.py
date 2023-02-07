class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, *args):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = list(args)

    def get_config(self):
        config = []
        config.append(f'Материнская плата: {self.name}')
        config.append(f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}')
        config.append(f'Слотов памяти: {self.total_mem_slots}')
        memory = [f'{mem.name}-{mem.volume}' for mem in self.mem_slots]
        config.append('Память: '+'; '.join(memory))
        return config

mb = MotherBoard('mb', CPU('sd', 100), Memory('mem1',100), Memory('mem2',200))
