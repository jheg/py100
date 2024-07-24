import sys

def py_falseys():
    false_types = [
        False,
        None,
        0,
        0.0,
        0j,
        "",
        [],
        {},
        (),
        set(),
        frozenset(),
        range(0)
    ]

    for item in false_types:
        if type(item) is str:
            print(f'"" is of type {type(item)} and is {bool(item)}')
        else:    
            print(f'{item} is of type {type(item)} and is {bool(item)}')

    print("You're welcome")
    print(f'This is program {__file__}')
    print(f'This was written in Python version {sys.version}')

py_falseys()