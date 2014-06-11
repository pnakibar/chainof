class Handler:
	sucessor = None

	def setSucessor(self, suc):
		self.sucessor = suc

	def setLastSucessor(self, suc):
		if (self.sucessor == None):
			self.setSucessor(suc)
		else:
			self.sucessor.setLastSucessor(suc)

	def handleRequest(self, request): pass



class ConcreteHandler1(Handler):
	def handleRequest(self, request):
		if (request >= 0 and request < 10):
			print("{0} handled request: {1}".format(__class__.__name__, request))
		if (self.sucessor != None):
			self.sucessor.handleRequest(request)

class ConcreteHandler2(Handler):
	def handleRequest(self, request):
		if (request >= 10 and request < 20):
			print("{0} handled request: {1}".format(__class__.__name__, request))
		if (self.sucessor != None):
			self.sucessor.handleRequest(request)

class ConcreteHandler3(Handler):
	def handleRequest(self, request):
		if (request >= 20 and request < 30):
			print("{0} handled request: {1}".format(__class__.__name__, request))
		if (self.sucessor != None):
			self.sucessor.handleRequest(request)
			


'''Programa principal'''

a = ConcreteHandler1()
b = ConcreteHandler2()
c = ConcreteHandler3()


a.setLastSucessor(b)
a.setLastSucessor(c)


requests = list(range(0, 40))

for e in requests:
	a.handleRequest(e)



