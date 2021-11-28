'''
This class defines the Dt List for enforcing specific data types on a list
'''
class Dt_list:

    def __init__(self, data_type, n_list) -> None:
        self.__data_type = None
        self.__root_list = []
        self.length = 0

        self.__data_type = data_type

        for item in n_list:
            if self.is_valid_data_type(item):
                 self.add(item)
            else:
                print(f'Error: {item} not of specified dt type')
                exit(1)
        self.length = len(self.__root_list)

    def is_valid_data_type(self, item):

        try:
           if self.__data_type == "int" and type(item) is int:
             item = int(item)
           elif self.__data_type == "str" and type(item) is str:
             item = str(item)
           elif self.__data_type == "float" and type(item) is float:
             item = float(item)
           elif self.__data_type == "bool" and type(item) is bool:
             item = bool(item)
           else:
             return False
           return True

        except:
            return False

    def __cast(self, item):
        if self.__data_type == "int":
             item = int(item)
        elif self.__data_type == "str":
             item = str(item)
        elif self.__data_type == "float":
             item = float(item)
        elif self.__data_type == "bool":
             item = bool(item)
        else:
            pass       

        return item 

    def add(self, item) -> None:

        if self.is_valid_data_type(item):
            self.__root_list.append(self.__cast(item))
            self.length += 1
        else:
            print(f'Error: {item}. Invalid Type for dt list')
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

    def length(self):
        return self.length

    def is_empty(self):
        return self.length == 0

    def remove_at(self, index):
        
        if index >= 0 and index < self.length -1:
            self.__root_list = self.__root_list[:index] + self.__root_list[index+1:]




