# Bộ Kiểm Thử Đăng Nhập Bằng Selenium

Dự án này bao gồm bộ bài kiểm thử viết bằng Python nhằm xác minh chức năng đăng nhập của trang [Herokuapp Secure Login Page](https://the-internet.herokuapp.com/login). Các bài kiểm thử sử dụng thư viện `Selenium` và `pytest`, bao gồm các kịch bản đăng nhập thành công, thất bại, và đăng xuất.

## Yêu Cầu

Đảm bảo các thành phần sau đã được cài đặt trên hệ thống trước khi chạy các bài kiểm thử:

1. **Python** (Phiên bản 3.8 trở lên)
2. **Google Chrome** (Phiên bản mới nhất)
3. **ChromeDriver** (Đảm bảo tương thích với phiên bản Chrome của bạn)
4. **Thư viện Python cần thiết**:
   - `selenium`
   - `pytest`
   - `pytest-html`

Cài đặt các thư viện bằng lệnh:

```bash
pip install selenium pytest pytest-html
```

## Cấu Trúc Thư Mục

```
project/
│
├── test_login.py          # Tệp chính chứa bài kiểm thử
├── README.md              # Tài liệu hướng dẫn (tệp này)
├── requirements.txt       # Danh sách phụ thuộc Python

```

## Cách Sử Dụng

### Chạy Bài Kiểm Thử

1. **Clone repository** hoặc lưu script trong một thư mục.
2. **Thiết lập đường dẫn WebDriver**:
   - Cập nhật đường dẫn đến tệp `chromedriver.exe` trong hàm `setup_driver`:
     ```python
     chrome_service = Service("D:/chromedriver-win64/chromedriver-win64/chromedriver.exe")
     ```
3. Chạy bài kiểm thử bằng lệnh:
   ```bash
   pytest test_login.py
   ```

4. **Tạo báo cáo HTML** (tuùy chọn):
   ```bash
   pytest --html=report.html
   ```

### Các Bài Kiểm Thử

Bộ bài kiểm thử bao gồm các tình huống sau:

1. **`test_login_success`**:
   - Kiểm tra đăng nhập thành công với thông tin đăng nhập hợp lệ.
   - Thông báo mong đợi: `"You logged into a secure area!"`

2. **`test_login_failure`**:
   - Kiểm tra đăng nhập thất bại với thông tin đăng nhập không hợp lệ.
   - Thông báo mong đợi: `"Your username is invalid!"`

3. **`test_logout`**:
   - Xác minh chức năng đăng xuất sau khi đăng nhập thành công.
   - Thông báo mong đợi khi đăng xuất: `"You logged out of the secure area!"`

## Logger

Script sử dụng thư viện `logging` của Python để ghi lại chi tiết thông tin thực thi, bao gồm:

- Khởi tạo và kết thúc WebDriver.
- Các bước thực thi và kết quả mong đợi.
- Bất kỳ lỗi nào phát sinh trong quá trình chạy bài kiểm thử.

Logs được in ra console để hỗ trợ debug thực tế.

## Lưu ý

- **Đường dẫn WebDriver**: Đảm bảo đường dẫn đến tệp `chromedriver.exe` phù hợp với cài đặt trên hệ thống.
- **Timeout**: Script sử dụng chờ tự động với thời gian chờ 10 giây để đảm bảo các phần tử được tải trước khi thao tác.
- **Tuỳ chỉnh bài kiểm thử**: Có thể thay đổi lớp `Locators` hoặc cài đặt WebDriver để phù hợp với môi trường khác.

## Giấy Phép

Dự án này được cấp phép theo giấy phép MIT.

## Link ChatGPT

https://chatgpt.com/share/678633a9-293c-800f-af9f-0a6565e78145
