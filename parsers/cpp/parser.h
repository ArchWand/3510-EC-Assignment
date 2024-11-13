#ifndef __PARSER_H__
#define __PARSER_H__

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

#include "../../src/Solutions.cpp"

class Parser {
public:
	virtual string run(ifstream &f) = 0;
};

static string print_vec(vector<int> v) {
	stringstream ss;
	ss << "[";
	for (int i = 0; i < v.size()-1; i++) {
		ss << v[i] << ", ";
	}
	ss << v[v.size()-1] << "]";
	return ss.str();
}

static string print_vecvec(vector<vector<int>> vv) {
	stringstream ss;
	ss << "[";
	for (int i = 0; i < vv.size()-1; i++) {
		ss << print_vec(vv[i]) << ", ";
	}
	ss << print_vec(vv[vv.size()-1]) << "]";
	return ss.str();
}

static void parse_push_back(ifstream &f, vector<int> &v, int n) {
	for (int i = 0; i < n; i++) {
		int x;
		f >> x;
		v.push_back(x);
	}
}

static void parse_push_back(ifstream &f, vector<vector<int>> &v, int n, int w) {
	for (int i = 0; i < n; i++) {
		v.emplace_back();
		for (int j = 0; j < w; j++) {
			int x;
			f >> x;
			v.back().push_back(x);
		}
	}
}

#endif
