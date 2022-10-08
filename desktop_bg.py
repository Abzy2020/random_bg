import ctypes
import requests

class BgManager:
    def __init__(self):
        self.path = r'C:\Users\zcool\Desktop\bgs'

    
    def make_request(self):
        res = requests.get('https://picsum.photos/2000/1000')
        with open(fr'{self.path}\randomimg.jpg', 'wb') as file:
            file.write(res.content)
            file.close()
        print(res.url)


    def set_desktop_bg(self):
        path = fr'{self.path}\randomimg.jpg'
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)


    def get_path(self):
        return self.path


manager = BgManager()
manager.make_request()