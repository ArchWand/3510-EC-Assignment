#include "parser.h"
#include <cstdio>
#include <format>
#include <sstream>
#include <string>
#include <vector>

class _14: public Parser {
public:
	string run(ifstream &f) {
		// Parse
		int n;
		f >> n;
		vector<pair<int, int>> locations;
		parse_push_back(f, locations, n);

		int cert;
		f >> cert;

		// Check solution
		long long ans = Solutions::minNetworkCost(locations);

		// Verify
		bool res = (cert == ans);

		// Handle error
		string error = "";
		if (!res) {
			stringstream ss;
			ss << "Input:\n"
				<< "locations = " << print_vecpair(locations) << "\n"
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
