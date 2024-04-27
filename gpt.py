import socket

target_ip = input("أدخل عنوان IP المستهدف: ")

def اختراق_أندرويد(ip):
    try:
        # إنشاء كائن للمأخذ
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        # الاتصال بالعنوان IP والمنفذ المستهدف
        s.connect((ip, 22))

        # إرسال الأوامر الخبيثة إلى الجهاز الأندرويد
        s.send(b'echo "لقد تم اختراقك"')

        # استقبال الرد من الجهاز
        response = s.recv(1024)

        print("الرد من الجهاز:", response.decode())
        print("تم اختراق الجهاز الأندرويد بنجاح!")

    except Exception as e:
        print("حدث خطأ:", e)

اختراق_أندرويد(target_ip)
