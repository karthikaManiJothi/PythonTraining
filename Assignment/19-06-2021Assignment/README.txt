
1) Write a python script to ask Argo his age, height, weight and calculate his BMI
      The Body Mass Index (BMI) or Quetelet index is a value derived from the mass (weight) and height of an individual, male or female. 
      The BMI is defined as the body mass divided by the square of the body height and is universally expressed in units of kg/m2,
       resulting from the mass in kilograms and height in meters. The formula is:
                           BMI = round(weight/ (height * height), 1)where,mass or weight is in Kg,height is in meters  

Expected Output:

Hi Argo, What is your Age?
27
What is your Weight in Kg?
65
What is your Height in metres?
1.79
The BMI is 20.2 -> #Return statement

---------------------------------------------------------------------------------

2)
Using the above BMI Script. Ask the User his name and then use  their name to ask their weight and height.
Based on Output of BMI Index, tell the user if they are underweight, healthy, overweight, or Obese
BMI Weight status
Below 18.5 underweight
18.5-24.9 normal
25.0-29.9 overweight
30.0 + obese

Expected Output 1:

What is your Name:
Argo
Hi Argo, What is your Height in metres?
1.79
What is your weight:
65
Your BMI is 20.2 which means you are healthy. -> #Return statement



Expected Output 2:

What is your Name:
Rahul
Hi Rahul, What is your height:
1.70
What is your weight:
88
Your BMI is 30.5 which means you are obese. -> #Return statement

-----------------------------------------------------------------------------------------------------------------------------
3)
Create these 3 lists:
numbers = [1,2,3,4,5]
Weekdays = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]
Num = [222,100,85,500,300]

Print numbers in list numbers one below the others using a for loop
Print numbers in list numbers one below the others using a while loop
Print the days of the week from list Weekdays using For loop
Print the days of the week from list Weekdays using the While loop
Calculate the sum of all numbers in the list Num using for loop
Calculate the sum of all numbers in the list Num using while loop

Expected Output:
1
2
3
4
5

1
2
3
4
5

Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday

Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday

The sum from for loop:1207
The sum from while loop:1207
--------------------------------------------------------------------------------------

4) Modify the same BMI script which you wrote in 2nd question
Replace Input type of name, weight and Height from user input to command Input  (coomand line arguments)

Expected Output 1:

python bmi.py Argo 1.79 65
Name: Argo
Height: 1.79
Weight 65
Your BMI is 20.2 which means you are healthy.


Expected Output 2:

python bmi.py Rahul 1.7 88
Name: Rahul
Height: 1.7
Weight 88
Your BMI is 30.5 which means you are obese
-------------------------------------------------------------------------------------------------------
5)The first line of input contains an integer , the number of mobile phone numbers.
 lines follow each containing a mobile number.
  Output Format
      Print  mobile numbers on separate lines in the required format.

	Sample Input
		3
		07895462130
		919875641230
		9195969878
	Sample Output

		+91 78954 62130
		+91 91959 69878
		+91 98756 41230

To solve the above question, make a list of the mobile numbers and pass it to a function that sorts the array in ascending order.
 Make a decorator that standardizes the mobile numbers and apply it to the function.

