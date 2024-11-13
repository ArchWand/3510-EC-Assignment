#include "parser.h"
#include <cstdio>
#include <format>
#include <ios>
#include <sstream>
#include <string>
#include <vector>

class _10: public Parser {
public:
	string run(ifstream &f) {
		// Parse
		int n;
		string ticket;
		f >> n >> ticket;

		bool cert;
		f >> boolalpha >> cert;

		// Check solution
		bool ans = Solutions::reviveStrings(n, ticket);

		// Verify
		bool res = (cert == ans);

		// Handle error
		string error = "";
		if (!res) {
			stringstream ss;
			ss << "Input:\n"
				<< "n = " << n << "\n"
				<< "ticket = " << ticket << "\n"
				<< "\n"
				<< "Expected:\n"
				<< boolalpha << cert << "\n"
				<< "\n"
				<< "Actual:\n"
				<< boolalpha << ans << "\n"
				<< endl;
			error = ss.str();
		}
		return error;
	}
};
