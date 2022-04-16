# Enter your code here. Read input from STDIN. Print output to STDOUT
import io
import os


def do_append(sio, W):
    sio.write(W)
    undo_info = len(W)
    return undo_info


def do_delete(sio, k):
    curr_pos = sio.tell()
    sio.seek(curr_pos - k)
    undo_info = sio.read(k)
    sio.seek(curr_pos - k)
    return undo_info


def do_print(sio, k):
    curr_pos = sio.tell()
    sio.seek(k - 1)
    ch = sio.read(1)
    print(ch)
    sio.seek(curr_pos)


def undo_append(sio, undo_info):
    W_len = undo_info
    curr_pos = sio.tell()
    sio.seek(curr_pos - W_len)


def undo_delete(sio, undo_info):
    deleted_W = undo_info
    sio.write(deleted_W)


UNDO_FUNCS = {"1": undo_append, "2": undo_delete}


def process_ops(ops):
    sio = io.StringIO()
    op_stack = []
    for op in ops:
        if op[0] == "4":
            op_id, undo_info = op_stack.pop()
            UNDO_FUNCS[op_id](sio, undo_info)
            continue

        if op[0] == "1":
            undo_info = do_append(sio, op[2:])
        elif op[0] == "2":
            undo_info = do_delete(sio, int(op[2:]))
        elif op[0] == "3":
            undo_info = do_print(sio, int(op[2:]))

        if undo_info is not None:
            op_stack.append((op[0], undo_info))


if __name__ == "__main__":
    with open(os.environ["INPUT_PATH"], "r") as f:
        Q = int(f.readline().rstrip())

        ops = []
        for i in range(Q):
            ops.append(f.readline().rstrip())
        process_ops(ops)
