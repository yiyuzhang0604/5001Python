from text_cleaner import TextCleaner


def test_constructor():
    """test the constructor """
    cleaner = TextCleaner("Lisa, you are a good dog.")
    assert cleaner.string == "Lisa, you are a good dog."


def test_convert_to_lower():
    """test the convert_to_lower function"""
    tx = TextCleaner("Lisa, you are a good dog.")
    tx.convert_to_lower("Lisa, you are a good dog.")
    assert tx.convert_to_lower("Lisa, you are a good dog.") == "lisa, you are a good dog."


def test_no_punctuation():
    """ test the no_puncuation function"""
    tx = TextCleaner("Lisa, you are a good dog.")
    tx.no_puntuation("Lisa, you are a good dog.")
    assert tx.no_puntuation("Lisa, you are a good dog.") == "Lisa COMMA you are a good dog."
