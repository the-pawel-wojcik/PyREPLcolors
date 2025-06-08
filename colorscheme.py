try:
    from _colorize import set_theme, default_theme, Syntax, ANSIColors
    # no overhead: _colorize imports dataclasses which imports copy
    from copy import replace
except ImportError:
    pass
else:
    theme = replace(
        default_theme,
        syntax=replace(
            default_theme.syntax,
            prompt=ANSIColors.BOLD_WHITE,
            keyword=ANSIColors.BOLD_YELLOW,
            comment=ANSIColors.GREY,
            string=ANSIColors.BACKGROUND_BLACK + ANSIColors.YELLOW,
            soft_keyword=ANSIColors.BOLD_YELLOW,
        )
    )
    set_theme(theme)
    del set_theme, default_theme, Syntax, ANSIColors
