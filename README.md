# Pelikan :flamingo:

Pelikan lets you convert notebooks to comment-free notebooks. In other words, It removes Python block and inline comments from source cells in order to point out only source code.


## How it works

```
$ pip install pelikan

$ pelikan --help
usage: pelikan [-h] --notebook NOTEBOOK --output OUTPUT

optional arguments:
  -h, --help            show this help message and exit
  --notebook NOTEBOOK, -n NOTEBOOK
                        The notebook file we want to remove comments from
  --output OUTPUT, -o OUTPUT
                        The name of the newly created comment-free notebook.

$ pelikan -n notebook_file.ipynb -o voila
$ ls
notebook_file.ipynb voila.ipynb
```


## LICENSE

MIT