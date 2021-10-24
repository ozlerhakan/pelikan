import argparse
import re
import sys
from pathlib import PosixPath

import nbformat
from nbconvert import NotebookExporter
from nbconvert.preprocessors import Preprocessor
from nbconvert.writers import FilesWriter
from traitlets.config import Config


class CommentRemovalSubCell(Preprocessor):

    def preprocess_cell(self, cell, resources, index):
        if cell.cell_type == 'code':
            cell.source = re.sub('(#).+', self._comment_repl, cell.source, flags=re.IGNORECASE)
        return cell, resources

    @staticmethod
    def _comment_repl(match_obj):
        if match_obj.group(0) == '#':
            return ''


class Pelikan:

    def __init__(self, notebook_path=None, notebook_name=None):
        assert notebook_path is not None
        assert notebook_name is not None

        self.notebook_name = notebook_name
        self.notebook_path = notebook_path

    def _convert_comment(self):
        with open(self.notebook_path) as fh:
            nb = nbformat.reads(fh.read(), nbformat.NO_CONVERT)

        c = Config()
        c.NotebookExporter.preprocessors = [CommentRemovalSubCell]
        exporter = NotebookExporter(config=c)
        return exporter.from_notebook_node(nb)

    def generate_notebook(self, destination_path=None) -> PosixPath:
        source, resources = self._convert_comment()

        fw = FilesWriter()
        if destination_path:
            fw.build_directory = destination_path
        return fw.write(source, resources, notebook_name=self.notebook_name)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--notebook",
        "-n",
        required=True,
        help="The notebook file we want to remove comments from")
    parser.add_argument(
        "--output",
        "-o",
        required=True,
        help="The name of the newly created comment-free notebook.")

    args = parser.parse_args(sys.argv[1:])
    pelikan = Pelikan(args.notebook, args.file_name)
    pelikan.generate_notebook()
