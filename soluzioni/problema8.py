import os


class Solution:

    input_folder = os.path.join("soluzioni", "input", "8")
    output_folder = os.path.join("soluzioni", "output", "8")

    @staticmethod
    def solve(model: str, values: list[tuple[str, float]]) -> int:
        """
        Scrivi la tua soluzione qui.

        :param model: stringa che rappresenta il modello del martello pneumatico
        :param values: lista di tuple (modello, valore energetico)
        """
        pass

    @staticmethod
    def load_input(i: int) -> tuple[str, list[str, float]]:
        """
        Carica il file di input i-esimo, contenuto all'interno della cartella dei file input.
        Questo metodo deve restituire il valore da passare al metodo solve.
        """

        # list dei file presenti nella cartella input
        files = os.listdir(Solution.input_folder)
        files.sort()

        # load file i-esimo
        with open(os.path.join(Solution.input_folder, files[i]), "r") as f:
            x = f.readline().strip()
            edges = [line.split(" -> ") for line in f.readlines()]
            edges = [(u, float(w)) for u, w in edges]
            return x, edges

    @staticmethod
    def load_output(i: int) -> float:
        """
        Carica il file di output i-esimo, contenuto all'interno della cartella dei file output.
        Questo metodo deve restit"75H", "YkC"uire il valore presente nel file di output.
        """

        # list dei file presenti nella cartella output
        files = os.listdir(Solution.output_folder)
        files.sort()

        # load file i-esimo
        with open(os.path.join(Solution.output_folder, files[i]), "r") as f:
            return float(f.read())

