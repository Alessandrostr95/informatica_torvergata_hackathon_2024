# Problema 7 - (*Gigino in magazzino*)

| **Difficoltà** | 🔥🔥 |
|:--------------:|:----:|

Gigino è stato mandato in magazzino.
Nel magazzino del cantiere ci sono solo $2$ scaffali $X$ e $Y$, e su ognuno di essi ci sono delle scatole con pesi $X_1,...,X_n$ e $Y_1,...,Y_m$, rispettivamente.

I carichi sui due scaffali sono **sbilanciati**, ovvero su uno scaffale c'è più peso che sull'altro.

È possibile **scambiare** due scatoloni $i, j$ (di pesi rispettivamente $X_i, Y_j$) in modo tale che i carichi sugli scaffali siano **equilibrati**.

Per esempio, supponiamo di avere i seguenti scaffali
```
X: ___2___18___
Y: ___16_______
```

- Sullo scaffale $X$ abbiamo $2$ scatole di peso $X_1 = 2$ e $X_2 = 18$. Il peso complessivo dello scaffale $X$ è $20$.
- Sullo scaffale $Y$ abbiamo una sola scatola di peso $Y_1 = 16$. Il peso complessivo dello scaffale $Y$ è $16$.

Una possibile soluzoine è quella di scambiare le scatole di peso $X_2$ e $Y_1$.
In questo caso avremo che i due scaffali avranno lo stesso peso, e la nuova disposizione dei pesi sarà:
```
X: ___2___16___
Y: ___18_______
```

A Gigino viene chiesto di individuare quale coppia di scatole $i,j$ deve essere scambiata tra i due scaffali $X$ e $Y$ in modo da equilibrare i pesi.

## Input
Due vettori $X$ e $Y$ di interi, di lunghezze $n$ ed $m$ rispettivamente.


## Output
Una coppia di indici $i,j$ che indica quali pacchi scambiare tra i due scaffali $X,Y$.

--------------

| [**<**](../6/README.md) | [**Home**](../../README.md) | [**>**](../8/README.md) |
|:-----:|:-----:|:-----:|