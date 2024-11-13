from . import _02
from . import _04

parse = {
	"02": _02.parser,
	"04": _04.parser,
}

verify = {
	"02": _02.verifier,
	"04": _04.verifier,
}

error = {
	"02": _02.error,
	"04": _04.error,
}
