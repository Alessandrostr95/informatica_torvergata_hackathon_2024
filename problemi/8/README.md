# Problema 8 (*Gigino demolitore*)

| **Difficoltà** | 🔥🔥🔥 |
|:--------------:|:------:|

Vista l'indole di Gigino nel fare danni, la AVL s.r.l. ha deciso di promuoverlo a ruolo di **demolitore**.
Viene chiesto a Gigino di abbattere un muro usando il nuovo modello di [martello demolitore](https://www.utensileriaonline.it/images/bosch/martello-demolitore-GSH-5-CE-Professional-Bosch-0611321000_03.jpg) appena acquistato dall'azienda.
Prima di accendere il martello Gigino deve attaccare la presa elettrica al muro, ma prima di farlo deve **assolutamente** assicurarsi che la manopola del martello sia impostata correttamente.
Se così non fosse, il martello andrebbe in corto circuito e Gigino rischierebbe di rimanere fulminato!

Per fortuna, la ditta che ha costruito il martello demolitore ha fornito un **manuale d'uso** che spiega come impostare la manopola di tutti i modelli di martello demolitore disponibili in commercio.
Gigino dovrà solamente trovare il modello del suo martello nel manuale e impostare la manopola come indicato.

Ogni modello di martello in commercio è identificato da un **codice** univoco, composto da **due stringhe** di lunghezza variabile.
Per esempio, il modello `Aa32-Cf12` è identificato dalle stringhe `Aa32` e `Cf12`.
Ad ogni stringa è associato un **valore numerico ignoto**!

Il valore energetico di un modello di martello è dato dal **rapporto** tra il valore numerico della prima stringa e il valore numerico della seconda stringa del codice del modello.
Per esempio, per il modello `Aa32-Cf12` il valore energetico è `Aa32 / Cf12 = 2`.

Nel manuale d'uso è presente solamente il valore energetico di ogni modello.
Prendiamo per esempio il manuale d'uso seguente:
```
Aa32-Cf12 -> 2
Bb12-Dd34 -> 3
Cf12-Ee78 -> 1
```

- Il modello `Aa32-Cf12` ha valore energetico `Aa32 / Cf12 = 2`.
- Il modello `Bb12-Dd34` ha valore energetico `Bb12 / Dd34 = 3`.
- Il modello `Cf12-Ee78` ha valore energetico `Cf12 / Ee78 = 1`.


Purtroppo, durante la pausa caffè, Gigino ha versato del caffè sul manuale ed ora sono leggibili solamente i valori energetici di alcuni modelli.
Inoltre, la macchia di caffè ha cancellato il valore energetico del modello di martello che la AVL ha appena acquistato.

Aiuta Gigino a derivare il valore energetico del modello di martello che deve utilizzare per abbattere il muro, in modo da non rischiare di rimanere fulminato!

## Input
La stringa $M$ che indica il modello del martello demolitore di Gigino, e una lista di coppie $(m, v)$, dove $m$ è una stringa che indica il modello di un martello e $v$ è un numero che indica il valore energetico del martello.

## Output
Un valore numerico che indica il valore energetico del modello $M$.

--------------

| [**<**](../7/README.md) | [**Home**](../../README.md) |
|:--------------------------------:|:-------------------------:|


