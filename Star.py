import json
class Star:
    
    def __init__(self, def_file: str = "def.json") -> None:
        self.__def_file = def_file
        self.__def_dict = self.__LoadDefDict__()

    def __LoadDefDict__(self) -> dict:
        try:
            f = open(self.__def_file, 'r')
        except(FileNotFoundError):
            print(f"Def File ({self.__def_file}) Not found")
            return {}
            #TODO: Create propper exception handling
        
        return json.load(f)["def"]["star"]

if(__name__ == "__main__"):
    print("This is a class lib file")