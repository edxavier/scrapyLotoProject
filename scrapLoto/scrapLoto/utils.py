
import logging

time_dic = {'11:00 AM': 0, '3:00 PM': 1, '9:00 PM': 2, '6:00 PM': 3}
month_dic = {'ENE': 1, 'FEB': 2, 'MAR': 3, 'ABRIL': 4, 'MAYO': 5, 'JUN': 6,
             'JUL': 7, 'AGO': 8, 'SEPT': 9, 'OCT': 10, 'NOV': 11, 'DIC': 12}

BASE_URL = 'http://127.0.0.1:8080'

def get_logger():
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                 datefmt='%d-%b-%y %H:%M:%S')
    handler = logging.FileHandler('scrap.log')
    handler.formatter = f_format
    logging.basicConfig(filemode='w', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
    logger = logging.getLogger("loto_logger")
    logger.addHandler(handler)
    return logger


def abort_request(request):
    """Case when to abort requests"""
    if request.resource_type == 'image':
        return True
    if request.resource_type == 'stylesheet':
        return True
    if request.resource_type == 'font':
        return True
    if request.resource_type == 'websocket':
        return True
    if request.resource_type == 'xhr':
        return True
    if 'google' in request.url:
        return True
    if 'facebook' in request.url:
        return True
    if 'fonts' in request.url:
        return True     
    if 'banner' in request.url:
        return True 
    if 'analytics' in request.url:
        return True 
    if 'theme' in request.url:
        return True
    if 'plugin' in request.url:
        return True
    return False
    
