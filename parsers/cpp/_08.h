#include "parser.h"
#include <cstdio>
#include <format>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>

class _08: public Parser {
public:
	string run(ifstream &f) {
		// Parse
		int n;
		f >> n;
		vector<string> formulas;
		parse_push_back(f, formulas, n);

		int c;
		unordered_set<string> cert;
		f >> c;
		parse_insert(f, cert, c);

		// Check solution
		string ans = Solutions::chemicalConcoctions(formulas);

		// Verify
		bool res = (cert.find(ans) != cert.end());

		// Handle error
		string error = "";
		if (!res) {
			stringstream ss;
			ss << "Input:\n"
				<< "formulas = " << print_vec(formulas) << "\n"
				<< "\n"
				<< "Expected:\n"
				<< print_set(cert) << "\n"
				<< "\n"
				<< "Actual:\n"
				<< ans << "\n"
				<< endl;
			error = ss.str();
		}
		return error;
	}
};
