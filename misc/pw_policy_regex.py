from re import compile

PW_REGEX = compile(r'(?P<min>\d)-(?P<max>\d) (?P<char>[a-z]): (?P<pw>[a-z]+)')


def parse_password(pw_str):
    """Return min, max, character and password using REGEX."""

    match_obj = PW_REGEX.fullmatch(pw_str)
    match_dict = match_obj.groupdict()

    match_dict['min'] = int(match_dict['min'])
    match_dict['max'] = int(match_dict['max'])

    return match_dict


def validate_password_dict(pw_dict):
    """Return True if password complies with policy."""

    char_count = pw_dict['pw'].count(pw_dict['char'])

    return char_count >= pw_dict['min'] and char_count <= pw_dict['max']


def count_valid_passwords(pw_list):
    """Return number of valid passwords."""

    valid_count = 0

    for pw_str in pw_list:
        pw_dict = parse_password(pw_str)

        if validate_password_dict(pw_dict):
            valid_count += 1

    return valid_count
