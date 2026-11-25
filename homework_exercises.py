def is_even(n):
    """Return True if n is even, False otherwise."""
    return n % 2 == 0


def can_vote(age):
    """Return True if age is 18 or older, False otherwise."""
    return age >= 18


def safe_average(numbers):
    """Return the average of a list of numbers, or 0 if the list is empty."""
    return sum(numbers) / len(numbers) if numbers else 0


def is_palindrome(text):
    """Return True if text reads the same forwards and backwards (case-insensitive)."""
    return text.lower() == text[::-1].lower()


def second_largest(numbers):
    """Return the second largest unique number in a list, or None if fewer than 2 unique numbers."""
    numbers = sorted(set(numbers))
    return numbers[-2] if len(numbers) >= 2 else None
