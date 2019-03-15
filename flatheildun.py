# Bjarki Þór Jónsson
import re

fall = str(input("Sláðu inn fall "))
efri = str(input("Sláðu inn efri mörk "))
nedri = str(input("Sláðu inn neðri mörk "))
merki = []
if fall[0] != "-":
    fall = "+" + fall
fall_listi = re.split("[+-]", fall)
fall_listi.remove("")

for x in fall:
    if x == "+" or x == "-":
        merki.append(x)


def heilda(listi):
    h_listi = []
    strengur = ""
    for x in listi:
        if "x" in x:
            i = ""
            ind = x.index("x")
            if ind == 0 and len(x) > 1:
                i = i + str(1 / (int(x[ind + 1:]) + 1)) + "*(x)**" + str(int(x[ind + 1:]) + 1)
                h_listi.append(i)
            elif ind == 0 and len(x) == 1:
                h_listi.append("0.5*(x)**2")
            elif len(x) > 2:
                i = i + str(int(x[:ind]) / (int(x[ind + 1:]) + 1)) + "*(x)**" + str(int(x[ind + 1:]) + 1)
                h_listi.append(i)
            else:
                i = i + str(int(x[:ind]) / 2) + "*(x)**" + "2"
                h_listi.append(i)
        else:
            h_listi.append(x + "*(x)")
    for x in range(len(h_listi)):
        strengur = strengur + merki[x] + h_listi[x]
    return (strengur)


nytt_fall = heilda(fall_listi)
fall_a = nytt_fall.replace("x",nedri)
fall_b = nytt_fall.replace("x",efri)
print("Flatarmál",abs(eval(fall_b)-eval(fall_a)))
