# coding=utf-8
import webapp2
from google.appengine.api.search import search

class PageHandler(webapp2.RequestHandler):
  def get(self):
    messages = []
    
    index = search.Index(name = 'DeleteMe')
    language = None
    fields = [
      search.AtomField(name = 'tag', value = 'zamówienia', language = language),
    ]
    document = search.Document(doc_id = 'deleteMe1', fields = fields, language = language)
    index.put(document)
    document = search.Document(doc_id = 'deleteMe2', fields = fields, language = language)
    index.put(document)
    
    queryString = ''
    queryOptions = search.QueryOptions(cursor = search.Cursor(), limit = 1)
    searchQuery = search.Query(queryString, options = queryOptions)
    results = index.search(searchQuery)
    messages.append(u'query = %s, hits = %s'
                    % (queryString, results.number_found))
    messages.append(dir(results))
    messages.append(results.results)
    messages.append(results.cursor)

    queryString = ''
    queryOptions = search.QueryOptions(cursor = search.Cursor(), limit = 3)
    searchQuery = search.Query(queryString, options = queryOptions)
    results = index.search(searchQuery)
    messages.append(u'query = %s, hits = %s'
                    % (queryString, results.number_found))
    messages.append(dir(results))
    messages.append(results.results)
    messages.append(results.cursor)

    self.response.out.write(u'<pre>')    
    self.response.out.write(u'\n'.join(unicode(x) for x in messages))
    self.response.out.write(u'</pre')


APP = webapp2.WSGIApplication([
    ('/.*', PageHandler),
], debug=True)
