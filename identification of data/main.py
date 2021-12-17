from pyopenms import*

protein_id = ProteinIdentification()
peptide_id = PeptideIdentification()

# Sets the Identifier
protein_id.setIdentifier("IdentificationRun1")
peptide_id.setIdentifier("IdentificationRun1")

# Prints the Identifier
print("Protein Identifier -", protein_id.getIdentifier())
print("Peptide Identifier -", peptide_id.getIdentifier())
# Create new protein identification object corresponding to a single search
protein_id = ProteinIdentification()
protein_id.setIdentifier("IdentificationRun1")

# Each ProteinIdentification object stores a vector of protein hits
protein_hit = ProteinHit()
protein_hit.setAccession("sp|MyAccession")
protein_hit.setSequence("PEPTIDERDLQMTQSPSSLSVSVGDRPEPTIDE")
protein_hit.setScore(1.0)
protein_hit.setMetaValue("target_decoy", b"target") # its a target protein

protein_id.setHits([protein_hit])


now = DateTime.now()
date_string = now.getDate()
protein_id.setDateTime(now)

# Example of possible search parameters
search_parameters = SearchParameters() # ProteinIdentification::SearchParameters
search_parameters.db = "database"
search_parameters.charges = "+2"
protein_id.setSearchParameters(search_parameters)

# Some search engine meta data
protein_id.setSearchEngineVersion("v1.0.0")
protein_id.setSearchEngine("SearchEngine")
protein_id.setScoreType("HyperScore")

# Iterate over all protein hits
for hit in protein_id.getHits():
  print("Protein hit accession:", hit.getAccession())
  print("Protein hit sequence:", hit.getSequence())
  print("Protein hit score:", hit.getScore())
  peptide_id = PeptideIdentification()

  peptide_id.setRT(1243.56)
  peptide_id.setMZ(440.0)
  peptide_id.setScoreType("ScoreType")
  peptide_id.setHigherScoreBetter(False)
  peptide_id.setIdentifier("IdentificationRun1")

  # define additional meta value for the peptide identification
  peptide_id.setMetaValue("AdditionalMetaValue", "Value")

  # create a new PeptideHit (best PSM, best score)
  peptide_hit = PeptideHit()
  peptide_hit.setScore(1.0)
  peptide_hit.setRank(1)
  peptide_hit.setCharge(2)
  peptide_hit.setSequence(AASequence.fromString("DLQM(Oxidation)TQSPSSLSVSVGDR"))

  ev = PeptideEvidence()
  ev.setProteinAccession("sp|MyAccession")
  ev.setAABefore(b"R")
  ev.setAAAfter(b"P")
  ev.setStart(123)  # start and end position in the protein
  ev.setEnd(141)
  peptide_hit.setPeptideEvidences([ev])

  # create a new PeptideHit (second best PSM, lower score)
  peptide_hit2 = PeptideHit()
  peptide_hit2.setScore(0.5)
  peptide_hit2.setRank(2)
  peptide_hit2.setCharge(2)
  peptide_hit2.setSequence(AASequence.fromString("QDLMTQSPSSLSVSVGDR"))
  peptide_hit2.setPeptideEvidences([ev])

  # add PeptideHit to PeptideIdentification
  peptide_id.setHits([peptide_hit, peptide_hit2])
  # Iterate over PeptideIdentification
  peptide_ids = [peptide_id]
  for peptide_id in peptide_ids:
      # Peptide identification values
      print("Peptide ID m/z:", peptide_id.getMZ())
      print("Peptide ID rt:", peptide_id.getRT())
      print("Peptide ID score type:", peptide_id.getScoreType())
      # PeptideHits
      for hit in peptide_id.getHits():
          print(" - Peptide hit rank:", hit.getRank())
          print(" - Peptide hit sequence:", hit.getSequence())
          print(" - Peptide hit score:", hit.getScore())
          print(" - Mapping to proteins:", [ev.getProteinAccession()
                                            for ev in hit.getPeptideEvidences()])
          # Store the identification data in an idXML file
          IdXMLFile().store("out.idXML", [protein_id], peptide_ids)
          # and load it back into memory
          prot_ids = [];
          pep_ids = []
          IdXMLFile().load("out.idXML", prot_ids, pep_ids)

          # Iterate over all protein hits
          for protein_id in prot_ids:
              for hit in protein_id.getHits():
                  print("Protein hit accession:", hit.getAccession())
                  print("Protein hit sequence:", hit.getSequence())
                  print("Protein hit score:", hit.getScore())
                  print("Protein hit target/decoy:", hit.getMetaValue("target_decoy"))

          # Iterate over PeptideIdentification
          for peptide_id in pep_ids:
              # Peptide identification values
              print("Peptide ID m/z:", peptide_id.getMZ())
              print("Peptide ID rt:", peptide_id.getRT())
              print("Peptide ID score type:", peptide_id.getScoreType())
              # PeptideHits
              for hit in peptide_id.getHits():
                  print(" - Peptide hit rank:", hit.getRank())
                  print(" - Peptide hit sequence:", hit.getSequence())
                  print(" - Peptide hit score:", hit.getScore())
                  print(" - Mapping to proteins:", [ev.getProteinAccession() for ev in hit.getPeptideEvidences()])