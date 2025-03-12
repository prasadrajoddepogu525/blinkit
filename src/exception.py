import sys  #sys gives access to system specific parameters and functions including error handling

def detailed_error_mesage(error,error_details:sys): ##error--> error object, error_details-->accepts the sys module to retrive exception
    #_ is a placeholder where we don't required values
    #exc_tb stores where the error occured it will captures the traceback object
    _,_,exc_tb=error_details.exc_info()  #ysy.exc_info---->returns a tuple with (exceptiontype,exception value,traceback)
    
    #getting the file name where it occured
    filen_name=exc_tb.tb_frame.f_code.co_filename
    #exc_tb.tb_frame gets the frame where error occured
    #f_code.co_filename retrives the name of the python script where issue occured

    #formatting the error message
    error_message="Error occured in python script [{0}] line number [{2}] error_message [{3}]".format(filen_name,exc_tb.tb_lineno,str(error))

    return error_message

##creating custom class exception

class CustomClassException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=detailed_error_mesage(error_message,error_details=error_detail)

    def __str__(self):
        return self.error_message
