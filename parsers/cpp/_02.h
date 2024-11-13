#include "parser.h"
#include <cstdio>
#include <format>
#include <sstream>
#include <string>
#include <vector>

class _02: public Parser {
public:
	string run(ifstream &f) {
		// Parse
		int n;
		f >> n;
		vector<vector<int>> packages;
		for (int i = 0; i < n; i++) {
			int a, b;
			f >> a >> b;
			packages.emplace_back(2);
			packages.back()[0] = a;
			packages.back()[1] = b;
		}

		int cert;
		f >> cert;

		// Check solution
		int ans = Solutions::maxPackages(packages);

		// Verify
		bool res = (cert == ans);

		// Handle error
		string error = "";
		if (!res) {
			stringstream ss_packages;
			ss_packages << "[ ";
			for (vector<int> x : packages) {
				ss_packages << "[" << x[0] << ", " << x[1] << "], ";
			}
			ss_packages << "]";

			stringstream ss;
			ss << "Input:\n"
				<< "packages = " << ss_packages.str() << "\n"
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
