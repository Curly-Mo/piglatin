import logging
import string

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

try:
    from nltk.corpus import cmudict
    logger.info('Loading NLTK pronunciation dictionary...')
    PRONUNCIATIONS = cmudict.dict()
except:
    logger.warn(
        'NLTK library not found, falling back to naive language processing.'
    )


def translate(text):
    """Convert a string into piglatin"""
    pig_words = translate_text(text)
    pig_text = ' '.join(pig_words)
    return pig_text


def translate_text(text):
    """Take a string and convert each word to piglatin"""
    # A naive split works better than nltk.word_tokenize
    for word in text.split(' '):
        word = word.strip()
        punctuation = None
        if word[-1] in string.punctuation:
            word, punctuation = word[:-1], word[-1:]
        word = translate_word(word)
        if punctuation:
            word = ''.join([word, punctuation])
        yield word


def translate_word(word):
    """Convert a word into piglatin"""
    if starts_with_vowel_sound(word.lower()):
        suffix = 'yay'
        idx = 0
    else:
        suffix = 'ay'
        try:
            # Get index of first vowel
            vowels = 'aeiouy'
            idx = next(i for i, c in enumerate(word) if c in vowels and i != 0)
        except StopIteration:
            # Index is zero if no vowel in word
            idx = 0
    pig_word = ''.join([word[idx:], word[:idx], suffix]).lower()
    # Capitalize first letter if the original did
    if word.istitle():
        pig_word = pig_word.capitalize()
    return pig_word


def starts_with_vowel_sound(word):
    """Returns whether a word begins with a vowel sound"""
    try:
        # Attempt to use nltk vowel phonemes
        for syllables in PRONUNCIATIONS.get(word, []):
            syllable = syllables[0]
            # Vowel phonemes end in an integer lexical stress marker
            return syllable[-1].isdigit()
        return False
    except:
        # Naive fallback
        vowels = 'aeiou'
        if word[0] in vowels:
            return True
        return False
