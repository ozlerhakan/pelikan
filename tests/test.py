import unittest

import nbformat
from nbconvert import NotebookExporter

from pelikan import Pelikan


class TestPelikanCases(unittest.TestCase):

    def test_remove_comments(self):
        path = 'data/'
        notebook = path + 'notebook-comments.ipynb'
        new_notebook_name = 'notebook-without-comments'
        file_extension = '.ipynb'
        comment_free_notebooks = path + new_notebook_name + file_extension

        pelikan = Pelikan(notebook, new_notebook_name)
        source_actual, resources_actual = pelikan._convert_comment()

        with open(comment_free_notebooks) as fh:
            nb_comment_free = nbformat.reads(fh.read(), nbformat.NO_CONVERT)

        exporter = NotebookExporter()
        source_expected, resources_expected = exporter.from_notebook_node(nb_comment_free)

        self.assertEqual(source_actual, source_expected)


if __name__ == "__main__":
    unittest.main()
