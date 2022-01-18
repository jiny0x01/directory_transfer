# directory_transfer
transfer local directory to remote

## dependency
> pip install paramiko

## usage
> python3 ./directory_transfer.py [host] [ip] [port] [password] [remote_destination_full_path] [transfer_src_directory_full_path]

### example
e.g): python3 ./directory_transfer.py root 192.123.456.78 8080 password1234! /home/root /c/Users/user1/Desktop/transfer_dir
