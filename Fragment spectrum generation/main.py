from pyopenms import *
tsg = TheoreticalSpectrumGenerator()
spec1 = MSSpectrum()
peptide = AASequence.fromString("DFPIANGER")
p = Param()
p.setValue("add_b_ions", "false")
p.setValue("add_metainfo", "true")
tsg.setParameters(p)
tsg.getSpectrum(spec1, peptide, 1, 1)
print("Spectrum 1 of", peptide, "has", spec1.size(), "peaks.")
for ion, peak in zip(spec1.getStringDataArrays()[0], spec1):
    print(ion.decode(), "is generated at m/z", peak.getMZ())
    import matplotlib.pyplot as plt

    plt.bar(spec1.get_peaks()[0], spec1.get_peaks()[1], snap=False)
    plt.xlabel("m/z")
    plt.ylabel("intensity")
    mz, i = spec1.get_peaks()
    annot = spec1.getStringDataArrays()[0]
    bars = plt.bar(mz, i, snap=False)
    idx = 0
    for rect in bars:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, annot[idx].decode(), ha='center', va='bottom',
                 rotation=90)
        idx += 1
    plt.ylim(top=1.2)
    plt.xlabel("m/z")
    plt.ylabel("intensity")
    spec2 = MSSpectrum()
    p.setValue("add_b_ions", "true")
    p.setValue("add_a_ions", "true")
    p.setValue("add_losses", "true")
    p.setValue("add_metainfo", "true")
    tsg.setParameters(p)
    tsg.getSpectrum(spec2, peptide, 1, 2)

    # Iterate over annotated ions and their masses
    print("Spectrum 2 of", peptide, "has", spec2.size(), "peaks.")
    for ion, peak in zip(spec2.getStringDataArrays()[0], spec2):
        print(ion.decode(), "is generated at m/z", peak.getMZ())

    exp = MSExperiment()
    exp.addSpectrum(spec1)
    exp.addSpectrum(spec2)
    MzMLFile().store("DFPIANGER.mzML", exp)
    import matplotlib.pyplot as plt

    plt.bar(spec2.get_peaks()[0], spec2.get_peaks()[1], snap=False)  # snap ensures that all bars are rendered
    plt.xlabel("m/z")
    plt.ylabel("intensity")