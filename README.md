# Dashboard Monitor di Sistema

Dashboard web in tempo reale per monitorare CPU, RAM e disco su Linux.

## Cosa fa
- Mostra CPU, RAM e disco in tempo reale in una pagina web
- Si aggiorna automaticamente ogni 5 secondi
- I valori diventano rossi quando superano le soglie di alert
- Accessibile dal browser su http://127.0.0.1:5000

## Tecnologie usate
- Python 3
- Flask
- psutil
- HTML5 / CSS3
- Linux (Debian)

## Come si usa
1. Installa le dipendenze: `sudo apt install python3-flask python3-psutil`
2. Avvia il server: `python3 app.py`
3. Apri il browser su `http://127.0.0.1:5000`

## Autrice
Progetto personale realizzato durante il percorso di self-learning in ambito IT.
