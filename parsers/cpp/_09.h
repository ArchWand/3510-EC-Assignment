#include "parser.h"
#include <cstdio>
#include <format>
#include <sstream>
#include <string>
#include <vector>

class _09: public Parser {
public:
	string run(ifstream &f) {
		// Parse
		int n;
		f >> n;
		vector<int> nums;
		parse_push_back(f, nums, n);

		int cert;
		f >> cert;

		// Check solution
		int ans = Solutions::maxNonAdjSum(nums);

		// Verify
		bool res = (cert == ans);

		// Handle error
		string error = "";
		if (!res) {
			stringstream ss;
			ss << "Input:\n"
				<< "nums = " << print_vec(nums) << "\n"
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
