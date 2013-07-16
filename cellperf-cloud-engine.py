import webapp2
import json
import logging
import os
import datetime

import wsgiref.handlers
from google.appengine.ext import ndb


class DataCheckException(Exception): pass

class DBEntry(ndb.Model):
    name = ndb.StringProperty(required=True)
    hire_date = ndb.DateProperty()
    new_hire_training_completed = ndb.BooleanProperty(indexed=False)


class DBEntryFoo:

    def generate(self, name):
        e = DBEntry()
        e.name = name
        e.hire_date = datetime.datetime.now().date()
        return e


class MainPage(webapp2.RequestHandler):


    def handle_client_error(self, error):
        logging.error(error)
        self.error(500)



    def marshall_json(self, data):
        return json.loads(data)


    def check_data(self, data):
        return True
        raise DataCheckException("array must contain excatly 2 members")


    def process_request(self, req):
        try:
            data = self.marshall_json(req.body)
            self.check_data(data)
        except ValueError as err:
            self.handle_client_error(err)
            return

        logging.error(data)

        obj = {
                'success': 'data stored correctly', 
        } 

        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(obj))


    def get(self):
        req = self.request
        self.process_request(req)


    def post(self):
        req = self.request
        self.process_request(req)


app = webapp2.WSGIApplication([ ('/', MainPage), ], debug=True)
