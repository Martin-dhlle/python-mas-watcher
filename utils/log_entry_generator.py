from datetime import date, time, datetime
from config.log_messages import LOG_MESSAGES

class Style():
  RED = "\033[31m"
  GREEN = "\033[32m"
  STOP = "\033[0m"

def generate_log(log_type: int, message_index: int, arg: str):
    '''
    log_type: 0 (basic, default color) ou 1 (error, red color)
    '''
    message = LOG_MESSAGES[message_index][1].replace("{arg}", arg)
    print(f"{Style.RED if log_type == 1 else ''}{date.today()} | {datetime.now().strftime('%H:%M:%S')} : {message}{Style.STOP}")