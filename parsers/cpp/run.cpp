#include <cstddef>
#include <iostream>
#include <fstream>
#include <string>
#include <filesystem>
namespace fs = std::filesystem;
using namespace std;

#include "_01.h"
#include "_02.h"
#include "_03.h"
#include "_04.h"
#include "_05.h"
#include "_06.h"
#include "_07.h"
#include "_08.h"
#include "_09.h"
#include "_10.h"
#include "_11.h"
#include "_12.h"
#include "_13.h"
#include "_14.h"

const string TESTS = "./tests";
string tests_dir(string num) { return TESTS + "/" + num; }
string tests_path(string num, string test_case) {
	return tests_dir(num) + "/" + test_case;
}

Parser *problems[] = { nullptr,
	new _01,
	new _02,
	new _03,
	new _04,
	new _05,
	new _06,
	new _07,
	new _08,
	new _09,
	new _10,
	new _11,
	new _12,
	new _13,
	new _14,
};


#define GREEN "\033[92m"
#define RED "\033[91m"
#define ENDC "\033[0m"

void print_help() {
	cout <<
		"./run [-h | -t [01 02 ...]]\n"
		"  Note that flags cannnot be combined.\n"
		"\n"
		"  -h   Print this help text.\n"
		"\n"
		"  -t   Test only specific problems. For example, to test 01, 04, and 12:\n"
		"           ./run -t 01 04 12\n"
	<< endl;
}

void run_tests(vector<string> tests) {
	// Loop over every problem we want to test
	for (string prob : tests) {
		cout << "Testing problem " << prob << endl;

		// Try every test case
		for (const fs::directory_entry &entry : fs::directory_iterator(tests_dir(prob))) {
			string test_case = entry.path().filename();
			ifstream f(entry.path());
			// Parse the test case file, run the solution, and verify the answer
			string err = problems[stoi(prob)]->run(f);
			if (err == "") {
				printf("Test case %s %spassed%s\n", test_case.c_str(), GREEN, ENDC);
			} else {
				printf("%sFailed%s on %s\n", RED, ENDC, test_case.c_str());
				cout << err;
				break;
			}
		}
	}
}

int main(int argc, char **argv) {
	vector<string> tests = {"01","02","03","04","05","06","07","08","09","10","11","12","13","14"};
	// Parse command line arguments
	if (argc > 1) {
		if (argv[1][0] != '-') {
			cout << "Invalid flag " << argv[1] << ", ignoring." << endl;
		} else {
			switch (argv[1][1]) {
				case 'h':
					print_help();
					return 0;
				case 't':
					tests.clear();
					for (int i = 2; i < argc; i++) {
						tests.push_back(argv[i]);
					}
					break;
				default:
					cout << "Invalid flag " << argv[1] << ", ignoring." << endl;
			}
		}
	}

	run_tests(tests);
}

