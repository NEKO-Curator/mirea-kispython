def zero(items, left, middle, right):
    if items[0] == 2011:
        return left
    if items[0] == 2012:
        return middle
    if items[0] == 1964:
        return right


def three(items, left, right):
    if items[3] == 1977:
        return left
    if items[3] == 1969:
        return right


def two(items, left, right):
    if items[2] == 'MUPAD':
        return left
    if items[2] == 'PUG':
        return right


def one(items, left, middle, right):
    if items[1] == 'PUG':
        return left
    if items[1] == 'XPROC':
        return middle
    if items[1] == 'M4':
        return right


def main(items):
    return one(
        items,
        zero(
            items,
            two(
                items,
                0,
                1,
            ),
            two(
                items,
                2,
                3,
            ),
            three(
                items,
                4,
                5,
            ),
        ),
        three(
            items,
            6,
            zero(
                items,
                7,
                8,
                9,
            )
        ),
        10,
    )

