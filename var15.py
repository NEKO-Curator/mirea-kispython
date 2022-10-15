def zero(items, left, right):
    if items[0] == 2014:
        return left
    if items[0] == 1981:
        return right


def three(items, left, right):
    if items[3] == 'XML':
        return left
    if items[3] == 'EC':
        return right


def two(items, left, right):
    if items[2] == 1981:
        return left
    if items[2] == 1984:
        return right


def one(items, left, middle, right):
    if items[1] == 'FISH':
        return left
    if items[1] == 'GLSL':
        return middle
    if items[1] == 'GAP':
        return right

def four(items, left, right):
    if items[4] == 1980:
        return left
    if items[4] == 1988:
        return right

def main(items):
    return two(
        items,
        zero(
            items,
            four(
                items,
                one(
                    items,
                    0,
                    1,
                    2,
                ),
                one(
                    items,
                    3,
                    4,
                    5,
                ),
            ),
            6
        ),
        three(
            items,
            7,
            four(
                items,
                8,
                zero(
                    items,
                    9,
                    10,
                ),
            ),
        ),
    )

print(main([2014, 'FISH', 1981, 'EC', 1980]))
