# Introduzione
Gigino Amatino, un ex-studente di informatica dell'università di Tor Vergata, era famoso più per le sue abilità nel saltare lezioni che per la sua dedizione allo studio.
Dopo un numero incalcolabile di anni fuori corso, i suoi genitori capirono che Gigino non era proprio fatto per lo studio e decisero che era ora di tagliare i cordoni per costringerlo a cercare un lavoro.


Il primo impiego di Gigino è un impiego da operaio presso la rinomata "Azienda Veloci Lavorazioni S.p.A.", meglio conosciuta come "AVL S.p.A.".
Come suggerisce il nome, la AVL è famosa per la sua efficienza ineguagliabile nelle ristrutturazioni.
E se Gigino vuole scalare le gerarchie aziendali, deve dimostrare di essere altrettanto veloce nel suo lavoro.

Ironia della sorte, come primo incarico Gigino è assegnato in un cantiere proprio nel cuore dell'università di Tor Vergata, là dove si trovava la facoltà di informatica che aveva abbandonato.
Quello che Gigino ancora non sa è che si troverà a dover affrontare problemi che sembrano usciti proprio da uno dei suoi vecchi esami di algoritmi e strutture dati, quelli che pensava di aver dimenticato insieme agli altri esami falliti.

Aiuta il nostro Gigino Amatino a dimostrare che anche uno che ha preferito la pausa caffè alla studio può avere il suo momento di gloria. E chissà, forse, tra un tubo piegato e una matrice ordinata, potrebbe ritrovare la sua strada verso il successo, a modo suo...

# Istruzioni
Sono stati forniti 9 problemi, numerati da 0 a 8, che dovrete risolvere.
Ad ogni problema è associato un livello di difficoltà, espresso in fiamme 🔥.
Più fiamme indicano una maggiore difficoltà, da un minimo di 1 a un massimo di 5.
Dovrete scrivere un programma in `Python` che risolva il problema assegnato, seguendo le specifiche fornite.
Ad ogni problema risolto vi verrà assegnato un **punteggio** che dipenderà da:
- il numero di test superati
- le performance della vostra soluzione
- la complessità della vostra soluzione

Alla fine dell'evento, il team con il punteggio più alto sarà dichiarato vincitore di questa edizione dell' Hackathon Tor Vergata 2024!

Come primo passo dovrete **clonare** il repository dell'evento sul vostro computer, utilizzando il comando:
```bash
git clone <url>
```
Se siete utenti Windows (🐣) o avete timore di usare il terminale, potete scaricare un file `.zip` di questa repository tramite il [link]().

Una volta clonata la repository, troverete le tracce dei problemi nelle rispettive cartelle `problemi/<numero problema>`.
Ogni cartella contiene un file `README.md` che descrive il problema da risolvere, i vincoli e i dettagli dell'input e dell'output.

Per ogni problema è fornito un file `.py` nel path `soluzioni/problema<numero problema>.py` all'interno del quale potrete trovare una funzione `solve`.
Il vostro compito è quello di implementare la funzione `solve` in modo che risolva il problema relativo al file.

Per esempio, se volete risolvere il problema `0`, dovrete per prima cosa aprire il file `soluzioni/problema0.py`.
Al suo interno trovere uno **scheletro** della funzione `solve` che dovrete implementare.
```python
class Solution:

    # ...

    @staticmethod
    def solve(n: int) -> int:
        """
        Scrivi qui la tua soluzione
        """
        pass

    # ...
```

Leggendo la *firma* della funzione `solve` potrete capire quali sono i parametri in input e il loro tipo, e quale è il tipo di ritorno della funzione.
In questo caso la funzione `solve` prende in input un **intero** `n` e restituisce un **intero**.

All'interno del file python ci sono molti altri metodi e funzioni, i quali **NON** devono essere modificate per nessuno motivo.
Questi metodi sono utili per il corretto funzionamento dei test che valuteranno le vostre soluzioni, e quelsiasi vostro tentativo di modifica verrà rilevato!

Una volta implementata la funzione `solve`, potrete **testare** la vostra soluzione eseguendo il file `run.py` presente nella root del progetto.
Dovrete eseguire i seguenti comandi da terminale:
```bash
# Esegui TUTTI i test
python3 run.py

# Esegui solo i test per un problema specifico, per esempio il problema 3
python3 run.py -t 3
python3 run.py --test 3
```

Il programma `run.py` esegue una serie di test basati su input ed output pre-calcolati, e vi darà un resoconto di quanti test sono stati superati e quanti no, qual è il punteggio ottenuto e quanto tempo è stato impiegato per eseguire i test.

Per ogni istanza di test superata, otterrete un punteggio variabile in base alla complessità del problema e alla performance della vostra soluzione.
Il punteggio totale sarà la somma dei punteggi ottenuti per ogni test superato.

**Attenzione**: ogni problema ha un *tempo limite* entro il quale la vostra soluzione deve restituire un risultato.
Se il tempo limite viene superato, il test verrà considerato fallito e non otterrete alcun punteggio per quel test.

Buona divertimento!

# Problemi
- [Problema 0](problemi/0/README.md) 🔥
- [Problema 1](problemi/1/README.md) 🔥🔥
- [Problema 2](problemi/2/README.md) 🔥🔥
- [Problema 3](problemi/3/README.md) 🔥🔥🔥🔥
- [Problema 4](problemi/4/README.md) 🔥🔥🔥
- [Problema 5](problemi/5/README.md) 🔥🔥🔥🔥🔥
- [Problema 6](problemi/6/README.md) 🔥🔥
- [Problema 7](problemi/7/README.md) 🔥🔥
- [Problema 8](problemi/8/README.md) 🔥🔥🔥