import signal
import sys

from ceptions import TimeoutException
from structureexecutor import StructureExecutor
from structurer import Structurer
from tracereader import EffectReader


def handler(signum, frame):
    raise TimeoutException("timeout")


class StructurerTester:
    def __init__(self, line, debug):
        reader = EffectReader(line)
        # reader = TraceReader(line)
        reader.parse_trace()
        self.code_size = len(reader.code)

        signal.signal(signal.SIGALRM, handler)
        signal.alarm(15)
        # print(reader.signature)
        analyzer = Structurer(reader.code)
        StructureExecutor(reader, analyzer, debug)
        signal.alarm(0)

    def get_code_size(self):
        return self.code_size


if __name__ == "__main__":
    line = open(sys.argv[1]).readline()
    StructurerTester(line, True)
