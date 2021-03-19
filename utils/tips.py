import time

def info(main_tips, print_out=True, show_cur_time=True):
    infos = main_tips
    if show_cur_time:
        cur_time = time.asctime(time.localtime(time.time()))
        infos = f"{cur_time}\n{infos}"
    if print_out:
        print(infos)
    return infos