#!/usr/bin/env python


from brubeck.request_handling import Brubeck, WebMessageHandler
from brubeck.autoapi import AutoAPIBase
from brubeck.queryset import DictQueryset
from brubeck.templating import Jinja2Rendering, load_jinja2_env
from brubeck.connections import Mongrel2Connection


from schematics.models import Model
from schematics.types import (UUIDType,
                              StringType,
                              IntType,
                              BooleanType)
from schematics.serialize import wholelist

import uuid


### Todo Model
class Todo(Model):
    id = UUIDType(auto_fill=True)
    done = BooleanType(default=False)
    order = IntType()
    text = StringType()
    class Options:
        roles = {
            'owner': wholelist(),
        }


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
    msg_conn=Mongrel2Connection('ipc://brubeck_incoming',
                                'ipc://brubeck_outgoing'),
    handler_tuples=((r'^/$', TodosHandler),),
    template_loader=load_jinja2_env('./templates')
)

### Register API with instance
app.register_api(TodosAPI)

### Rev the engine.
app.run()
