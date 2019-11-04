gewichtAlsString = input("geef mij gewicht (in kg): ");
lengteAlsString = input("geef mij lengte (in meter): ");

gewicht = int(gewichtAlsString);
lengte = float(lengteAlsString);

bmi =  gewicht / (lengte * lengte); 

print ('BMI = ')
print (bmi)