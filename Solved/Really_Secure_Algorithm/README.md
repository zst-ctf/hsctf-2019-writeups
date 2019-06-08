# Really Secure Algorithm
Cryptography

## Challenge 

I heard about RSA, so I took a go at implementing it.

The numbers are decently large...

## Solution

Factor using YAFU

	$ ./yafu-prime-sieve/yafu
	>> factor(263267198123727104271550205341958556303174876064032565857792727663848160746900434003334094378461840454433227578735680279553650400052510227283214433685655389241738968354222022240447121539162931116186488081274412377377863765060659624492965287622808692749117314129201849562443565726131685574812838404826685772784018356022327187718875291322282817197153362298286311745185044256353269081114504160345675620425507611498834298188117790948858958927324322729589237022927318641658527526339949064156992164883005731437748282518738478979873117409239854040895815331355928887403604759009882738848259473325879750260720986636810762489517585226347851473734040531823667025962249586099400648241100437388872231055432689235806576775408121773865595903729724074502829922897576209606754695074134609)

	***factors found***

	P386 = 16225510719965861964299051658340559066224635411075742500953901749924501886090804067406052688894869028683583501052917637552385089084807531319036985272636554557876754514524927502408114799014949174520357440885167280739363628642463479075654764698947461583766215118582826142179234382923872619079721726020446020581078274482268162477580369246821166693123724514271177264591824616458410293414647
	P386 = 16225510719965861964299051658340559066224635411075742500953901749924501886090804067406052688894869028683583501052917637552385089084807531319036985272636554557876754514524927502408114799014949174520357440885167280739363628642463479075654764698947461583766215118582826142179234382923872619079721726020446020581078274482268162477580369246821166693123724514271177264591824616458410293414647

The 2 factors are equal, meaning n = p^2.

- https://crypto.stackexchange.com/questions/26861/why-should-the-primes-used-in-rsa-be-distinct

Now we can decrypt the as per normal, but we need to take note that phi = p(p-1) for equal primes

- https://crypto.stackexchange.com/a/26864
- https://crypto.stackexchange.com/a/53127

## Flag

	hsctf{square_number_time}