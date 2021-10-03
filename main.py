from Star import Star

a = {}
for i in range(100):
    s = Star()
    print(f"{s.GetTemperature()}, {s.GetClass()}{s.GetScaler()}, {s.GetMass() / s.s_mass}\n")

    try:
        a[f"{s.GetClass()}{s.GetScaler()}"] += 1
    except(KeyError):
        a[f"{s.GetClass()}{s.GetScaler()}"] = 1

for k, v in a.items():
    print(f"{k}, {v}")
