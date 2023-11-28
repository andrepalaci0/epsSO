import os

def main():
    print("Hello, world from the parent process")

    # Realiza o fork para criar um processo filho
    child_pid = os.fork()

    if child_pid == 0:
        # Código executado pelo processo filho
        print("Hello, world from the child process")
    elif child_pid > 0:
        # Código executado pelo processo pai
        # Aguarda o processo filho terminar
        os.wait()
    else:
        # Erro ao criar o processo filho
        print("Fork failed")

if __name__ == "__main__":
    main()
