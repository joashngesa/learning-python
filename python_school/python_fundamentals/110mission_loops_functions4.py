#remove invalid values (-999)
#convert each valid temperature from Celsius to Fahrenheit
#calculate average temperature manually
#return temperatures above 80°F
#wrap everything in one function

#remove invalid values (-999)
temperatures = [23, -999, 18, 31, -999, 27, 40]

def invalids_removal(temperatures):
    
    validation = [val for val in temperatures if val != -999]
    return validation

#convert each valid temperature from Celsius to Fahrenheit
#   C = (C * 1.8) + 32)
def fahrenheit_conversion(validation):
    fahrenheit = [round((far * 1.8 + 32),2) for far in validation]
    return fahrenheit

def average_temp(fahrenheit):

    if len(fahrenheit) == 0:
        return None
    total_temp = 0
    for avr in fahrenheit:
        total_temp += avr

    average_tmp = total_temp / len(fahrenheit)
    return average_tmp

#return temperatures above 80°F
def above_80F(fahrenheit):
    
    above_80 = [abv for abv in fahrenheit if abv > 80] 
    return above_80

validated = invalids_removal(temperatures)
fahrenheit_temp = fahrenheit_conversion(validated)
temp_average = average_temp(fahrenheit_temp)
temps_above_80F = above_80F(fahrenheit_temp)

print("validated temperature: ",validated)
print("temperatures in fahrenheit: ",fahrenheit_temp)
print("Average temperature: ",temp_average)
print("Temperatures above 80F: ",temps_above_80F)


###All in one function
#remove invalid values (-999)
#convert each valid temperature from Celsius to Fahrenheit
#calculate average temperature manually
#return temperatures above 80°F
#wrap everything in one function

def temperatures_pipeline(temperatures):

    cleaning = [cln for cln in temperatures if cln != -999]

    conversion_to_F = [round((con * 1.8 + 32),2) for con in cleaning]

    if len(conversion_to_F) == 0:
        return None
    total_t = 0
    for tot in conversion_to_F:
        total_t += tot
    temp_avg = total_t / len(conversion_to_F)

    temps_above80F = [temps for temps in conversion_to_F if temps > 80]

    return cleaning, conversion_to_F, temp_avg, temps_above_80F


cleaning, conversion_to_F, temp_avg, temps_above80F = temperatures_pipeline(temperatures)

print("Cleaned temperatures: ",cleaning)
print("Converted to F temperatures: ",conversion_to_F)
print("Temperature average: ",temp_avg)
print("Temperatures above 80F: ",temps_above80F)
   
    
#####different case scenario
#removes invalid values -9999
#increases each valid profit by 10%
#calculates total profit manually
#returns profits above 400
#wraps everything in one function

profits = [500, -9999, 200, 0, 350, -9999, 1000]
def profits_pipeline(profits):
    
    cleaned_pft = [gain for gain in profits if gain != -9999]

    gain_inc_pcnt = 0.1
    increased_pft = [round(gain + (gain * gain_inc_pcnt)) for gain in cleaned_pft ]

    gains_tot = 0
    for gain in increased_pft:
        gains_tot += gain

    pft_above_400 = [gain for gain in increased_pft if gain > 400]

    return cleaned_pft, increased_pft, gains_tot, pft_above_400

cleaned_pft, increased_pft, gains_tot, pft_above_400 = profits_pipeline(profits)

print("Cleaned profits: ",cleaned_pft)
print("Increased profits: ",increased_pft)
print("Total profit: ",gains_tot)
print("Profits above 400: ",pft_above_400)

    
