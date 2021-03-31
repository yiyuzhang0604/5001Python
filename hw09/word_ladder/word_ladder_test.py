from word_ladder import WordLadder


# TODO: Write appropriate unit tests
def test_make_ladder():
    word_set = create_dict("cat", "ha")
    ladder = WordLadder("cat", "ha", word_set)
    assert ladder.make_ladder() is None

    word_set = create_dict("cat", "hat")
    ladder = WordLadder("cat", "hat", word_set)
    assert ladder.make_ladder().items == ["cat", "hat"]

    word_set = create_dict("love", "hate")
    ladder = WordLadder("love", "hate", word_set)
    assert ladder.make_ladder().items == ["love", "hove", "have", "hate"]

    word_set = create_dict("angel", "devil")
    ladder = WordLadder("angel", "devil", word_set)
    assert ladder.make_ladder().items == ["angel", "anger", "aeger", "leger",
                                          "lever", "level", "devel", "devil"]

    word_set = create_dict("earth", "ocean")
    ladder = WordLadder("earth", "ocean", word_set)
    assert ladder.make_ladder().items == ["earth", "barth", "barih", "baris",
                                          "batis", "bitis", "aitis", "antis",
                                          "antas", "antal", "ontal", "octal",
                                          "octan", "ocean"]


def create_dict(w1, w2):
    word_dict = {}
    f = open('words_alpha.txt')
    for line in f.read().split():
        if len(line) in word_dict.keys():
            word_dict[len(line)].add(line)
        else:
            word_dict[len(line)] = {line}
    return word_dict[len(w1)]
