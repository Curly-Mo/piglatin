import unittest
from mock import patch

from piglatin import piglatin


class TestTranslate(unittest.TestCase):
    def test_vowel(self):
        test_words = [
            ('hello', False),
            ('yay', False),
            ('an', True),
            ('honest', True),
        ]
        for word, expected in test_words:
            actual = piglatin.starts_with_vowel_sound(word)
            self.assertEqual(
                actual,
                expected,
                msg='"{}" should be {}'.format(word, expected)
            )

    @patch("piglatin.piglatin.PRONUNCIATIONS")
    def test_vowel_fallback(self, cmudict_mock):
        cmudict_mock = None
        test_words = [
            ('hello', False),
            ('yay', False),
            ('an', True),
        ]
        for word, expected in test_words:
            actual = piglatin.starts_with_vowel_sound(word)
            self.assertEqual(
                actual,
                expected,
                msg='"{}" should be {}'.format(word, expected)
            )

    def test_translate_word(self):
        test_words = [
            ('hello', 'ellohay'),
            ('yay', 'ayyay'),
            ('honest', 'honestyay'),
            ('pig', 'igpay'),
            ('banana', 'ananabay'),
            ('trash', 'ashtray'),
            ('happy', 'appyhay'),
            ('duck', 'uckday'),
            ('glove', 'oveglay'),
            ('eat', 'eatyay'),
            ('omelet', 'omeletyay'),
            ('are', 'areyay'),
        ]
        for word, expected in test_words:
            actual = piglatin.translate_word(word)
            self.assertEqual(
                actual,
                expected,
                msg='"{}" should translate to {}'.format(word, expected)
            )

    def test_translate_text(self):
        text = "This is a test."
        expected = ('Isthay', 'isyay', 'ayay', 'esttay.')
        actual = piglatin.translate_text(text)
        self.assertEqual(tuple(actual), expected)

    def test_translate(self):
        text = (
            "Some words should be Capitalized, for instance Mr. H. Jon "
            "Benjamin. "
            "Contractions shouldn't be a problem. We could even Embiggen our "
            "dictionary with fake smlorbs, and other perfectly cromulent "
            "fleebs."
            )
        expected = (
            "Omesay ordsway ouldshay ebay Apitalizedcay, orfay instanceyay "
            "Mray. Hyay. Onjay Enjaminbay. "
            "Ontractionscay ouldn'tshay ebay ayay oblempray. Eway ouldcay "
            "evenyay Embiggenyay ouryay ictionaryday ithway akefay orbssmlay, "
            "andyay otheryay erfectlypay omulentcray eebsflay."
        )
        self.maxDiff = None
        actual = piglatin.translate(text)
        self.assertEqual(actual, expected)

    @patch("piglatin.piglatin.PRONUNCIATIONS")
    def test_translate_fallback(self, cmudict_mock):
        cmudict_mock = None
        piglatin.PRONUNCIATIONS = None
        text = (
            "Some words should be Capitalized, for instance Mr. Bovine Joni. "
            "Contractions shouldn't be a problem. We could even Embiggen our "
            "dictionary with fake smlorbs, and other perfectly cromulent "
            "fleebs."
            )
        expected = (
            "Omesay ordsway ouldshay ebay Apitalizedcay, orfay instanceyay "
            "Mray. Ovinebay Onijay. "
            "Ontractionscay ouldn'tshay ebay ayay oblempray. Eway ouldcay "
            "evenyay Embiggenyay ouryay ictionaryday ithway akefay orbssmlay, "
            "andyay otheryay erfectlypay omulentcray eebsflay."
        )
        self.maxDiff = None
        actual = piglatin.translate(text)
        self.assertEqual(actual, expected)
