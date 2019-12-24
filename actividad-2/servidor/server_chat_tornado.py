from __future__ import print_function
import os

import sys

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket
from tornado.options import options, define

import pika
from pika.adapters.tornado_connection import TornadoConnection


# Define available options
define("port", default=8888, type=int, help="run on the given port")
define("cookie_secret", help="random cookie secret")
define("queue_host", default="127.0.0.1", help="Host for amqp daemon")
define("queue_user", default="guest", help="User for amqp daemon")
define("queue_password", default="guest", help="Password for amqp daemon")

PORT = 8888

global channels

channels = sys.argv[1:]
if not channels:
    print ("No channels to listen")
    sys.exit(1)

class PikaClient(object):

    def __init__(self):

        # Construct a queue name we'll use for this instance only

        #Giving unique queue for each consumer under a channel.
        self.queue_name = "queue-%s" % (id(self),)
        # Default values
        self.connected = False
        self.connecting = False
        self.connection = None
        self.channel = None
        self._url = "amqp://guest:guest@172.20.0.10:5672/"

        #Webscoket object.
        self.websocket = None

    def connect(self):

        if self.connecting:
                print('PikaClient: Already connecting to RabbitMQ')
                return

        print('PikaClient: Connecting to RabbitMQ on 172.20.0.10:5672, Object: %s' % (self,))

        self.connecting = True

        self.connection = TornadoConnection(pika.URLParameters(self._url),
                                            self.on_connected)

    def add_on_connection_close_callback(self):
        self.connection.add_on_close_callback(self.on_connection_closed)

    def open_channel(self):
        self.connection.channel(on_open_callback=self.on_channel_open)

    def on_connected(self, unused_connection):
        #:param pika.SelectConnection _unused_connection: The connection
        print('PikaClient: Connected to RabbitMQ on 172.20.0.10:5672')
        
        self.add_on_connection_close_callback()
        self.open_channel()

        self.connected = True

    def on_channel_open(self, channel):
        print('PikaClient: Channel Open, Declaring Exchange, Channel ID: %s' %
              (channel,))
        self.channel = channel

        exchange = 'tornado'
        self.channel.exchange_declare(exchange=exchange,
                                      exchange_type="direct",
                                      auto_delete=True,
                                      durable=False,
                                      callback=self.on_exchange_declared)

    def on_exchange_declared(self, frame):
        print('PikaClient: Exchange Declared, Declaring Queue')
        self.channel.queue_declare(auto_delete=True,
                                   queue=self.queue_name,
                                   durable=False,
                                   exclusive=True,
                                   callback=self.on_queue_declared)

    def on_queue_declared(self, frame):

        print('PikaClient: Queue Declared, Binding Queue')
        channels = sys.argv[1:]
        channels+=["tornado.*"]
        for c_id in channels:
            self.channel.queue_bind(exchange='tornado',
                                    queue=self.queue_name,
                                    routing_key=c_id,
                                    callback=self.on_queue_bound)

    def on_queue_bound(self, frame):
        print('PikaClient: Queue Bound, Issuing Basic Consume')
        self.channel.basic_consume(on_message_callback=self.on_pika_message,
                                   queue=self.queue_name)

    def on_pika_message(self, channel, basic_deliver, properties, body):
        print('PikaCient: Received message from %s: %s' %  (basic_deliver.consumer_tag,body))


        #Send the Cosumed message via Websocket to browser.
        self.websocket.write_message(body)

    def on_basic_cancel(self, frame):
        print('PikaClient: Basic Cancel Ok')
        # If we don't have any more consumer processes running close
        self.connection.close()

    def on_connection_closed(self, connection, reason):
        # We've closed our pika connection so stop the demo
        tornado.ioloop.IOLoop.instance().stop()

    def sample_message(self, ws_msg):
        #Publish the message from Websocket to RabbitMQ
        pass_e,r_key,msg = self.parse_message(ws_msg)
        if pass_e:
            properties = pika.BasicProperties(
                content_type="text/plain", delivery_mode=1)

            self.channel.basic_publish(exchange='tornado',
                                    routing_key=r_key,
                                    body=msg,
                                    properties=properties)
        else:
            self.websocket.write_message(msg)
        
    def parse_message(self, msg):
        if msg[0]=="*": #mensaje un canal
            try:
                channel_id,_msg = msg.split(":")
                channel_id=channel_id[1:]
                return (True,channel_id,_msg)
            except:
                
                return (False,'tornado.*','Error: Usa la sintaxis {*canal:mensaje}')
        else:
            return (True,'tornado.*',msg)



class LiveChat(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):

        # Send our main document
        self.render("demo_chat.html",
                    connected=self.application.pika.connected)


class WebSocketServer(tornado.websocket.WebSocketHandler):
    'WebSocket Handler, Which handle new websocket connection.'

    def open(self):
        'Websocket Connection opened.'

        #Initialize new pika client object for this websocket.
        self.pika_client = PikaClient()

        #Assign websocket object to a Pika client object attribute.
        self.pika_client.websocket = self

        ioloop.add_timeout(1000, self.pika_client.connect)

    def on_message(self, msg):
        'A message on the Webscoket.'
        
        #Publish the received message on the RabbitMQ
        self.pika_client.sample_message(msg)

    def on_close(self):
        'Closing the websocket..'
        print("WebSocket Closed")

        #close the RabbiMQ connection...
        self.pika_client.connection.close()


class TornadoWebServer(tornado.web.Application):
    ' Tornado Webserver Application...'
    def __init__(self):

        #Url to its handler mapping.
        handlers = [(r"/ws_channel", WebSocketServer),
                    (r"/", LiveChat)]

        #Other Basic Settings..
        settings = dict(
            cookie_secret=options.cookie_secret,
            login_url="/signin",
            template_path=os.path.join(os.path.dirname(__file__),
                                       "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
            debug=True)

        #Initialize Base class also.
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':

    #Tornado Application
    print("Initializing Tornado Webapplications settings...")
    application = TornadoWebServer()

    # Helper class PikaClient makes coding async Pika apps in tornado easy
    pc = PikaClient()
    application.pika = pc  # We want a shortcut for below for easier typing

    # Start the HTTP Server
    print("Starting Tornado HTTPServer on port %i" % PORT)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(PORT)

    # Get a handle to the instance of IOLoop
    ioloop = tornado.ioloop.IOLoop.instance()

    # Add our Pika connect to the IOLoop since we loop on ioloop.start
    #ioloop.add_timeout(1000, application.pika.connect)

    # Start the IOLoop
    ioloop.start()
