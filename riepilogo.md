# Riepilogo del lavoro di gruppo

##  Componenti
- Zilioli Christian  
- Alfieri Andrea  
- Paggi Matteo  

---

## Suddivisione dei compiti

Il progetto è stato suddiviso in funzionalità (*feature*), ciascuna sviluppata in un branch dedicato e collegata a una issue GitHub.

- **Zilioli Christian**  
  - Feature: Modalità disegno  
  - Issue: #3  
  - Branch: `feature/3-modalita-disegno`  

- **Alfieri Andrea**  
  - Feature: Reset della griglia  
  - Issue: #2  
  - Branch: `feature/2-reset`  

- **Paggi Matteo**  
  - Feature: Salvataggio configurazione  
  - Issue: #4  
  - Branch: `feature/4-salvataggio`  

---

## 🔀 Organizzazione del lavoro

È stato adottato un workflow ispirato a **GitFlow**:

- `master` come branch stabile
- `develop` come branch di integrazione
- `feature/...` per lo sviluppo delle singole funzionalità

Le feature sono state integrate tramite **Pull Request** collegate alle rispettive issue (`Closes #...`).

---

## 📄 Documentazione e CI/CD

- Il codice è stato commentato e documentato.
- È stata implementata una pipeline di **CI/CD** con GitHub Actions.
- La documentazione del codice viene generata automaticamente con **pdoc** e pubblicata su **GitHub Pages**.

---
