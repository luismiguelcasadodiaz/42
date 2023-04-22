#!/usr/bin/python3


def has_only_one_parameter(fun) -> bool:
    """
    https: //stackoverflow.com/questions/847936/
    how-can-i-find-the-number-of-arguments-of-a-python-function
    """
    return (fun.__code__.co_argcount == 1)


def ft_map(fun,  ite):
    """Map the function to all elements of the iterable.
    Args:
    function_to_apply:  a function taking an iterable.
    iterable:  an iterable object (list,  tuple,  iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """
    try:
        if ite is not None and fun is not None:

            if not has_only_one_parameter(fun):
                msg = f"function '{fun.__name__}' accepts\
                      more than one parameter"
                raise ValueError(msg)
            else:
                msg = ""
                result = []
                for elem in ite:
                    result.append(fun(elem))

                if isinstance(ite,  list):
                    yield result
                if isinstance(ite,  tuple):
                    yield tuple(result)
                if isinstance(ite,  dict):
                    yield dict(zip(ite.keys(),  result))
                if isinstance(ite,  set):
                    yield set(result)
                if isinstance(ite,  str):
                    yield ''.join(result)
        else:
            if fun is not None:
                msg = f"Can not filter object {ite} \
                    with function {fun.__name__}"
            else:
                msg = f"Can not filter object {ite} \
                    with function {fun}"
            raise ValueError("ft_filter:  " + msg)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    my_set_ = set(my_list)
    my_tupl = tuple(my_list)
    my_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
    my_stri = "1234b67890"

    def duplicate(elem):
        return elem * 2

    def triplicate(elem):
        return elem * 3

    print("======================testing Extrem cases =====================")
    print("==>ft_map(None,  None)")
    print(ft_map(None, None))
    for elem in ft_map(None,  None):
        print(elem)

    print("==>ft_map(duplicate, None)")
    print(ft_map(duplicate, None))
    for elem in ft_map(duplicate,  None):
        print(elem)

    print("==>ft_map(None,  my_list)")
    print(ft_map(None,  my_list))
    for elem in ft_map(None,  my_list):
        print(elem)

    print("==>ft_map(my_dict,  my_list)")
    print(ft_map(my_dict,  my_list))
    for elem in ft_map(my_dict,  my_list):
        print(elem)

    print("======================testing list ==========================")
    print("==>ft_map(triplicate,  my_list)")
    print(ft_map(triplicate, my_list))
    for elem in ft_map(triplicate,  my_list):
        print(elem)
    print("Original list ==>",  my_list)
    print("==>ft_map(duplicate, my_list)")
    print(ft_map(duplicate, my_list))
    for elem in ft_map(duplicate,  my_list):
        print(elem)
    print("Original list ==>",  my_list)
    print("==>ft_map(duplicate,  [])")
    print(ft_map(duplicate,  []))
    for elem in ft_map(duplicate,  []):
        print(elem)
    print("======================testing sets ==========================")
    print("==>ft_map(triplicate,  ()))")
    print(ft_map(triplicate,  set()))
    for elem in ft_map(triplicate,  set()):
        print(elem)
    print("==>ft_map(duplicate,  my_set_)")
    print(ft_map(duplicate,  my_set_))
    for elem in ft_map(duplicate,  my_set_):
        print(elem)
    print("Original set ==>",  my_set_)
    print("==>ft_map(duplicate, [])")
    print(ft_map(duplicate, set()))
    for elem in ft_map(duplicate, set()):
        print(elem)

    print("======================testing strings ==========================")
    print("==>ft_map(triplicate,  my_stri)")
    print(ft_map(triplicate,  my_stri))
    for elem in ft_map(triplicate,  my_stri):
        print(elem)
    print("Original string ==>",  my_stri)

    print("==>ft_map(duplicate,  '""')")
    print(ft_map(duplicate,  ""))
    for elem in ft_map(duplicate,  ""):
        print(elem)
    print("==>ft_map(duplicate,  my_stri)")
    print(ft_map(duplicate,  my_stri))
    for elem in ft_map(duplicate,  my_stri):
        print(elem)
    print("Original string ==>",  my_stri)
    print("==>ft_map(triplicate,  '""')")
    print(ft_map(duplicate,  ""))
    for elem in ft_map(duplicate,  ""):
        print(elem)

    print("======================testing tuples ==========================")
    print("==>ft_map(triplicate,  (1,  2,  3,  4,  5,  'b',  7,  8,  9,  10)")
    print(ft_map(triplicate,  (1, 2, 3, 4, 5, 'b', 7, 8, 9, 10)))
    for elem in ft_map(triplicate,  (1, 2, 3, 4, 5, 'b', 7, 8, 9, 10)):
        print(elem)

    print("==>ft_map(triplicate,  my_tupl)")
    print(ft_map(triplicate,  my_tupl))
    for elem in ft_map(triplicate,  my_tupl):
        print(elem)
    print("Original tup ==>",  my_tupl)

    print("==>ft_map(duplicate,  my_tupl)")
    print(ft_map(duplicate,  my_tupl))
    for elem in ft_map(duplicate,  my_tupl):
        print(elem)
    print("Original tup ==>",  my_tupl)

    print("==>ft_map(triplicate,  tuple())")
    print(ft_map(duplicate,  tuple()))
    for elem in ft_map(duplicate,  ""):
        print(elem)

    print("======================testing dictionaries =======================")
    print("==>ft_map(triplicate,{1: 1, 2: 2, 3: 3, 4: 4, 5: 'b', 6: 6, \
          7: 7, 8: 8, 9: 9, 10: 10}")
    print(ft_map(triplicate,
                 {1: 1, 2: 2, 3: 3, 4: 4, 5: 'b', 6: 6, 7: 7,
                  8: 8, 9: 9, 10: 10}))
    for elem in ft_map(triplicate,
                       {1: 1, 2: 2, 3: 3, 4: 4, 5: 'b', 6: 6,
                        7: 7, 8: 8, 9: 9, 10: 10}):
        print(elem)

    print("==>ft_map(triplicate,  my_dict)")
    print(ft_map(triplicate,  my_dict))
    for elem in ft_map(triplicate,  my_dict):
        print(elem)
    print("Original dict ==>",  my_dict)

    print("==>ft_map(duplicate,  my_dict)")
    print(ft_map(duplicate,  my_dict))
    for elem in ft_map(duplicate,  my_dict):
        print(elem)
    print("Original dict ==>",  my_dict)

    print("==>ft_map(triplicate,  dict())")
    print(ft_map(duplicate,  dict()))
    for elem in ft_map(duplicate,  dict()):
        print(elem)
