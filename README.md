# ascii2hex
Simple python code for convert ASCII string to HEX string

# how to run
That python code allow to convert ASCII string to hex in 2 type format, "%" or "\x", or other ones you need.
You can select the format by using -p flag and specefie the pattern.

# example
└─$ python3 ./ascii2hex.py -s '<? phpinfo() ?>'

%3c%3f%20%70%68%70%69%6e%66%6f%28%29%20%3f%3e

└─$ python3 ./ascii2hex.py -s '<? phpinfo() ?>' -p \\x

\x3c\x3f\x20\x70\x68\x70\x69\x6e\x66\x6f\x28\x29\x20\x3f\x3e
                                        
