# Problema 4 (*Problemi di muffa*)
Uno dei problemi che affliggono il vecchio edificio di sogene è la muffa.
Per combattere la muffa, Gigino ha deciso di fare un trattamento antimuffa alle pareti.
Il trattamento antimuffa consiste nell'applicare un prodotto specifico sulle pareti per eliminare la muffa e prevenire la sua ricomparsa.

Il prodotto antimuffa ha un costo al metro quadrato di 5 euro, e visto che Gigino vuole fare bella figura con la AVL srl, ha deciso di applicare il minimo prodotto possibile.
Per fare ciò, Gigino deve applicare il prodotto **solamente** sulle macchie di muffa, e non su tutta la parete.

Per capire dove applicare il prodotto, Gigino utilizza un sensore speciale che gli permette di rilevare la presenza di muffa sulle pareti.
Il sensore produce una matrice $A$ di dimensione `N x M` in cui ogni cella contiene un valore **intero**.
Se $A[i][j] = 0$, allora la cella $(i, j)$ non contiene muffa, altrimenti se $A[i][j] > 0$, allora la cella $(i, j)$ contiene muffa.

Per essere sicuri di avere abbastanza prodotto antimuffa è meglio comprarne un po' di più, ma non troppo.
In particolare, a Gigino viene chiesto di calcolare un **upper bound** della quantità di prodotto antimuffa.
Una quantità di prodotto *sufficiente* è sicuramente pari al numero di macchie di muffa presenti sulle pareti moltiplicato per l'area della macchia più grande.

Ecco un esempio di input/output:

```
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 0 1 1 1 1 0 0 0 0 0 0
0 0 0 1 1 0 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 1
0 1 1 0 0 0 0 0 0 0 0 0 0 1 1 1
0 1 1 0 0 0 0 0 0 0 0 0 0 1 1 1
```

In questo caso abbiamo 4 macchie di muffa, e l'area della macchia più grande è 14.
Quindi la quantità di prodotto antimuffa sufficiente è $4 \times 14 = 56$.

Aiuta Gigino a calcolare la quantità di prodotto antimuffa *sufficiente* per eliminare la muffa dalle pareti.

## Input
Una matrice $A$ di dimensione `N x M` in cui ogni cella contiene un valore **intero**.

## Output
Un numero intero, la quantità di prodotto antimuffa sufficiente per eliminare la muffa dalle pareti.

