# Feature 4 — Salvataggio e caricamento della configurazione (in memoria)

##  Descrizione
Questa feature introduce la possibilità di **salvare temporaneamente** la configurazione corrente della griglia direttamente **in memoria**, senza usare file esterni.

Il salvataggio avviene copiando la griglia attuale in una variabile dedicata (`savedGriglia`).  
Il caricamento ripristina la griglia a partire da questa copia.

Si tratta di uno “snapshot” dello stato corrente del gioco, valido solo finché il programma rimane aperto.


##  Obiettivi della feature

- Salvare la configurazione della griglia in una variabile interna.
- Consentire il ripristino dello stato salvato.
- Evitare salvataggi durante la simulazione (permesso solo quando `start == False`).
- Aggiornare graficamente la griglia dopo il caricamento.
- Documentare la feature e aggiornare il README.


## Dettagli tecnici dell’implementazione

### ► Come funziona il salvataggio
Alla pressione del tasto **S**, viene creata una **copia superficiale** della griglia:

```python
savedGriglia = griglia.copy()