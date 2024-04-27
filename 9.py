import socket

target_ip = input("أدخل عنوان الآي بي المستهدف: ")

def اختراق_أندرويد(ip):
    try:
        # إنشاء كائن مأخذ
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        # الاتصال بعنوان الآي بي والمنفذ المستهدف
        s.connect((ip, 22))

        print("تم التوصيل بنجاح!")

    except Exception as e:
        print("حدث خطأ:", e)

اختراق_أندرويد(target_ip)
