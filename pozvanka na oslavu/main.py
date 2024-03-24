text = "Aleš novák"

def Prevod(text):
  print(text)
  print(text.lower())
  print(text.upper())


def Inicialy(text):
  jmeno, prijmeni = text.split(" ")
  #print(jmeno, prijmeni)
  inicialy = ""
  inicialy += jmeno[0].upper() + "."
  inicialy += prijmeni[0].upper() + "."
  print(inicialy)


#Milý/Milá ...(jmeno)
#Rád bych tě pozval na svojí oslavu narozenin.
#Bude se konat ...(datum)
#Těším se ...(moje jméno)

def Zprava(osloveni, jmeno, datum, mojejmeno):
  text = f"""{osloveni} {jmeno},
Rád bych tě pozval na svojí oslavu narozenin.
Bude se konat {datum}.
Těším se, {mojejmeno}
  """

  print(text)

Osloveni = ["Milý", "Milý", "Milý", "Milá", "Milá"]
Jmena = ["Adame", "Filipe", "Karle", "Aničko", "Báro"]
Data = ["3.5.2024", "v pátek", "zítra", "1.1.2024", "o půlnoci"]
MojeJmeno = "Ondra"


#Zprava(Osloveni[0], Jmena[0], Data[0], MojeJmeno)

for i in range(5):
  Zprava(Osloveni[i], Jmena[i], Data[i], MojeJmeno)