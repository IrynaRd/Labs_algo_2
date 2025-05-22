def read_from_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        width, height = map(int, f.readline().split())
        matrix = [f.readline().strip() for _ in range(height)]
    return width, height, matrix

w, h, matrix = read_from_file("ijones.in")
def count_paths(w, h):
    prev_col = [1] * h
    if w == 1:
        if h > 1:
            return prev_col[0] + prev_col[-1]
        return prev_col[0]

    cum = {}
    for c in range(1, w):
        prev_totals = {}
        for r in range(h):
            letter = matrix[r][c - 1]
            if letter not in prev_totals:
                prev_totals[letter] = 0
            prev_totals[letter] += prev_col[r]

        curr = [0] * h
        for r in range(h):
            letter = matrix[r][c]
            paths_step = prev_col[r]

            paths_jump = cum.get(letter, 0) + prev_totals.get(letter, 0)
            if matrix[r][c - 1] == letter:
                paths_jump -= prev_col[r]

            curr[r] = paths_step + paths_jump

        for letter in prev_totals:
            if letter not in cum:
                cum[letter] = 0
            cum[letter] += prev_totals[letter]

        prev_col = curr

    return prev_col[0] + prev_col[-1]

def write_file(filename, result):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(str(result))

ans = count_paths(w, h)
write_file("ijones.out", ans)
