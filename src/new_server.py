from gevent.wsgi import WSGIServer 
import requests
import falcon
import math
#import similarity
import gevent
import signal
import json
import time as time_
import wikipedia
import releavent
import timeline
class process(object):
#print  wikipedia.page("google")
	def on_post(self, req, resp):
		data = json.load(req.bounded_stream)
		if data:
			word = data["word"]
			num = int(data['n'])
			similarity_dict={}
			
			#print releavent.releavent_search(word)
			#print timeline.timeline(num)
			similarity_dict['releavant page']=str(releavent.releavent_search(word))
			similarity_dict['releavant Timelines']=list(timeline.timeline(num))
			resp.set_header('Content-Type','text/plain')
			resp.status = falcon.HTTP_200
			resp.body= json.dumps(similarity_dict, ensure_ascii=False)
		  
def main():
    api = app = falcon.API()
    startProceesPosts = process();	
    app.add_route( "/way2push/api/v1.1/process",startProceesPosts)
    try:
        http_server = WSGIServer(('', 5252), app)
        def stop_nicely():
            print 'handling signal'
            if http_server.started:
                http_server.close()
        gevent.signal(signal.SIGTERM, stop_nicely)

        print 'starting server'
        http_server.serve_forever()
        print 'done with server'
        gevent.wait(G)

    except (KeyboardInterrupt, SystemExit):
        print 'Shutting down on interrupt.'

        if http_server.started:
            http_server.stop()
    finally:
        print 'Shutting down.'    
if __name__ == '__main__':
    main()
