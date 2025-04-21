# import traceback #
# import sys

# class CustomException(Exception): #inherits from Exception
#     def __init__(self, error_message,error_details:sys):
#         super().__init__(error_message)
#         self.error_message = self.get_detailed_error_message(error_message, error_details)
    
#     @staticmethod
#     def get_detailed_error_message(error_message,error_details:sys):
#         _,_,exc_tb =  error_details.exc_info() #1st parameter is not required so _ neither 2nd so _ 
#         file_name = exc_tb.tb_frame.f_code.co_filename 
#         line_number = exc_tb.tb_lineno #Line number where the error occurred    
        
#         return f"Error occurred in script: [{file_name}] at line number: [{line_number}] with error message: [{error_message}]"
    
#     def __str__(self):
#         return self.error_message
    
    
import traceback
import sys

class CustomException(Exception):

    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = self.get_detailed_error_message(error_message,error_detail)

    @staticmethod
    def get_detailed_error_message(error_message , error_detail:sys):

        _, _, exc_tb = traceback.sys.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno

        return f"Error in {file_name} , line {line_number} : {error_message}"
    
    def __str__(self):
        return self.error_message
