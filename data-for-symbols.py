#Given a symbol set, generate a minimal-length file that uses every
#symbol in the set.
import gzip
from sys import argv

class Generator:
    ADD_FMT = ("A,{seqnum},{refnum},N,{ordty},{count}"
               ",{symbol},{price},{sec},{ms},L,AARCA")

    def __init__(self, symbols):
        self._symbols = symbols

    def generate(self):
        # num_gen = itertools.count() *)
        return "\n".join([self.ADD_FMT.format(
            seqnum=num,
            refnum=num,
            ordty="B" if num % 2 else "S",
            count=num,
            symbol=symbol,
            price=num,
            sec=num,
            ms=num) for num, symbol in enumerate(self._symbols, start=1)])

    def to_file(self, path):
        with gzip.open(path, "w", compresslevel=9) as f:
            f.write(bytes(self.generate(), 'UTF-8'))

def main(inpath, outpath):
    in_symbols = [symbol.strip() for symbol in open(inpath).readlines()]
    generator = Generator(in_symbols)

    generator.to_file(outpath)

if __name__ == '__main__':
    main(argv[1], argv[2])
