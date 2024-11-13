#include "parser.h"
#include <cstdio>
#include <format>
#include <sstream>
#include <string>
#include <vector>

class _13: public Parser {
public:
	string run(ifstream &f) {
		// Parse
		string text, pattern;
		f >> text >> pattern;

		int cert;
		f >> cert;

		// Check solution
		int ans = Solutions::numDistinct(text, pattern);

		// Verify
		bool res = (cert == ans);

		// Handle error
		string error = "";
		if (!res) {
			stringstream ss;
			ss << "Input:\n"
				<< "text = " << text << "\n"
				<< "pattern = " << pattern << "\n"
				<< "\n"
				<< "Expected:\n"
				<< cert << "\n"
				<< "\n"
				<< "Actual:\n"
				<< ans << "\n"
				<< endl;
			error = ss.str();
		}
		return error;
	}
};
