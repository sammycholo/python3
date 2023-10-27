import socket
class WebBrowser:
    def __init__(self):
        print("Welcome to Simple Web Browser...! | Python 3")
        self.url = None
        
    def get_host(self, url)->str:
        s = url.split("://")
        s1 = s[1].split("/")
        return s1[0]
    
    def get_page(self, url)->None:
        self.url = url
        host = self.get_host(self.url)
        cmd = "GET "+self.url+" HTTP/1.0\r\n\r\n"
        cmd = cmd.encode()
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((host,80))
        mysock.send(cmd)
        while True:
            data = mysock.recv(512)
            if len(data) < 1:
                break
            print(data.decode(),end="")
        mysock.close()

    

    
    

new = WebBrowser()
new.get_page("http://data.pr4e.org/page1.htm")
