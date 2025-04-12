# Searching for 'From:' lines
fhand = open('mbox-short.txt')
for line in fhand:
  if line.startswith('From:'):
    print(line)

# Same, with rstrip and continue
fhand = open('mbox-short.txt')
for line in fhand:
  line = line.rstrip()
  if not line.startswith('From:'):
    continue
  print(line)

# Search lines with @uct.ac.za
fhand = open('mbox-short.txt')
for line in fhand:
  line = line.rstrip()
  if line.find('@uct.ac.za') == -1:
    continue
  print(line)
