
import argparse
from typing import Callable


def arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    trace_parser = subparsers.add_parser('trace', help='Create a trace of an aglorithm execution')
    trace_parser.add_argument('input', type=argparse.FileType('r'), help='input YAML filepath')
    trace_parser.add_argument("-o", "--output", type=argparse.FileType('w'), help="increase output verbosity")

    timeit_parser = subparsers.add_parser('timeit', help='Create a timing profile of the algorithm')
    timeit_parser.add_argument('input', help='input YAML filepath')
    timeit_parser.add_argument("-o", "--output", type=argparse.FileType('w'), help="increase output verbosity")

    return parser


def main(algo_fn: Callable):
    parser = arg_parser()
    args = parser.parse_args()
