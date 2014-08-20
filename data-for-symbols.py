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
            ms=num) for num, symbol in enumerate(symbols)])

    def to_file(self, path):
        with gzip.open(path, "wb", compresslevel=9) as f:
            f.write(self.generate())

def main(inpath, outpath):
    in_symbols = [symbol.strip() for symbol in inpath.read()]
    generator = Generator(in_symbols)

    to_file(out_path)

if __name__ == '__main__':
    main(argv[1], argv[2])
