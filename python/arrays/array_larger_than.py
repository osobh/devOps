#Interview Question 01

string01 = "112"
string02 = "111"

#Given the strings above, find the larger of the 2

def larger_than(string01, string02):
    if len(string01) > len(string02):
        return True
    elif len(string02) > len(string01):
        return False

    for i in range(len(string01)):
        if string01[i] == string02[i]:
            continue
        elif string01[i] > string02[i]:
            print True
            return True
        else:
            print False
            return False
    print False
    return False


larger_than(string01,string02)
