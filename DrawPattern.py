from tkinter import *
import pygame
from tkinter.font import Font #tuodaan fonttikirjasto.
from tkinter import filedialog
import os

pygame.init()

#määritellään käytettävät värit RGB-arvoina
WHITE = (255,255,255)
BLACK = (0,0,0)

#funktio neliön piirtämiseen.
def drawRect():
    #tallennetaan width,height,xaxis ja yaxis muuttujiin
    #syötekenttiin syötetyt arvot.
    
    Width = int(Entry.get(value1))
    Height = int(Entry.get(value2))
    Xaxis = int(Entry.get(value3))
    Yaxis = int(Entry.get(value4))
    
    #piirretään alkupisteestä loppupisteeseen käyttäjän syöttämien
    #arvojen (x-akseli, y-akseli,korkeus ja leveys) kokoinen neliö
    #valkoisella värillä.
    pygame.draw.rect(screen, WHITE,[Xaxis,Yaxis,Width,Height],5)
    pygame.display.flip()

#funktio ellipsin piirtämiseen.
def drawEllipse():
    Width = int(Entry.get(value1))
    Height = int(Entry.get(value2))
    Xaxis = int(Entry.get(value3))
    Yaxis = int(Entry.get(value4))
    pygame.draw.ellipse(screen, WHITE,[Xaxis,Yaxis,Width,Height],5)
    pygame.display.flip()

#funktio ympyrän piirtämiseen.
def drawCircle():
    center = int(Entry.get(value1))
    radius = int(Entry.get(value2))
    pygame.draw.circle(screen, WHITE,(center,radius),50)
    pygame.display.flip()

#fuktio pygame ikkunan tyhjentämiseen.
def clear():
    screen.fill(BLACK)
    pygame.display.flip()

#funktio pygame ikkunan sulkemiseen.
def close():
     pygame.quit() 

#luodaan funktio, jonka avulla kuva tallennetaan jpg-muodossa.
def saveFile():
    file = filedialog.asksaveasfilename()
    file = pygame.image.save(screen,file+'.jpg')

#luodaan funktio, jonka avulla voidaan avata jpg-muodossa oleva tallennettu kuva.
def loadFile():
    file = filedialog.askopenfilename(filetypes=[('Jpg-files', '*.jpg')])
    file = pygame.image.load(file)
    screen.blit(file,(20,20))
    pygame.display.flip()
    
 
     
    

#luodaan pohjakomponentti
root = Tk()
root.title('Draw')

#tallennetaan muuttujaan fontti, jota käytetään ohjelmassa.
appfont = Font (family = 'Times New Roman')

#luodaan alasvetovalikko
menubar = Menu(root)
root.config(menu=menubar)
funcmenu = Menu(menubar)

#annetaan valikolle otsikko
menubar.add_cascade(label = 'Functions', menu = funcmenu)

#lisätään valikkoon pygame ikkunan sulkemistoiminto, command komennolla
#kerrotaan mikä funktio suoritetaan kun vaihtoehtoa klikataan.
funcmenu.add_command(label = 'Save picture', command = saveFile)
funcmenu.add_command(label = 'Load picture', command = loadFile)
funcmenu.add_command(label = 'Close PyGame window', command = close)



#luodaan frame komponentit joilla asemoidaan muut komponentit.
frame1 = Frame()
frame2 = Frame()
frame3 = Frame()
frame4 = Frame()
frame5 = Frame()

#luodaan syötekentät, width komennolla annetaan kerrotaan niiden koko.
value1 = Entry(frame1, width = 5)
value2 = Entry(frame2, width = 5)
value3 = Entry(frame5, width = 5)
value4 = Entry(frame5, width = 5)

#label komennolla luodaan tekstikomponentit.
title = Label(root, text = 'Draw patterns',font = appfont)
widthtxt = Label(frame1, text = 'Width or circle center: ',font = appfont)
heighttxt = Label(frame2, text = 'Height or circle radius: ', font = appfont)
xaxisLabel = Label(frame5, text = 'X-axis: ')
yaxisLabel = Label(frame5, text = 'Y-axis: ')
positionLabel = Label(root, text = 'Position on the X and Y axis')

#Button komennolla luodaan painikkeet, command komennolla kerrotaan,
#mikä funktio suoritetaan, kun painiketta painetaan.

rectbtn = Button(frame3, text = 'Draw rectangle', command = drawRect, relief = 'solid')
ellipsebtn = Button(frame3, text = 'Draw ellipse',command = drawEllipse, relief = 'solid')
clearbtn = Button(frame4, text = 'Clear display',command = clear, relief = 'solid')
circlebtn = Button(frame4, text = 'Draw circle', command = drawCircle, relief = 'solid')

#annetaan pygame ikkunan korkeus ja leveysarvot pikseleinä.
size=(400,500)
#tallennetaan muuttujaan pygameikkuna.
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Draw patterns')


#pakataan komponentit, side komennolla sijoitetaan ne ja pady/padx komennoilla
#lisätään tyhjää tilaa komponenttien ympärille. side komennolla kerrotaan mihin
#komponentti sijoitetaan.
title.pack()
frame1.pack()
widthtxt.pack(side=LEFT)
value1.pack(side=RIGHT,pady=2)

frame2.pack()
heighttxt.pack(side=LEFT)
value2.pack(side=RIGHT,pady=2)

positionLabel.pack()
frame5.pack()
xaxisLabel.pack(side=LEFT)
value3.pack(side=RIGHT)

yaxisLabel.pack(side=RIGHT)
value4.pack(side=RIGHT)
frame3.pack()

rectbtn.pack(side=RIGHT,padx=5,pady=4)
ellipsebtn.pack(side=LEFT,pady=4,padx=5)
frame4.pack()

clearbtn.pack(side=RIGHT,padx=5,pady=4)
circlebtn.pack(pady=4,padx=5)
mainloop()


