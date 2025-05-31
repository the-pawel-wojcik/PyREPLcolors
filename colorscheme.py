import _colorize

ARGPARSE_COLORS = {
    'usage': _colorize.ANSIColors.BOLD_BLUE,
    'prog': _colorize.ANSIColors.BOLD_MAGENTA,
    'prog_extra': _colorize.ANSIColors.MAGENTA,
    'heading': _colorize.ANSIColors.BOLD_BLUE,
    'summary_long_option': _colorize.ANSIColors.CYAN,
    'summary_short_option': _colorize.ANSIColors.GREEN,
    'summary_label': _colorize.ANSIColors.YELLOW,
    'summary_action': _colorize.ANSIColors.GREEN,
    'long_option': _colorize.ANSIColors.BOLD_CYAN,
    'short_option': _colorize.ANSIColors.BOLD_GREEN,
    'label': _colorize.ANSIColors.BOLD_YELLOW,
    'action': _colorize.ANSIColors.BOLD_GREEN,
    'reset': _colorize.ANSIColors.RESET,
}

SYNTAX_COLORS = {
    'prompt': _colorize.ANSIColors.BOLD_WHITE,
    'keyword': _colorize.ANSIColors.BOLD_YELLOW,
    'builtin': _colorize.ANSIColors.CYAN,
    'comment': _colorize.ANSIColors.RED,
    'string': _colorize.ANSIColors.BOLD_GREEN,
    'number': _colorize.ANSIColors.YELLOW,
    'op': _colorize.ANSIColors.RESET,
    'definition': _colorize.ANSIColors.BOLD,
    'soft_keyword': _colorize.ANSIColors.BOLD_YELLOW,
    'reset': _colorize.ANSIColors.RESET,
}

TRACEBACK_COLORS = {
    'type': _colorize.ANSIColors.BOLD_GREEN,
    'message': _colorize.ANSIColors.GREEN,
    'filename': _colorize.ANSIColors.GREEN,
    'line_no': _colorize.ANSIColors.GREEN,
    'frame': _colorize.ANSIColors.GREEN,
    'error_highlight': _colorize.ANSIColors.BOLD_RED,
    'error_range': _colorize.ANSIColors.RED,
    'reset': _colorize.ANSIColors.RESET,
}

UNITTEST_COLORS = {
    'passed': _colorize.ANSIColors.GREEN,
    'warn': _colorize.ANSIColors.YELLOW,
    'fail': _colorize.ANSIColors.RED,
    'fail_info': _colorize.ANSIColors.BOLD_RED,
    'reset': _colorize.ANSIColors.RESET,
}

theme = _colorize.Theme(
    argparse=_colorize.Argparse(**ARGPARSE_COLORS),
    syntax=_colorize.Syntax(**SYNTAX_COLORS),
    traceback=_colorize.Traceback(**TRACEBACK_COLORS),
    unittest=_colorize.Unittest(**UNITTEST_COLORS),
)
_colorize.set_theme(theme)
del theme
del ARGPARSE_COLORS
del SYNTAX_COLORS
del TRACEBACK_COLORS
del UNITTEST_COLORS
