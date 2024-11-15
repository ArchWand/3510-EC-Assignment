def parser(f):
	text = f.readline().strip()
	pattern = f.readline().strip()

	assert(f.readline() == "\n")

	cert = int(f.readline())
	assert(f.readline().strip() == "")

	return cert, (text, pattern,)

def verifier(cert, ans):
	return cert == ans

def error(cert, input, ans):
	print("Input:")
	print("text = " + str(input[0]))
	print("pattern = " + str(input[1]))
	print("")
	print("Expected:")
	print(cert)
	print("")
	print("Actual:")
	print(ans)
	print()
