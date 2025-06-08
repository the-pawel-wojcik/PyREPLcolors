# Python REPL colors
Python 3.14 by default colors syntax in REPL. The script in this repository
enables configuration of the coloring scheme.

## Installation
```bash
# .bashrc
export PYTHONSTARTUP=/path/to/this/repo/colorscheme.py
```

## Configuration
The `_colorize` module includes predefined colors
```
>>> import _colorize
>>> dir(_colorize.ANSIColors)
['BLACK', 'BLUE', 'CYAN', 'GREEN', 'MAGENTA', 'RED', 'WHITE', 'YELLOW', ...]
```
each of them can be prefixed with `BACKGROUND_`, `BOLD_`, `INTENSE_`, 
`INTENSE_BACKGROUND_`. There exist also the unprefix-able `GREY` and two
specifiers: `RESET`, and `BOLD`.

# References
[Announcement](https://docs.python.org/3.14/whatsnew/3.14.html#whatsnew314-pyrepl-highlighting)

[Forum discussion](https://discuss.python.org/t/pyrepl-color-themes)
