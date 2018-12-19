with open("camp.contig") as f:
    i = 0
    avg = 0
    for line in f:
        if line[0] == '#':
            i += 1
            bases = int(line.split()[2])
            avg += bases
            print(bases)



print(i)
print(avg / i)
