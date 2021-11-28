from dt_list import Dt_list

if __name__ == "__main__":
    my_list = Dt_list('int', [1,2,4,4,5,6])
    my_list.add(2)
    my_list.add(23)
    print(my_list)

    my_list.remove_at(6)
    print(my_list)

    my_list2 = Dt_list('str', [])
    my_list2.add('2')
    my_list2.add("string")

    print(my_list2)
    print(my_list.length)
