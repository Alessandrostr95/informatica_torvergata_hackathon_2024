# Problema 5 (*Gigino idraulico*)

| **Difficoltà** | 🔥🔥🔥🔥🔥 |
|:--------------:|:-----------:|

C'è un problema con il sistema idraulico dell'edificio di Sogene.
Sogene è un edificio con una forma alquanto longilinea, e l'intero sistema idraulico è connesso ad un unico *lungo* tubo principale.
Il tubo principale è suddiviso in $N$ nodi adiacenti, numerati da $0$ a $N-1$.
Ogni nodo controlla la pressione dell'acqua di una intera sezione di Sogene.
Su ognuno di questi nodi è presente una **valvola di sfogo**, che può essere aperta per rilasciare la pressione in eccesso.
Ogni valvola di sfogo $i$ può rilasciare una quantità di pressione pari a $P_i$ unità al minuto.

A Gigino viene dato un semplicissimo incarico: quando la pressione dell'acqua di una sezione di Sogene diventa troppo alta, deve aprire la valvola di sfogo della sezione corrispondente per rilasciare la pressione in eccesso.
Purtroppo però Gigino è il solito pasticcione, e si addormenta durante il lavoro.

Gigino viene svegliato da un rumore assordante: la sirena di allarme del sistema idraulico!
La pressione dell'acqua in tutta Sogene è diventata troppo alta, e si rischia un disastro idraulico.
Il monitor del sistema idraulico comunica che sono disponibili solo $t$ minuti prima che l'intero sistema idraulico esploda.

Gigino deve agire velocemente: deve aprire le valvole di sfogo dei nodi per rilasciare quanta più pressione possibile entro i prossimi $t$ minuti.

Gigino sa che aprire una valvola di sfogo richiede un minuto, e che spostarsi da un nodo al suo vicino richiede un minuto.
Inoltre, se apre la valvola di sfogo del nodo $i$ al tempo $y \leq t$, essa rilascerà una quantità di pressione pari a $P_i \cdot (t - y - 1)$ ($-1$ perché spendo un minuto per aprire la valvola).

Un esempio di come potrebbe essere il sistema idraulico di Sogene è il seguente:
```
Nodi: 0 -- 1 -- 2
Pressione: 5 2 10
t: 7
```

Una possibile strategia per Gigino potrebbe essere:
```
=== Minuto 0 ===
Gigino si trova al nodo 0.
Gigino apre la valvola di sfogo del nodo 0.

=== Minuto 1 ===
La valvola 0 è aperta, sono stati rilasciati 5 unità di pressione fino ad ora.
Gigino si sposta al nodo 1.

=== Minuto 2 ===
La valvola 0 è aperture, sono stati rilasciati 10 unità di pressione fino ad ora.
Gigino apre la valvola di sfogo del nodo 1.

=== Minuto 3 ===
La valvola 0 e 1 sono aperte, sono stati rilasciati 17 unità di pressione fino ad ora.
Gigino si sposta al nodo 2.

=== Minuto 4 ===
La valvola 0 e 1 sono aperte, sono stati rilasciati 24 unità di pressione fino ad ora.
Gigino apre la valvola di sfogo del nodo 2.

=== Minuto 5 ===
La valvola 0, 1 e 2 sono aperte, sono stati rilasciati 41 unità di pressione fino ad ora.
Gigino non fa nulla.

=== Minuto 6 ===
La valvola 0, 1 e 2 sono aperte, sono stati rilasciati 58 unità di pressione fino ad ora.
Gigino non fa nulla.

=== Minuto 7 ===
La valvola 0, 1 e 2 sono aperte, sono stati rilasciati 75 unità di pressione fino ad ora.
Gigino non fa nulla.
```

In questo caso, Gigino ha aperto in ordine le valvole dei nodi `0`, `1` e `2` rilasciato $75$ unità di pressione in $7$ minuti.
È possibile vedere che si può fare meglio.
Per esempio, Gigino avrebbe potuto aprire in ordine le valvole sui nodi `0`, `2` e `1`, rilasciando $79$ unità di pressione in $7$ minuti, anziché $75$.

```
=== Minuto 0 ===
Gigino si trova al nodo 0.
Gigino apre la valvola di sfogo del nodo 0.

=== Minuto 1 ===
La valvola 0 è aperta, sono stati rilasciati 5 unità di pressione fino ad ora.
Gigino si sposta al nodo 1.

=== Minuto 2 ===
La valvola 0 è aperta, sono stati rilasciati 10 unità di pressione fino ad ora.
Gigino si sposta al nodo 2.

=== Minuto 3 ===
La valvola 0 è aperta, sono stati rilasciati 15 unità di pressione fino ad ora.
Gigino apre la valvola di sfogo del nodo 2.

=== Minuto 4 ===
La valvola 0 e 2 sono aperte, sono stati rilasciati 30 unità di pressione fino ad ora.
Gigino si sposta al nodo 1.

=== Minuto 5 ===
La valvola 0 e 2 sono aperte, sono stati rilasciati 45 unità di pressione fino ad ora.
Gigino apre la valvola di sfogo del nodo 1.

=== Minuto 6 ===
La valvola 0, 1 e 2 sono aperte, sono stati rilasciati 62 unità di pressione fino ad ora.
Gigino non fa nulla.

=== Minuto 7 ===
La valvola 0, 1 e 2 sono aperte, sono stati rilasciati 79 unità di pressione fino ad ora.
Gigino non fa nulla.
```

Sapendo che Gigino parte dal nodo $0$ e ha a disposizione $t$ minuti, aiutalo ad individuare **una** sequenza di valvole da aprire che permetta di rilasciare quante più unità di pressione possibile entro i prossimi $t$ minuti.


##### IMPORTANTE
In questo problema non vi è chiesto di trovare necessariamente la soluzione **ottima**, ma una qualsiasi soluzione **ammissibile**.
Ovviamente, il punteggio dipenderà dalla qualità della soluzione trovata.


## Input
Un intero $t$ che rappresenta i minuti a disposizione di Gigino.
Un interno $N$ che rappresenta il numero di nodi del sistema idraulico di Sogene.
Un array $P$ di $N$ interi, dove $P\left[ i \right]$ rappresenta la quantità di pressione $P_i$ che può rilasciare la valvola di sfogo del nodo $i$.


## Output
Un array $A$ di $N$ interi, che rappresenta la sequenza di valvole da aprire.


--------------------

| [**<**](../4/README.md) | [**Home**](../../README.md) | [**>**](../6/README.md)
|:------:|:------:|:------:|

