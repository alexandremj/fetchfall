import re

"""
Test class for the regex used on the bot

Feel free to add more test cases

All tests should use re.search(pattern) since that's what
telegram.ext.MessageHandler.Filters.regex() uses
"""

class TestRegex:
    
    # Make a basic match to check if regex is working 
    def test_basic(self):
        assert self.regex.search(r'[[foo]]').group() == '[[foo]]'

    # Check for finding a pattern in the middle of text
    def test_amidst_text(self):
        message = r'Nobody expects the [[Spanish]] Inquisition'
        assert self.regex.search(message).group() == '[[Spanish]]'

    # Test behavior on multiple matches on a single message
    # Currently not passing
    # def test_multiple_matches_test(regex):
    #     message = r'[[foo]] bar [[bla]]'
    #     assert (regex.search(message).groups()
    #             == ('[[foo]]', '[[bla]]'))

    self.regex = re.compile('\[\[([\w | \. | \s |,])*\]\]*')

