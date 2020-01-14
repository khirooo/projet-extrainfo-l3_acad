#KANOUN Lila , FERGANI Kheireddine
import sys,re

corpus=open(sys.argv[1])
substdic=open("subst.dic","a",encoding="utf-16-le")
substenridic=open("subst_enri.dic","w",encoding="utf-16")#ou utf-16-le + BOM
info2=open("info2.txt","w")

#extraire les substances/medicaments
substlist=[]
cmpt=0
dicinfo={}
for line in corpus.readlines():
    x=re.search("^-?\s?(\w+-?\w+) :? ?(\d|,|\.)+? ?(g|mg|ml|ui|ug|ML|MG|hélule)",line)# ui: ACTRAPID 100 ui/mL g: pipéracilline-tazobactam 4g/500mg
    if(x):
        cmpt+=1
        print(str(cmpt)+": "+x.group(1).lower()+"\n")
        substlist.append(x.group(1).lower())
        #remplir dicinfo
        dicinfo[x.group(1)[0].upper()]=dicinfo.get(x.group(1)[0].upper(),0)+1


#enrechire subst.dic 
for subst in substlist:
    substdic.write(subst+",.N+subst\n")
    substenridic.write(subst+",.N+subst\n") #garder trace

#remplire info2
for alpha in sorted(dicinfo.keys()):
    info2.write(alpha+": "+str(dicinfo[alpha])+"\n")
info2.write("le nombre totale: "+str(cmpt))


corpus.close()
substdic.close()
substenridic.close()
info2.close()


#trier et eliminer les doublons
substdic=open("subst.dic","r",encoding="utf-16")
substlist=[]
for subst in substdic:
    #eliminer la duplication
    if(subst not in substlist):
        substlist.append(subst)
substdic.close()

#trier
substlist.sort()

#reconstruire subst.dic
substdic=open("subst.dic","w",encoding="utf-16-le")
substdic.write("\ufeff")

for subst in substlist:
    substdic.write(subst)
substdic.close()
