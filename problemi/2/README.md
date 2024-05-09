# Problema 2 (*Affitto attrezzatura*)

| **Difficoltà** | 🔥🔥 |
|---------------:|:----:|

Come primo incarico a Gigino viene chiesto di gestire l'affitto delle varie attrezzature per i lavori.
A Gigino viene fornita una *lista* di attrezzi, identificati con un codice, e per ciascun attrezzo viene fornito il **prezzo giornaliero** dell'affitto e il range di giorni per cui l'attrezzo deve essere affittato.

Per esempio, la lista di attrezzi potrebbe essere la seguente:
```
MARTELLONE 10 1 3
TRAPANO 5 1 5
SEGACCIO 3 4 7
MARTELLONE 10 5 10
```
In questo caso è richiesto di:
- affittare il MARTELLONE dal giorno 1 al giorno 3 al prezzo di 10 euro al giorno, e dal giorno 5 al giorno 10 al prezzo di 10 euro al giorno.
- affittare il TRAPANO dal giorno 1 al giorno 5 al prezzo di 5 euro al giorno.
- affittare il SEGACCIO dal giorno 4 al giorno 7 al prezzo di 3 euro al giorno.

Il costo totale dell'affitto è quindi di $10 \times 3 + 5 \times 5 + 3 \times 4 + 10 \times 6 = 127$ euro.

Esiste però l'opportunità di affittare uno **strumento universale** che può sostituire uno qualsiasi degli attrezzi.
Lo strumento universale ha un costo giornaliero di $K$, e se affittato il giorno $i$ può essere usato al posto di **tutti** gli strumenti necessari il giorno $i$.
Quindi, se affittato opportunamente può portare ad un risparmio.

Per esempio, supponiamo che il costo dello strumento universale sia $K = 15$.
Nell'esempio precedente, se Gigino affitta lo strumento universale il giorno $5$, il costo complessivo sarà di $10 \times 3 + 5 \times 4 + 3 \times 3 + 10 \times 5 + 15 \times 1 = 124$ euro, risparmiando quindi $3$ euro.

Aiuta Gigino a calcolare il costo **minimo** dell'affitto delle attrezzature.

## Input
In input si avrà un intero $K$ che rappresenta il costo giornaliero dello strumento universale, e una lista di *quadruple* con le seguenti informazioni **in ordine**:
- il nome dell'attrezzo (una breve stringa senza spazi)
- il costo giornaliero dell'affitto dell'attrezzo
- il giorno di inizio dell'affitto
- il giorno di fine dell'affitto

**IMPORTANTE**: uno stesso attrezzo può comparire più volte nella lista di quadruple, ma i range di giorni non si sovrappongono mai. Inoltre, il costo giornaliero di un attrezzo che compare più volte è sempre lo stesso.

## Output
Il programma deve restituire il costo minimo dell'affitto delle attrezzature.


-------------

| [**<**](../1/README.md) | [**Home**](../../README.md) | [**>**](../3/README.md) |
|:-----:|:-----:|:-----:|

