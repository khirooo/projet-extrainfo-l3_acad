#KANOUN Lila , FERGANI Kheireddine
import os,sys,requests,re

b1,b2=sys.argv[1].split('-')

if len(sys.argv)==2 or sys.argv[2]=="80":#pas de port ou c le port part defaut
    port=''#ou port=80
else:
    port=sys.argv[2]

#verifier l'intervalle de pages et le construire
if( not( b1.isalpha() ) or not( b2.isalpha() ) or (b1>b2)):
    print("intervalle non valide")
    exit()

pages=[]
while(b1<=b2):
    pages.append(b1)
    b1=chr(ord(b1)+1) #pour avoir la prochaine lettre



        #preparer  l'URL + remplir liste des pages html demander
path=''
pagesHTML=[]
for page in pages:
                #localhost   80(defaut)                                [A-Z]
    path="http://127.0.0.1:"+port+"/vidal/vidal-Sommaires-Substances-"+page+".htm"
    res=requests.get(path)
    #passer le meme codage que les pages vidal
    res.encoding="utf-8" 
    pagesHTML.append([page,(res.text)]) #[lettre,page-html]
        #preparer  l'URL + remplir liste des pages html demander



#construire le dictionnaire + infos.txt
dictionnaire=open("subst.dic","w",encoding="utf-16-le")
dictionnaire.write("\ufeff")#BOM
info=open("infos.txt","w")


        #remplire le dictionnaire
substlist=[]
cmpt=0
for page in pagesHTML:
    #extraire nos informations
    substlist=re.findall("<a href=\"Substance/.+>(.+)</a>",page[1]) #le point pour matcher tout éàèI...0123...
    #ecrire le nombre de subs pour notre lettre
    info.write(page[0]+": "+str(len(substlist))+"\n")
    #compter le nombre totale de subs
    cmpt+=len(substlist)

    for subst in substlist:
        dictionnaire.write(subst+",.N+subst\n")
info.write("le nombre totale= "+str(cmpt)+"\n")

info.close
dictionnaire.close()
        #remplire le dictionnaire
