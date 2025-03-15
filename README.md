** Thông tin sinh viên **
# Sinh viên:
 - Họ và tên : Bùi Như Ý
 - MSSV : 22728001
 - STT: 78

** Mô tả cài đặt project
 Blog có hai tác nhân chính:

- Actor: Người viết bài

- User: Người đọc bài và bình luận

Các chức năng chính bao gồm:

- Đăng nhập / Đăng ký tài khoản

- Tạo, chỉnh sửa, xóa bài viết

- Bình luận trên bài viết

- Hiển thị bài viết kèm hình ảnh ngẫu nhiên từ Picsum Photos

Giao diện: Layout 1 (Single Column - Một Cột)

Chức năng mở rộng: Trang dashboard thể hiện thông tin trang blog
### Cài đặt Project

Yêu cầu hệ thống:

Python 3.8+

Flask

SQLite3

Flask-Login, Flask-SQLAlchemy, Flask-WTF

1. Clone repository từ GitHub:
   ```
   git clone https://github.com/nhuy152204/ptud-gk-de-1
   ```
2. Di chuyển đến thư mục chính
   ```
    cd ptud-gk-de-1
   ```

Script này sẽ:

- Tạo môi trường ảo Python

- Cài đặt thư viện Flask
3. Chạy script cài đặt:
   ```
    .\setup.bat
   ```
   Script này sẽ:
   - Tạo môi trường ảo Python
   - Cài đặt thư viện Flask

4. Khôi phục dữ liệu (bài viết và hình ảnh):
     ``` 
   .\restore-data.bat
      ```
   Script này sẽ:
   - Khôi phục cơ sở dữ liệu từ bản sao lưu
   - Khôi phục hình ảnh từ thư mục data

5. Chạy ứng dụng:
   ```
   .\run.bat
   ```
- Ứng dụng sẽ chạy tại: http://localhost:5000
*** Lưu ý cho người sử dụng:

Sau khi clone repository, chạy lệnh sau để cài đặt hệ thống:

.\setup.bat

Khôi phục dữ liệu để có bài viết và hình ảnh đầy đủ:

.\restore-data.bat

Chạy ứng dụng:
.\run.bat

