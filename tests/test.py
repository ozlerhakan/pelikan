import unittest
from pelikan import Pelikan


class TestPelikanCases(unittest.TestCase):

    def test_remove_commennts(self):
        path = 'tests/data/'
        notebook = path + 'notebook-comments.ipynb'
        new_notebook_name = 'notebook-without-comments'
        file_extension = '.ipynb'

        pelikan = Pelikan(notebook, new_notebook_name)
        destination = pelikan.generate_notebook(path)

        self.assertIsNotNone(destination)
        self.assertEqual("/".join(destination.parts), path + new_notebook_name + file_extension)


if __name__ == "__main__":
    unittest.main()