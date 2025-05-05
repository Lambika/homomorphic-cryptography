import base64


def write_data(file_name :str,data:bytes):
    data = base64.b64encode(data)
    with open(file_name, 'wb') as file:
        file.write(data)
        
def read_data(file_name :str)->bytes:
    with open(file_name, 'rb') as file:
        data = file.read()
    data = base64.b64decode(data)
    return data       
