import platform
import subprocess

def check_command(cmd):
    try:
        result = subprocess.run([cmd, '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=2)
        if result.returncode == 0: return f"✅ Đã cài ({result.stdout.splitlines()[0].strip()})"
    except: pass
    return "❌ Chưa cài"

print("⏳ Đang quét cấu hình máy tính của bạn...")
detailed_os = f"Windows {platform.win32_ver()[0]} (Build {platform.win32_ver()[1]})"
tools = {"Git": "git", "Python": "py", "Pip": "pip"}
tool_status = {name: check_command(cmd) for name, cmd in tools.items()}

markdown_output = f"""
### 📋 THÔNG TIN MÁY TÍNH CỦA BẠN:
- **Hệ điều hành:** {detailed_os}
- **Kiến trúc Chip:** {platform.machine()}
- **Trạng thái Git:** {tool_status['Git']}
- **Trạng thái Python:** {tool_status['Python']}
"""
print(markdown_output)
with open("ai_context_ready.txt", "w", encoding="utf-8") as f:
    f.write(markdown_output)
print("🎉 Xong! Đã lưu kết quả ra file ai_context_ready.txt ngoài Desktop.")