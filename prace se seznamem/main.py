barvy = ["zelená", "červená", "modrá"]

barvy.append("fialová") #přidá prvek nakonec seznamu

barvy.insert(1, "žlutá") #přidá na určenou pozici

barvy.extend(("černá", "růžová", "stříbrná")) #přidá víc prvků najednou nakonec seznamu

barvy.pop()  #odstraní poslední prvek seznamu

barvy.remove("žlutá") #odstraní daný prvek podle názvu

#barvy.clear() #odstraní celý seznam

barvy.sort() #seřadí prvky

barvy.reverse() #obrátí seznam

barvy[1] = "zlatá" #přepíše prvek na daném místě

del barvy[2] #odstraní prvek na daném místě

print(barvy)

def Cisla():
  seznam = [3, 2, 5, 0, 1, 1, 26, 2, 15, 3, 2, 18, 9]
  seznam.sort()
  #seznam.remove(2)
  #while 2 in seznam:
  #  seznam.remove(2)
  pocet = 0
  index = 0

  for i in range(len(seznam)):
    if seznam[i] == 2:
      if pocet == 0:
        index = i
      pocet += 1

  print(seznam)
  print(pocet, index)

  del seznam[index: index + pocet]
  print(seznam)

Cisla()