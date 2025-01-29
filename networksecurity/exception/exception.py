import sys
from networksecurity.logging import logger 
class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_detail:sys):
        self.error_message = error_message
        self.error_detail = error_detail
        _,_,exc_tb=self.error_detail.exc_info()
        self.file_name=exc_tb.tb_frame.f_code.co_filename
        self.lineno=exc_tb.tb_lineno
    def __str__(self):
        return f"Error occured in python script [{self.file_name}] line number [{self.lineno}] with error message of {str({self.error_message})}"
    
if __name__=='__main__':
    try:
        logger.logging.info('entered the try block')
        a=1/0
        print('this will not be printed')
    except Exception as e:
        raise NetworkSecurityException(e,sys)

