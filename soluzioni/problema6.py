import os


class Solution:

    input_folder = os.path.join("soluzioni", "input", "6")
    output_folder = os.path.join("soluzioni", "output", "6")

    @staticmethod
    def solve(m: int, buffet: list[int]) -> int:
        """
        Scrivi la tua soluzione qui.

        :param m: numero postazioni consecutive dalle quali si può prendere il cibo
        :param buffet: lista di postazioni di cibo del buffet
        """
        pass

    @staticmethod
    def load_input(i: int) -> tuple[int, list[int]]:
        """
        Carica il file di output i-esimo, contenuto all'interno della cartella dei file output.
        Questo metodo deve restituire il valore presente nel file di output.
        """

        # list dei file presenti nella cartella output
        files = os.listdir(Solution.input_folder)
        files.sort()

        # load file i-esimo
        with open(os.path.join(Solution.input_folder, files[i]), "r") as f:
            lines = f.readlines()
            m = int(lines[0])
            buffet = [l.strip() for l in lines[1:]]
            return m, buffet

    @staticmethod
    def load_output(i: int) -> int:
        """
        Carica il file di output i-esimo, contenuto all'interno della cartella dei file output.
        Questo metodo deve restituire il valore presente nel file di output.
        """

        # list dei file presenti nella cartella output
        files = os.listdir(Solution.output_folder)
        files.sort()

        # load file i-esimo
        with open(os.path.join(Solution.output_folder, files[i]), "r") as f:
            return int(f.read())

