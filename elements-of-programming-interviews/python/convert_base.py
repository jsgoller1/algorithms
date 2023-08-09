from test_framework import generic_test


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    # TODO - you fill in here.
    return ''


if __name__ == '__main__':

    assert convert_base("1234", 10, 2) == bin(1234)

    """
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
    """
