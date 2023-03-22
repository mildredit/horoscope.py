import requests

def get_horoscope(zodiac_sign):
  # response = requests.post('https://aztro.sameerkumar.website/')
   
    url = f'https://aztro.sameerkumar.website/'
    response = requests.post(url)
    # if response.status_code == 200:
    #     horoscope = response.json()['description']
    #     return horoscope
    # else:
    #     return 'Error getting horoscope.'

def get_zodiac_sign():

    zodiac_sign = input("Enter your zodiac sign: ")
    return zodiac_sign

# day = input("Enter the horoscope day (today, tomorrow, or yesterday): ")
# params = (("day", day))
def main():
    zodiac_sign = get_zodiac_sign()
    horoscope = get_horoscope(zodiac_sign)
    print(horoscope)

if __name__ == "__main__":
    main()



# import requests

# # Get parameters from user

# # Get their sign (Aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius, pisces)
# zodiac_sign():
#   sign =input("Enter your zodiac sign: ")

# def get_day():
#   day = input("Enter the horoscope day (today, tomorrow, or yesterday): ")
#   return day

# #parameters for the HTTP request (Aztro)
# params = (("sign", get_sign), ("day", get_day))

# response = requests.post('https://aztro.sameerkumar.website/', params=params)

# # print(response.json())

# '''
# {'date_range': 'Jan 20 - Feb 18', 'current_date': 'March 22, 2023', 'description': "Need to figure out an exit strategy? Why not run it by one of your closest pals? Not only do they know you inside and out, but they'll be able to bring their own unique point of view to help you cover any patchy spots.", 'compatibility': 'Virgo', 
# 'mood': 'Friendly', 
# 'color': 'Pink', 
# 'lucky_number': '61', 
# 'lucky_time': '12pm'}
# ''' 

