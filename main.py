
def isMatch(ch1, ch2):
    if ch2 == "{" and ch1 == "}":
        return True
    if ch2 == "[" and ch1 == "]":
        return True
    if ch2 == "(" and ch1 == ")":
        return True
    return False


def isLeft(ch):
    # if ch == "(" or ch == "{" or ch == "[":
    if ch in '({[':
        return True
    else:
        return False


def isValid(s: str) -> bool:
    chStack = []
    for i in range(len(s)):
        curCh = s[i]
        if isLeft(curCh):
            chStack.append(curCh)
        else:
            if len(chStack) == 0:
                return False
            stackCh = chStack.pop()
            if not isMatch(curCh, stackCh):
                return False
    if len(chStack) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    result = isValid("[]")
    print("The result is: ", result)

    result = isValid("[}")
    print("The result is: ", result)

    result = isValid("[()]")
    print("The result is: ", result)

    result = isValid("[{")
    print("The result is: ", result)

    result = isValid("")
    print("The result is: ", result)

    result = isValid("(){}}{")
    print("The result is: ", result)

