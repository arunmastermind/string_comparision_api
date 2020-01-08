from __future__ import unicode_literals
from stringFuzzer.StringMatcher import StringMatcher as SequenceMatcher
from difflib import SequenceMatcher
import stringFuzzer.utils as utils
import stringFuzzer.utils

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords,wordnet

@utils.check_for_none
@utils.check_for_equivalence
@utils.check_empty_string
def matchPercent(s1, s2):
    s1, s2 = utils.make_type_consistent(s1, s2)

    m = SequenceMatcher(None, s1, s2)
    return utils.intr(100 * m.ratio())

@utils.check_for_none
@utils.check_for_equivalence
@utils.check_empty_string
def partial_matchPercent(s1, s2):
    s1, s2 = utils.make_type_consistent(s1, s2)

    if len(s1) <= len(s2):
        shorter = s1
        longer = s2
    else:
        shorter = s2
        longer = s1

    m = SequenceMatcher(None, shorter, longer)
    blocks = m.get_matching_blocks()

    scores = []
    for block in blocks:
        long_start = block[1] - block[0] if (block[1] - block[0]) > 0 else 0
        long_end = long_start + len(shorter)
        long_substr = longer[long_start:long_end]

        m2 = SequenceMatcher(None, shorter, long_substr)
        r = m2.ratio()
        if r > .995:
            return 100
        else:
            scores.append(r)

    return utils.intr(100 * max(scores))

def tokeniseString(str):
    filtered_sentence = []
    stop_words = set(stopwords.words("english"))
    for words in word_tokenize(str):
        if words not in stop_words:
            # if words.isalnum():
                # print(words)
            filtered_sentence.append(words)
    return filtered_sentence
    # filtered_sentence1 = tokeniseString(str1)
    # filtered_sentence2 = tokeniseString(str2)
