import re
import nbformat

from pathlib import PosixPath
from traitlets.config import Config
from nbconvert import NotebookExporter
from nbconvert.writers import FilesWriter
from nbconvert.preprocessors import Preprocessor


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
        fw.build_directory = destination_path
        return fw.write(source, resources, notebook_name=self.notebook_name)


if __name__ == "__main__":
    import sys

    assert len(sys.argv) > 2

    notebook_path = sys.argv[1]
    notebook_name = sys.argv[2]

    pelikan = Pelikan(notebook_path, notebook_name)
    pelikan.generate_notebook()

    import logging

    logging.basicConfig(level=logging.INFO, format='%(levelname)s : %(message)s')
    logging.info("the file '" + notebook_name + "' is ready.")
    logging.info("use it without Python comments, thanks to pelikan.")
