gewichtAlsString = ''; 
lengteAlsString = ''; 

gewicht = 0; 
lengte = 0.0; 

while len(gewichtAlsString) <= 0 or gewicht <= 0:
   gewichtAlsString = input("geef mij gewicht (in kg): ");
   if gewichtAlsString.isdigit():
       gewicht = int(gewichtAlsString);  
   
while len(lengteAlsString) <= 0 or lengte <= 0:
   lengteAlsString = input("geef mij lengte (in meter): ");
   lengte = float(lengteAlsString);

bmi =  gewicht / (lengte * lengte); 

print ('BMI = ', round(bmi, 2));
