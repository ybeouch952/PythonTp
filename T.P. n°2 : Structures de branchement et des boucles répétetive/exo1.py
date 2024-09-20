# nom = " Younes "
# age = 20
# print(f"Je m'appele {nom} et j'ai  {age} ans")

moyenne = float((input("Entrez votre moyenne :")))
print (type(moyenne))
if (moyenne>= 18):
    print("Excellent")
elif (14<=moyenne<18) :
    print ("Tres bien")
elif (10<=moyenne<14):
    print("Assez bien")
elif(5<=moyenne<10):
    print("Insufissant")
else:
    print ("Catastropique")