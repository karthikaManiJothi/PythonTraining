# using command line arguments
import sys
from BMIvalidation import validation

name,height,weight=sys.argv[1:]
print("name:",name)
print("Height:",float(height))
print("Weight:",float(weight))

# from validation class, importing validate function
validation.validate(float(weight),float(height))
