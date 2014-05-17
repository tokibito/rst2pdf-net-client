import sys
from argparse import ArgumentParser

from . import client


class Command(object):
    def make_argument_parser(self):
        parser = ArgumentParser()
        return parser

    def make_client(self):
        return client.Client()

    def get_input(self, args):
        # TODO: 引数のファイル指定を見る
        return sys.stdin

    def get_output(self, args):
        # TODO: 引数のファイル指定を見る
        return sys.stdout

    def run(self):
        parser = self.make_argument_parser()
        args = parser.parse_args()
        client = self.make_client()
        input_stream = self.get_input()
        output_stream = self.get_output()


def main():
    cmd = Command()
    cmd.run()
