import socket

target_ip = input("الرجاء إدخال عنوان IP المستهدف: ")

def اختراق_الهاتف_الذكي(ip):
    try:
        for port in range(1, 1025):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                print("المنفذ", port, "مفتوح")
                # هنا يمكنك إضافة رمز استغلال المنفذ المفتوح
                break
            else:
                print("المنفذ", port, "مغلق")
                # هنا يمكنك إضافة رمز البحث عن ثغرات والاستغلال المباشر للجهاز بالكامل

    except Exception as e:
        print("حدث خطأ:", e)

اختراق_الهاتف_الذكي(target_ip)
