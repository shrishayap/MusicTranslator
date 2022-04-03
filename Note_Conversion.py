def convert(list,shift):
    western = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
    shift=int(shift*2)
    converted = []
    for i in list:
        index = western.index(i)
        index = (index+shift)% len(western)
        converted.append(western[index])
    return converted


toConvert = ["A","B","C"]
toShift = 2.5
print(convert(toConvert,toShift))



