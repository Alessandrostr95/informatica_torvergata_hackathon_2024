# Problema 4 (*Problemi di muffa*)

| **Difficoltà** | 🔥🔥🔥 |
|:--------------:|:------:|

Uno dei problemi che affliggono il vecchio edificio di Sogene è la muffa.
Per combattere la muffa bisogna fare un trattamento antimuffa alle pareti.
Il trattamento antimuffa consiste nell'applicare un prodotto specifico sulle pareti per eliminare la muffa e prevenire la sua ricomparsa.

A Gigino viene chiesto di applicare il trattamento **solamente** sulla macchia di muffa più grande.
Il prodotto antimuffa ha un costo al metro quadro abbastanza elevto, e visto che Gigino vuole fare bella figura con la AVL srl, ha deciso di applicare il minimo prodotto possibile.
Per fare ciò, Gigino deve applicare una quantità di prodotto pari all'**area** della macchia più grande (non di più, non di meno).

Per capire dove applicare il prodotto, Gigino utilizza un sensore speciale che gli permette di rilevare la presenza di muffa sulle pareti.
Il sensore produce una matrice $A$ di dimensione $N \times M$ in cui ogni cella contiene un valore **intero**.
Se $A[i][j] = 0$, allora la cella $(i, j)$ **non** contiene muffa, altrimenti se $A[i][j] > 0$ la cella $(i, j)$ contiene muffa.

Ecco un esempio:

```
0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0
0 0 1 1 0 0 0 0 0 0 1 1 0 0 0 0
0 0 1 1 1 0 1 1 1 1 0 0 0 0 0 0
0 0 0 1 1 0 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 1
0 1 1 0 0 0 0 0 0 0 0 0 0 1 1 1
0 1 1 0 0 0 0 0 0 0 0 0 0 1 1 1
```

Una macchia di muffa è una **regione** di celle **adiacenti** tra loro che contengono muffa.
Due celle sono adiacenti se sono **orizzontalmente** o **verticalmente** vicine (però **non** in diagonale).

Nel nosrto caso abbiamo $5$ macchie di muffa, e l'area della macchia più grande è $14$.
Aiuta Gigino a calcolare la quantità di prodotto antimuffa che gli serve per 

## Input
Una matrice $A$ di dimensione $N \times M$ in cui ogni cella contiene un valore **intero**.

## Output
Un numero intero pari all'area della macchia di muffa più grande.

--------------

| [**<**](../3/README.md) | [**Home**](../../README.md) | [**>**](../5/README.md) |
|:-----:|:-----:|:-----:|

