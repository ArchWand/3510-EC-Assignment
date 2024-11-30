#!/bin/python3
import os
from parsers.py import parse, verify, error
import src.Solutions
import sys

TESTS = "./tests"
def tests_dir(num: str):
    return f"{TESTS}/{num}"
def tests_path(num: str, case: str):
    return f"{tests_dir(num)}/{case}"

# Ordered dict, depends on Python 3.7
sol = src.Solutions.Solutions
problems = {
    "01": sol.realEstatePrices,
    "02": sol.maxPackages,
    "03": sol.minSwap,
    "04": sol.modTwoSum,
    "05": sol.maximumMagicPathPower,
    "06": sol.divideTheHarvest,
    "07": sol.coloringSidewalks,
    "08": sol.chemicalConcoctions,
    "09": sol.maxNonAdjSum,
    "10": sol.reviveStrings,
    "11": sol.buildBrickWall,
    "12": sol.findNeededBridges,
    "13": sol.numDistinct,
    "14": sol.minNetworkCost,
}

def print_help():
    print("py run.py [-h | -t [01 02 ...]]")
    print("  Note that flags cannnot be combined.")
    print("")
    print("  -h   Print this help text.")
    print("")
    print("  -t   Test only specific problems. For example, to test 01, 04, and 12:")
    print("           py run.py -t 01 04 12")
    print("")

GREEN = '\033[92m'
RED = '\033[91m'
ENDC = '\033[0m'

# Run all tests listed in the given list
def run_tests(tests: list[str]):
    # Loop over every problem we want to test
    for prob in tests:
        print(f"Testing problem {prob}")

        # Try every test case
        for test_case in sorted(os.listdir(tests_dir(prob))):
            test_case = os.fsdecode(test_case)

            with open(tests_path(prob, test_case)) as f:
                # Parse the test case file, run the solution, and verify the answer
                cert, test_in = parse[prob](f)
                ans = problems[prob](*test_in)
                res = verify[prob](cert, ans)

                # Say whether the answer was right
                if res:
                    print(f"Test case {test_case} {GREEN}passed{ENDC}")
                else:
                    print(f"{RED}Failed{ENDC} on {test_case}")
                    error[prob](cert, test_in, ans)
                    break

if __name__ == "__main__":
    tests = list(problems.keys())
    # Parse command line arguments
    if len(sys.argv) > 1:
        match sys.argv[1]:
            case "-h":
                print_help()
                exit()
            case "-t":
                tests = [ s for s in sys.argv[2:] ]
            case _:
                print(f"Invalid flag {sys.argv[1]}, ignoring.")
    run_tests(tests)
