class RoseDictionary : 
    
    def __init__(self , ini_data = None):
        self.data = ini_data or {}
    
    def __setitem__(self,key,value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __getitem__(self,key):
        return self.data[key]

    def keys(self) : 
        return list(self.data.keys())
    
    def values(self) :
        return list(self.data.values())
    
    def items(self) :
        return list(self.data.items())
    

    
    def pop_item(self, raise_error = None , error_msg = None , default = None ):
        n = len(self.keys()) - 1
        if n == -1:
            if raise_error == True:
                if error_msg != None:
                    print('KeyError: \'{}\''.format(error_msg))
                elif error_msg == None:
                    print('KeyError: \'error_msg\'')
            else:
                if default != None:
                    return default
                else:
                    if error_msg != None:
                        print(error_msg)
                    else:
                       print('Dictionary was empty and no default value/message was specified.')
        else:
            value = self.values()[n]
            key = self.keys()[n]
            self.__delitem__(key)
            return value
        


    def get_item(self, key, raise_error= None, error_msg= None, default= None):
        try:
            return self.data[key]
        except KeyError:
            if raise_error == True:
                if error_msg != None:
                    print('KeyError: \'{}\''.format(error_msg))
                elif error_msg == None:
                    print('KeyError: \'error_msg\'')
            else:
                if default != None:
                    return default
                else:
                    if error_msg != None:
                        print(error_msg)
                    else:
                       print('Value was not found and no default value/message was specified.')
