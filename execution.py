import numpy
from numpy import int32
MEMSIZE = 2**16

class ExecutionState:
    def __init__(self):
        self.mem = numpy.zeros([MEMSIZE], dtype=numpy.int32)
        self.stack_ptr = int32(0)
        self.program_cntr = int32(0)

    def push_int32(self, value):
        self.mem[self.stack_ptr] = int32(value)
        self.stack_ptr += 1

    def pop_int32(self):
        self.stack_ptr -= 1
        return self.mem[self.stack_ptr]

    def peek_int32(self):
        return self.mem[self.stack_ptr - 1]
    
    def read_stack_addr(self):
        return int32(self.stack_ptr)

    def write_stack_addr(self, addr):
        self.stack_ptr = int32(addr)

    def read_mem(self, addr):
        return self.mem[addr]

    def write_mem(self, addr, data):
        self.mem[addr] = int32(data)

    def read_program_cntr(self):
        return self.program_cntr

    def write_program_cntr(self, addr):
        self.program_cntr = addr

    def __str__(self):
        return str([self.mem[v] for v in range(0, self.stack_ptr)])
