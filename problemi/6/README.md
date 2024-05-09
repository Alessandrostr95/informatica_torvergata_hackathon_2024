# Problema 6 (*Gigino al buffet*)

| **Difficoltà** | 🔥🔥 |
|:--------------:|:----:|

E' ora di pranzo e la AVL s.r.l. ha preparato un [buffet](https://www.hoteliermiddleeast.com/2021/06/DYbTCR5K-buffet-HME-CID-CME.jpg) per i suoi dipendenti.

Le portate del buffet sono poste una accanto all'altra lungo una **lunga** tavolata.
La tavolata del buffet è rappresentata come una sequenza $A_1, ..., A_n$ di portate, ed ogni portata può trovarsi ripetuta in diversi punti del buffet.

Per esempio:
```
lasagna - lasagna - cannelloni - slasiccia - lasagna - cannelloni - lasagna
```

Gigino può iniziare da un punto qualsiasi della tavolata, e potrà servirsi e spostarsi verso **destra** solamente per $M$ volte consecutive.
Per esempio, se $M = 3$ e Gigino decide di partire dalla posizione $i$, potrà servirsi solamente delle portate $A_i, A_{i+1}, A_{i+2}$.
Nel caso dell'esempio precedente, Gigino può partire da una delle seguenti posizioni:

1. `lasagna` `lasagna` `cannelloni`
2. `lasagna` `cannelloni` `slasiccia`
3. `cannelloni` `slasiccia` `lasagna`
4. `slasiccia` `lasagna` `cannelloni`
5. `lasagna` `cannelloni` `lasagna`
    
Gigino, essendo goloso, vorrebbe trovare la posizione di partenza che gli consenta di servirsi con quante più portate **differenti** possibile.
Nell'esempio precedente, le posizioni di partenza migliori sono le posizioni $2$, $3$ e $4$, in quanto consentono a Gigino di mangire ben $3$ portate *differenti*.
Se invece parte dalla posizione $1$ o dalla posizione $5$, può mangare solamente $2$ tipologie di portate differenti: `lasagna` e `cannelloni`.

Aiuta Gigino a capire qual è la quantità massima di portate differenti che può mangiare dal buffet, sapendo che può servirsi solamente di $M$ postazioni contigue.

## Input
Una vettore $A$ di $n$ stringhe, rappresentanti le portate presenti nelle $n$ postazioni del buffet, e un intero $M < n$.

## Output
La quantità massima di portate differenti che Gigino può mangiare, spaendo che può servirsi solamente da $M$ postazioni contigue.

--------------

| [**<**](../5/README.md) | [**Home**](../../README.md) | [**>**](../7/README.md) |
|:-----:|:-----:|:-----:|

