def get_levenshtein_distance(a, b):
    """"Calculates the Levenshtein distance between a and b."""
    n, m = len(a), len(b)

    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a, b = b, a
        n, m = m, n
    current_row = range(n+1)    # Keep current and previous row, not entire matrix

    for i in range(1, m+1):
        previous_row, current_row = current_row, [i]+[0]*n
        for j in range(1, n+1):
            add, delete, change = previous_row[j]+1, current_row[j-1]+1, previous_row[j-1]
            if a[j-1] != b[i-1]:
                change += 1
            current_row[j] = min(add, delete, change)
    return current_row[n]


if __name__ == "__main__":

    list_a = ["Chandler", "Dayton", "Alexandria", "Madison"]
    list_b = ["Channel", "Daytons", "Maxima", "Mississippi"]

    for i in range(0, len(list_a)):
        print(f"{list_a[i]} vs {list_b[i]} >> {get_levenshtein_distance(list_a[i], list_b[i])}")

