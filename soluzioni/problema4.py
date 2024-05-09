import os


class Solution:

    input_folder = os.path.join("soluzioni", "input", "4")
    output_folder = os.path.join("soluzioni", "output", "4")

    @staticmethod
    def solve(wall: list[list[int]]) -> int:
        """
        Scrivi la tua soluzione qui.

        :param wall: griglia che rappresenta le macchie di muffa sul muro
        """
        pass

    @staticmethod
    def load_input(i: int) -> list[list[int]]:
        """
        Carica il file di input i-esimo, contenuto all'interno della cartella dei file input.
        Questo metodo deve restituire il valore da passare al metodo solve.
        """

        # list dei file presenti nella cartella input
        files = os.listdir(Solution.input_folder)
        files.sort()

        # load file i-esimo
        with open(os.path.join(Solution.input_folder, files[i]), "r") as f:
            lines = f.readlines()
            return [list(map(int, line.strip().split())) for line in lines]

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

