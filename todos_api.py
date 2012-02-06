#!/usr/bin/env python


from brubeck.request_handling import Brubeck, WebMessageHandler
from brubeck.autoapi import AutoAPIBase
from brubeck.queryset import DictQueryset
from brubeck.templating import Jinja2Rendering, load_jinja2_env


from dictshield.document import Document
from dictshield.fields import (StringField,
                               IntField,
                               BooleanField)

import uuid


### Todo Model
class Todo(Document):
    done = BooleanField(default=False)
    order = IntField()
    text = StringField()

    def __init__(self, *a, **kw):
        super(Todo, self).__init__(*a, **kw)
        if not self.id:
            self.id = uuid.uuid4()  # Set a new id by default


### API Implementation
class TodosAPI(AutoAPIBase):
    queries = DictQueryset()
    model = Todo

    def render(self, **kwargs):
        return super(TodosAPI, self).render(hide_status=True, **kwargs)


### Landing Page
class TodosHandler(Jinja2Rendering):
    def get(self):
        return self.render_template('index.html')


### Instantiate app instance
app = Brubeck(
    mongrel2_pair=('ipc://brubeck_incoming', 'ipc://brubeck_outgoing'),
    handler_tuples=((r'^/$', TodosHandler),),
    template_loader=load_jinja2_env('./templates')
)

### Register API with instance
app.register_api(TodosAPI)

### Rev the engine.
app.run()
