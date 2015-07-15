#!/usr/bin/env python

from server import pinchats
from subprocess import Popen

# create sqlite database
p = Popen(["sqlite3", "pinchats.db"])
p.terminate()

# create tables for Models
pinchats.init_db()
pinchats.Base.metadata.create_all(bind=pinchats.engine)
