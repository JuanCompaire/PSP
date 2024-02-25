import paramiko

def explore_remote_directory():
    # Configura los detalles de conexión SSH
    ssh_host = '127.0.0.1'  # Dirección IP del servidor SSH
    ssh_port = 2222  # Puerto SSH configurado en tu servidor
    ssh_username = 'linuxserver'  # Nombre de usuario SSH
    ssh_password = 'password'  # Contraseña SSH (cámbiala por la correcta)

    # Crea una instancia del cliente SSH
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Conéctate al servidor SSH
        ssh_client.connect(hostname=ssh_host, port=ssh_port, username=ssh_username, password=ssh_password)

        # Ejecuta comandos remotos para explorar el sistema de archivos
        stdin, stdout, stderr = ssh_client.exec_command('ls -d -1 /home/*')

        # Lee la salida estándar para obtener la lista de archivos y directorios en el directorio remoto
        remote_files = stdout.readlines()

        # Imprime la lista de archivos y directorios remotos con la ruta completa
        print("Archivos en el directorio remoto:")
        for file in remote_files:
            file_path = file.strip()
            print(file_path)

    except Exception as e:
        print("Error durante la conexión SSH:", str(e))

    finally:
        # Cierra la conexión SSH
        ssh_client.close()

explore_remote_directory()  # Llama a la función para explorar el sistema de archivos remoto
