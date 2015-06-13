import argparse


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description=__doc__,
        # formatter_class=argparse.RawDescriptionHelpFormatter
        )

    parser.add_argument("-a", "--agents",
                        type=int,
                        default=10,
                        # action="store_true",
                        help="Specify the number of agents to instantiate")

    if argv is not None:  # to mock terminal input, for functional tests
        args = parser.parse_args(argv)
    else:
        args = parser.parse_args()
    return args

def main(argv=None):
    params = parse_args(argv)
    if params.agents < 1:
        raise Exception("Model requires at least two agents, got {} instead."
                        .format(params.agents))



if __name__ == "__main__":
    main()
