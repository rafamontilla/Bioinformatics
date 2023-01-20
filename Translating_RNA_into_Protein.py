Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
for i in range(len(s)):
    if i%3==0:
        codon = s[i:i+3]
        if codon == 'AUG':
            print ('M',end="")
        elif codon == 'AUU' or codon == 'AUC' or codon == 'AUA':
            print ('I',end="")
        elif codon == 'ACU' or codon == 'ACC' or codon == 'ACA' or codon == 'ACG':
            print ('T',end="")
        elif codon == 'AAU' or codon == 'AAC':
            print ('N',end="")
        elif codon == 'AAA' or codon == 'AAG':
            print ('K',end="")
        elif codon == 'AGU' or codon == 'AGC' or codon == 'UCU' or codon == 'UCC' or codon == 'UCA' or codon == 'UCG':
            print ('S',end="")
        elif codon == 'AGA' or codon == 'AGG' or codon == 'CGG' or codon == 'CGA' or codon == 'CGC' or codon == 'CGU':
            print ('R',end="")
        elif codon == 'GUU' or codon == 'GUC' or codon == 'GUA' or codon == 'GUG':
            print ('V',end="")
        elif codon == 'GCU' or codon == 'GCC' or codon == 'GCA' or codon == 'GCG':
            print ('A',end="")
        elif codon == 'GAU' or codon == 'GAC':
            print ('D',end="")
        elif codon == 'GAA' or codon == 'GAG':
            print ('E',end="")
        elif codon == 'GGU' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG':
            print ('G',end="")
        elif codon == 'CUU' or codon == 'CUC' or codon == 'CUA' or codon == 'CUG' or codon == 'UUA' or codon == 'UUG':
            print ('L',end="")
        elif codon == 'CCU' or codon == 'CCC' or codon == 'CCA' or codon == 'CCG':
            print ('P',end="")
        elif codon == 'CAU' or codon == 'CAC':
             print('H',end="")
        elif codon == 'CAA' or codon == 'CAG':
             print ('Q',end="")
        elif codon == 'UUU' or codon == 'UUC':
             print ('F',end="")
        elif codon == 'UAU' or codon == 'UAC':
             print ('Y',end="")
        elif codon == 'UGU' or codon == 'UGC':
             print ('C',end="")
        elif codon == 'UGG':
             print('W',end="")
        else:
            break