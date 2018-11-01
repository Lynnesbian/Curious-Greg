#!/usr/bin/env python3
#Curious Greg - Curious Cat to Mastodon crossposter
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import requests, sqlite3, json, argparse
from mastodon import Mastodon

db = sqlite3.connect("database.db")
c = db.cursor()

c.execute("CREATE TABLE IF NOT EXISTS `data` (username VARCHAR NOT NULL, secret VARCHAR NOT NULL, latest_post VARCHAR)")



