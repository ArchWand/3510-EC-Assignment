# CS 3510 EC Local Autograder

A suite of tests for the Brito's Fall 2024 CS 3510 extra credit assignment. Supports all three languages allowed for submission: C++, Java, and Python.

## Usage

Write the code for your solutions in `src/Solutions.*`. If you are contributing back to this public repository, be sure that you have not included these files in your pull request.

Note: print debugging can be useful. If a test case fails, then user print debugging will be shown directly above the error text.

### Running

These commands should be run from the same directory as this file. Each option also supports the `-h` flag for help text, and the `-t` flag to run tests for only a specific subset of problems. Note that the inputs to `-t` must be zero-padded to be 2 digits since they are directly interpreted as folder names.

* C++

**Dependencies**: make, g++
```
make
./runcpp
```

* Java

**Dependencies**: make, java (java, javac, jar)
```
make jar
java -jar run.jar
```

* Python

**Dependencies**: python3
```
python3 run.py
```

## Test Cases

Please make a pull request with any test cases you add; any help is greatly appreciated. The test cases live in `./tests`; there is a directory for each problem, and each test case is a text file in the corresponding problem directory. The following section details the input format of each test case.

#### Problem 1

The first line of each test case contains a single integer $n$.

Each of the following $n$ lines should contain 1 integer; the elements of the input array.

The next line must be blank.

The last line contains the answer as a single integer.

#### Problem 2

The first line of each test case contains a single integer $n$.

Each of the following $n$ lines should contain 2 integers; the width and height of the package.

The next line must be blank.

The last line contains the answer as a single integer.

#### Problem 3

The first line of each test case contains a single integer $n$.

Each of the following $n$ lines should contain 1 integer; the elements of the array `block1`.

Each of the following $n$ lines should contain 1 integer; the elements of the array `block2`.

The next line must be blank.

The last line contains the answer as a single integer.

#### Problem 4

The first line of each test case contains 2 integers $n$ and `k`.

Each of the following $n$ lines should contain 1 integer; the elements of the array `A`.

The next line must be blank.

The last line contains the answer as a single integer.

#### Problem 5

The first line of each test case contains 3 integers $n$, $m$, and `maxTime`.

Each of the following $n$ lines should contain 1 integer; the elements of the `energies` array.

Each of the following $m$ lines should contain 3 integers; $u_j$, $v_j$, and time$_j$: the elements of the `edges` array.

The next line must be blank.

The last line contains the answer as a single integer.

#### Problem 6

The first line of each test case contains 2 integers $n$ and `k`.

Each of the following $n$ lines should contain 1 integer; the elements of the `quantity` array.

The next line must be blank.

The last line contains the answer as a single integer.

#### Problem 7

The first line of each test case contains a single integer $n$.

Each of the following $n$ lines should contain 3 integers; the elements of the input array.

The next line must be blank.

The last line contains the answer as a single integer.

#### Problem 8

The first line of each test case contains a single integer $n$.

Each of the following $n$ lines should each contain a string; the elements of the input array.

The next line must be blank.

The first line of the answer should contain a single integer $c$.

Each of the following $c$ lines should contain a string; these are all the valid answers.

#### Problem 9

The first line of each test case contains a single integer $n$.

Each of the following $n$ lines should contain 1 integer; the elements of the input array.

The next line must be blank.

The last line contains the answer as a single integer.

#### Problem 10

The first line of each test case contains a single integer $n$.

The next line contains a string of length $n$; the input. All characters must be either digits or '*'.

The next line must be blank.

The last line contains the answer: either "true" or "false".

#### Problem 11

The first line of each test case contains 2 integers $n$ and `l`.

Each of the following $n$ lines should contain 1 integer; the elements of the `B` array.

The next line must be blank.

The last line contains the answer as a single integer.

#### Problem 12

The first line of each test case contains 2 integers `n` and $m$.

Each of the following $m$ lines should contain 2 integers; the end points of each bridge: the elements of the input array.

The next line must be blank.

The first line of the answer should contain a single integer $c$.

Each of the following $c$ lines should contain 2 integers denoting a bridge that would disconnect some islands if it is removed.

#### Problem 13

The first line contains the `text`.

The second line contains the `pattern`.

The next line must be blank.

The last line contains the answer as a single integer.

#### Problem 14

The first line of each test case contains a single integer $N$.

Each of the following $n$ lines should contain 2 integers; the locations of each bee.

The next line must be blank.

The last line contains the answer as a single integer.

## Technical details

The autograder for each language works fairly similarly. First, command line arguments are parsed and handled, and `run_tests()` is called with a list of all problems to test. The function loops over all problems and all test cases for each problem in turn, opening the file and passing it to the verifier code.

Each verifier consists of 4 parts: parse, run, verify, and error handling. C++ uses a list of abstract classes, Java uses a list of Interfaces, and Python uses a dictionary lookup for each part.

Parsing reads the given file and converts it into a set of inputs and a certificate `cert`, which contains a way to check the correctness of an answer. For most problems, the certificate is an integer, and the input consists of a list or list of lists, possibly with an additional integer. Note that the python verifiers contain stronger assertions; if a test case has an assertion error when run on the python autograder, then it likely has a formatting error.

Running takes an input from the results of parsing and runs the code in `src/Solutions.*` take get an answer. Each verifier handles calling the correct function, and passing in the correct arguments from the input. In C++, this is done by keeping everything in the same scope. In Java, the input is an `Object[]`, and we make unsafe casts to appropriately retrieve the arguments. In Python, the input is a tuple, and we use tuple unpacking to provide the arguments.

Verifying takes the certificate from parsing and the answer from running and compares them. If the certificate proves that the answer is correct, we return a boolean result saying as much. In most cases, since the certificate and answer are both integers, a simple equality check is used.

If the result is verified to be correct, a message is printed saying that the test case was passed. Otherwise, we go into error handling, which shows the input, the expected answer in the form of the certificate, and the actual answer that the solution returned.

