---
name: gpt-footprinting
description: 'Skill: gpt-footprinting'
license: MIT
tags:
- general
---

[Intelligent Platform Management Interface](https://www.thomas-krenn.com/en/wiki/IPMI_Basics) (`IPMI`) is a set of standardized specifications for hardware-based host management systems used for system management and monitoring. It acts as an autonomous subsystem and works independently of the host's BIOS, CPU, firmware, and underlying operating system. IPMI provides sysadmins with the ability to manage and monitor systems even if they are powered off or in an unresponsive state. It operates using a direct network connection to the system's hardware and does not require access to the operating system via a login shell. IPMI can also be used for remote upgrades to systems without requiring physical access to the target host. IPMI is typically used in three ways:

- Before the OS has booted to modify BIOS settings
- When the host is fully powered down
- Access to a host after a system failure

When not being used for these tasks, IPMI can monitor a range of different things such as system temperature, voltage, fan status, and power supplies. It can also be used for querying inventory information, reviewing hardware logs, and alerting using SNMP. The host system can be powered off, but the IPMI module requires a power source and a LAN connection to work correctly.

#### footprinting 

IPMI communicates over port 623 UDP. Systems that use the IPMI protocol are called Baseboard Management Controllers (BMCs). BMCs are typically implemented as embedded ARM systems running Linux, and connected directly to the host's motherboard. BMCs are built into many motherboards but can also be added to a system as a PCI card. Most servers either come with a BMC or support adding a BMC. The most common BMCs we often see during internal penetration tests are HP iLO, Dell DRAC, and Supermicro IPMI. If we can access a BMC during an assessment, we would gain full access to the host motherboard and be able to monitor, reboot, power off, or even reinstall the host operating system. Gaining access to a BMC is nearly equivalent to physical access to a system. Many BMCs (including HP iLO, Dell DRAC, and Supermicro IPMI) expose a web-based management console, some sort of command-line remote access protocol such as Telnet or SSH, and the port 623 UDP, which, again, is for the IPMI network protocol. Below is a sample Nmap scan using the Nmap [ipmi-version](https://nmap.org/nsedoc/scripts/ipmi-version.html) NSE script to footprint the service.

Nmap

```shell-session
tr01ax@htb[/htb]$ sudo nmap -sU --script ipmi-version -p 623 ilo.inlanfreight.local
```

During internal penetration tests, we often find BMCs where the administrators have not changed the default password. Some unique default passwords to keep in our cheatsheets include:

|Product|Username|Password|
|---|---|---|
|Dell iDRAC|root|calvin|
|HP iLO|Administrator|randomized 8-character string consisting of numbers and uppercase letters|
|Supermicro IPMI|ADMIN|ADMIN|

If default credentials do not work to access a BMC, we can turn to a [flaw](http://fish2.com/ipmi/remote-pw-cracking.html) in the RAKP protocol in IPMI 2.0. During the authentication process, the server sends a salted SHA1 or MD5 hash of the user's password to the client before authentication takes place. This can be leveraged to obtain the password hash for ANY valid user account on the BMC. These password hashes can then be cracked offline using a dictionary attack using `Hashcat` mode `7300`. In the event of an HP iLO using a factory default password, we can use this #Hashcat mask attack command `hashcat -m 7300 ipmi.txt -a 3 ?1?1?1?1?1?1?1?1 -1 ?d?u` which tries all combinations of upper case letters and numbers for an eight-character password.

### Linux Remote Management Protocols

#linux #ssh [[Lesson 17 - Linux managment protocols]]

#### SSH

One of the tools we can use to fingerprint the SSH server is [ssh-audit](https://github.com/jtesta/ssh-audit). It checks the client-side and server-side configuration and shows some general information and which encryption algorithms are still used by the client and server. Of course, this could be exploited by attacking the server or client at the cryptic level later.

#### Rsync

[Rsync](https://linux.die.net/man/1/rsync) is a fast and efficient tool for locally and remotely copying files. It can be used to copy files locally on a given machine and to/from remote hosts. It is highly versatile and well-known for its delta-transfer algorithm. This algorithm reduces the amount of data transmitted over the network when a version of the file already exists on the destination host. It does this by sending only the differences between the source files and the older version of the files that reside on the destination server. It is often used for backups and mirroring. It finds files that need to be transferred by looking at files that have changed in size or the last modified time. By default, it uses port `873` and can be configured to use SSH for secure file transfers by piggybacking on top of an established SSH server connection.

This [guide](https://book.hacktricks.xyz/network-services-pentesting/873-pentesting-rsync) covers some of the ways Rsync can be abused, most notably by listing the contents of a shared folder on a target server and retrieving files. This can sometimes be done without authentication. Other times we will need credentials. If you find credentials during a pentest and run into Rsync on an internal (or external) host, it is always worth checking for password re-use as you may be able to pull down some sensitive files that could be used to gain remote access to the target.

Let's do a bit of quick footprinting. We can see that Rsync is in use using protocol 31.

Scanning for Rsync

```shell-session
tr01ax@htb[/htb]$ sudo nmap -sV -p 873 127.0.0.1
```

Probing for Accessible Shares

```shell-session
tr01ax@htb[/htb]$ nc -nv 127.0.0.1 873
```

Enumerating an Open Share

```shell-session
tr01ax@htb[/htb]$ rsync -av --list-only rsync://127.0.0.1/dev
```
From here, we could sync all files to our attack host with the command `rsync -av rsync://127.0.0.1/dev`. If Rsync is configured to use SSH to transfer files, we could modify our commands to include the `-e ssh` flag, or `-e "ssh -p2222"` if a non-standard port is in use for SSH. This [guide](https://phoenixnap.com/kb/how-to-rsync-over-ssh) is helpful for understanding the syntax for using Rsync over SSH.

#### R-Services

R-Services are a suite of services hosted to enable remote access or issue commands between Unix hosts over TCP/IP. Initially developed by the Computer Systems Research Group (`CSRG`) at the University of California, Berkeley, `r-services` were the de facto standard for remote access between Unix operating systems until they were replaced by the Secure Shell (`SSH`) protocols and commands due to inherent security flaws built into them. Much like `telnet`, r-services transmit information from client to server(and vice versa.) over the network in an unencrypted format, making it possible for attackers to intercept network traffic (passwords, login information, etc.) by performing man-in-the-middle (`MITM`) attacks.

`R-services` span across the ports `512`, `513`, and `514` and are only accessible through a suite of programs known as `r-commands`. They are most commonly used by commercial operating systems such as Solaris, HP-UX, and AIX. While less common nowadays, we do run into them from time to time during our internal penetration tests so it is worth understanding how to approach them.

The [R-commands](https://en.wikipedia.org/wiki/Berkeley_r-commands) suite consists of the following programs:

- rcp (`remote copy`)
- rexec (`remote execution`)
- rlogin (`remote login`)
- rsh (`remote shell`)
- rstat
- ruptime
- rwho (`remote who`)

The table below will provide a quick overview of the most frequently abused commands, including the service daemon they interact with, over what port and transport method to which they can be accessed, and a brief description of each.

|**Command**|**Service Daemon**|**Port**|**Transport Protocol**|**Description**|
|---|---|---|---|---|
|`rcp`|`rshd`|514|TCP|Copy a file or directory bidirectionally from the local system to the remote system (or vice versa) or from one remote system to another. It works like the `cp` command on Linux but provides `no warning to the user for overwriting existing files on a system`.|
|`rsh`|`rshd`|514|TCP|Opens a shell on a remote machine without a login procedure. Relies upon the trusted entries in the `/etc/hosts.equiv` and `.rhosts` files for validation.|
|`rexec`|`rexecd`|512|TCP|Enables a user to run shell commands on a remote machine. Requires authentication through the use of a `username` and `password` through an unencrypted network socket. Authentication is overridden by the trusted entries in the `/etc/hosts.equiv` and `.rhosts` files.|
|`rlogin`|`rlogind`|513|TCP|Enables a user to log in to a remote host over the network. It works similarly to `telnet` but can only connect to Unix-like hosts. Authentication is overridden by the trusted entries in the `/etc/hosts.equiv` and `.rhosts` files.|

#### Scanning for R-Services

Scanning for R-Services

```shell-session
tr01ax@htb[/htb]$ sudo nmap -sV -p 512,513,514 10.0.17.2
```

Logging in Using Rlogin

```shell-session
tr01ax@htb[/htb]$ rlogin 10.0.17.2 -l htb-student
```

Listing Authenticated Users Using Rusers

```shell-session
tr01ax@htb[/htb]$ rusers -al 10.0.17.5
```

### Windows Remote Management Protocols
#windows #rpc
[[Lesson 18 - Windows Remote Management Protocols]]

Windows servers can be managed locally using Server Manager administration tasks on remote servers. Remote management is enabled by default starting with Windows Server 2016. Remote management is a component of the Windows hardware management features that manage server hardware locally and remotely. These features include a service that implements the WS-Management protocol, hardware diagnostics and control through baseboard management controllers, and a COM API and script objects that enable us to write applications that communicate remotely through the WS-Management protocol.

The main components used for remote management of Windows and Windows servers are the following:

- Remote Desktop Protocol (`RDP`)
- Windows Remote Management (`WinRM`)
- Windows Management Instrumentation (`WMI`)

#### Footprinting the Service

Scanning the RDP service can quickly give us a lot of information about the host. For example, we can determine if `NLA` is enabled on the server or not, the product version, and the hostname.

```shell-session
tr01ax@htb[/htb]$ nmap -sV -sC 10.129.201.248 -p3389 --script rdp*
```

In addition, we can use `--packet-trace` to track the individual packages and inspect their contents manually. We can see that the `RDP cookies` (`mstshash=nmap`) used by Nmap to interact with the RDP server can be identified by `threat hunters` and various security services such as [Endpoint Detection and Response](https://en.wikipedia.org/wiki/Endpoint_detection_and_response) (`EDR`), and can lock us out as penetration testers on hardened networks.

```shell-session
tr01ax@htb[/htb]$ nmap -sV -sC 10.129.201.248 -p3389 --packet-trace --disable-arp-ping -n
```

A Perl script named [rdp-sec-check.pl](https://github.com/CiscoCXSecurity/rdp-sec-check) has also been developed by [Cisco CX Security Labs](https://github.com/CiscoCXSecurity) that can unauthentically identify the security settings of RDP servers based on the handshakes.

Authentication and connection to such RDP servers can be made in several ways. For example, we can connect to RDP servers on Linux using `xfreerdp`, `rdesktop`, or `Remmina` and interact with the GUI of the server accordingly.

Initiate an RDP Session

```shell-session
tr01ax@htb[/htb]$ xfreerdp /u:cry0l1t3 /p:"P455w0rd!" /v:10.129.201.248
```

#### WinRM

The Windows Remote Management (`WinRM`) is a simple Windows integrated remote management protocol based on the command line. WinRM uses the Simple Object Access Protocol (`SOAP`) to establish connections to remote hosts and their applications. Therefore, WinRM must be explicitly enabled and configured starting with Windows 10. WinRM relies on `TCP` ports `5985` and `5986` for communication, with the last port `5986 using HTTPS`, as ports 80 and 443 were previously used for this task. However, since port 80 was mainly blocked for security reasons, the newer ports 5985 and 5986 are used today.

As we already know, WinRM uses TCP ports `5985` (`HTTP`) and `5986` (`HTTPS`) by default, which we can scan using Nmap. However, often we will see that only HTTP (`TCP 5985`) is used instead of HTTPS (`TCP 5986`).

```shell-session
tr01ax@htb[/htb]$ nmap -sV -sC 10.129.201.248 -p5985,5986 --disable-arp-ping -n
```

If we want to find out whether one or more remote servers can be reached via WinRM, we can easily do this with the help of PowerShell. The [Test-WsMan](https://docs.microsoft.com/en-us/powershell/module/microsoft.wsman.management/test-wsman?view=powershell-7.2) cmdlet is responsible for this, and the host's name in question is passed to it. In Linux-based environments, we can use the tool called [evil-winrm](https://github.com/Hackplayers/evil-winrm), another penetration testing tool designed to interact with WinRM.

```shell-session
tr01ax@htb[/htb]$ evil-winrm -i 10.129.201.248 -u Cry0l1t3 -p P455w0rD!
```

#### WMI

Windows Management Instrumentation (`WMI`) is Microsoft's implementation and also an extension of the Common Information Model (`CIM`), core functionality of the standardized Web-Based Enterprise Management (`WBEM`) for the Windows platform. WMI allows read and write access to almost all settings on Windows systems. Understandably, this makes it the most critical interface in the Windows environment for the administration and remote maintenance of Windows computers, regardless of whether they are PCs or servers. WMI is typically accessed via PowerShell, VBScript, or the Windows Management Instrumentation Console (`WMIC`). WMI is not a single program but consists of several programs and various databases, also known as repositories.

The initialization of the WMI communication always takes place on `TCP` port `135`, and after the successful establishment of the connection, the communication is moved to a random port. For example, the program [wmiexec.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/wmiexec.py) from the Impacket toolkit can be used for this.

WMIexec.py

```shell-session
tr01ax@htb[/htb]$ /usr/share/doc/python3-impacket/examples/wmiexec.py Cry0l1t3:"P455w0rD!"@10.129.201.248 "hostname"
```
