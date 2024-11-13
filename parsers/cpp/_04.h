#include "parser.h"
#include <cstdio>
#include <format>
#include <sstream>
#include <string>
#include <vector>

class _04: public Parser {
public:
	string run(ifstream &f) {
		// Parse
		int n, k;
		f >> n >> k;
		vector<int> A;
		parse_push_back(f, A, n);

		int cert;
		f >> cert;

		// Check solution
		int ans = Solutions::modTwoSum(A, k);

		// Verify
		bool res = (cert == ans);

		// Handle error
		string error = "";
		if (!res) {
			stringstream ss;
			ss << "Input:\n"
				<< "A = " << print_vec(A) << "\n"
				<< "k = " << k << "\n"
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
