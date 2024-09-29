def strongPasswordChecker(password: str) -> int:
    n = len(password)
    
    # Determine whether we need to add a lowercase, uppercase, or digit
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    # Count the number of missing character types
    missing_types = int(not has_lower) + int(not has_upper) + int(not has_digit)
    
    # Count the number of replacements needed for three consecutive characters
    replace = 0
    one_mod = two_mod = 0
    i = 2
    while i < n:
        if password[i] == password[i - 1] == password[i - 2]:
            length = 2
            while i < n and password[i] == password[i - 1]:
                length += 1
                i += 1
            replace += length // 3
            if length % 3 == 0:
                one_mod += 1
            elif length % 3 == 1:
                two_mod += 1
        else:
            i += 1
    
    if n < 6:
        return max(missing_types, 6 - n)
    elif n <= 20:
        return max(missing_types, replace)
    else:
        # If length is greater than 20, we need to delete characters
        excess_length = n - 20
        # Delete from sequences of length % 3 == 0, then length % 3 == 1, and then the rest
        replace -= min(excess_length, one_mod * 1) // 1
        replace -= min(max(excess_length - one_mod, 0), two_mod * 2) // 2
        replace -= max(excess_length - one_mod - 2 * two_mod, 0) // 3
        return excess_length + max(missing_types, replace)

