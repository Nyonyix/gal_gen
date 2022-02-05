from os import truncate
from Star import Star

a = {}
for i in range(1000):
    s = Star()
    print(f"{s.GetTemperature() }, {s.GetClass()}{s.GetScaler()}, {round(s.GetMass() / s.s_mass, 3)}, {round(s.GetLuminosity() / s.s_luminosity, 3)}, {round(s.GetAge(), 3):,}\n")

    try:
        a[f"{s.GetClass()}{s.GetScaler()}"] += 1
    except(KeyError):
        a[f"{s.GetClass()}{s.GetScaler()}"] = 1

    b = dict(sorted(a.items(), key=lambda item: item[1]), reversed=True)

for k, v in b.items():
    print(f"{k}, {v}")