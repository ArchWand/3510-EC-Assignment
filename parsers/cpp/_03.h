#include "parser.h"
#include <cstdio>
#include <format>
#include <sstream>
#include <string>
#include <vector>

class _03: public Parser {
public:
	string run(ifstream &f) {
		// Parse
		int n;
		f >> n;
		vector<int> blocks1;
		vector<int> blocks2;
		parse_push_back(f, blocks1, n);
		parse_push_back(f, blocks2, n);

		int cert;
		f >> cert;

		// Check solution
		int ans = Solutions::minSwap(blocks1, blocks2);

		// Verify
		bool res = (cert == ans);

		// Handle error
		string error = "";
		if (!res) {
			stringstream ss;
			ss << "Input:\n"
				<< "blocks1 = " << print_vec(blocks1) << "\n"
				<< "blocks2 = " << print_vec(blocks2) << "\n"
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
