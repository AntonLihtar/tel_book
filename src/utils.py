def parse_command(command):
    # return 'fail', ''

    if '\"' in command:
        comm, *name = filter(lambda el: el != "", map(lambda el: el.strip(), command.split('"')))
        return comm, tuple(name)
    lst = command.split()
    return lst[0], tuple(lst[1:])
