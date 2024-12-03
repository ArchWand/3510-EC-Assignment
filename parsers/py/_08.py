def parser(f):
    n = int(f.readline())
    formulas = [ f.readline().strip() for _ in range(n) ]

    for s in formulas:
        for c in s:
            assert('a' <= c and c <= 'z')
    assert(f.readline() == "\n")

    m = int(f.readline())
    cert = set( f.readline().strip() for _ in range(m) )
    if m == 0:
        cert.add("")
    for s in cert:
        for c in s:
            assert('a' <= c and c <= 'z')
    assert(f.readline().strip() == "")

    # Assert that the ordering exists
    for x, y in zip(formulas[:-1], formulas [1:]):
        # Find common prefix
        prefix = x
        while not y.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                break;
        assert((len(prefix) < len(x) and len(prefix) < len(y))
            or (y.startswith(x) and len(y) > len(x)) # Condition 2
        )

    return cert, (formulas,)

def verifier(cert, ans):
    return ans in cert

def error(cert, input, ans):
    print("Input:")
    print("formulas = " + str(input[0]))
    print("")
    print("Expected:")
    print(cert)
    print("")
    print("Actual:")
    print(ans)
    print()
