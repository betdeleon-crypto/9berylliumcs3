def enter_year():         #will check if the user inputted year aligns with the standard baseline of 1900
    year = int(input("Enter your birth year: "))
    if year<1900:         #is the year from the 20th century?
        print("Invalid Year, it should not be earlier than 1900.")
    else:
        return year
        
def try_zodiac(year):    #checks the zodiac sign
    zodiac = ["Rat (鼠 / Shǔ)","Ox (牛 / Niú)","Tiger (虎 / Hǔ)","Rabbit (兔 / Tù)",
              "Dragon (龙 / Lóng)","Snake (蛇 / Shé)","Horse (马 / Mǎ)","Goat (羊 / Yáng)",
              "Monkey (猴 / Hóu)","Rooster (鸡 / Jī)","Dog (狗 / Gǒu)","Pig (猪 / Zhū)"]
    r = (year-1900)%12
    '''sets baseline of birthyear as 1900
    follows the 12-year cycle of the zodiacs'''
    return zodiac[r]
    
birthyear = enter_year()        #checks if given birthyear is in the 20th century
zodiac = try_zodiac(birthyear)  #finds out what chinese zodiac is associated with the user inputted year
print(f"Your Chinese Zodiac Sign is: {zodiac}.")    #displays final results
