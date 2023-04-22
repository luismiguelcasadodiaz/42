#!/usr/bin/python3
"""
Python’s filter() is a built-in function that allows you to process an
iterable and extract those items that satisfy a given condition.

Iterables are
List
Tuple
Dictionary
set
"""


def has_only_one_parameter(fun) -> bool:
    return (fun.__code__.co_argcount == 1)


def ft_filter(fun, ite):
    """
    Filter the result of function apply to all elements of the iterable.
    Args:
        function_to_apply:  a function taking an iterable.
        iterable:  an iterable object (list, tuple, iterator).
    Return:
        An iterable.
        None if the iterable can not be used by the function.
    """
    try:
        if ite is not None and fun is not None:
            if str(type(fun)) == "<class 'function'>":
                if has_only_one_parameter(fun):
                    if isinstance(ite, list):
                        return filter_lis(ite, fun)
                    if isinstance(ite, tuple):
                        return filter_tup(ite, fun)
                    if isinstance(ite, dict):
                        return filter_dic(ite, fun)
                    if isinstance(ite, set):
                        return filter_set(ite, fun)
                    if isinstance(ite, str):
                        return filter_str(ite, fun)
                    msg = f"Can not filter object {type(ite)}"
                else:
                    msg = f"function '{fun.__name__}' accepts\
                          more than one parameter"
            else:
                msg = f"Argument function is not a function"
        else:
            msg = f"Can not filter object {ite} \
                with function {fun.__name__}"
        raise ValueError("ft_filter:  " + msg)
    except Exception as e:
        print(e)


def filter_lis(ite, fun):
    result = []
    for elem in ite:
        if fun(elem):
            result.append(elem)
    yield result


def filter_tup(ite, fun):
    result = tuple()
    for elem in ite:
        if fun(elem):
            result = result + (elem,)
    yield result


def filter_dic(ite, fun):
    result = {}
    for k, v in ite.items():
        if fun(v):
            result[k] = v
    yield result


def filter_set(ite, fun):
    result = set()
    for elem in ite:
        if fun(elem):
            result.add(elem)
    yield result


def filter_str(ite, fun):
    result = ""
    for elem in ite:
        if fun(elem):
            result = result + elem
    yield result


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    my_set_ = set(my_list)
    my_tupl = tuple(my_list)
    my_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
    my_stri = "1234b67890"

    def even(elem):
        return (elem % 2 == 0)

    def filter_b(elem):
        return (elem == 'b')
    print("======================testing Extrem cases ====================")
    print("==>ft_filter(None, None)")
    print(ft_filter(None, None))

    print("==>ft_filter(even, None)")
    print(ft_filter(even, None))

    print("==>ft_filter(None, my_list)")
    print(ft_filter(None, my_list))

    print("==>ft_filter(my_dict, my_list)")
    print(ft_filter(my_dict, my_list, ))
    print("======================testing list ==========================")
    print("==>ft_filter(filter_b, my_list)")
    print(ft_filter(filter_b, my_list))

    print("==>ft_filter(even, my_list)")

    for elem in ft_filter(even, my_list):
        print(elem)
    print("Original list ==>", my_list)

    print("==>ft_filter(even, [])")
    print(ft_filter(even, []))
    for elem in ft_filter(even, []):
        print(elem)
    print("======================testing sets ==========================")
    print("==>ft_filter(filter_b, ()))")
    print(ft_filter(filter_b, set()))

    print("==>ft_filter(even, my_set_)")
    print(ft_filter(even, my_set_))

    print("==>ft_filter(even,[])")
    print(ft_filter(even, set()))

    print("======================testing stings ==========================")
    print("==>ft_filter(filter_b, my_stri)")
    print(ft_filter(filter_b, my_stri))

    print("==>ft_filter(even, '""')")
    print(ft_filter(even, ""))

    print("==>ft_filter(even, my_stri)")
    print(ft_filter(even, my_stri))

    print("==>ft_filter(filter_b, '""')")
    print(ft_filter(even, ""))
    print("======================testing tuples ==========================")
    print("==>ft_filter(filter_b, (1, 2, 3, 4, 5, 'b', 7, 8, 9, 10)")
    print(ft_filter(filter_b, (1, 2, 3, 4, 5, 'b', 7, 8, 9, 10)))

    print("==>ft_filter(filter_b, my_tupl)")
    print(ft_filter(filter_b, my_tupl))
    print("==>ft_filter(even, my_tupl)")
    print(ft_filter(even, my_tupl))

    print("==>ft_filter(filter_b, tuple())")
    print(ft_filter(even, tuple()))
    print("======================testing dictionaries =====================")
    print("==>ft_filter(filter_b,\
           {1: 1,2: 2,3: 3,4: 4,5: 'b',6: 6,7: 7,8: 8,9: 9,10: 10}")
    print(ft_filter(filter_b,
                    {1: 1, 2: 2, 3: 3, 4: 4, 5: 'b',
                    6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
                    ))

    print("==>ft_filter(filter_b, my_tupl)")
    print(ft_filter(filter_b, my_dict))
    print("==>ft_filter(even, my_tupl)")
    print(ft_filter(even, my_dict))

    print("==>ft_filter(filter_b, tuple())")
    print(ft_filter(even, dict()))
