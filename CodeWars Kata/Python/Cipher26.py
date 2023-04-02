def cipher26(message):
    decrypted = ""
    prev_sum = 0
    for char in message:
        curr_value = ord(char) - ord('a')
        decrypted_value = (curr_value - prev_sum + 26) % 26
        decrypted_char = chr(decrypted_value + ord('a'))
        decrypted += decrypted_char
        prev_sum += decrypted_value
    return decrypted
