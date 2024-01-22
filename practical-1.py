file=open("Practical-1.txt",'w')

temp=int(input("choice to enter the temperature in respected degree:\n 1.celsius\n2.fahrenheit\n"))

if (temp  == 1):
    fahrenheit=int(input("Enter the temperature in Fahrenheit:"))
    celsius=(fahrenheit-32)*5/9
    file.write(f"celsius:{str(celsius)} C")
elif (temp == 2):
    celsius=int(input("Enter the temperature in Celsius: "))
    fahrenheit=(9/5)*celsius+32
    file.write(f"fahrenheit:{str(fahrenheit)} f")
else :
    file.write()
