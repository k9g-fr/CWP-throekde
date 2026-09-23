"""ไฟล์หลักสำหรับตรวจจับการ Checkmate"""

def checkmate(board):
    if not isinstance(board, str):
        print("Error")
        return

    lines = board.split('\n')
    n = len(lines)
    if n == 0:
        print("Error")
        return
    
    for line in lines:
        if len(line) != n:
            print("Error")
            return

    kr, kc = -1, -1
    k_count = 0
    for r in range(n):
        for c in range(n):
            if lines[r][c] == 'K':
                kr = r
                kc = c
                k_count += 1

    if k_count != 1:
        print("Error")
        return

    pieces = ['K', 'P', 'B', 'R', 'Q']

    for row_step, col_step in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r, c = kr + row_step, kc + col_step
        while 0 <= r < n and 0 <= c < n:
            p = lines[r][c]
            if p in ['R', 'Q']:
                print("Success")
                return
            if p in pieces:
                break
            r += row_step
            c += col_step

    for row_step, col_step in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        r, c = kr + row_step, kc + col_step
        step = 1
        while 0 <= r < n and 0 <= c < n:
            p = lines[r][c]
            if p in ['B', 'Q']:
                print("Success")
                return
            if p == 'P' and row_step == 1 and step == 1:
                print("Success")
                return
            if p in pieces:
                break
            r += row_step
            c += col_step
            step += 1
            
    print("Fail")