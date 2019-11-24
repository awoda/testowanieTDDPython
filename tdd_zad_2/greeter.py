def names_parser(names):
    names_string = ""
    if len(names) == 1:
        return names[0]
    for x in range(1, len(names)):
        if x == len(names) - 1:
            names_string += "and " + names[x]
        else:
            names_string += names[x] + ", "

    return "{}, {}".format(names[0], names_string)


def greet(*additional_names):
    additional_names = list(additional_names)
    if len(additional_names) == 0:
        additional_names.append("my friend")

    names_uppercase = []
    names_normal = []

    for name in additional_names:
        if name.isupper():
            names_uppercase.append(name)
        else:
            names_normal.append(name)

    if len(names_normal) > 0 and len(names_uppercase) == 0:
        return "Hello {}.".format(names_parser(names_normal))

    if len(names_normal) == 0 and len(names_uppercase) > 0:
        return 'HELLO {}!'.format(names_parser(names_uppercase))

    if len(names_normal) > 0 and len(names_uppercase) > 0:
        normal_names = names_parser(names_normal)
        upper_names = names_parser(names_uppercase).upper()
        return 'Hello {}. AND HELLO {}!'.format(normal_names, upper_names)
