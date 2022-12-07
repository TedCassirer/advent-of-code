from dataclasses import dataclass, field


@dataclass
class Directory:
    name: str
    parent: "Directory"
    files: list["File"] = field(default_factory=list)
    directories: list["Directory"] = field(default_factory=list)

    def cd(self, path):
        if path == "..":
            return self.parent
        else:
            for d in self.directories:
                if d.name == path:
                    return d

    def addFile(self, size, name):
        self.files.append(File(size=size, name=name))

    def addDirectory(self, name):
        self.directories.append(Directory(parent=self, name=name))

    def size(self):
        totalFileSize = sum(f.size for f in self.files)
        totalSubDirSize = sum(d.size() for d in self.directories)
        return totalFileSize + totalSubDirSize

    def dirTree(self):
        yield self
        for d in self.directories:
            yield from d.dirTree()


@dataclass
class File:
    name: str
    size: int


def parseFileSystem(data):
    root = Directory(parent=None, name="")
    root.addDirectory(name="/")
    current = root
    for line in data.splitlines():
        parts = line.split(" ")
        if parts[0] == "$":
            if parts[1] == "cd":
                current = current.cd(parts[2])
            # else ls -> do nothing
        elif parts[0] == "dir":
            current.addDirectory(parts[1])
        else:
            current.addFile(int(parts[0]), parts[1])
    return root.cd("/")


def part1(data):
    root = parseFileSystem(data)
    return sum(d.size() for d in root.dirTree() if d.size() < 100_000)


def part2(data):
    root = parseFileSystem(data)
    diskSize = 70000000
    usedDiskSpace = root.size()
    unusedDiskSpace = diskSize - usedDiskSpace
    requiredUnused = 30000000
    minToFree = requiredUnused - unusedDiskSpace
    return min(d.size() for d in root.dirTree() if d.size() >= minToFree)


if __name__ == "__main__":
    from aocd import get_data

    data = get_data(year=2022, day=7)

    print(part1(data))
    print(part2(data))
