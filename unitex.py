import os

#sous_windows

os.system("rd /s corpus-medical_snt")
os.mkdir("corpus-medical_snt")
os.system("UnitexToolLogger Normalize  corpus-medical.txt -r Norm.txt")
os.system("UnitexToolLogger Tokenize corpus-medical.snt  -a Alphabet.txt")
os.system("UnitexToolLogger Compress subst.dic")
os.system("UnitexToolLogger Dico  -t corpus-medical.snt  -a Alphabet.txt -m Delaf.bin  subst.bin")
os.system("UnitexToolLogger Grf2Fst2  posologie.grf")
os.system("UnitexToolLogger Locate  -t corpus-medical.snt  posologie.fst2  -a Alphabet.txt  -L -I --all")
os.system("UnitexToolLogger Concord corpus-medical_snt/concord.ind  -f \"courrier new\" -s 12 -l 40 -r 55") 


#sous linux/mac-os
    
""" os.system("rm -rf corpus-medical_snt") #rm -rf sous linux == rd /s sous windows
os.mkdir("corpus-medical_snt")
os.system(" './UnitexToolLogger' Normalize 'corpus-medical.txt' '-rNorm.txt' ")
os.system(" './UnitexToolLogger' Tokenize 'corpus-medical.snt' '-aAlphabet.txt'")
os.system(" './UnitexToolLogger' Compress 'subst.dic'")
os.system(" './UnitexToolLogger' Dico '-tcorpus-medical.snt' '-aAlphabet.txt' '-mDelaf.bin' 'subst.bin'")
os.system(" './UnitexToolLogger' Grf2Fst2 'posologie.grf' ")
os.system(" './UnitexToolLogger' Locate '-tcorpus-medical.snt' 'posologie.fst2' '-aAlphabet.txt' -L -I --all ")
os.system(" './UnitexToolLogger' Concord 'corpus-midical_snt/concord.ind' '-f\"Courrier new\"' -s12 -l40 -r55")
 """