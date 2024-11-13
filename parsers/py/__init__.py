from . import _01, _02, _03, _04

parse = {
	"01": _01.parser,
	"02": _02.parser,
	"03": _03.parser,
	"04": _04.parser,
}

verify = {
	"01": _01.verifier,
	"02": _02.verifier,
	"03": _03.verifier,
	"04": _04.verifier,
}

error = {
	"01": _01.error,
	"02": _02.error,
	"03": _03.error,
	"04": _04.error,
}
