name = input("Enter file")
handle = open(name)
counts = dict()
for i in handle:
    words = line.sprit