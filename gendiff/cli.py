import argparse


TEXT_DESCRIPTION = 'Compares two configuration files and shows a difference.'


def common_parser():
    parser = argparse.ArgumentParser(description=TEXT_DESCRIPTION)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        "-f", "--format",
        default='stylish',
        choices=['stylish', 'plain', 'json'],
        help="set format of output",
    )
    args = parser.parse_args()
    return args
