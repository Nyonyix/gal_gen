import json
import random
class Star:

    #Solar Constants
    s_mass = 1.98847E30
    s_radius = 6.957E8
    s_luminosity = 3.828E26
    s_temperature = 5778
    
    def __init__(self, def_file: str = "def.json") -> None:
        self.__def_file = def_file
        self.__def_dict = self.LoadDefDict()
        self.__temperature = self.GenerateTemperature()
        self.__class = self.GenerateClass() 
        self.__scaler = self.GenerateScaler()
        self.__luminosity = 1.0
        self.__mass = 1.0
        self.__radius = 1.0

    def GetTemperature(self) -> float:
        return self.__temperature

    def GetClass(self) -> str:
        return self.__class
    
    def GetScaler(self) -> float:
        return self.__scaler

    def GetLuminosity(self) -> float:
        return self.__luminosity

    def GetMass(self) -> float:
        return self.__mass

    def GetRadius(self) -> float:
        return self.__radius

    def LoadDefDict(self) -> dict:
        '''
        Tries to load the def json file.
        Returns a dict.
        '''
        try:
            f = open(self.__def_file, 'r')
        except(FileNotFoundError):
            print(f"Def File ({self.__def_file}) Not found")
            return {}
            #TODO: Create propper exception handling
        
        return json.load(f)["def"]["star"]

    def GenValueList(self, value: str) -> tuple:
        '''
        Generates a list of values from the def file with the fractions.
        Returns tuple(list, list).
        '''
        tmp_lst = []
        frac_list = []
        for v in self.__def_dict["classes"].values():
            tmp_lst.append(v[value])
            frac_list.append(v["frac"])
        return (tmp_lst, frac_list)

    def GenerateTemperature(self) -> int:
        '''
        Generates temperature based on percentage fraction and temps defined in def_file.
        Returns int.
        '''
        class_list, frac_list = self.GenValueList("temp")
        temp_range = random.choices(class_list, weights=frac_list, k=1)[0]

        return random.randint(temp_range[0], temp_range[1])

    def GenerateClass(self) -> tuple:
        '''
        Generates or finds the spectral class of the star.
        Returns tuple(str, float)
        '''
        class_temp_list, a = self.GenValueList("temp")
        class_letter_list = list(self.__def_dict["classes"])
        counter = 0
        for l in class_temp_list:
            if self.__temperature < l[1]:
                break
            else:
                counter += 1
        star_class = class_letter_list[counter]

        return star_class

    def GenerateScaler(self) -> float:
        '''
        Determin the subclass of the star.
        Returns float.
        '''
        temp_range = self.__def_dict["classes"][self.__class]["temp"]
        increment = (temp_range[1] - temp_range[0]) / 10
        inc_count = temp_range[0] + increment
        count = 0

        for i in range(10):
            if self.__temperature < inc_count:
                return count
            else:
                inc_count += increment
                count += 1

    def GenerateLuminosity(self) -> float:
        '''
        Generates luminosity based on percentage fraction and temps defined in def_file.
        Returns float.
        '''
        pass

if(__name__ == "__main__"):
    print("This is a class lib file")