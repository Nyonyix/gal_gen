from Star import Star

a = {}
for i in range(100000):
    s = Star()
    #print(f"{s.GetTemperature()}, {s.GetClass()}{s.GetScaler()}, {s.GetMass() / s.s_mass}, {s.GetLuminosity() / s.s_luminosity}\n")

    try:
        a[f"{s.GetClass()}{s.GetScaler()}"] += 1
    except(KeyError):
        a[f"{s.GetClass()}{s.GetScaler()}"] = 1

    b = dict(sorted(a.items(), key=lambda item: item[1]))

for k, v in b.items():
    print(f"{k}, {v}")
