public class QuickSort {

    /**
     * Sorts an array using the quicksort algorithm
     * 
     * @param arr the array to sort
     */
    public static void quickSort(int[] arr) {
        if (arr == null || arr.length <= 1) {
            return;
        }
        quickSort(arr, 0, arr.length - 1);
    }

    /**
     * Recursive quicksort implementation
     * 
     * @param arr  the array to sort
     * @param low  the starting index
     * @param high the ending index
     */
    private static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            // Partition the array and get the pivot index
            int pivotIndex = partition(arr, low, high);

            // Recursively sort elements before and after partition
            quickSort(arr, low, pivotIndex - 1);
            quickSort(arr, pivotIndex + 1, high);
        }
    }

    /**
     * Partitions the array around a pivot element
     * 
     * @param arr  the array to partition
     * @param low  the starting index
     * @param high the ending index
     * @return the final position of the pivot
     */
    private static int partition(int[] arr, int low, int high) {
        // Choose the rightmost element as pivot
        int pivot = arr[high];

        // Index of smaller element, indicates right position of pivot
        int i = low - 1;

        for (int j = low; j < high; j++) {
            // If current element is smaller than or equal to pivot
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }

        // Place pivot in correct position
        swap(arr, i + 1, high);
        return i + 1;
    }

    /**
     * Swaps two elements in an array
     * 
     * @param arr the array
     * @param i   first index
     * @param j   second index
     */
    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    /**
     * Utility method to print an array
     * 
     * @param arr the array to print
     */
    public static void printArray(int[] arr) {
        for (int value : arr) {
            System.out.print(value + " ");
        }
        System.out.println();
    }

    // Example usage
    public static void main(String[] args) {
        System.out.println("================================================================================");
        System.out.println("                    QUICKSORT PERFORMANCE EXPERIMENTS");
        System.out.println("================================================================================");

        // Test configurations: {array_size, iterations}
        int[][] testConfigs = {
                { 1000, 100 },
                { 5000, 50 },
                { 10000, 25 },
                { 25000, 10 },
                { 50000, 5 },
                { 100000, 3 }
        };

        System.out.printf("%-12s %-12s %-15s %-15s %-15s %-15s%n",
                "Array Size", "Iterations", "Avg Time (ms)", "Min Time (ms)", "Max Time (ms)", "Total Time (s)");
        System.out.println("--------------------------------------------------------------------------------");

        for (int[] config : testConfigs) {
            int size = config[0];
            int iterations = config[1];

            double[] times = new double[iterations];
            long totalStart = System.currentTimeMillis();

            for (int i = 0; i < iterations; i++) {
                // Generate random array for each iteration
                int[] arr = generateRandomArray(size);

                // Measure sorting time
                long startTime = System.nanoTime();
                quickSort(arr);
                long endTime = System.nanoTime();

                double durationMs = (endTime - startTime) / 1_000_000.0; // Convert to milliseconds
                times[i] = durationMs;

                // Progress indicator for larger tests
                if (iterations <= 10 && size >= 25000) {
                    System.out.print("\r  Progress: " + (i + 1) + "/" + iterations + " completed for size " + size);
                    System.out.flush();
                }
            }

            long totalEnd = System.currentTimeMillis();
            double totalTime = (totalEnd - totalStart) / 1000.0;

            // Calculate statistics
            double avgTime = 0;
            double minTime = times[0];
            double maxTime = times[0];

            for (double time : times) {
                avgTime += time;
                if (time < minTime)
                    minTime = time;
                if (time > maxTime)
                    maxTime = time;
            }
            avgTime /= times.length;

            // Clear progress line if it was printed
            if (iterations <= 10 && size >= 25000) {
                System.out.print("\r" + " ".repeat(50) + "\r");
            }

            // Print results
            System.out.printf("%-12d %-12d %-15.3f %-15.3f %-15.3f %-15.2f%n",
                    size, iterations, avgTime, minTime, maxTime, totalTime);
        }

        System.out.println("--------------------------------------------------------------------------------");
        System.out.println("\nDetailed Analysis:");
        System.out.println("- Times shown are in milliseconds (ms)");
        System.out.println("- Each test uses randomly generated arrays");
        System.out.println("- Arrays contain integers between 1 and 10,000");
        System.out.println("- Average case complexity: O(n log n)");
        System.out.println("- Worst case complexity: O(n²)");

        // Quick demonstration with small array
        System.out.println("\n==================================================");
        System.out.println("DEMONSTRATION WITH SMALL ARRAY:");
        System.out.println("==================================================");

        int[] demoArr = { 64, 34, 25, 12, 22, 11, 90, 6 };
        System.out.println("Original array:");
        printArray(demoArr);

        long startTime = System.nanoTime();
        quickSort(demoArr);
        long endTime = System.nanoTime();

        long durationNs = endTime - startTime;
        double durationMs = durationNs / 1_000_000.0;

        System.out.println("Sorted array:");
        printArray(demoArr);
        System.out.printf("Time taken: %d ns (%.6f ms)%n", durationNs, durationMs);
        System.out.println("==================================================");
    }

    /**
     * Generates an array of random integers
     * 
     * @param size the size of the array
     * @return array filled with random integers
     */
    private static int[] generateRandomArray(int size) {
        int[] arr = new int[size];
        for (int i = 0; i < size; i++) {
            arr[i] = (int) (Math.random() * 1000);
        }
        return arr;
    }
}