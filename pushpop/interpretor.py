from program import Program
import commands
from execution import ExecutionState
import sys
DEBUG_MODE = True


def execute_file(fname):
    program = Program(fname)
    state = ExecutionState()
    done = False

    try:
        while not done:
            pc = state.read_program_cntr()
            state.write_program_cntr(pc + 1)
            cmd = program.fetch(pc)
            if DEBUG_MODE:
                print "Executing: '"+str(cmd)+"'"
            done = cmd.execute(state)

    except Exception as e: print e
    finally: print "Stack:", str(state)
