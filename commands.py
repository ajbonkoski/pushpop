import re

class CommandConstructError(Exception): pass
def ConstructCommand(cmd, args):
    if cmd not in CommandTable:
        raise CommandConstructError("Failed to find command: '"+str(cmd)+"' with args: '"+str(args)+"'");
    cmd_class = CommandTable[cmd]
    return cmd_class(args)


def SetSymbolTable(symbol_table):
    global SymbolTable
    SymbolTable = symbol_table

CommandTable = {}
def NewCommand(cmd):
    CommandTable[cmd.name] = cmd
    return cmd

def is_int(arg):
    return re.search('^(-|\+)?[0-9]+$', arg) != None

def is_symbol(arg):
    return re.search('^[A-Za-z]+$', arg) != None

class Command:
    def require_args(self, args, types):
        self.args = args

        i = 0
        if len(args) == len(types):
            for arg, type in zip(args, types):

                if type == 'int':
                    if not is_int(arg): break
                    
                elif type == 'symbol':
                    if not is_symbol(arg): break

                else: break
                i += 1

        if i != len(args):    
            raise CommandConstructError("Invalid arg count for '"+self.name+"' at "+str(i))
    
    def __str__(self):
        return ' '.join([self.name] + self.args)

@NewCommand
class NoopCommand(Command):
    name = 'noop'
    def __init__(self, args=[]): 
        self.require_args(args, []);

    def execute(self, state):
        return False

@NewCommand
class HaltCommand(Command):
    name = 'halt'
    def __init__(self, args=[]): 
        self.require_args(args, []);

    def execute(self, state):
        return True

@NewCommand
class PushCommand(Command):
    name = 'push'
    def __init__(self, args): 
        self.require_args(args, ['int']);
        self.value = int(args[0])

    def execute(self, state):
        state.push_int32(self.value)
        return False

@NewCommand
class DupCommand(Command):
    name = 'dup'
    def __init__(self, args): 
        self.require_args(args, []);

    def execute(self, state):
        a = state.peek_int32()
        state.push_int32(a)
        return False

@NewCommand
class FlipCommand(Command):
    name = 'flip'
    def __init__(self, args): 
        self.require_args(args, []);

    def execute(self, state):
        b = state.pop_int32()
        a = state.pop_int32()
        state.push_int32(b)
        state.push_int32(a)
        return False

@NewCommand
class SubCommand(Command):
    name = 'sub'
    def __init__(self, args): 
        self.require_args(args, []);

    def execute(self, state):
        b = state.pop_int32()
        a = state.pop_int32()
        state.push_int32(a-b)
        return False

@NewCommand
class NandCommand(Command):
    name = 'nand'
    def __init__(self, args): 
        self.require_args(args, []);

    def execute(self, state):
        b = state.pop_int32()
        a = state.pop_int32()
        state.push_int32(~(a&b))
        return False

@NewCommand
class ShiftCommand(Command):
    name = 'shift'
    def __init__(self, args): 
        self.require_args(args, []);

    def execute(self, state):
        mode = state.pop_int32()
        amt = state.pop_int32()
        n = state.pop_int32()
        result = n << amt if mode&1 == 0 else n >> amt
        state.push_int32(result)
        return False

@NewCommand
class PushSpCommand(Command):
    name = 'pushsp'
    def __init__(self, args): 
        self.require_args(args, []);

    def execute(self, state):
        a = state.read_stack_addr()
        state.push_int32(a)
        return False

@NewCommand
class PopSpCommand(Command):
    name = 'popsp'
    def __init__(self, args): 
        self.require_args(args, []);

    def execute(self, state):
        a = state.pop_int32()
        state.write_stack_addr(a)
        return False

@NewCommand
class PushPcCommand(Command):
    name = 'pushpc'
    def __init__(self, args): 
        self.require_args(args, []);

    def execute(self, state):
        a = state.read_program_cntr()
        state.push_int32(a)
        return False

@NewCommand
class PopSpCommand(Command):
    name = 'popsp'
    def __init__(self, args): 
        self.require_args(args, []);

    def execute(self, state):
        a = state.pop_int32()
        state.write_program_cntr(a)
        return False

@NewCommand
class LoadCommand(Command):
    name = 'load'
    def __init__(self, args): 
        self.require_args(args, []);

    def execute(self, state):
        addr = state.pop_int32()
        data = state.read_mem(addr)
        state.push_int32(data)
        return False

@NewCommand
class StoreCommand(Command):
    name = 'store'
    def __init__(self, args): 
        self.require_args(args, []);

    def execute(self, state):
        addr = state.pop_int32()
        data = state.pop_int32()
        state.write_mem(addr, data)
        return False

@NewCommand
class StoreCommand(Command):
    name = 'store'
    def __init__(self, args): 
        self.require_args(args, []);

    def execute(self, state):
        addr = state.pop_int32()
        data = state.pop_int32()
        state.write_mem(addr, data)
        return False

@NewCommand
class BranchLessEqualCommand(Command):
    name = 'ble'
    def __init__(self, args): 
        self.require_args(args, ['symbol']);
        self.target = SymbolTable[args[0]]

    def execute(self, state):
        cond = state.pop_int32()
        if cond <= 0:
            pc_plus1 = state.read_program_cntr()
            state.write_program_cntr(self.target)
        return False
