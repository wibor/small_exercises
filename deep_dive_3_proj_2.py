from itertools import zip_longest

template = {
    'user_id': int,
    'name': {
        'first': str,
        'last': str
    },
    'bio': {
        'dob': {
            'year': int,
            'month': int,
            'day': int
        },
        'birthplace': {
            'country': str,
            'city': str
        }
    }
}
john = {
    'user_id': 100,
    'name': {
        'first': 'John',
        'last': 'Cleese'
    },
    'bio': {
        'dob': {
            'year': 1939,
            'month': 11,
            'day': 27
        },
        'birthplace': {
            'country': 'United Kingdom',
            'city': 'Weston-super-Mare'
        }
    }
}
eric = {
    'user_id': 101,
    'name': {
        'first': 'Eric',
        'last': 'Idle'
    },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 3,
            'day': 29
        },
        'birthplace': {

        }
    }
}
michael = {
    'user_id': 100,
    'name': {
        'first': 'Michael',
        'last': 'Palin'
    },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 'May',
            'day': 5
        },
        'birthplace': {
            'country': 'United Kingdom',
            'city': 'Sheffield'
        }
    }
}

# my ugly solution
def is_match(data, pattern):
    if data.keys() != pattern.keys():
        mismatch = [p for d, p in zip_longest(data.keys(),pattern.keys()) if d!=p]
        print('ERROR value missing: ' + str(mismatch))
        return False
    else:
        for data_value, pattern_value in zip_longest(data.values(), pattern.values()):
            if isinstance(pattern_value, dict):
                result = is_match(data_value, pattern_value)
                if not result:
                    return False
            elif not isinstance(data_value, pattern_value):
                print('ERROR value wrong type: ' + data_value + ' is not ' + str(pattern_value.__name__))
                return False

    return True

if __name=='__main__':
    print(is_match(john, template))
    print(is_match(eric, template))
    print(is_match(michael, template))
