import socket

# تحديد عنوان IP ومنفذ الهدف
target_ip = 'عنوان_IP_الهدف'
target_port = 12345  # افتراضي: 12345

# إنشاء كائن socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# الاتصال بالجهاز الهدف
client_socket.connect((target_ip, target_port))

# إرسال بيانات
client_socket.send(b'Hello, Android!')

# استقبال الرد من الجهاز الهدف
response = client_socket.recv(1024)
print("Response from Android:", response.decode())

# إغلاق الاتصال
client_socket.close()
