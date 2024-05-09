import os


class Solution:

    input_folder = os.path.join("soluzioni", "input", "7")
    output_folder = os.path.join("soluzioni", "output", "7")

    @staticmethod
    def solve(X: list[int], Y: list[int]) -> tuple[int, int]:
        """
        Scrivi la tua soluzione qui.

        :param X: lista di interi che rappresenta i pesi delle scatole sullo scaffale X
        :param Y: lista di interi che rappresenta i pesi delle scatole sullo scaffale Y

        :return: una tupla di due interi i, j che rappresentano le posizioni delle scatole da scambiare, in modo che
                    la somma dei pesi delle scatole su X e Y diventi uguale dopo lo scambio.
        """
        pass

    @staticmethod
    def load_input(i: int) -> tuple[list[int], list[int]]:
        """
        Carica il file di output i-esimo, contenuto all'interno della cartella dei file output.
        Questo metodo deve restituire il valore presente nel file di output.
        """

        # list dei file presenti nella cartella output
        files = os.listdir(Solution.input_folder)
        files.sort()

        # load file i-esimo
        with open(os.path.join(Solution.input_folder, files[i]), "r") as f:
            X = list(map(int, f.readline().split()))
            Y = list(map(int, f.readline().split()))
            return X, Y

    @staticmethod
    def load_output(i: int) -> tuple[int, int]:
        """
        Carica il file di output i-esimo, contenuto all'interno della cartella dei file output.
        Questo metodo deve restituire il valore presente nel file di output.
        """

        # list dei file presenti nella cartella output
        files = os.listdir(Solution.output_folder)
        files.sort()

        # load file i-esimo
        with open(os.path.join(Solution.output_folder, files[i]), "r") as f:
            i, j = map(int, f.readline().split())
            return i, j

    @staticmethod
    def evaluate_solution(istance_number: int, solution: tuple[int, int]) -> int:
        X, Y = Solution.load_input(istance_number)
        i, j = solution

        assert 0 <= i < len(X)
        assert 0 <= j < len(Y)

        if sum(X) - X[i] + Y[j] == sum(Y) - Y[j] + X[i]:
            return 10
        else:
            return 0

