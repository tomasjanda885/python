
import playsound
import sys # to access the system
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
#print("Tata je žába")
#playsound.playsound("C:/Users/tomas/Downloads/zaba.mp3")
#playsound.playsound("C:/Users/tomas/Downloads/osel.mp3")

#img = mpimg.imread('your_image.png')
#imgplot = plt.imshow(img)
#plt.show()

cesta = os.getcwd()


for i in range (1,1000000000000000000000):
    print("Míra je osel")
    playsound.playsound(cesta + "/Recording.mp3")
    playsound.playsound(cesta + "/osel2.mp3")
    print ("čislo je " , i, " osel" , i+1)



















