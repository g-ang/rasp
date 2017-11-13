import pika

class Link:
    connection=""
    def __init__(self):
	    parameters=pika.URLParameters("amqp://g:gang@42.121.58.47:5673")
	    self.connection=pika.BlockingConnection(parameters)

    def callback(self,ch, method, properties, body):
	    self.send(body)
	    print body
   
    def receice(self):
		channel = self.connection.channel()
		channel.queue_declare(queue='hello')
		channel.basic_consume(self.callback,queue='hello',no_ack=True)
		channel.start_consuming()

    def send(self,body):
		channel = self.connection.channel()
		channel.exchange_decare(exchange='screen',type='fanout')
		channel.basic_publish('',
                      'screen',
                      body,
                      pika.BasicProperties(content_type='text/plain',
                                           delivery_mode=1))

if __name__ == "__main__":
    t=Link()
    t.receice()