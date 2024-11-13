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
		for (int i = 0; i < n; i++) {
			int x;
			f >> x;
			A.push_back(x);
		}

		int cert;
		f >> cert;

		// Check solution
		vector<int> const &const_A = A;
		int ans = Solutions::modTwoSum(const_A, k);

		// Verify
		bool res = (cert == ans);

		// Handle error
		string error = "";
		if (!res) {
			string str_A = "[ ";
			for (int x : A) {
				str_A += to_string(x) + " ";
			}
			str_A += "]";

			stringstream ss;
			ss << "Input:\n"
				<< "A = " << str_A << "\n"
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
