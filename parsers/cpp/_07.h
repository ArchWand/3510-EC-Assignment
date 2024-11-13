#include "parser.h"
#include <cstdio>
#include <format>
#include <sstream>
#include <string>
#include <vector>

class _07: public Parser {
public:
	string run(ifstream &f) {
		// Parse
		int n;
		f >> n;
		vector<vector<int>> time;
		parse_push_back(f, time, n, 3);

		int cert;
		f >> cert;

		// Check solution
		int ans = Solutions::coloringSidewalks(time);

		// Verify
		bool res = (cert == ans);

		// Handle error
		string error = "";
		if (!res) {
			stringstream ss;
			ss << "Input:\n"
				<< "time = " << print_vecvec(time) << "\n"
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
