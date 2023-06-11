import codewars_test as test


def same_structure_as(original, other):
    if type(original) != type(other) or len(original) != len(other):
        return False

    length = len(original)

    for i in range(length):
        # if type(original[i]) != type(other[i]):
        if (
            type(original[i]) == list
            and type(other[i]) != list
            or type(original[i]) != list
            and type(other[i]) == list
        ):
            return False

        if type(original[i]) == list:
            if not check_same_array(original[i], other[i]):
                return False
    return True


def check_same_array(original, other):
    if len(original) != len(other):
        return False

    length = len(original)
    for i in range(length):
        if type(original[i]) != type(other[i]):
            return False

        if type(original[i]) == list:
            if not check_same_array(original[i], other[i]):
                return False

    return True


test.assert_equals(
    same_structure_as([1, [1, 1]], [2, [2, 2]]), True, "[1,[1,1]] same as [2,[2,2]]"
)
test.assert_equals(
    same_structure_as([1, [1, 1]], [[2, 2], 2]),
    False,
    "[1,[1,1]] not same as [[2,2],2]",
)
test.assert_equals(same_structure_as([1, [1, 1]], [2, [2]]), False)
test.assert_equals(same_structure_as([], 1), False)
test.assert_equals(same_structure_as([1, "[", "]"], ["[", "]", 1]), True)
