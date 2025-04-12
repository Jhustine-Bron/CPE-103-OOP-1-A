#Writing Files

fout = open('output.txt', 'w')


line1 = "This here's the wattle, \n"
fout.write(line1)

line2 = 'the emblem of our land. \n'
fout.write(line2)
print(fout)
fout.close()