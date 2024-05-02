#email valid check /
#length /
#range
import re


def emailcheck(email):
    import re
    # email  format will be any letter/number/symbol @ letters. 2 letters min
    formatview = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z]+(\.[A-Z|a-z]{2,})+')

    # check if email meets the format
    if re.fullmatch(formatview, email) and lengthcheck(email, 6, 2):
        return True
    else:
        return False


def lengthcheck(character, lengthcompare, symbol):
    # either ==, >=, >, <=, <
    if symbol == 1:
        if len(character) == lengthcompare:
            return True
        else:
            return False

    elif symbol == 2:
        if len(character) >= lengthcompare:
            return True
        else:
            return False

    elif symbol == 3:
        if len(character) > lengthcompare:
            return True
        else:
            return False

    elif symbol == 4:
        if len(character) <= lengthcompare:
            return True
        else:
            return False

    elif symbol == 5:
        if len(character) < lengthcompare:
            return True
        else:
            return False

    else:
        return False


def rangecheck(num, minimum, maximum):
    if num.isnumeric() and minimum.isnumeric() and maximum.isnumeric():
        if num >= minimum and num <= maximum:
            return True
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    print(emailcheck('e@g.bm'))



    # test to see works dsjkdfhsfdhsdfklhsdlhs