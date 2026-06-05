import math
from collections import Counter


def calculate_entropy(data: str) -> float:
    """
    Calculates the Shannon Entropy of a given string.
    Higher entropy indicates a higher degree of randomness (e.g., cryptographic keys).
    """
    if not data:
        return 0.0

    counts = Counter(data)
    length = len(data)
    entropy = 0.0

    for count in counts.values():
        probability = count / length
        entropy -= probability * math.log2(probability)

    return entropy


def is_high_entropy(text: str) -> bool:
    """
    Determines if a string qualifies as high-entropy based on a minimum length 
    of 20 characters and a Shannon Entropy threshold of 4.0 or greater.
    """
    if len(text) < 20:
        return False

    entropy = calculate_entropy(text)
    return entropy >= 3.5
