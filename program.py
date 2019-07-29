import pathlib
from pprint import pprint

import parser

data = pathlib.Path("tests.log").open().read()
template_path = pathlib.Path.joinpath(pathlib.Path.cwd(), "templates", "log.textfsm")

parsed_data = parser.parse_data(template_path, data)

pprint(parsed_data)
