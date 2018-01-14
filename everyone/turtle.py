import turtle as t
import time

def spiral(sp_len):
    if sp_len <= 5:
        return

    t.forward(sp_len)
    t.right(90)
    spiral(sp_len - 5)


def tri(tri_len):
    if tri_len <= 10:
        for i in range(0, 3):
            t.forward(tri_len)
            t.left(120)
        return

    new_len = tri_len / 2
    tri(new_len)
    t.forward(new_len)
    tri(new_len)
    t.backward(new_len)
    t.left(60)
    t.forward(new_len)
    t.right(60)
    tri(new_len)
    t.left(60)
    t.backward(new_len)
    t.right(60)


def tree(br_len):
    if br_len <= 5:
        return

    new_len = br_len * 0.7
    t.forward(br_len)
    t.right(20)
    tree(new_len)
    t.left(40)
    tree(new_len)
    t.right(20)
    t.backward(br_len)


def snow_line(snow_len):
    if snow_len <= 10:
        t.forward(snow_len)
        return

    new_len = snow_len / 3
    snow_line(new_len)
    t.left(60)
    snow_line(new_len)
    t.right(120)
    snow_line(new_len)
    t.left(60)
    snow_line(new_len)

if __name__ == '__main__':
    t.speed(0)
    snow_line(150)
    t.right(120)
    snow_line(150)
    t.right(120)
    snow_line(150)

    time.sleep(3)
    t.reset()

