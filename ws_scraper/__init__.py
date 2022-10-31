#! /usr/bin/env nix-shell
#! nix-shell -i python

import asyncio
import logging
import sys
import websockets
import aiosqlite
import json
from os.path import isfile as path_exists
from time import time

logging.basicConfig(level = logging.INFO)

def python_dict_diff(a, b):
    sa, sb = set(a.items()), set(b.items())
    return dict(sa - sb)



async def init_db(db_path):
    if not path_exists(db_path):
        logging.info("Database not found at {db_path}, creating a new one")
    async with aiosqlite.connect(db_path) as db:
        await db.execute('''
                  CREATE TABLE IF NOT EXISTS data (
                      id INTEGER PRIMARY KEY,
                      date INTEGER,
                      json_diff TEXT
                  )
        ''')



async def listen(url, db_path):
    await init_db(db_path)
    currentState  = None
    async for ws in websockets.connect(url):
        try: 
            async for msg in ws:
                newState = json.loads(msg)
                if currentState is None:
                    diff = newState
                else:
                    diff = python_dict_diff(newState, currentState)
                currentState = newState
                if diff != {}:
                    async with aiosqlite.connect(db_path) as db:
                        await db.execute('INSERT INTO data (date, json_diff) VALUES ( ? , ? )', (int(time()), json.dumps(diff)))
                        logging.info(f"Inserted data into db. diff={diff}")
        except websockets.ConnectionClosed as e:
            logging.info(f"Exception caught: {e}")
        logging.info("Connection ended, retrying")
    logging.info("End of script")

def main():
    asyncio.run(listen(sys.argv[1], sys.argv[2]))

if __name__ == "__main__" :
    main()
