# ns1cli
Basic commandline tool for communicating with the NS1 DNS services. Not nearly as fancy as "true" cli tools. Hacked together by python novice. Google is my best friend.

This cli tool's purpose to pull DNS Zone/Record data and create some standard DNS records without the additional features that NS1 offers. #BasicAF
![image](https://user-images.githubusercontent.com/108297740/176026665-cca4c854-dcbe-43b4-9b4f-0ccd956a8f41.png)

# Pre-Reqs
1. NS1 API Key
2. Python v3.8
3. Libraries Used:
 getopt,
 sys,
 pprint,
 ns1-python,
 pandas,
 tabulate,
 colorama,
 termcolor,
 pyfiglet
 4. Create directory "ns1cli" to add the scripts
  
# Windows ALIAS Creation
Create an ALIAS for executing scripts
1. Open Powershell and run "$PROFILE"
![image](https://user-images.githubusercontent.com/108297740/176015899-70772faa-1994-4fe4-b6bd-305221eded9b.png)

2. Open the profile by running "notepad $PROFILE output path"
![image](https://user-images.githubusercontent.com/108297740/176016339-937b3846-7029-484f-b3b9-c6d42bbb56ad.png)

3. Notepad will open and you can add the function to run the py scripts along with setting the ALIAS for the function.
```powershell
function ns1get {py C:\Users\Username\ns1cli\ns1cli-get.py @args}
Set-Alias -Name ns1cli-get -Value ns1get

function ns1txt {py C:\Users\Username\ns1cli\ns1cli-txt.py @args}
Set-Alias -Name ns1cli-txt -Value ns1txt

function ns1alias {py C:\Users\Username\ns1cli\ns1cli-alias.py @args}
Set-Alias -Name ns1cli-alias -Value ns1alias

function ns1cname {py C:\Users\Username\ns1cli\ns1cli-cname.py @args}
Set-Alias -Name ns1cli-cname -Value ns1cname

function ns1a {py C:\Users\Username\ns1cli\ns1cli-a.py @args}
Set-Alias -Name ns1cli-a -Value ns1a

function ns1spf {py C:\Users\Username\ns1cli\ns1cli-spf.py @args}
Set-Alias -Name ns1cli-spf -Value ns1spf

function ns1add {py C:\Users\Username\ns1cli\ns1cli-add.py @args}
Set-Alias -Name ns1cli-add -Value ns1add

function ns1cli-h {py C:\Users\Username\ns1cli\ns1cli.py}
Set-Alias -Name ns1cli -Value ns1cli-h
```

# Dependencies
Refer to the [ns1-python](https://github.com/ns1/ns1-python) documentation for interacting with the API

