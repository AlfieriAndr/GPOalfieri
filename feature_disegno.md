# Feature 3 — Modalità Disegno

##  Descrizione
Questa feature introduce una **modalità disegno** che permette all’utente di modificare velocemente la griglia trascinando il mouse.  
Invece di cliccare una cella per volta, ora è possibile “pennellare” celle vive o cancellarle mentre la simulazione è ferma.

La modalità disegno migliora notevolmente l’usabilità, rendendo più semplice creare pattern complessi o configurazioni personalizzate.


##  Obiettivi della feature

- Permettere all’utente di attivare celle vive trascinando il mouse.
- Permettere all’utente di cancellare celle trascinando il mouse con il tasto destro.
- Impedire modifiche alla griglia durante la simulazione.
- Aggiornare graficamente le celle in tempo reale.
- Aggiungere documentazione e aggiornare il README.


##  Dettagli tecnici dell’implementazione

### Modalità disegno
- *Tasto sinistro del mouse*: disegna celle vive.
- *Tasto destro del mouse*: cancella celle (stato morto).
- Attivazione solo se `start == False`.

### Gestione eventi Pygame
```python
if event.type == pygame.MOUSEBUTTONDOWN and not start:
    if event.button == 1:
        disegna = True
    elif event.button == 3:
        cancella = True
