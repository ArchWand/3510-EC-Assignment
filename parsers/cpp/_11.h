#include "parser.h"
#include <cstdio>
#include <format>
#include <sstream>
#include <string>
#include <vector>

class _11: public Parser {
public:
	string run(ifstream &f) {
		// Parse
		int n, l;
		f >> n >> l;
		vector<int> B;
		parse_push_back(f, B, n);

		int cert;
		f >> cert;

		// Check solution
		int ans = Solutions::buildBrickWall(B, l);

		// Verify
		bool res = (cert == ans);

		// Handle error
		string error = "";
		if (!res) {
			stringstream ss;
			ss << "Input:\n"
				<< "B = " << print_vec(B) << "\n"
				<< "l = " << l << "\n"
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
