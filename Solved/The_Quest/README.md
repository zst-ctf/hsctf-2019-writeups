# The Quest
Web

## Challenge 

You think you are worthy of obtaining the flag? Try your hand at The Quest to Obtain the Flag.

https://forms.gle/7pyAWuG3GvYL443NA

Hint: Maybe you don't have to complete the challenges...

## Solution

We have a google form where the first page is a password.

But the password is seen on the webpage's javascript area.

	$ curl https://docs.google.com/forms/d/e/1FAIpQLSfwHhSWucbXWdI7qsZRRCBGKa-yNKtl3CyNfTbmu7YiZap83Q/viewform

	<snip>

	,[347872675,"Impossible!","The previous challenge was impossible!",8]
	,[1965733913,"Impossible!","The first challenge was impossible!",8]
	]
	,["The flag is: hsctf{google_forms_regex_cant_stop_nobody}",0,0,0,0]
	,null,[null,null,null,null,null,[null,null,null,[103,58,183,null,2]
	,[209,196,233,null,1]
	,0]
	]
	,[0,0]

	<snip>


## Flag

	hsctf{google_forms_regex_cant_stop_nobody}
