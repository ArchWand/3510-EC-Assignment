from . import _01, _02, _03, _04, _05, _06, _07, _08, _09, _10, _11, _12, _13, _14

parse = {
	"01": _01.parser,
	"02": _02.parser,
	"03": _03.parser,
	"04": _04.parser,
	"05": _05.parser,
	"06": _06.parser,
	"07": _07.parser,
	"08": _08.parser,
	"09": _09.parser,
	"10": _10.parser,
	"11": _11.parser,
	"12": _12.parser,
	"13": _13.parser,
	"14": _14.parser,
}

verify = {
	"01": _01.verifier,
	"02": _02.verifier,
	"03": _03.verifier,
	"04": _04.verifier,
	"05": _05.verifier,
	"06": _06.verifier,
	"07": _07.verifier,
	"08": _08.verifier,
	"09": _09.verifier,
	"10": _10.verifier,
	"11": _11.verifier,
	"12": _12.verifier,
	"13": _13.verifier,
	"14": _14.verifier,
}

error = {
	"01": _01.error,
	"02": _02.error,
	"03": _03.error,
	"04": _04.error,
	"05": _05.error,
	"06": _06.error,
	"07": _07.error,
	"08": _08.error,
	"09": _09.error,
	"10": _10.error,
	"11": _11.error,
	"12": _12.error,
	"13": _13.error,
	"14": _14.error,
}
