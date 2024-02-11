import paramiko

def ssh_connect_and_show_file_content(server_ip, username, private_key_path, file_path):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    private_key = paramiko.RSAKey.from_private_key_file(private_key_path)
    client.connect(server_ip, username=username, pkey=private_key)
    stdin, stdout, stderr = client.exec_command(f'cat {file_path}')
    output = stdout.read().decode()
    print(output)


ssh_connect_and_show_file_content('your_server_ip', 'your_username', 'key.pem', '/tmp/demo.txt')
