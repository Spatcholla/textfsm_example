import textfsm


def parse_data(template_file, parse_input):
    with template_file.open() as template:
        parser = textfsm.TextFSM(template)
        fsm_results = parser.ParseText(parse_input)
    return fsm_results


def main():
    pass


if __name__ == '__main__':
    main()
