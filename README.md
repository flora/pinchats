# :sparkles: :heart: PinChats :heart: :sparkles:

An app that matches humans periodically and schedules a chat session on their gCal.  
Built by pro Pinterest engineers for a hackathon, summer 2015.

## To start the app:

`python server/pinchats.py -p $PORT`  

## To create the db (in a python shell):
`from server.pinchats import init_db, db_session`  
`init_db()`  
`db_session.commit()`  
