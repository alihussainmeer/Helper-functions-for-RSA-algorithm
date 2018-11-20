# Helper-functions-for-RSA-algorithm
In order to apply RSA algorithm we have to evaluate various metrics which can consume a lot of time. Before explaining what this helper function will do We will list the metrics that are required in this 

q - prime number <br>
p - primitive root <br>
e - public key (1 < e < phi && it must not be coprime of phi) <br>
The above stated entities must have to be provided by the user. <br>

The expression that has been used insted of eucledian method is :- d = (1+ (k + phi)) / e

Result:- 'd' and the value of k at which we get integer value of d in the expression.<br>
'Where d is the required private key'
