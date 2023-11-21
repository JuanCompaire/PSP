import psutil

def list_all_processes():
    print("List of processes with PID:")
    for process in psutil.process_iter(['pid', 'name']):
        print(f"PID: {process.info['pid']}, Name: {process.info['name']}")

def terminate_process_by_pid(pid):
    try:
        process = psutil.Process(pid)
        process.terminate()
        print(f"Process with PID {pid} terminated successfully.")
    except psutil.NoSuchProcess:
        print(f"No process found with PID {pid}.")
    except psutil.AccessDenied:
        print(f"Access denied to terminate process with PID {pid}.")




if __name__ == "__main__":
    
    list_all_processes()

    try:
        pid_to_terminate = int(input("Enter the PID of the process to terminate: "))
        terminate_process_by_pid(pid_to_terminate)
    except ValueError:
        print("Invalid input. Please enter a valid PID.")