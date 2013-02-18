import commands
import re

class PushPopParser:
    def __init__(self):    
        pass

    def parse(self, line):
        cmd = re.split('\s+', line)
        if len(cmd) == 1:
            return commands.NoopCommand()
        
        return commands.ConstructCommand(cmd[1], cmd[2:])  ## instantiate

