import paramiko
import sys
import os


class MySFTPClient(paramiko.SFTPClient):
    def put_dir(self, source, target):
        ''' Uploads the contents of the source directory to the target path. The
            target directory needs to exists. All subdirectories in source are 
            created under target.
        '''
        for item in os.listdir(source):
            if os.path.isfile(os.path.join(source, item)):
                self.put(os.path.join(source, item), '%s/%s' % (target, item))
            else:
                self.mkdir('%s/%s' % (target, item), ignore_existing=True)
                self.put_dir(os.path.join(source, item), '%s/%s' % (target, item))

    def mkdir(self, path, mode=511, ignore_existing=False):
        ''' Augments mkdir by adding an option to not fail if the folder exists  '''
        try:
            super(MySFTPClient, self).mkdir(path, mode)
        except IOError:
            if ignore_existing:
                pass
            else:
                raise


def help():
    print("usage:./directory_transfer [host] [ip] [port] [password] [remote_destination_full_path] [transfer_src_directory_full_path]")
    print("e.g): ./directory_transfer root 192.123.456.78 8080 password1234! /home/root /c/Users/user1/Desktop/transfer_dir")

if __name__ == "__main__":
    print("argument length:", len(sys.argv))
    if len(sys.argv) == 7:
        user = str(sys.argv[1])
        host_ip = str(sys.argv[2])
        port = int(sys.argv[3])
        pw = str(sys.argv[4])
        target_path = str(sys.argv[5])
        source_path = os.getcwd() + str(sys.argv[6])
        print("user:", user)
        print("host_ip:", host_ip)
        print("port:", port)
        print("pw:", pw)
        print("target_path:", target_path)
        print("source_path:", source_path)

        transport = paramiko.Transport((host_ip, port))
        transport.connect(username=user, password=pw)
        sftp = MySFTPClient.from_transport(transport)
        sftp.mkdir(target_path, ignore_existing=True)
        sftp.put_dir(source_path, target_path)
        sftp.close()
    else:
        help()
        
