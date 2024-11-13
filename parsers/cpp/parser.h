#ifndef __PARSER_H__
#define __PARSER_H__

#include <iostream>
#include <fstream>
using namespace std;

#include "../../src/Solutions.cpp"

class Parser {
public:
	virtual string run(ifstream &f) = 0;
};

#endif
