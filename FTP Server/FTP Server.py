__author__ = '13123935 - Jordan Harman'

import os
import threading


class FTP_Server():
    def __init__(self, (connection, address)):
        self.connection = connection
        self.address = address
        self.base_directory = os.path.abspath('.')
        self.current_working_directory = self.base_directory
        self.rest = True
        self.user_logged_in = True
        self.passive = False
        self.current_user = ""
        self.current_user_password = ""
        self.server_transfer_type = "L8"
        self.encoding = "utf8"
        threading.Thread.__init__(self)

    def run(self):
        pass

    # commands
    def ABOR(self, cmd):
        pass

    def ACCT(self, cmd):
        pass

    def ADAT(self, cmd):
        pass

    def ALLO(self, cmd):
        pass

    def APPE(self, cmd):
        pass

    def AUTH(self, cmd):
        pass

    def CCC(self, cmd):
        pass

    def CDUP(self, cmd):
        pass

    def CONF(self, cmd):
        pass

    def CWD(self, cmd):
        pass

    def DELE(self, cmd):
        pass

    def ENC(self, cmd):
        pass

    def EPRT(self, cmd):
        pass

    def EPSV(self, cmd):
        pass

    def FEAT(self, cmd):
        pass

    def HELP(self, cmd):
        pass

    def HOST(self, cmd):
        pass

    def LANG(self, cmd):
        pass

    def LIST(self, cmd):
        pass

    def LPRT(self, cmd):
        pass

    def LPSV(self, cmd):
        pass

    def MDTM(self, cmd):
        pass

    def MIC(self, cmd):
        pass

    def MKD(self, cmd):
        pass

    def MLSD(self, cmd):
        pass

    def MLST(self, cmd):
        pass

    def MODE(self, cmd):
        pass

    def NLST(self, cmd):
        pass

    def NOOP(self, cmd):
        self.connection.send('200 OK.\r\n')

    def OPTS(self, cmd):
        if cmd[5:-2].lower() == "utf8 on"():
            self.connection.send("200 OK.\r\n")
            self.encoding = "utf8"
        else:
            self.connection.send("451 Not supported.\r\n")

    def PASS(self, cmd):
        if cmd[5:-2].lower() == "password":
            self.connection.send("230 Login Successful\r\n")
            self.user_logged_in = True
        else:
            self.connection.send("530 Login Incorrect\r\n")
            self.current_user = ""
            self.current_user_password = ""

    def PASV(self, cmd):
        pass

    def PBSZ(self, cmd):
        pass

    def PORT(self, cmd):
        pass

    def PROT(self, cmd):
        pass

    def PWD(self, cmd):
        if self.user_logged_in:
            cwd = os.path.relpath(self.current_working_directory, self.base_directory)
            if cwd == ".":
                cwd = "/"
            else:
                cwd = "/" + cwd
            self.connection.send("257 {} \r\n".format(cwd))

    def QUIT(self, cmd):
        pass

    def REIN(self, cmd):
        pass

    def REST(self, cmd):
        pass

    def RETR(self, cmd):
        pass

    def RMD(self, cmd):
        pass

    def RNFR(self, cmd):
        pass

    def RNTO(self, cmd):
        pass

    def SITE(self, cmd):
        pass

    def SIZE(self, cmd):
        pass

    def SMNT(self, cmd):
        pass

    def STAT(self, cmd):
        pass

    def STOR(self, cmd):
        pass

    def STOU(self, cmd):
        pass

    def STRU(self, cmd):
        pass

    def SYST(self, cmd):
        if self.user_logged_in:
            self.connection.send("215 Windows_NT Type: {}\r\n".format(self.server_transfer_type))

    def TYPE(self, cmd):
        pass

    def USER(self, cmd):
        if cmd[5:] == "admin":
            self.current_user = cmd[5:]
            self.connection.send("331 Please Specify Password \r\n")
        else:
            self.connection.send("530 Login Incorrect\r\n")
            self.current_user = ""

    def XCUP(self, cmd):
        pass

    def XMKD(self, cmd):
        pass

    def XPWD(self, cmd):
        pass

    def XRCP(self, cmd):
        pass

    def XRMD(self, cmd):
        pass

    def XRSQ(self, cmd):
        pass

    def XSEM(self, cmd):
        pass

    def XSEN(self, cmd):
        pass
