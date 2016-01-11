def is_pangram(string, alphabet = 'abcdefghijklmnopqrstuvwxyz', recurring = False):
    if alphabet == "":
        return True
    if recurring:
        string = string.lower() 
    search_char = alphabet[0]
    if search_char in string:
        new_alphabet = alphabet[1:]
        new_string = string.replace(search_char, "")
        return is_pangram(new_string, alphabet=new_alphabet, recurring = True)
    else:
        return False

# def is_pangram(string, alphabet = 'abcdefghijklmnopqrstuvwxyz'):
#     string = map(lambda x: x.lower() if x.lower() in alphabet else None, string)
#     print string
#     alpha_sum = sum(map(lambda x: ord(x.lower()), list(alphabet)))
#     string_sum = sum(map(lambda x: ord(x), string))
#     return alpha_sum == string_sum
# this aint mine

def _is_pangram(letters):
    if len(letters) != 26:
        return False
    else:
        ords = map(lambda x: ord(x.lower()), letters)
        return True if sum(ords) == 2847 and len(list(set(ords))) == 26 else False