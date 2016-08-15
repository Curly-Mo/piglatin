import logging

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


VOWELS = 'aeiouy'


def translate(text):
    pig_words = translate_text(text)
    pig_text = ' '.join(pig_words)
    return pig_text


def translate_text(text):
    for word in text.split(' '):
        word = word.strip()
        punct = ''
        punctuation = '.,'
        if word[-1] in punctuation:
            word, punct = word[:-1], word[-1:]
        word = translate_word(word)
        word = ''.join([word, punct])
        yield word


def translate_word(word):
    if starts_with_vowel_sound(word.lower()):
        suffix = 'yay'
        idx = 0
    else:
        suffix = 'ay'
        try:
            # Get index of first vowel
            idx = max(next(i for i, c in enumerate(word) if c in VOWELS), 1)
        except StopIteration:
            # Index is zero if no vowel in word
            idx = 0
    pig_word = ''.join([word[idx:], word[:idx], suffix]).lower()
    if word.istitle():
        pig_word = pig_word.capitalize()
    return pig_word


def starts_with_vowel_sound(word):
    """Returns true if word begins with a vowel sound"""
    try:
        # Attempt to use nltk vowel phonemes
        for syllables in PRONUNCIATIONS.get(word, []):
            syllable = syllables[0]
            # Vowel phonemes end in an integer lexical stress marker
            return syllable[-1].isdigit()
        return False
    except:
        # Naive fallback
        if word[0] in VOWELS:
            return True
        return False
