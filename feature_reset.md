# Feature 2 — Modalità Reset

##  Descrizione
Questa feature introduce una **modalità reset** che permette all’utente di resettare la griglia quando il gioco non è avviato.


##  Obiettivi della feature

- Permettere all’utente di resettare la griglia.
- Impedire modifiche alla griglia durante la simulazione.
- Aggiungere documentazione e aggiornare il README.

##  Dettagli tecnici dell’implementazione

### Funzione Reset
- *Tasto z*: reset delle celle.
- Attivazione solo se `start == False`.

### Gestione eventi Pygame
```python
elif event.key == pygame.K_z and not start:
    griglia = generaCelle()
    disegnaCelle(griglia)
