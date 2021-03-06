class SSH(object):

    def __init__(self, device_name, username, password, buffer="65535",
                 delay="1", port="22"):
        self.device_name = device_name
        self.username = username
        self.password = password
        self.buffer = buffer
        self.delay = delay
        self.port = int(port)

    def connect(self):
        import paramiko
        import time

        self.pre_conn = paramiko.SSHClient()
        self.pre_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.pre_conn.connect(self.device_name, username=self.username,
                              password=self.password, allow_agent=False,
                              look_for_keys=False, port=self.port)
        self.client_conn = self.pre_conn.invoke_shell()
        time.sleep(float(self.delay))
        return self.client_conn.recv(self.buffer)

    def close(self):
        return self.pre_conn.close()

    def clear_buffer(self):
        if self.client_conn.recv_ready():
            return self.client_conn.recv(self.buffer)
        else:
            return None

    def set_enable(self, enable_password):
        import re

        if re.search('>$', self.command('\n')):
            enable = self.command('enable')
            if re.search('Password', enable):
                send_pwd = self.command(enable_password)
                return send_pwd
        elif re.search('#$', self.command('\n')):
            return "Action: None. Already in enable mode."
        else:
            return "Error: Unable to determine user privilege status."

    def disable_paging(self, command='term len 0'):
        self.clear_buffer()
        return self.client_conn.sendall(command + "\n")

    def save(self. sw_type):
        if sw_type == "cisco" or sw_type == "ruijie":
            command( "end")
            res = command( "write")
            print res
        elif sw_type == "huawei":
            command("return")
            self.client_conn.sendall("save\n")
            res = ssh.command("q")

    def command(self, command):
        import time

        self.client_conn.sendall(command + "\n")
        not_done = True
        output = ""
        #self.clear_buffer()
        while not_done:
            time.sleep(float(self.delay))
            if self.client_conn.recv_ready():
                output += self.client_conn.recv(self.buffer)
            else:
                not_done = False
        return output