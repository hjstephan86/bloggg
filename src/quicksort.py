import time


def quick_sort(arr):
    """
    Sorts an array using the quicksort algorithm

    Args:
        arr: the array to sort
    """
    if arr is None or len(arr) <= 1:
        return
    quick_sort_recursive(arr, 0, len(arr) - 1)


def quick_sort_recursive(arr, low, high):
    """
    Recursive quicksort implementation

    Args:
        arr: the array to sort
        low: the starting index
        high: the ending index
    """
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quick_sort_recursive(arr, low, pivot_index - 1)
        quick_sort_recursive(arr, pivot_index + 1, high)


def partition(arr, low, high):
    """
    Partitions the array around a pivot element

    Args:
        arr: the array to partition
        low: the starting index
        high: the ending index

    Returns:
        the final position of the pivot
    """
    # Choose the rightmost element as pivot
    pivot = arr[high]

    # Index of smaller element, indicates right position of pivot
    i = low - 1

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)

    # Place pivot in correct position
    swap(arr, i + 1, high)
    return i + 1


def swap(arr, i, j):
    """
    Swaps two elements in an array

    Args:
        arr: the array
        i: first index
        j: second index
    """
    arr[i], arr[j] = arr[j], arr[i]


def print_array(arr):
    """
    Utility method to print an array

    Args:
        arr: the array to print
    """
    print(" ".join(map(str, arr)))


# Example usage
def main():
    import random
    import sys

    print(
        "================================================================================"
    )
    print("                    QUICKSORT PERFORMANCE EXPERIMENTS")
    print(
        "================================================================================"
    )

    # Test configurations: [array_size, iterations]
    test_configs = [
        [1000, 100],
        [5000, 50],
        [10000, 25],
        [25000, 10],
        [50000, 5],
        [100000, 3],
    ]

    print(
        f"{'Array Size':<12} {'Iterations':<12} {'Avg Time (ms)':<15} {'Min Time (ms)':<15} {'Max Time (ms)':<15} {'Total Time (s)':<15}"
    )
    print(
        "--------------------------------------------------------------------------------"
    )

    for config in test_configs:
        size = config[0]
        iterations = config[1]

        times = []
        total_start = time.time()

        for i in range(iterations):
            # Generate random array for each iteration
            arr = [random.randint(1, 10000) for _ in range(size)]

            # Measure sorting time
            start_time = time.time_ns()
            quick_sort(arr)
            end_time = time.time_ns()

            duration_ms = (end_time - start_time) / 1_000_000  # Convert to milliseconds
            times.append(duration_ms)

            # Progress indicator for larger tests
            if iterations <= 10 and size >= 25000:
                print(
                    f"\r  Progress: {i + 1}/{iterations} completed for size {size}",
                    end="",
                )
                sys.stdout.flush()

        total_end = time.time()
        total_time = total_end - total_start

        # Calculate statistics
        avg_time = sum(times) / len(times)
        min_time = min(times)
        max_time = max(times)

        # Clear progress line if it was printed
        if iterations <= 10 and size >= 25000:
            print("\r" + " " * 50 + "\r", end="")

        # Print results
        print(
            f"{size:<12} {iterations:<12} {avg_time:<15.3f} {min_time:<15.3f} {max_time:<15.3f} {total_time:<15.2f}"
        )

    print(
        "--------------------------------------------------------------------------------"
    )
    print("\nDetailed Analysis:")
    print("- Times shown are in milliseconds (ms)")
    print("- Each test uses randomly generated arrays")
    print("- Arrays contain integers between 1 and 10,000")
    print("- Average case complexity: O(n log n)")
    print("- Worst case complexity: O(n²)")

    # Quick demonstration with small array
    print("\n==================================================")
    print("DEMONSTRATION WITH SMALL ARRAY:")
    print("==================================================")

    demo_arr = [64, 34, 25, 12, 22, 11, 90, 5]
    print("Original array:")
    print_array(demo_arr)

    start_time = time.time_ns()
    quick_sort(demo_arr)
    end_time = time.time_ns()

    duration_ns = end_time - start_time
    duration_ms = duration_ns / 1_000_000

    print("Sorted array:")
    print_array(demo_arr)
    print(f"Time taken: {duration_ns} ns ({duration_ms:.6f} ms)")
    print("==================================================")


if __name__ == "__main__":
    main()
