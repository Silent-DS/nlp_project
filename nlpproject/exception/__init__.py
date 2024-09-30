import os
import sys
#import exception produces error though not necessary as part of python


# Function to capture detailed error message
def err_msg_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name= exc_tb.tb_frame.f_code.co_filename
    error_msg = "Error occurred python script [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )

    return error_msg

#Use of concept of super class , Learn it
# Custom Exception Class
class CustomException(Exception):
    def __init__(self, error_msg,error_detail):
        super().__init__(error_msg)   # Call the base class constructor
        self.error_msg = err_msg_detail(error_msg,error_detail=error_detail)

    def __str__(self):
        return self.error_msg  
    


try:
    a = 1 / 0
except Exception as e:
    raise CustomException("Division by zero occurred", sys)    
