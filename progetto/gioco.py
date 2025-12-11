import pygame
import random


# Gioco della Vita di Conway implementato con Pygame.
# REGOLE: https://editor.p5js.org/codingtrain/sketches/UtSMCB1zv

def aggiornaGriglia():
    """
    Calcola la generazione successiva della griglia in base alle regole
    del Gioco della Vita.

    Per ogni cella:
    - conta le vicine vive
    - applica le regole di sopravvivenza/morte/nascita
    """
    nuovaGriglia = []
    global griglia
    for x in range(celleX):
        riga = []
        for y in range(celleY):
            vicineVive = 0
            # considero solo le celle che non sono sul bordo
            if 0 < x < len(griglia)-1 and 0 < y < len(griglia[0])-1:
                #controllo le celle vicine
                for vx in [-1, 0, 1]:
                    for vy in [-1, 0, 1]:
                        if not (vx == 0 and vy == 0):  # non conto la cella stessa
                            if griglia[x+vx][y+vy].stato == 1:
                                vicineVive += 1

            #controllo regole vive/muore
            nuovaCella = griglia[x][y].copy()
            if griglia[x][y].stato == 1:
                if vicineVive < 2 or vicineVive > 3:
                    nuovaCella.cambiaStato()
            else:
                if vicineVive == 3:
                    nuovaCella.cambiaStato()

            riga.append(nuovaCella)
        nuovaGriglia.append(riga)
    griglia = nuovaGriglia

def disegnaCelle(arr):
    """
    Ridisegna tutte le celle sullo schermo in base al loro stato.
    """
    for i in range(celleX):
        riga = arr[i]
        for j in range(celleY):
            cellula = riga[j]
            pygame.draw.rect(screen, cellula.colore, cellula.rettangolo)
        
        
def generaCelle():
    """
    Inizializza la griglia di celle.

    Ogni cella viene creata morta (stato 0) e posizionata in una griglia
    regolare usando rettangoli Pygame.
    """
    arr = []
    x = baseX
    y = baseY
    for i in range(celleX):
        riga = []
        for j in range(celleY):
            riga.append(Cellula(0)) #random.randrint(0,1)
            y+=cellWidth+cellSpace
            riga[j].rettangolo = pygame.Rect(x, y, cellWidth, cellWidth)
        arr.append(riga)
        x+=cellWidth+cellSpace
        y=baseY
    return arr

class Cellula:
    """
    Rappresenta una cella del Gioco della Vita.

    Attributi:
    - stato: 0 = morta, 1 = viva
    - colore: giallo se viva, nero se morta
    - rettangolo: area grafica su schermo (pygame.Rect)
    """
    def __init__(self, stato):
        self.stato = stato  # Stato della cellula: 0 (morta) o 1 (viva)
        self.colore = pygame.Color("yellow") if stato == 1 else pygame.Color("black")
        self.rettangolo = None

    def cambiaStato(self):
        """
        Inverte lo stato della cella:
        - se è morta → viva
        - se è viva → morta
        e aggiorna il colore di conseguenza.
        """
        if self.stato == 0:
            self.stato = 1
            self.colore = pygame.Color("yellow")
        else:
            self.stato = 0
            self.colore = pygame.Color("black")
        
    def viva(self):
        """
        Rende la cella viva.
        """
        self.stato = 1
        self.colore = pygame.Color("yellow")

    def morta(self):
        """
        Rende la cella morta.
        """
        self.stato = 0
        self.colore = pygame.Color("black")
    
    def copy(self):
        """
        Restituisce una nuova Cellula con lo stesso stato e gli stessi attributi.

        Nota: il rettangolo viene copiato come riferimento, non duplicato,
        perché rappresenta la stessa posizione a schermo.
        """
        nuova = Cellula(self.stato)
        nuova.colore = self.colore
        nuova.rettangolo = self.rettangolo
        return nuova
    


screenWidth = 800
screenHeight = 700
widthPennello = 5  #larghezza pennello per il disegno
baseX = 5 # posizione di partenza della griglia
baseY = -5
cellWidth = 10 #dimensione cella 
cellSpace = 1 #spaziatura celle
FPS = 10
FPSdisegno = 60
FPSgioco = FPS

celleX = (screenWidth - baseX) // (cellWidth + cellSpace)
celleY = (screenHeight - baseY) // (cellWidth + cellSpace)
nCelle = min(celleX, celleY)

pygame.init()
screen = pygame.display.set_mode((screenWidth, screenWidth))
pygame.display.set_caption("Gioco della vita")
screen.fill(pygame.Color("gray"))
clock = pygame.time.Clock()

griglia = generaCelle()
savedGriglia = []
disegnaCelle(griglia)

running = True
start = False
disegna = False
cancella = False
while running:
    #gestione eventi tasti
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #gestione mouse disegno
        if event.type == pygame.MOUSEBUTTONDOWN and not start:
            FPS = FPSdisegno
            if event.button == 1:  # Sinistro --> disegna
                disegna = True
            elif event.button == 3:  # Destro --> cancella
                cancella = True
        elif event.type == pygame.MOUSEBUTTONUP and not start:
            FPS = FPSgioco
            cancella = False
            disegna = False
        
        #gestione tasti
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c: #start --> c
                start = True
            elif event.key == pygame.K_x: #stop --> x
                start = False
            elif event.key == pygame.K_s and not start: #salva una griglia --> s
                savedGriglia = griglia.copy()
                print("griglia salvata")
            elif event.key == pygame.K_a and not start: #stampa la griglia salvata --> a
                if savedGriglia != []:
                    griglia = savedGriglia.copy()
                    disegnaCelle(griglia)

    #logica di aggiornamento
    if disegna or cancella:
        pos = pygame.mouse.get_pos()
        rect_pos = pygame.Rect(pos[0], pos[1], widthPennello, widthPennello)
        for i in range(len(griglia)):
            for j in range(len(griglia[i])):
                if griglia[i][j].rettangolo.colliderect(rect_pos):
                    if disegna: griglia[i][j].viva()
                    else: griglia[i][j].morta()
                    pygame.draw.rect(screen, griglia[i][j].colore, griglia[i][j].rettangolo)
                    print(f"Cella cliccata: ({i}, {j}), Nuovo stato: {griglia[i][j].stato}")
        
    if start == True:
        aggiornaGriglia()
        disegnaCelle(griglia)
            
        
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()