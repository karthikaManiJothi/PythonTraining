class BMI:
    @staticmethod
    def bmi_calculate(weight,height):
        bmi = round(weight / (height * height), 1)
        return bmi

if __name__=='__main__':
 age =int(input("Hi Argo, What is your Age?"))
 weight =float(input("What is your weight in Kg?"))
 height=float(input("What is your height in metres?"))

 b =BMI()
 print("The BMI is",b.bmi_calculate(weight,height))