def convert(list,shift):
    western = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
    shift=int(shift*2)
    converted = []
    for i in list:
        index = western.index(i)
        index = (index+shift)% len(western)
        converted.append(western[index])
    return converted

def translate(list,shift):
    western = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    carnatic = ["N", "N2", "N3" ,"S" ,"R" ,"G" ,"G2" ,"G3" ,"M" ,"M2" ,"P" ,"D"]
    shifted = convert(list,shift)
    translated = []
    for i in shifted:
        index = western.index(i)
        translated.append(carnatic[index])
    return translated



toConvert = ["A","B","C"]
toShift = 2.5
print(convert(toConvert,toShift))



toTranslate = ["C","D","E"]
toShift = 4
print(translate(toTranslate,toShift))





