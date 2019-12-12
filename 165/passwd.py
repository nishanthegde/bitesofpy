DEFAULT_SHELL = 'bash'
# https://github.com/avar/git-anyonecanedit-etc/blob/master/passwd

OTHER_PASSWD_OUTPUT = """root:!:0:0::/:/usr/bin/ksh
daemon:!:1:1::/etc:
bin:!:2:2::/bin:
sys:!:3:3::/usr/sys:
adm:!:4:4::/var/adm:
uucp:!:5:5::/usr/lib/uucp:
guest:!:100:100::/home/guest:
nobody:!:4294967294:4294967294::/:
lpd:!:9:4294967294::/:
lp:*:11:11::/var/spool/lp:/bin/false
invscout:*:200:1::/var/adm/invscout:/usr/bin/ksh
nuucp:*:6:5:uucp login user:/var/spool/uucppublic:/usr/sbin/uucp/uucico
paul:!:201:1::/home/paul:/usr/bin/ksh
jdoe:*:202:1:John Doe:/home/jdoe:/usr/bin/ksh"""


PASSWD_OUTPUT = """root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/bin/sh
man:x:6:12:man:/var/cache/man:/bin/sh
lp:x:7:7:lp:/var/spool/lpd:/bin/sh
mail:x:8:8:mail:/var/mail:/bin/sh
news:x:9:9:news:/var/spool/news:/bin/sh
uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh
proxy:x:13:13:proxy:/bin:/bin/sh
www-data:x:33:33:www-data:/var/www:/bin/sh
backup:x:34:34:backup:/var/backups:/bin/sh
list:x:38:38:Mailing List Manager:/var/list:/bin/sh
irc:x:39:39:ircd:/var/run/ircd:/bin/sh
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
nobody:x:65534:65534:nobody:/nonexistent:/bin/sh
libuuid:x:100:101::/var/lib/libuuid:/bin/sh
Debian-exim:x:101:103::/var/spool/exim4:/bin/false
statd:x:102:65534::/var/lib/nfs:/bin/false
sshd:x:103:65534::/var/run/sshd:/usr/sbin/nologin
ftp:x:104:65534::/home/ftp:/bin/false
messagebus:x:105:106::/var/run/dbus:/bin/false
mysql:x:106:107:MySQL Server,,,:/var/lib/mysql:/bin/false
avar:x:1000:1000::/home/avar:/bin/bash
chad:x:1001:1001::/home/chad:/bin/bash
git-svn-mirror:x:1002:1002:Git mirror,,,:/home/git-svn-mirror:/bin/bash
gerrit2:x:1003:1003:Gerrit User,,,:/home/gerrit2:/bin/bash
avahi:x:107:108:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false
postfix:x:108:112::/var/spool/postfix:/bin/false
ssh-rsa:x:1004:1004::/home/ssh-rsa:/bin/bash
artagnon:x:1005:1005:Ramkumar R,,,,Git GSOC:/home/artagnon:/bin/bash"""


def get_users_for_shell(passwd_output: str = PASSWD_OUTPUT,
                        grep_shell: str = DEFAULT_SHELL) -> list:
    """Match the passwd_output string for users with grep_shell.
       Return a list of users.
    """
    backchar = len(grep_shell) + 1
    lines = passwd_output.splitlines()
    # return [l.strip().split(':')[0] for l in lines if l.strip()[-backchar:] == '\'+DEFAULT_SHELL]
    # return [l.strip().split(':')[0] for l in lines if l.strip()[-backchar:] == '\\{}'.format(DEFAULT_SHELL)]
    return [l.strip().split(':')[0] for l in lines if l.strip()[-backchar:] == '/{}'.format(grep_shell)]


# def main():
#     print('thank you for everything...')
#     actual = get_users_for_shell()
#     expected = ['artagnon', 'avar', 'chad', 'gerrit2',
#                 'git-svn-mirror', 'root', 'ssh-rsa']
#     assert sorted(actual) == expected

#     actual = get_users_for_shell(grep_shell='sh')
#     expected = ['backup', 'bin', 'daemon', 'games', 'gnats', 'irc',
#                 'libuuid', 'list', 'lp', 'mail', 'man', 'news',
#                 'nobody', 'proxy', 'sys', 'uucp', 'www-data']
#     # print(actual)
#     assert sorted(actual) == expected

#     actual = get_users_for_shell(passwd_output=OTHER_PASSWD_OUTPUT,
#                                  grep_shell='ksh')
#     expected = ['invscout', 'jdoe', 'paul', 'root']
#     assert sorted(actual) == expected


# if __name__ == '__main__':
#     main()
