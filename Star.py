import json
import random
from warnings import resetwarnings
class Star:

    #Solar Constants
    s_mass = 1.98847E30
    s_radius = 6.957E8
    s_luminosity = 3.828E26
    s_temperature = 5778

    def __init__(self, def_file: str = "def.json") -> None:
        self.__def_file = def_file
        self.__def_dict = self.LoadDefDict()
        self.__spec_class = self.GenerateClass()
        print(self.__spec_class)
        self.__temperature = self.GenerateTemperature()
        self.__scaler = self.GenerateScaler()
        self.__luminosity = 1.0
        self.__mass = self.GenerateMass()
        self.__radius = 1.0

    def GetTemperature(self) -> float:
        return self.__temperature

    def GetClass(self) -> str:
        return self.__spec_class

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

    def GenerateClass(self):
        class_list = list(self.__def_dict["classes"].keys())
        weights = []
        for s in class_list:
            weights.append(self.__def_dict["classes"][s]["frac"])

        return random.choices(class_list, weights=weights, k=1)[0]

    def GenerateTemperature(self) -> int:
        '''
        Generates temperature based on percentage fraction and temps defined in def_file.
        Returns int.
        '''
        temp_range = self.__def_dict["classes"][self.__spec_class]["temp"]
        return random.randint(temp_range[0], temp_range[1])

    def GenerateScaler(self) -> float:
        '''
        Determin the subclass of the star.
        Returns float.
        '''
        temp_range = self.__def_dict["classes"][self.__spec_class]["temp"]
        increment = (temp_range[1] - temp_range[0]) / 10
        count = 0
        inc_count =  temp_range[1]
        half_inc = increment / 2
        
        for i in range(11):
            if inc_count - half_inc <= self.__temperature <= inc_count + half_inc:
                return count
            elif count == 9:
                return count
            else:
                inc_count -= increment
                count += 1

    def GenerateMass(self) -> float:
        '''
        '''
        mass_range = self.__def_dict["classes"][self.__spec_class]["mass"]
        increment = (mass_range[1] - mass_range[0]) / 10
        class_mass_value = mass_range[0] + (increment * self.__scaler)
        class_mass_range = [class_mass_value - increment / 2, class_mass_value + increment / 2]

        mass = random.uniform(class_mass_range[0], class_mass_range[1])

        if mass_range[0] >= mass:
            mass = mass_range[0]
        if mass_range[1] <= mass:
            mass = mass_range[1]

        return mass * self.s_mass

    def GenerateLuminosity(self) -> float:
        '''
        Generates luminosity based on percentage fraction and temps defined in def_file.
        Returns float.
        '''
        return 1.0

if(__name__ == "__main__"):
    print("This is a class lib file")
