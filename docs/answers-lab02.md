1. Vì sao phải đồng bộ `master` trước khi PR?
Đồng bộ nhánh làm việc với `master` nhằm đảm bảo nhánh đang phát triển chứa những thay đổi mới nhất của dự án trước khi tích hợp.
Nếu không đồng bộ, nhánh làm việc có thể dựa trên phiên bản mã nguồn cũ, dẫn đến:
- Bỏ sót những thay đổi mới được tích hợp vào `master`.
- Phát sinh xung đột khi merge Pull Request.
- Các thay đổi riêng lẻ có thể hoạt động bình thường nhưng không tương thích với phiên bản mới nhất của dự án.
Vì vậy, cần sử dụng `git fetch` để cập nhật thông tin từ remote, sau đó tích hợp `origin/master` vào nhánh làm việc và kiểm thử lại trước khi tạo Pull Request.

2. Khi nào không được rebase?
Không nên rebase những commit đã được chia sẻ công khai và có khả năng được người khác sử dụng làm cơ sở phát triển.

Nguyên nhân là rebase tạo ra các commit mới với mã SHA khác so với commit ban đầu, mặc dù nội dung thay đổi có thể giống nhau. Điều này làm thay đổi lịch sử commit và có thể gây khó khăn khi đồng bộ với những người đang sử dụng lịch sử cũ.

Do đó:
- Có thể rebase nhánh cá nhân chưa được chia sẻ để làm lịch sử commit gọn gàng hơn.
- Không nên rebase các nhánh dùng chung hoặc những commit đã được người khác dựa vào, trừ khi cả nhóm thống nhất và phối hợp xử lý.

3. `feature/*` khác `topic/*` ra sao?
Cả hai đều là quy ước đặt tên nhánh để phân chia công việc, nhưng thường được sử dụng cho các mục đích khác nhau:

- **`feature/*`**: Dùng để phát triển một chức năng cụ thể của phần mềm. Ví dụ: `feature/cart-print` bổ sung chức năng hiển thị giỏ hàng và `feature/search-by-title` bổ sung chức năng tìm kiếm DVD theo tiêu đề.
- **`topic/*`**: Dùng cho một chủ đề hoặc hạng mục công việc cụ thể, thường liên quan đến tài liệu, cấu hình hoặc các công việc hỗ trợ dự án. Ví dụ: `topic/pr-template` bổ sung mẫu mô tả Pull Request và `topic/use-case-diagram` bổ sung tài liệu sơ đồ Use Case.

Như vậy, `feature/*` tập trung vào việc phát triển chức năng, còn `topic/*` có phạm vi rộng hơn, dùng để tổ chức các công việc theo từng chủ đề. Đây là quy ước đặt tên được sử dụng trong Lab 02, không phải sự phân biệt bắt buộc của Git.