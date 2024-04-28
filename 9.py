import socket

target_ip = input("أدخل عنوان الآي بي المستهدف: ")

def البحث_عن_المنافذ_المفتوحة(ip):
    print("جاري فحص المنافذ المفتوحة على", ip)
    for port in range(1, 1025):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                print("المنفذ", port, "مفتوح")
            s.close()
        except KeyboardInterrupt:
            print("\nتم إيقاف البحث.")
            break
        except Exception as e:
            print("حدث خطأ:", e)

البحث_عن_المنافذ_المفتوحة(target_ip)
