from queue import Queue


def is_prime(num):
    # Function to check if a number is prime
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def min_days_to_reach_confidence(D, K):
    prime_numbers = [i for i in range(2, 100) if is_prime(i)]  # Generate a list of prime numbers

    visited = set()  # To keep track of visited confidence levels
    queue = Queue()  # Initialize a queue for BFS

    queue.put((0, 0))  # Tuple format: (confidence_level, days_taken)
    visited.add(0)

    while not queue.empty():
        confidence, days_taken = queue.get()

        # Check if target confidence is reached
        if confidence == D:
            return days_taken

        # Perform each exercise and add to the queue
        for p in prime_numbers[:K]:
            new_confidence = confidence + p
            if new_confidence not in visited:
                visited.add(new_confidence)
                queue.put((new_confidence, days_taken + 1))

    return -1  # Target confidence is not achievable


# Test examples
print(min_days_to_reach_confidence(10, 1))  # Output: 5
print(min_days_to_reach_confidence(11, 3))  # Output: 3
