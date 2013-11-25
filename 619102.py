import sys
# https://code.google.com/codejam/contest/619102/dashboard#s=p0
def getSections(wires):
    all = 0
    sections = 0
    i = 1
    while i < len(wires):
        if sections == 2:
            i += 1
            continue
        if wires[i-1][1] > wires[i][1]:
            sections = sections + 1
        i += 1
        all += sections
    return all

def main():
    file = sys.argv[1]
    with open(file) as f:
        T = int(f.readline())
        for a in xrange(T):
            N = int(f.readline())
            wires = []
            for x in xrange(N):
                seq = f.readline()[:-1].split(" ")
                w = (int(seq[0]), int(seq[1]))
                wires.append(w)
            print "Case #%d: %d" % (N, getSections(wires))
if __name__ == '__main__':
    main()
