def above_freezing(temp):
    return temp >= 0

def Upper(sent):
    return sent.upper()

def make_to_dict(some_list):
    try:
        return dict(some_list)
    except ValueError:
        print("not suitable")
