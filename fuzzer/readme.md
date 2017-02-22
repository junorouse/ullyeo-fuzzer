# ullyeo fuzzer structures

* WS (server)
	* handler
		* parser
		* module list

WS
```python
from ullyeo import handler
from settings import module_list

my_handler = handler.BasicHandler()
my_handler.set_modules(module_list)

ws = WS(port=8787)
ws.set_handler(my_handler)
ws.run()
```		

Handler
```python
def set_modules(self, module_lsit):
	self.module_list = module_list

def handle(self):
	result = parser(self.detail)
	for x in self.module_list:
		call(x, result, callback) # async true

def callback(self):
	if result == True: # hackable
		push_db()
```


#ullyeo