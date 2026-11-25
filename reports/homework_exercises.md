# Bug reports for homework_exercises.py

Line: 3
Problem: The condition `n % 2 == 1` checks if a number is odd, not even. For an even number, the remainder when divided by 2 should be 0. The docstring states "Return True if n is even", but the code returns True when n is odd.
Example: is_even(4) returns False (expected True); is_even(3) returns True (expected False)
Fix: return n % 2 == 0

Line: 8
Problem: The function `can_vote(age)` should return True if age is 18 or older, but the condition `age > 18` excludes age 18. The docstring says "Return True if age is 18 or older", which includes 18.
Example: can_vote(18) returns False (expected True)
Fix: return age >= 18

Line: 13
Problem: The function `safe_average(numbers)` returns 0 if the list is empty, but `len(numbers)` will be 0, causing division by zero. The docstring says "Return the average... or 0 if the list is empty", but division by zero is undefined and will raise an error.
Example: safe_average([]) raises ZeroDivisionError
Fix: return sum(numbers) / len(numbers) if numbers else 0

Line: 18
Problem: The function `is_palindrome(text)` compares the text directly with its reverse, but it does not handle case-insensitivity as required. The docstring specifies "case-insensitive", but the current code is case-sensitive.
Example: is_palindrome("Aa") returns False (expected True)
Fix: return text.lower() == text[::-1].lower()

Line: 23
Problem: The function `second_largest(numbers)` sorts the list and returns `numbers[-2]`, but this assumes the list has at least two unique elements. If there are duplicates, the second largest might not be unique. Also, if there are fewer than 2 unique numbers (e.g., all elements the same), the function returns the second last element which may not be valid. The docstring says "Return the second largest unique number", but the code does not ensure uniqueness.
Example: second_largest([5, 5, 5]) returns 5 (but there's only one unique number, so should return None)
Fix: numbers = sorted(set(numbers)); return numbers[-2] if len(numbers) >= 2 else None
