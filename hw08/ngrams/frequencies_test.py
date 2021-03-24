from ngrams import NgramFrequencies


def test_constructor():
    """ test the constructor """
    uni = NgramFrequencies("It's a good dog.", 1)
    assert uni.dict == {}
    assert uni.count == 0
    assert uni.total_count == 0
    assert uni.list == []


def test_add_item():
    uni = NgramFrequencies("It's a good dog.", 1)
    uni.add_item("good")
    uni.add_item("a")
    assert uni.dict["good"] == 1
    assert uni.dict["a"] == 1


def test_get_list():
    uni = NgramFrequencies("It's a good dog.", 1)
    uni.get_list("It's a good dog.", 1)
    assert uni.list == ["It's", "a", "good", "dog."]
    assert uni.total_count == 4


def test_top_n_counts():
    uni = NgramFrequencies("It's a good dog.", 1)
    uni.get_list("It's a good dog.", 1)
    res = uni.top_n_counts(3)
    assert res == [("It's", 1), ("a", 1), ("good", 1)]


def test_frequency():
    uni = NgramFrequencies("It's a good dog.", 1)
    uni.get_list("It's a good dog.", 1)
    freq = uni.frequency("good")
    assert freq == 0.25


def test_top_n_frequency():
    uni = NgramFrequencies("It's a good dog.", 1)
    uni.get_list("It's a good dog.", 1)
    res = uni.top_n_freqs(3)
    assert uni.dict == {"It's": 1, "a": 1, "good": 1, "dog.": 1}
    assert uni.total_count == 4
    assert uni.freq == {"It's": 0.25, "a": 0.25, "good": 0.25, "dog.": 0.25}
