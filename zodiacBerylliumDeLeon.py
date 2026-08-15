def enter_year():         #will check if the user inputed year aligns with the standard baseline of 1900
    year = int(input("Enter your birth year: "))
    if year<1900:         #is the year from the 20th century?
        print("Invalid Year, it should not be earlier than 1900.")
    else:
        return year
        
def try_zodiac(year):    #checks the zodiac sign
    r = (year-1900)%12   #sets baseline of birthyear as 1900 then
    match(r):            #matches the year to its chinese zodiac according to the 12-year cycle
        case 0:
            zodiac = "Rat (鼠 / Shǔ)"
        case 1:
            zodiac = "Ox (牛 / Niú)"
        case 2:
            zodiac = "Tiger (虎 / Hǔ)"
        case 3:
            zodiac = "Rabbit (兔 / Tù)"
        case 4:
            zodiac = "Dragon (龙 / Lóng)"
        case 5:
            zodiac = "Snake (蛇 / Shé)"
        case 6:
            zodiac = "Horse (马 / Mǎ)"
        case 7:
            zodiac = "Goat (羊 / Yáng)"
        case 8:
            zodiac = "Monkey (猴 / Hóu)"
        case 9:
            zodiac = "Rooster (鸡 / Jī)"
        case 10:
            zodiac = "Dog (狗 / Gǒu)"
        case 11:
            zodiac = "Pig (猪 / Zhū)"
    return zodiac
    
birthyear = enter_year()        #checks if given birthyear is in the 20th century
zodiac = try_zodiac(birthyear)  #finds out what chinese zodiac is associated with the user inputted year
print(f"Your Chinese Zodiac Sign is: {zodiac}.")    #displays final results
