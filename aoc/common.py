def readFile(path):
    with open(path) as f:
        return [l.rstrip() for l in f]
