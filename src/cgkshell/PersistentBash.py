# -*- coding: utf-8 -*

import fcntl
import os
import subprocess
import time

class PersistentBash(object):
    shell = None
    delay = None

    def __init__(self, delay=0.5):
        self.delay = delay
        self.shell = subprocess.Popen(['/bin/bash'], stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE)
        fcntl.fcntl(self.shell.stdout.fileno(), fcntl.F_SETFL, os.O_NONBLOCK)

    def execute(self, command):
        self.shell.stdin.write(command.strip() + '\n')
        time.sleep(self.delay)
        lines = []
        try:
            while True:
                lines.append(self.shell.stdout.readline())
                time.sleep(self.delay)
        except IOError, e:
            # Resource temporarily unavailable, error thrown when no more input
            # can be read.
            if e.errno == 11:
                pass
            else:
                raise
        output = ''.join(lines)
        return output

    def __enter__(self):
        return self

    def __exit__(self, exc_type, value, traceback):
        self.shell.stdin.close()
