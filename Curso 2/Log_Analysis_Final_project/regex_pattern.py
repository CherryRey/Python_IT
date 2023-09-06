import re

def find_user(linea):
    pattern = r" ticky: ([\w]+).* \((\w+)\)$"
    find = re.search(pattern, linea)
    if find is None:
        return None
    return "Mensaje: {} y Usuario: {}".format(find[1],find[2])


print(find_user("Jan 31 20:56:58 ubuntu.local ticky: INFO Closed ticket [#4372] (username)"))
print(find_user("Jan 31 02:55:31 ubuntu.local ticky: ERROR Ticket doesn't exist (xlg)"))

def find_error(linea):
    pattern = r" ticky: ([\w]+) (.*) \((\w+)\)$"
    find = re.search(pattern, linea)
    if find is None:
        return None
    return find[2]

print(find_error("Jan 31 02:55:31 ubuntu.local ticky: ERROR Ticket doesn't exist (xlg)"))



def find_info(linea):
    pattern = r" ticky: ([\w]+) (.*) (\[\#\d+\]) \((\w+)\)$"
    find = re.search(pattern, linea)
    if find is None:
        return None
    return find[2]
print(find_info("Jan 31 20:56:58 ubuntu.local ticky: INFO Closed ticket [#4372] (username)"))

print(re.search(r" ticky: ([\w]+) (.* )\((\w+)\)$", "Jan 31 20:56:58 ubuntu.local ticky: INFO Closed ticket [#4372] (BLOSSOM)").group(3))

def find_match(linea):
    match = r"ticky: ([\w]+) ([\w\s']*) ?(\[#\d*\])? \((.*)\)$"
    find = re.search(match, linea)
    if find is None:
        return None
    return find[4]

print(find_match("Jan 31 20:56:58 ubuntu.local ticky: INFO Closed ticket [#4372] (username)"))
print(find_match("Jan 31 02:55:31 ubuntu.local ticky: ERROR Ticket doesn't exist (xlg)"))
print(find_match("Jan 31 15:28:15 ubuntu.local ticky: ERROR Permission denied while closing ticket (enim.non)"))