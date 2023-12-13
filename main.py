""" Фаил с функциями """

import markdown


def bold(s: str) -> str:
    """ Функция возвращающая
        выражение с
        тегами <em> и </em>
    """
    if s[0] == "*" and s[-1] == "*" and s.count("*") == 2:
        print(markdown.markdown(s))
        return markdown.markdown(s)
    else:
        print(s)
        return s


def itallic(s: str) -> str:
    """ Функция возвращающая
            выражение с
            тегами <strong> и </strong>
    """
    if s[:2] == "**" and s[-2:] == "**":
        print(markdown.markdown(s))
        return markdown.markdown(s)
    else:
        print(s)
        return s