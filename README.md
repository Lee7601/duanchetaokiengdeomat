# Test any system before use  AI , to give AI agent best answers base on hardware and version of software it uses. 
# 🛠️ AI Environment Surveyor (Chặn đứng AI đoán mò cấu hình)

Một công cụ nhỏ bằng Python giúp tự động quét cấu hình phần cứng, hệ điều hành và các phần mềm sẵn có trên máy tính của bạn, xuất ra định dạng Markdown chuẩn để nạp làm ngữ cảnh (Context) cho AI (ChatGPT, Gemini, Claude...).

## 🛑 Vấn đề giải quyết
AI thường hướng dẫn sai, đưa ra các câu lệnh lỗi thời hoặc lệch hệ điều hành (ví dụ máy chạy chip Apple M1 nhưng đưa lệnh cài của chip Intel, hoặc máy Windows nhưng đưa lệnh của Linux) do **không được khảo sát cấu hình máy trước khi trả lời**.

## 🚀 Cách sử dụng cực nhanh

1. Tải tệp `survey.py` về máy tính của bạn.
2. Mở Terminal / Command Prompt tại thư mục chứa tệp và chạy lệnh:
   ```bash
   python survey.py   # Hoặc python3 survey.py trên Mac/Linux
