#include "parser.h"
#include <algorithm>
#include <cstdio>
#include <format>
#include <sstream>
#include <string>
#include <vector>

class _05: public Parser {
public:
	string run(ifstream &f) {
		// Parse
		int n, m, maxTime;
		f >> n >> m >> maxTime;
		vector<int> energies;
		parse_push_back(f, energies, n);
		vector<vector<int>> edges;
		parse_push_back(f, edges, m, 3);

		int cert;
		f >> cert;

		// Check solution
		int ans = Solutions::maximumMagicPathPower(energies, edges, maxTime);

		// Verify
		bool res = (cert == ans);

		// Handle error
		string error = "";
		if (!res) {
			stringstream ss;
			ss << "Input:\n"
				<< "energies = " << print_vec(energies) << "\n"
				<< "edges = " << print_vecvec(edges) << "\n"
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
