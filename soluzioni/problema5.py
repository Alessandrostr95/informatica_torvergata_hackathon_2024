import os


class Solution:

    input_folder = os.path.join("soluzioni", "input", "5")
    output_folder = os.path.join("soluzioni", "output", "5")

    @staticmethod
    def solve(t: int, n: int, valves: list[int]) -> list[int]:
        """
        Scrivi la tua soluzione qui.
        """
        pass

    @staticmethod
    def load_input(i: int) -> tuple[int, int, list[int]]:
        """
        Carica il file di input i-esimo, contenuto all'interno della cartella dei file input.
        Questo metodo deve restituire il valore da passare al metodo solve.
        """

        # list dei file presenti nella cartella input
        files = os.listdir(Solution.input_folder)
        files.sort()

        # load file i-esimo
        with open(os.path.join(Solution.input_folder, files[i]), "r") as f:
            t = int(f.readline().strip())
            n = int(f.readline().strip())
            valves = [int(x) for x in f.readline().strip().split()]
            return t, n, valves

    @staticmethod
    def load_output(i: int) -> int:
        """
        Carica il file di output i-esimo, contenuto all'interno della cartella dei file output.
        Questo metodo deve restituire il valore da confrontare con quello restituito dal metodo solve.
        """

        # list dei file presenti nella cartella output
        files = os.listdir(Solution.output_folder)
        files.sort()

        # load file i-esimo
        with open(os.path.join(Solution.output_folder, files[i]), "r") as f:
            return int(f.readline().strip())

    @staticmethod
    def evaluate_solution(istance_number: int, solution: list[int]) -> float:
        t, n, valves = Solution.load_input(istance_number)
        max_value = Solution.load_output(istance_number)

        assert n == len(solution)
        assert t >= 0

        value = 0
        last = 0
        t += 1
        for i in range(n):
            current = solution[i]
            t -= abs(last - current) + 1
            if t < 0:
                break

            value += t * valves[current]
            last = current

        return 10 * value / max_value
