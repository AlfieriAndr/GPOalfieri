import pygame
import random

# REGOLE
# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
#https://editor.p5js.org/codingtrain/sketches/UtSMCB1zv

#creare un bottone start che faccia partire la simulazione --> magari tipo "premi c per iniziare" 
#creare un bottone reset che resetti la griglia/simulazione e fa tornare le cellule al punto di inizio
#fare un modo che durante la simulazione non si possano cambiare le cellule

def aggiornaGriglia():
    nuovaGriglia = []
    global griglia
    #controllo stato vicine
    for x in range(len(griglia)):
        riga = []
        for y in range(len(griglia)):
            vicineVive = 0

            if 0 < x < len(griglia)-1 and 0 < y < len(griglia[0])-1:
                for vx in [-1, 0, 1]:
                    for vy in [-1, 0, 1]:
                        if not (vx == 0 and vy == 0):  # non conto la cella stessa
                            if griglia[x+vx][y+vy].stato == 1:
                                vicineVive += 1

            #controllo regole vive/muore
            nuovaCella = griglia[x][y].copy()  # serve un metodo che duplica la cella
            if griglia[x][y].stato == 1:
                if vicineVive < 2 or vicineVive > 3:
                    nuovaCella.cambiaStato()
            else:
                if vicineVive == 3:
                    nuovaCella.cambiaStato()

            riga.append(nuovaCella)
        nuovaGriglia.append(riga)
    griglia = nuovaGriglia

def disegnaCelle():
    global griglia
    for i in range(nCelle):
        riga = griglia[i]
        for j in range(nCelle):
            cellula = riga[j]
            pygame.draw.rect(screen, cellula.colore, cellula.rettangolo)
        
def generaCelle():
    x = baseX
    y = baseY
    for i in range(nCelle):
        riga = []
        for j in range(nCelle):
            riga.append(Cellula(0))
            y+=width+space
            riga[j].rettangolo = pygame.Rect(x, y, width, width)
        griglia.append(riga)
        x+=width+space
        y=baseY

class Cellula:
    def __init__(self, stato):
        self.stato = stato  # Stato della cellula: 0 (morta) o 1 (viva)
        self.colore = pygame.Color("yellow") if stato == 1 else pygame.Color("black")
        self.rettangolo = None

    def cambiaStato(self):
        if self.stato == 0:
            self.stato = 1
            self.colore = pygame.Color("yellow")
        else:
            self.stato = 0
            self.colore = pygame.Color("black")
    
    def copy(self):
        nuova = Cellula(self.stato)
        # se serve copiare anche altri attributi:
        nuova.colore = self.colore
        nuova.rettangolo = self.rettangolo  # attenzione: punta allo stesso oggetto
        return nuova
    

screenWidth = 800
screenHeight = 700

baseX = 5
baseY = -5

width = 10
space = 1

celleX = (screenWidth - baseX) // (width + space)
celleY = (screenHeight - baseY) // (width + space)
nCelle = min(celleX, celleY)

FPS = 10

pygame.init()
screen = pygame.display.set_mode((screenWidth, screenWidth))
pygame.display.set_caption("Gioco della vita")
screen.fill(pygame.Color("gray"))
clock = pygame.time.Clock()

griglia = []
generaCelle()
disegnaCelle()

running = True
start = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #cambia stato cellule
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for i in range(len(griglia)):
                for j in range(len(griglia[i])):
                    if griglia[i][j].rettangolo.collidepoint(pos):
                        griglia[i][j].cambiaStato()
                        pygame.draw.rect(screen, griglia[i][j].colore, griglia[i][j].rettangolo)
                        print(f"Cella cliccata: ({i}, {j}), Nuovo stato: {griglia[i][j].stato}")
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                start = True
            elif event.key == pygame.K_x:
                start = False
        
    if start == True:
        aggiornaGriglia()
        disegnaCelle()
            
        
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()