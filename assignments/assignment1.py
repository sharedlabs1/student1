def calculate_mean(numbers):
    """
    Calculate the arithmetic mean (average) of a list of numbers.
    
    Args:
        numbers (list): A list of numbers (int or float)
        
    Returns:
        float: The arithmetic mean of the numbers
        
    Raises:
        ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("The list is empty")
    return sum(numbers) / len(numbers)


def find_median(numbers):
    """
    Find the median value of a list of numbers.
    If the list has an odd number of elements, return the middle element.
    If the list has an even number of elements, return the average of the two middle elements.
    
    Args:
        numbers (list): A list of numbers (int or float)
        
    Returns:
        float: The median value
        
    Raises:
        ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("The list is empty")
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]


def count_frequency(items):
    """
    Count the frequency of each item in the list.
    
    Args:
        items (list): A list of items
        
    Returns:
        dict: A dictionary mapping each item to its frequency
    """
    frequency = {}
    for item in items:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency


def find_range(numbers):
    """
    Calculate the range of a list of numbers (max - min).
    
    Args:
        numbers (list): A list of numbers (int or float)
        
    Returns:
        float: The range of the numbers
        
    Raises:
        ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("The list is empty")
    return max(numbers) - min(numbers)

if __name__ == "__main__":
    # Example usage
    numbers = [1, 2, 3, 4, 5]
    print(calculate_mean(numbers))
    print(find_median(numbers))
    print(count_frequency(numbers))
    print(find_range(numbers))
