#!/usr/bin/env python3
from pandocfilters import toJSONFilter, RawBlock, HorizontalRule

def hrule_to_latex(key, value, format, meta):
    if key == 'HorizontalRule':
        # Traduction de --- en \noindent\rule{\linewidth}{0.4pt}
        return RawBlock('latex', r'\noindent\rule{\linewidth}{0.4pt}')

if __name__ == "__main__":
    toJSONFilter(hrule_to_latex)
