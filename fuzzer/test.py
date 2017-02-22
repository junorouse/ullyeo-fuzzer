from ullyeo.handler import BaseHandler

x = BaseHandler(server='', sock='', address='')

x.data = '{"Type":"SendHeaders","Details":{"frameId":0,"method":"GET","parentFrameId":-1,"requestId":"20705","tabId":234,"timeStamp":1487750756749.038,"type":"main_frame","url":"http://docs.sqlalchemy.org/en/latest/orm/tutorial.html"},"TabInfo":{"active":true,"audible":false,"autoDiscardable":true,"discarded":false,"favIconUrl":"http://www.sqlalchemy.org/favicon.ico","height":905,"highlighted":true,"id":234,"incognito":false,"index":0,"mutedInfo":{"muted":false},"pinned":false,"selected":true,"status":"loading","title":"docs.sqlalchemy.org/en/latest/orm/tutorial.html","url":"http://docs.sqlalchemy.org/en/latest/orm/tutorial.html","width":1680,"windowId":1}}'
x.handleMessage()
