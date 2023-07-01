import base64
import os

def file_to_base64(file_path):
    """ Reads file and converts its contetr to base64 string
    """
    with open(file_path, "rb") as file:
        file_contents = file.read()
        base64_contents = base64.b64encode(file_contents).decode("utf-8")
        return base64_contents
    

def base64_bytes_to_bytes(raw_data):
    """ Converts encoded result data to bytearray
    """
    return bytearray(base64.b64decode(str(raw_data)))


def create_results_dir():    
    """ Creates results dir
    """
    dir_path = 'results'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)