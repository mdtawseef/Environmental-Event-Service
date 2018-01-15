import sys

from app import app
from flask_script import Manager, Server
# from flask_debugtoolbar import DebugToolbarExtension

if __name__ == '__main__':
    # toolbar = DebugToolbarExtension(app)
    app.run(host='0.0.0.0', port=8888)
    server = Server(host='0.0.0.0', port=8888)
    manager = Manager(app)
    manager.add_command("runserver", server)
    manager.run()

    