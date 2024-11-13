#ifndef __PARSER_H__
#define __PARSER_H__

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;

#include "../../src/Solutions.cpp"

class Parser {
public:
	virtual string run(ifstream &f) = 0;
};

template <typename T>
static string print_vec(vector<T> v) {
	if (v.size() == 0) { return "[]"; }
	stringstream ss;
	ss << "[";
	for (int i = 0; i < v.size()-1; i++) {
		ss << v[i] << ", ";
	}
	ss << v[v.size()-1] << "]";
	return ss.str();
}

static string print_vecvec(vector<vector<int>> vv) {
	if (vv.size() == 0) { return "[]"; }
	stringstream ss;
	ss << "[";
	for (int i = 0; i < vv.size()-1; i++) {
		ss << print_vec(vv[i]) << ", ";
	}
	ss << print_vec(vv[vv.size()-1]) << "]";
	return ss.str();
}

static string print_vecpair(vector<pair<int, int>> vv) {
	if (vv.size() == 0) { return "[]"; }
	stringstream ss;
	ss << "[";
	for (int i = 0; i < vv.size()-1; i++) {
		ss << "(" << vv[i].first << ", " << vv[i].second << "), ";
	}
	ss << "(" << vv[vv.size()-1].first << ", " << vv[vv.size()-1].second << ")]";
	return ss.str();
}

static string print_set(unordered_set<string> v) {
	stringstream ss;
	ss << "{";
	auto it = v.begin();
	while (it != v.end()) {
		cout << *it << endl;
		ss << *it;
		it++;
		if (it == v.end()) {
			break;
		}
		ss << ", ";
	}
	ss << "}";
	return ss.str();
}

template <typename T>
static void parse_push_back(ifstream &f, vector<T> &v, int n) {
	for (int i = 0; i < n; i++) {
		T x;
		f >> x;
		v.push_back(x);
	}
}

static void parse_push_back(ifstream &f, vector<pair<int, int>> &v, int n) {
	for (int i = 0; i < n; i++) {
		v.emplace_back();
		int x, y;
		f >> x >> y;
		v[i].first = x;
		v[i].second = y;
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

static void parse_insert(ifstream &f, unordered_set<string> &v, int n) {
	for (int i = 0; i < n; i++) {
		string x;
		f >> x;
		v.insert(x);
	}
}

#endif
