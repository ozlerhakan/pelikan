
# Pelikan

Pelikan lets you convert notebooks to comment-free notebooks. In other words, It removes Python block and inline comments from source cells in order to point out only source code.


## How it works

```
$ pip install pelikan
$ pelikan --help
usage: pelikan [-h] --notebook NOTEBOOK --file_name FILE_NAME

optional arguments:
  -h, --help            show this help message and exit
  --notebook NOTEBOOK   The notebook file we want to remove comments from
  --file_name FILE_NAME
                        The name of the newly created comment-free notebook.

$ pelikan --notebook notebook_file.ipynb voila
$ ls
notebook_file.ipynb voila.ipynb
```