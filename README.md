# Todos

This is a Brubeck adaption of [this well-known backbone.js demo](http://documentcloud.github.com/backbone/examples/todos/index.html).

The API implementation is generated using Brubeck's AutoAPI (undocumented as of
this writing). It generates the REST interface from a simple description of a
todo item. The interactions between Javascript and the API are handled via
[backbone.js](http://documentcloud.github.com/backbone/).

This project is currently a rough draft / example of Brubeck's AutoAPI. The
AutoAPI is liable to change in the near term but compatibility with backbone.js
will be preserved.

## Screenshots

![Empty todo list](/j2labs/todos/raw/master/media/screenshots/empty_list.png)

A fresh, empty todo list.

![Three items in the list](/j2labs/todos/raw/master/media/screenshots/three_items.png)

Three items in the list, one is accomplished.

![Empty todo list](/j2labs/todos/raw/master/media/screenshots/editing_a_todo.png)

Editing the name of one of the list items

![Empty todo list](/j2labs/todos/raw/master/media/screenshots/json_api.png)

The actual output from the AutoAPI.
