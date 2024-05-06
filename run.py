import time
import soluzioni
import signal
import os
from pprint import pprint

TIMEOUT = [
    3,  # problem 0
    20,  # problem 1
    3,  # problem 2
    3,  # problem 3
    3,  # problem 4
]


def color_print(text: str, color: str, **kwargs):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "purple": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
    }
    end = kwargs.get("end", "\n")
    print(f"{colors[color]}{text}\033[0m", end=end)


def timeout_handler(signum, frame):
    raise TimeoutError("Timeout occurred!")


def run_solution(problem_number: int, args) -> int:
    problem = soluzioni.problem[problem_number]

    if isinstance(args, (tuple)):
        return problem.solve(*args)
    else:
        return problem.solve(args)


def run(problem_number: int, args, timeout: int) -> dict[str, any]:
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)
    start_time = time.time()
    test_info = {
        "timeout": False,
        "result": None,
        "time": None,
        "error": False,
        "error_message": "",
    }

    try:
        result = run_solution(problem_number, args)
        delta = time.time() - start_time
        test_info["result"] = result
        test_info["time"] = delta
    except TimeoutError:
        test_info["timeout"] = True
    except Exception as e:
        test_info["error"] = True
        test_info["error_message"] = str(e)
    finally:
        signal.alarm(0)  # Disabilita l'allarme al termine

    return test_info


def load_input(problem_number: int) -> tuple:

    num_tests = len(os.listdir(os.path.join("soluzioni", "input", f"{problem_number}")))

    inputs = []
    for i in range(num_tests):
        inputs.append(soluzioni.problem[problem_number].load_input(i))

    return tuple(inputs)


def load_output(problem_number: int) -> tuple:
    num_tests = len(
        os.listdir(os.path.join("soluzioni", "output", f"{problem_number}"))
    )

    outputs = []
    for i in range(num_tests):
        outputs.append(soluzioni.problem[problem_number].load_output(i))

    return tuple(outputs)


def test(problem_number: int) -> float:
    inputs = load_input(problem_number)
    outputs = load_output(problem_number)

    start_time = time.time()

    print(f"Running tests for problem {problem_number}...")
    score = 0
    normalization_factor = 0
    timeout = TIMEOUT[problem_number]

    for i, (input, output) in enumerate(zip(inputs, outputs)):
        normalization_factor += 2**i

        # print without caching
        print(f"\tRunning test {i}...", end=" ", flush=True)

        test_info = run(problem_number, input, timeout=timeout)
        if test_info["timeout"]:
            color_print(f"Timeout occurred for test {i}!", "purple")
        elif test_info["error"]:
            color_print(
                f"An error occurred for test {i}: {test_info['error_message']}", "red"
            )
        else:
            if test_info["result"] != output:
                color_print(
                    f"Test {i} failed: expected {output}, got {test_info['result']}",
                    "yellow",
                )
            else:
                color_print("OK", "green")
                score += (2**i) * normalize_time(test_info["time"], timeout, i + 1)

    final_score = (problem_number + 1) * 100 * score / normalization_factor

    delta = time.time() - start_time
    print(f"\fProblem {problem_number} runs in {delta:.2f}sec.")
    color_print(f"Score for problem {problem_number}: {final_score:.2f}", "cyan")
    print()

    return final_score


def normalize_time(time: float, factor: int, difficutly: int) -> float:
    return 1 - (time / factor) / (2**difficutly)


if __name__ == "__main__":
    scores = 0
    scores += test(0)
    scores += test(1)
    scores += test(2)
    scores += test(3)
    scores += test(4)

    color_print(f"Total score: {scores:.2f}", "blue")
