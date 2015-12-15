def sort_a_list(l):
    return(sorted(l, reverse=True))


def sort_by_mark(my_class):
    return(sorted(my_class, reverse=True))


def sort_by_name(my_class):
    from operator import itemgetter
    return(sorted(my_class, key=itemgetter(1)))
