import socket

target_ip = input("ادخل عنوان الآي بي المستهدف: ")

def اخترق_أندرويد(ip):
    try:
        # إنشاء كائن المأخذ
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        # الاتصال بالآي بي والمنفذ المستهدف
        s.connect((ip, 22))

        # إرسال بعض الأوامر الخبيثة إلى الجهاز الأندرويد
        s.send(b'echo "لقد تم اختراقك"')

        # استقبال الرد من الجهاز
        response = s.recv(1024)

        print("الرد من الجهاز:", response.decode())
        print("بوووم! تم اختراق الجهاز الأندرويد بنجاح!")

    except Except
