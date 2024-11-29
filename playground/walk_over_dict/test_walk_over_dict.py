from operator import getitem, setitem

from playground.walk_over_dict.walk_over_dict import walk_dict


def test_simple_dict():
    dct = {"a": 10}

    items = list(walk_dict(dct))

    assert items == [
        (10, ("a",)),
    ]


def test_simple_list():
    lst = [{"a": 1}]
    items = list(walk_dict(lst))

    assert items == [
        (1, (0, "a")),
        ({"a": 1}, (0,)),
    ]


def test_nested_dict():
    dct = {"a": 10, "b": {"c": 12}}

    items = list(walk_dict(dct))

    assert items == [
        (10, ("a",)),
        (12, ("b", "c")),
        ({"c": 12}, ("b",)),
    ]


def test_dict_with_list():
    dct = {"a": [1, 2]}

    items = list(walk_dict(dct))

    assert items == [
        (1, ("a", 0)),
        (2, ("a", 1)),
        ([1, 2], ("a",)),
    ]


def test_dict_with_list_of_dicts():
    dct = {"a": [{"b": 1}, {"c": 2}]}

    items = list(walk_dict(dct))

    assert items == [
        (1, ("a", 0, "b")),
        ({"b": 1}, ("a", 0)),
        (2, ("a", 1, "c")),
        ({"c": 2}, ("a", 1)),
        ([{"b": 1}, {"c": 2}], ("a",)),
    ]


def test_set_value_lazy():
    dct = {"replace": 10, "a": [6, {"replace": 11}]}

    for _, path in list(walk_dict(dct)):
        if path[-1] == "replace":
            mother = dct
            for parent in path[:-1]:
                mother = getitem(mother, parent)
            setitem(mother, path[-1], -1)

    assert dct == {"replace": -1, "a": [6, {"replace": -1}]}
