import paramiko

class SecureFileTransferSystem:
    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.transport = None
        self.sftp = None

    def connect(self):
        try:
            self.transport = paramiko.Transport((self.hostname, self.port))
            self.transport.connect(username=self.username, password=self.password)
            self.sftp = paramiko.SFTPClient.from_transport(self.transport)
            print("Connected to the server.")
        except Exception as e:
            print(f"Error connecting: {e}")

    def disconnect(self):
        if self.transport is not None:
            self.transport.close()
            print("Disconnected from the server.")

    def upload_file(self, local_path, remote_path):
        try:
            self.sftp.put(local_path, remote_path)
            print(f"File '{local_path}' uploaded to '{remote_path}'.")
        except Exception as e:
            print(f"Error uploading file: {e}")

    def download_file(self, remote_path, local_path):
        try:
            self.sftp.get(remote_path, local_path)
            print(f"File '{remote_path}' downloaded to '{local_path}'.")
        except Exception as e:
            print(f"Error downloading file: {e}")

if __name__ == "__main__":
    # Replace these values with your server details
    hostname = "your_server_hostname"
    port = 22  # default SSH port
    username = "your_username"
    password = "your_password"

    # Replace these paths with your local and remote file paths
    local_file_path = "local_file.txt"
    remote_file_path = "remote_file.txt"

    try:
        transfer_system = SecureFileTransferSystem(hostname, port, username, password)
        transfer_system.connect()

        # Upload a file
        transfer_system.upload_file(local_file_path, remote_file_path)

        # Download the file back
        transfer_system.download_file(remote_file_path, "downloaded_file.txt")

    finally:
        if transfer_system:
            transfer_system.disconnect()
