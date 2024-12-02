def parser(f):
    n = int(f.readline())
    values = [ int(f.readline()) for _ in range(n) ]

    assert(f.readline() == "\n")

    cert = int(f.readline())
    assert(f.readline().strip() == "")

    # Values can be assumed to be non-negative:
    # https://edstem.org/us/courses/63506/discussion/5702458
    for x in values:
        assert(x >= 0)

    return cert, (values,)

def verifier(cert, ans):
    return cert == ans

def error(cert, input, ans):
    print("Input:")
    print("values = " + str(input[0]))
    print("")
    print("Expected:")
    print(cert)
    print("")
    print("Actual:")
    print(ans)
    print()
