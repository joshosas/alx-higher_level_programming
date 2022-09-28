#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def s_r_elm(element):
        return (element if element != search else replace)
    return list(map(s_r_element, my_list))
