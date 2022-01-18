# directory_transfer
transfer local directory to remote

## dependency
> pip install paramiko, pyinstaller



## usage
> pyinstaller --onefile ./directory_transfer.py
> cd dist
> ./directory_transfer [host] [ip] [port] [password] [remote_destination_full_path] [transfer_src_directory_full_path]

### example
e.g): ./directory_transfer.py root 192.123.456.78 8080 password1234! /home/root /c/Users/user1/Desktop/transfer_dir
