from Star import Star

for i in range(1000):
    s = Star()
    print(f"{s.GetTemperature()}, {s.GetClass()}{s.GetScaler()}, {s.GetMass() / s.s_mass}")