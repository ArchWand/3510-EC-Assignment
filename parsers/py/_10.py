def parser(f):
    n = int(f.readline())
    ticket = f.readline().strip()

    assert(n == len(ticket))
    for c in ticket:
        assert(c == '*' or ('0' <= c and c <= '9'))
    assert(f.readline() == "\n")

    cert = f.readline().strip()
    assert(cert == "true" or cert == "false")
    assert(f.readline().strip() == "")
    if cert == "true":
        cert = True
    else:
        cert = False

    assert(sum(1 for i in ticket if i == '*') % 2 == 0)

    return cert, (n, ticket,)

def verifier(cert, ans):
    return cert == ans

def error(cert, input, ans):
    print("Input:")
    print("n = " + str(input[0]))
    print("ticket = " + str(input[1]))
    print("")
    print("Expected:")
    print(cert)
    print("")
    print("Actual:")
    print(ans)
    print()
