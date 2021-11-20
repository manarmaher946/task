#element
from pyopenms import *
ed = ElementDB()

ed.hasElement("O")
ed.hasElement("S")

oxygen = ed.getElement("O")
print(oxygen.getName())
print(oxygen.getSymbol())
print(oxygen.getMonoWeight())
print(oxygen.getAverageWeight())

sulfur = ed.getElement("S")
print(sulfur.getName())
print(sulfur.getSymbol())
print(sulfur.getMonoWeight())
print(sulfur.getAverageWeight())
isotopes = sulfur.getIsotopeDistribution()

print ("One mole of oxygen weigh", 2*oxygen.getAverageWeight(), "gram")
print ("One mole of 16O2 weigh", 2*oxygen.getMonoWeight(), "gram")
#*************************************************************************
#isotopes
methanol = EmpiricalFormula("CH3OH")
ethanol = EmpiricalFormula("CH2") + methanol
print("fine isotope distribution:")
isotopes = ethanol.getIsotopeDistribution( FineIsotopePatternGenerator(1e-6) )
prob_sum = sum([iso.getIntensity() for iso in isotopes.getContainer()])
print("Thiscovers", prob_sum, "probability")
for iso in isotopes.getContainer():
    print ("isotope", iso.getMZ(), "hasabundance", iso.getIntensity()*100, "%")
    #**************************************************************
    #amino acids
    lys = ResidueDB().getResidue("lysine")
    print(lys.getName())
    print(lys.getThreeLetterCode())
    print(lys.getOneLetterCode())
    print(lys.getAverageWeight())
    print(lys.getMonoWeight())
    print(lys.getPka())
    print(lys.getFormula().toString())
    #amino acid modifications
    ox = ModificationsDB().getModification("Oxidation")
    print(ox.getUniModAccession())
    print(ox.getUniModRecordId())
    print(ox.getDiffMonoMass())
    print(ox.getId())
    print(ox.getFullId())
    print(ox.getFullName())
    print(ox.getDiffFormula())
    #ribonucleotides
    uridine = RibonucleotideDB().getRibonucleotide(b"U")
    print(uridine.getName())
    print(uridine.getCode())
    print(uridine.getAvgMass())
    print(uridine.getMonoMass())
    print(uridine.getFormula().toString())
    print(uridine.isModified())
    methyladenosine = RibonucleotideDB().getRibonucleotide(b"m1A")
    print(methyladenosine.getName())
    print(methyladenosine.isModified())

