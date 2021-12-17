#Human protein sequence
from pyopenms import *
from urllib.request import urlretrieve
gh = "https://www.uniprot.org/uniprot/P01241.fasta"
urlretrieve (gh , "human.fasta")

dig = ProteaseDigestion()
dig.getEnzymeName() # Trypsin
bsa = "".join([l.strip() for l in open("human.fasta").readlines()[1:]])
bsa = AASequence.fromString(bsa)
# create all digestion products
result = []
dig.digest(bsa, result)
print(result[1].toString())
len(result) # 22 peptides
# only create peptides of length 7-40
dig.digest(bsa, result, 5, 40)
# print the results
for s in result:
    print(s.toString())
    # Allow two missed cleavages
    dig.setMissedCleavages(3)
    # only create peptides of length 7-40
    dig.digest(bsa, result, 7, 60)
    # print the results
    for s in result:
        print(s.toString())

        #YEAST protien sequence
from urllib.request import urlretrieve
gh = "https://www.uniprot.org/uniprot/P46672.fasta"
urlretrieve (gh , "YEAST.fasta")

dig = ProteaseDigestion()
dig.getEnzymeName() # Trypsin
bsa = "".join([l.strip() for l in open("YEAST.fasta").readlines()[1:]])
bsa = AASequence.fromString(bsa)
# create all digestion products
result = []
dig.digest(bsa, result)
print(result[9].toString())
len(result) # 54 peptides
# only create peptides of length 7-40
dig.digest(bsa, result, 7, 40)
# print the results
for s in result:
    print(s.toString())
    # Allow two missed cleavages
    dig.setMissedCleavages(2)
    # only create peptides of length 7-40
    dig.digest(bsa, result, 7, 40)
    # print the results
    for s in result:
        print(s.toString())
        #Proteolytic Digestion with Lys-C
names = []
ProteaseDB().getAllNames(names)
len(names) # at least 25 by default
print(names)

e = ProteaseDB().getEnzyme('Lys-C')
e.getRegExDescription()
from urllib.request import urlretrieve
gh = "https://www.uniprot.org/uniprot/P01241.fasta"
urlretrieve (gh , "human.fasta")

dig = ProteaseDigestion()
dig.setEnzyme('Lys-C')
bsa = "".join([l.strip() for l in open("human.fasta").readlines()[1:]])
bsa = AASequence.fromString(bsa)
result = []
dig.digest(bsa, result)
print(result[6].toString())
len(result) # 10 peptides
h = "https://www.uniprot.org/uniprot/P46672.fasta"
urlretrieve (gh , "YEAST.fasta")

dig = ProteaseDigestion()
dig.setEnzyme('Lys-C')
bsa = "".join([l.strip() for l in open("YEAST.fasta").readlines()[1:]])
bsa = AASequence.fromString(bsa)
result = []
dig.digest(bsa, result)
print(result[4].toString())
len(result) # 44 peptides