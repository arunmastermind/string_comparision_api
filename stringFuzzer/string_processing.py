from __future__ import unicode_literals
import re
import string
import sys

PY3 = sys.version_info[0] == 3
if PY3:
    string = str

class StringProcessor(object):
    regex = re.compile(r"(?ui)\W")

    @classmethod
    def replace_non_letters_non_numbers_with_whitespace(cls, a_string):
        """
        This function replaces any sequence of non letters and non
        numbers with a single white space.
        """
        return cls.regex.sub(" ", a_string)

    strip = staticmethod(string.strip)
    to_lower_case = staticmethod(string.lower)
    to_upper_case = staticmethod(string.upper)
