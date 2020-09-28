# My password

У нас есть *.mem файл - дамп оперативной памяти. 

Смотрим профиль и забираем profile

```sh 
$ volatility -f 20200925.mem imageinfo
Volatility Foundation Volatility Framework 2.6
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x86_23418, Win7SP0x86, Win7SP1x86_24000, Win7SP1x86
                     AS Layer1 : IA32PagedMemoryPae (Kernel AS)
                     AS Layer2 : FileAddressSpace (/home/sonq/Документы/Tasks/GitHub/Forensics/My password/20200925.mem)
                      PAE type : PAE
                           DTB : 0x185000L
                          KDBG : 0x82962c28L
          Number of Processors : 1
     Image Type (Service Pack) : 1
                KPCR for CPU 0 : 0x82963c00L
             KUSER_SHARED_DATA : 0xffdf0000L
           Image date and time : 2020-09-25 13:45:38 UTC+0000
     Image local date and time : 2020-09-25 17:45:38 +0400
``` 
Проверяем, что подгружены SAM и SYSTEM

```sh
$ volatility -f 20200925.mem --profile=Win7SP1x86_23418 hivelistVolatility Foundation Volatility Framework 2.6
Virtual    Physical   Name
---------- ---------- ----
0x8dd33540 0x1aa3e540 \SystemRoot\System32\Config\SOFTWARE
0x8f032008 0x16077008 \SystemRoot\System32\Config\SAM
0x913ff9c8 0x1812d9c8 \SystemRoot\System32\Config\DEFAULT
0x92714008 0x19867008 \Device\HarddiskVolume1\Boot\BCD
0x8240a9c8 0x0816c9c8 \??\C:\System Volume Information\Syscache.hve
0x8246f2c0 0x0e8d62c0 \??\C:\Users\SonQ\ntuser.dat
0x825fc228 0x0b27a228 \??\C:\Users\SonQ\AppData\Local\Microsoft\Windows\UsrClass.dat
0x8760c008 0x1b7e3008 [no name]
0x8761b008 0x1baea008 \REGISTRY\MACHINE\SYSTEM
0x87645008 0x1b9d6008 \REGISTRY\MACHINE\HARDWARE
0x87b0b9c8 0x09ec49c8 \??\C:\Windows\ServiceProfiles\NetworkService\NTUSER.DAT
0x87bae9c8 0x02d649c8 \??\C:\Windows\ServiceProfiles\LocalService\NTUSER.DAT
0x89ff1008 0x1a920008 \SystemRoot\System32\Config\SECURITY
```
Берем виртуальные адреса SAM и SYSTEM, получаем hashdump

```sh
$ volatility -f 20200925.mem --profile=Win7SP1x86_23418 hashdump -y 0x8761b008 -s 0x8f032008
Volatility Foundation Volatility Framework 2.6
:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
SonQ:1001:aad3b435b51404eeaad3b435b51404ee:b9f917853e3dbf6e6831ecce60725930:::
HomeGroupUser$:1002:aad3b435b51404eeaad3b435b51404ee:e0948781244b482dba5e83d88cf98018:::
```
Нас интересует учетка SonQ
Ее хэш: b9f917853e3dbf6e6831ecce60725930
Хэш можно крякнуть, но советую сначала погуглить. Обычные пароли находятся без проблем.

Получаем флаг: 4hsl33p{passw0rd}