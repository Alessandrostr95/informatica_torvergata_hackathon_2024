import os


class Solution:

    input_folder = os.path.join("soluzioni", "input", "2")
    output_folder = os.path.join("soluzioni", "output", "2")

    @staticmethod
    def solve(K: int, attrezzatture: list[tuple[str, int, int, int]]) -> int:
        """
        Scrivi la tua soluzione qui.
        """
        pass

    @staticmethod
    def load_input(i: int) -> tuple[int, list[tuple[str, int, int, int]]]:
        """
        Carica il file di input i-esimo, contenuto all'interno della cartella dei file input.
        Questo metodo deve restituire il valore da passare al metodo solve.
        """

        # list dei file presenti nella cartella input
        files = os.listdir(Solution.input_folder)
        files.sort()

        # load file i-esimo
        with open(os.path.join(Solution.input_folder, files[i]), "r") as f:
            K = int(f.readline())
            attrezzatture = [line.strip().split() for line in f.readlines()]

            return K, list(
                map(lambda x: (x[0], int(x[1]), int(x[2]), int(x[3])), attrezzatture)
            )
        
    
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
