import re
import logging
import nbformat

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


def convert_notebook(notebook_path, notebook_name):
    assert notebook_path is not None
    assert notebook_name is not None

    with open(notebook_path) as fh:
        nb = nbformat.reads(fh.read(), nbformat.NO_CONVERT)

    c = Config()
    c.NotebookExporter.preprocessors = [CommentRemovalSubCell]
    exporter = NotebookExporter(config=c)
    source, resources = exporter.from_notebook_node(nb)

    fw = FilesWriter()
    fw.write(source, resources, notebook_name=notebook_name)

    logging.basicConfig(level=logging.INFO, format='%(levelname)s : %(message)s')
    logging.info("the file '" + notebook_name + "' is ready.")
    logging.info("use it without comments thanks to pelikan.")
