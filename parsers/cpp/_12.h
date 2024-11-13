#include "parser.h"
#include <algorithm>
#include <cstdio>
#include <format>
#include <sstream>
#include <string>
#include <vector>

class _12: public Parser {
public:
	string run(ifstream &f) {
		// Parse
		int n, m;
		f >> n >> m;
		vector<pair<int, int>> E;
		parse_push_back(f, E, n);

		int c;
		f >> c;
		vector<pair<int, int>> cert;
		parse_push_back(f, cert, c);

		// Check solution
		vector<pair<int, int>> ans = Solutions::findNeededBridges(n, E);

		// Verify
		auto comp = [](const std::pair<int, int>& a, const std::pair<int, int>& b) {
			if (a.first == b.first) { return a.second < b.second; }
			return a.first < b.first;
		};
		sort(cert.begin(), cert.end(), comp);
		sort(ans.begin(), ans.end(), comp);
		bool res = (cert == ans);

		// Handle error
		string error = "";
		if (!res) {
			stringstream ss;
			ss << "Input:\n"
				<< "n = " << n << "\n"
				<< "E = " << print_vecpair(E) << "\n"
				<< "\n"
				<< "Expected:\n"
				<< print_vecpair(cert) << "\n"
				<< "\n"
				<< "Actual:\n"
				<< print_vecpair(ans) << "\n"
				<< endl;
			error = ss.str();
		}
		return error;
	}
};
