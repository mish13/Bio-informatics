amino_acid_mapping = dict()
#A
amino_acid_mapping["AAA"] = 'K'
amino_acid_mapping["AAG"] = 'K'
amino_acid_mapping["AAC"] = 'N'
amino_acid_mapping["AAU"] = 'N'

amino_acid_mapping["ACA"] = 'T'
amino_acid_mapping["ACU"] = 'T'
amino_acid_mapping["ACG"] = 'T'
amino_acid_mapping["ACC"] = 'T'


amino_acid_mapping["AGU"] = 'S'
amino_acid_mapping["AGC"] = 'S'
amino_acid_mapping["AGA"] = 'R'
amino_acid_mapping["AGG"] = 'R'

amino_acid_mapping["AUA"] = 'I'
amino_acid_mapping["AUC"] = 'I'
amino_acid_mapping["AUU"] = 'I'
amino_acid_mapping["AUG"] = 'M'

#C
amino_acid_mapping["CAA"] = 'Q'
amino_acid_mapping["CAG"] = 'Q'
amino_acid_mapping["CAC"] = 'H'
amino_acid_mapping["CAU"] = 'H'

amino_acid_mapping["CCA"] = 'P'
amino_acid_mapping["CCU"] = 'P'
amino_acid_mapping["CCG"] = 'P'
amino_acid_mapping["CCC"] = 'P'


amino_acid_mapping["CGU"] = 'R'
amino_acid_mapping["CGC"] = 'R'
amino_acid_mapping["CGA"] = 'R'
amino_acid_mapping["CGG"] = 'R'

amino_acid_mapping["CUA"] = 'L'
amino_acid_mapping["CUC"] = 'L'
amino_acid_mapping["CUU"] = 'L'
amino_acid_mapping["CUG"] = 'L'

#G
amino_acid_mapping["GAA"] = 'E'
amino_acid_mapping["GAG"] = 'E'
amino_acid_mapping["GAC"] = 'D'
amino_acid_mapping["GAU"] = 'D'

amino_acid_mapping["GCA"] = 'A'
amino_acid_mapping["GCU"] = 'A'
amino_acid_mapping["GCG"] = 'A'
amino_acid_mapping["GCC"] = 'A'


amino_acid_mapping["GGU"] = 'G'
amino_acid_mapping["GGC"] = 'G'
amino_acid_mapping["GGA"] = 'G'
amino_acid_mapping["GGG"] = 'G'

amino_acid_mapping["GUA"] = 'V'
amino_acid_mapping["GUC"] = 'V'
amino_acid_mapping["GUU"] = 'V'
amino_acid_mapping["GUG"] = 'V'

#U
amino_acid_mapping["UAA"] = ''
amino_acid_mapping["UAG"] = ''
amino_acid_mapping["UAC"] = 'Y'
amino_acid_mapping["UAU"] = 'Y'

amino_acid_mapping["UCA"] = 'S'
amino_acid_mapping["UCU"] = 'S'
amino_acid_mapping["UCG"] = 'S'
amino_acid_mapping["UCC"] = 'S'

amino_acid_mapping["UGU"] = 'C'
amino_acid_mapping["UGC"] = 'C'
amino_acid_mapping["UGA"] = ''
amino_acid_mapping["UGG"] = 'W'

amino_acid_mapping["UUA"] = 'L'
amino_acid_mapping["UUC"] = 'F'
amino_acid_mapping["UUU"] = 'F'
amino_acid_mapping["UUG"] = 'L'

rna = input()
len_rna = len(rna)
out = ""
i = 0
while i+3 < len_rna:
  out+= amino_acid_mapping[rna[i:i+3]]
  i+=3
  
print(out)
