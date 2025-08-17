def parse_command(command):
    if '\"' in command:
        comm, name, number = map(lambda el: el.strip(), command.split('"'))
        return comm, (name, number)
    lst = command.split()
    return lst[0] , (lst[1], lst[2])
