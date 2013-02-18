import commands
import re

class Program:
    def __init__(self, fname):
        self.fname = fname
        self._read_symbols(open(self.fname, 'r'))
        self._read_instructions(open(self.fname, 'r'))

    def _read_symbols(self, infile):
        self.symbol_table = {}
        for i, line in enumerate(infile):
            cmd = re.split('\s+', line)
            if cmd[0] != '':
                self.symbol_table[cmd[0]] = i

    def _read_instructions(self, infile):
        self.instructions = []
        commands.SetSymbolTable(self.symbol_table)
        for i, line in enumerate(infile):
            cmd = re.split('\s+', line)
            if cmd[-1] == '': cmd = cmd[:-1]
            command = commands.NoopCommand() if len(cmd[1]) == 0 else commands.ConstructCommand(cmd[1], cmd[2:])
            self.instructions.append(command)
    
    def fetch(self, num):
        return self.instructions[num]

    def __str__(self):
        return "Symbol Table:\n"+"\n".join([str(key)+": "+str(val) for key,val in self.symbol_table])+"\n\n"+\
               "Instructions:\n"+"\n".join([str(i)+": "+str(inst) for i,inst in enumerate(self.instructions)])


if __name__ == '__main__':
    program = Program('input.pp')
