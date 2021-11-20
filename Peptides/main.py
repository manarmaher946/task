
#AminoAcidSequences
from pyopenms import *
seq = AASequence.fromString("DFPIANGER")
prefix = seq.getPrefix(4)
suffix = seq.getSuffix(5)
concat = seq + seq
print("sequence:", seq)
print("prefix:", prefix)
print("suffix:", suffix)
print("concatnated:", concat)
mfull = seq.getMonoWeight()
mprecursor = seq.getMonoWeight(Residue.ResidueType.Full, 2)
mz = seq.getMonoWeight(Residue.ResidueType.Full, 2) / 2.0
mz = seq.getMZ(2)
print()
print("monoisotopic mass of peptide[m]is", mfull)
print("monoisotopic mass of peptide precursor [M+2H]2+ is", mprecursor)
print("monoisotopic m/z of [M+2H]2+ is", mz)
#*************************************************************************
#peptideDFPIANGER
seq = AASequence.fromString("DFPIANGER")

print("The peptide", str(seq), "consists of the following amino acids:")
for a in seq:
    print(a.getName(), ":", a.getMonoWeight())
    seq = AASequence.fromString("C[143]PKCK(Label:13C(6)15N(2))CR")
    if seq.hasNTerminalModification():
        print("N-Term Modification: ", seq.getNTerminalModification().getFullId())
    if seq.hasCTerminalModification():
        print("C-Term Modification: ", seq.getCTerminalModification().getFullId())
    for aa in seq:
        if (aa.isModified()):
            print(aa.getName(), ":", aa.getMonoWeight(), ":", aa.getModificationName())
        else:
            print(aa.getName(), ":", aa.getMonoWeight())
            #Molecular formula
            seq = AASequence.fromString("DFPIANGER")
            seq_formula = seq.getFormula()
            print("Peptide", seq, "has molecular formula", seq_formula)
                #Isotope patterns

            coarse_isotopes = seq_formula.getIsotopeDistribution(CoarseIsotopePatternGenerator(6))
            for iso in coarse_isotopes.getContainer():
                print("Isotope", iso.getMZ(), "has abundance", iso.getIntensity() * 100, "%")
                #Fragment ions
                suffix = seq.getSuffix(3)
                print("=" * 35)
                print("y3 ion sequence:", suffix)
                y3_formula = suffix.getFormula(Residue.ResidueType.YIon, 2)
                suffix.getMonoWeight(Residue.ResidueType.YIon, 2) / 2.0
                suffix.getMonoWeight(Residue.ResidueType.XIon, 2) / 2.0
                suffix.getMonoWeight(Residue.ResidueType.BIon, 2) / 2.0
                print("y3 mz:", suffix.getMonoWeight(Residue.ResidueType.YIon, 2) / 2.0)
                print("y3 molecular formula:", y3_formula)

                #Modified Sequences
                seq = AASequence.fromString("PEPTIDESEKUEM(Oxidation)CER")
                print(seq.toUnmodifiedString())
                print(seq.toString())
                print(seq.toUniModString())
                print(seq.toBracketString())
                print(seq.toBracketString(False))

                print(AASequence.fromString("DFPIAM(uniMod:35)GER"))
                print(AASequence.fromString("DFPIAM[+16]GER"))
                print(AASequence.fromString("DFPIAM[+15.99]GER"))
                print(AASequence.fromString("DFPIAM[147]GER"))
                print(AASequence.fromString("DFPIAM[147.035405]GER"))


