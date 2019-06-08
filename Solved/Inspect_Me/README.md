# Inspect Me
Web

## Challenge 

Keith's little brother messed up some things...

https://inspect-me.web.chal.hsctf.com

Note: There are 3 parts to the flag!

## Solution

Part 1

	$ curl https://inspect-me.web.chal.hsctf.com/
	<!doctype html>
	<html lang="en">
	    <head>
	        <meta charset="utf-8">
	        <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
	        <title>inspect-me</title>
	        <link rel="stylesheet" href="style.css">
	    </head>
	    <body>
	        <main>
	            <p>Keith was working on his CTF problem, but his little brother accidently moved the flag around. Can you help Keith find the flag?</p>
	            <!-- The first part of the flag is: hsctf{that_was_ -->
	        </main>
	        <script src="script.js"></script>
	    </body>
	</html>

Part 2

	$ curl https://inspect-me.web.chal.hsctf.com/style.css
	body {
	    font-family: Arial, Helvetica, sans-serif;
	    background-color: #000;
	}

	main {
	    max-width: 70ch;
	    padding: 2ch;
	    margin: auto;
	}

	/* The second part of the flag is: pretty_easy_ */

Part 3
	
	$ curl https://inspect-me.web.chal.hsctf.com/script.js
	document.addEventListener('contextmenu', function(e) {
	    e.preventDefault();
	});

	// The last part of the flag is: right}

## Flag

	hsctf{that_was_pretty_easy_right}
