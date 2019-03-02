import os, datetime

class Utils():  
    @classmethod
    def draw_header(self):
        print("\n\033[1;36;40m ========== YTubeBOT ========== \033[0m\n")
    
    @classmethod
    def draw_system_end(self):
        print("\033[1;36;40m\n =========== Finish =========== \033[0m")
    
    @classmethod
    def draw_log(self, status=True, datetime='', message=''):
        # Check parameters
        if not datetime or not message:
            raise Exception ('Invalid parrameters on draw_log function...')

        # Check status message: True = OK, False = Error
        if status:
            status = 'OK'
            print("\033[1;32;40m [ {} ] \033[0m: \033[1;33;40m{} \033[0m - {}".format(status, datetime.strftime('%Y-%m-%d:%H:%M:%S'), message))
        else:
            status = 'ERROR'
            print("\033[1;31;40m [ {} ] \033[0m: \033[1;33;40m{} \033[0m - {}".format(status, datetime.strftime('%Y-%m-%d:%H:%M:%S'), message))
    
    @classmethod
    def get_current_datetime(self):
        current_datetime = datetime.datetime.now()
        return current_datetime