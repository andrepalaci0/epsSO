public class HelloWorldThread extends Thread {
    public void run() {
        System.out.println("Hello, world from thread!");
    }

    public static void main(String[] args) {
        System.out.println("Hello, world from the main process!");

        int numThreads = 5; // Defina o número de threads que deseja criar

        for (int i = 0; i < numThreads; i++) {
            HelloWorldThread thread = new HelloWorldThread();
            thread.start();
        }
    }
}
