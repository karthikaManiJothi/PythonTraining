from BMIcal import BMI

class validation:
    @staticmethod
    def validate(weight,height):

        # by using bmical module
        bmi_value = BMI.bmi_calculate(weight, height)

        if bmi_value < 18.5:
            print("your BMI is",bmi_value,"which means you are underweight person")
        elif bmi_value >= 18.5 and bmi_value <= 24.9:
            print("your BMI is", bmi_value, "which means you are healthy")
        elif bmi_value > 25.0 and bmi_value <= 29.9:
            print("your BMI is", bmi_value, "which means you are overweight person")
        elif bmi_value>=30.0:
            print("your BMI is", bmi_value, "which means you are obese")

if __name__ =='__main__':
 name =input("What is your Name:")
 string="Hi "+name+", What is your height in metres?"
 height =float(input(str(string)))
 weight =float(input("What is your weight:"))
 val =validation()
 val.validate(weight,height)

