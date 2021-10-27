'''
This class defines the Dt List for enforcing specific data types on a list
'''
class Dt_list:

    __root_list = []
    __data_type = None

    def __init__(self, data_type, n_list) -> None:
        self.__data_type = data_type
        self.__root_list = n_list

    def is_valid_list(self, m_list):
        pass



    def add(self, item) -> None:

        try:
            if self.__data_type == "int":
                item = int(item)
            elif self.__data_type == "str":
                item = str(item)
            elif self.__data_type == "float":
                item = float(item)
            elif self.__data_type == "bool":
                item = bool(item)
            else:
                print("No Data Type Matches")
                exit(1)

            self.__root_list.append(item)

        except:
            print(f'{item} is not of type {self.__data_type}')
            exit(1)
        
    def __str__(self) -> str:
        output = "["
        for index, num in enumerate(self.__root_list):
            if index > 0 :
                output += f', {num}' 
            else:
                 output += f'{num}'
        output += "]"
        return output
