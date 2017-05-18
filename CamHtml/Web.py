import sys
import os
import serial
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options
from tornado.options import define,options
define("port",default=2333,type=int)

ser = serial.Serial('/dev/ttyAMA0',         # Device name varies
        baudrate=9600,         # Set baud rate  to 38400
        bytesize=8,
        parity='N',
        stopbits=1)
#MSP430命令
cmd = ""
class IndexHandler(tornado.web.RequestHandler):
        def get(self):
                self.render("index.html")
        def post(self):
                arg = self.get_argument('k')
                if(arg=='w'):
                        cmd = "w"
                elif(arg=='s'):
                        cmd = "s"
                elif(arg=='a'):
                        cmd = "a"
                elif(arg=='d'):
                        cmd = "d"
                else:                
                    return False
                ser.write(cmd.encode('utf-8'))
                self.write(arg)
if __name__ == '__main__':
        tornado.options.parse_command_line()
        settings = {
                "static_path": os.path.join(os.path.dirname(__file__), "static") 
                }#配置静态文件路径
        app = tornado.web.Application(handlers=[(r"/",IndexHandler)], **settings)
        http_server = tornado.httpserver.HTTPServer(app)
        http_server.listen(options.port)
        tornado.ioloop.IOLoop.instance().start()
