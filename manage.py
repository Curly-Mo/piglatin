#!/usr/bin/env python

from flask_script import Manager, Server
from flask_script.commands import ShowUrls, Clean
from piglatin_microservice import create_app

app = create_app('piglatin_microservice.settings.ProdConfig')

manager = Manager(app)
manager.add_command("server", Server())
manager.add_command("show-urls", ShowUrls())
manager.add_command("clean", Clean())


if __name__ == "__main__":
    manager.run()
