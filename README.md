# Gioco della Vita — Simulazione con Pygame

Questo progetto è un’implementazione del **Game of Life** di *John Conway*, realizzata in **Python** tramite la libreria **Pygame**.
L’utente può modificare la configurazione iniziale cliccando sulla griglia e avviare la simulazione secondo le regole classiche dell’automa cellulare.

## Funzionalità principali

* Griglia quadrata generata dinamicamente in base alle dimensioni della finestra.
* Possibilità di **attivare/disattivare** ogni cella cliccando con il mouse.
* Avvio della simulazione tramite tastiera.
* Evoluzione automatica della griglia secondo le regole originali del Game of Life.
* Visualizzazione grafica tramite Pygame.

## Comandi

| Input                     | Azione                                |
| ------------------------- | ------------------------------------- |
| **Click sinistro**        | Attiva una cella (viva)                                     |
| **Click destro**          | Disattiva una cella (morta)                                 |
| **Trascinamento mouse**   | Modalità disegno/cancellazione                              |
| **C**                     | Avvia la simulazione                  |
| **X**                     | Ferma la simulazione                  |
| **S** | Salva lo stato attuale della griglia |
| **A** | Ripristina la configurazione salvata e la ridisegna |
| **Z** | Resetta la griglia |
| **Tasto chiudi finestra** | Termina il programma                  |


## Modalità disegno

La **modalità disegno** permette di modificare rapidamente la configurazione iniziale trascinando il mouse sulla griglia.

Funzionamento:
- Tenendo premuto il tasto sinistro si “pennellano” celle vive.
- Tenendo premuto il tasto destro si cancellano le celle (stato morto).
- La modalità è attiva solo se la simulazione non è in esecuzione.

Utilità:
- Permette di creare pattern complessi in modo rapido.
- Facilita la sperimentazione con diverse configurazioni iniziali.

## Salvataggio e caricamento della configurazione (in memoria)
Il programma permette di **salvare temporaneamente** la configurazione attuale della griglia in memoria e di ripristinarla successivamente.

## Reset della griglia
Il programma permette di **resettare la griglia** tornando allo stato originale rendendo morte tutte le celle.

### Note
- Il salvataggio e il reset sono disponibili **solo con simulazione ferma**.
- Il salvataggio NON è permanente: viene perso quando il programma viene chiuso.

## Regole del Game of Life

Per ogni generazione, ogni cella segue queste regole:

1. **Sopravvivenza:**
   Una cella viva continua a vivere solo se ha **2 o 3 vicine vive**.
2. **Morte per solitudine:**
   Meno di 2 vicine → la cella muore.
3. **Morte per sovrappopolazione:**
   Più di 3 vicine → la cella muore.
4. **Nascita:**
   Una cella morta con **esattamente 3 vicine vive** diventa viva.

L’implementazione si trova nel file `gioco.py` .


## Struttura del progetto

```
📁 progetto
 ├── gioco.py
 └── (eventuali altri file)
README.md
```


##  Avvio del progetto

### 1. Installazione dipendenze

Assicurati di avere installato Python 3.x e Pygame:

```bash
pip install pygame
```

### 2. Avvio del programma

```bash
python gioco.py
```

## Possibili estensioni

* Start/Stop più avanzato → pulsanti grafici anziché tastiera
* ~~Reset della griglia~~
* ~~Blocco delle celle durante la simulazione~~
* Aggiunta di pattern predefiniti
* Modalità di esecuzione lenta/veloce
* ~~Salvataggio/caricamento configurazioni~~     
* ~~Modalità "disegno" per attivare/disattivare le celle~~
* Interfaccia grafica migliorata

##  Autori

Zilioli Christian - Alfieri Andrea - Paggi Matteo


