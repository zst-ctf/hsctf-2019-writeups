# Agent Keith
Web

## Challenge 

Keith was looking at some old browsers and made a site to hold his flag.

https://agent-keith.web.chal.hsctf.com

Hint: Check the source?

## Solution

See debug value on webpage

	$ curl https://agent-keith.web.chal.hsctf.com
	<!doctype html>
	<html lang="en">
	    <head>
	        <meta charset="utf-8">
	        <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
	        <title>agent-keith</title>
	        <link rel="stylesheet" href="http://localhost:8002/static/style.css">
	    </head>
	    <body>
	        <main>
	            <h2>If you're not Keith, you won't get the flag!</h2>
	            <p><b>Your agent is:</b> curl/7.54.0</p>
	            <p><b>Flag:</b> Access Denied</p>
	            <!-- DEBUG (remove me!!): NCSA_Mosaic/2.0 (Windows 3.1) -->
	        </main>
	    </body>
	</html>

Change useragent via CURL

	 $ curl https://agent-keith.web.chal.hsctf.com --user-agent "NCSA_Mosaic/2.0 (Windows 3.1)"
	<!doctype html>
	<html lang="en">
	    <head>
	        <meta charset="utf-8">
	        <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
	        <title>agent-keith</title>
	        <link rel="stylesheet" href="http://localhost:8002/static/style.css">
	    </head>
	    <body>
	        <main>
	            <h2>If you're not Keith, you won't get the flag!</h2>
	            <p><b>Your agent is:</b> NCSA_Mosaic/2.0 (Windows 3.1)</p>
	            <p><b>Flag:</b> hsctf{wow_you_are_agent_keith_now}</p>
	            <!-- DEBUG (remove me!!): NCSA_Mosaic/2.0 (Windows 3.1) -->
	        </main>
	    </body>
	</html>

## Flag

	hsctf{wow_you_are_agent_keith_now}
