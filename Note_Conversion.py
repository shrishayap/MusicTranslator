def convert(list,shift):
    western = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    shift=int(shift*2)
    converted = []
    for i in list:
        index = western.index(i)
        index = (index+shift)% len(western)
        converted.append(western[index])
    return converted

def translate(list,shift):
    western = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    carnatic = ["S", "S3", "R" ,"R3" ,"G" ,"M" ,"M3" ,"P" ,"P3" ,"D" ,"D3" ,"N3"]
    shifted = convert(list,shift)
    translated = []
    for i in shifted:
        index = western.index(i)
        translated.append(carnatic[index])
    return translated

def flat_to_sharp(list):
    flats = ["Db","Eb","Fb","E#", "Gb","Ab","Bb","Cb","B#"]
    sharps = ["C#", "D#", "E","F","F#", "G#", "A#","B", "C"]
    for i in list:
        if i in flats:
            index1 = list.index(i)
            index2 = flats.index(i)
            list[index1] = sharps[index2]

    return list





toConvert = ["C","D","E"]
toShift = 3
print(convert(toConvert,toShift))



toTranslate = ["C","D","E"]
toShift = 3
print(translate(toTranslate,toShift))


To_convert_to_sharp = flats = ["Db","Eb","Fb","E#", "Gb","Ab","Bb","Cb","B#"]
print(flat_to_sharp(To_convert_to_sharp))

