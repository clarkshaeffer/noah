print('input name of file (including extension): ')
print('(e.g.    >Hello World.pdf.links.txt   )')
x = input('>')

with open(x) as f:
    lines = f.readlines()

for line in lines:
    digit = line.split('}')[0].split(';')[-1]
    print(int(float(digit)) == 0)
    
