import argparse
from simulation import simulate


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
    parser.add_argument("-s", "--steps",
                        type=int,
                        default=100,
                        # action="store_true",
                        help="Specify the number of steps agents will take " +
                              "before simulation finishes.")
    parser.add_argument("-nl", "--no-logging",
                        # type=bool,
                        # default=True,
                        action="store_false",
                        help="Turn off output to CSV")

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
    else:
        simulate(**params.__dict__)


if __name__ == "__main__":
    main()
