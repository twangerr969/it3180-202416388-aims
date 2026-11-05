## Câu 1. Vì sao chuẩn bị phát hành trên `master` trước, không sửa trên nhánh `release`?

Việc chuẩn bị phát hành cần được thực hiện trên `master` vì đây là nhánh chứa các thay đổi đã được tích hợp từ những nhánh phát triển thông qua Pull Request. Do đó, `master` là cơ sở để tổng hợp và kiểm tra những thay đổi trước khi tạo một phiên bản phát hành.

Cụ thể, các công việc như cập nhật số phiên bản, bổ sung CHANGELOG và điều chỉnh thông tin hiển thị của chương trình được thực hiện trên nhánh riêng, sau đó tạo Pull Request để merge vào `master`. Khi các thay đổi đã được tích hợp, nhánh `release/labXX` mới được tạo từ `master`.

Cách làm này giúp:
- Đảm bảo phiên bản phát hành chứa những thay đổi đã được tích hợp và kiểm tra.
- Tuân thủ quy trình Pull Request, tránh chỉnh sửa trực tiếp trên nhánh release đã được bảo vệ.
- Giữ cho nhánh release đóng vai trò lưu trữ một baseline cụ thể, hạn chế những thay đổi không cần thiết.

## Câu 2. Vì sao `release/*` không merge ngược vào `master`? So sánh với GitFlow.

Trong Release Flow của bài thực hành, nhánh `release/*` được tạo từ `master` để lưu giữ trạng thái mã nguồn tại thời điểm phát hành. Sau khi được tạo, nhánh này đóng vai trò là baseline phục vụ nộp bài và bảo trì phiên bản tương ứng.

Nhánh `master` vẫn tiếp tục nhận các tính năng mới thông qua Pull Request. Vì vậy, nếu merge toàn bộ `release/*` ngược trở lại `master`, có thể đưa những thay đổi chỉ phục vụ quá trình phát hành hoặc bảo trì phiên bản cũ vào nhánh phát triển hiện tại, làm phức tạp lịch sử và luồng tích hợp.

Thay vào đó, khi cần sửa lỗi trên một phiên bản đã phát hành, ta sử dụng nhánh `hotfix/*` và đưa bản sửa đến những nhánh cần thiết theo quy trình của bài thực hành.

So sánh với GitFlow:
- **Release Flow trong bài thực hành:** sử dụng `master` làm nhánh phát triển chính; tạo `release/*` từ `master` để đóng băng phiên bản. Nhánh release không merge ngược vào master.
- **GitFlow:** thường sử dụng thêm nhánh `develop` để tích hợp tính năng. Nhánh `release` được tạo từ `develop`; sau khi hoàn tất phát hành, nhánh release thường được merge vào cả `main/master` và `develop` để đồng bộ trạng thái phát hành.

Như vậy, điểm khác biệt chính là cách tổ chức các nhánh và cách đồng bộ thay đổi sau phát hành. Release Flow của bài thực hành được đơn giản hóa để tập trung vào việc quản lý baseline và bảo trì nhiều phiên bản.

## Câu 3. Vì sao chọn phiên bản `1.0.0` mà không phải `0.4.0`?

Theo Semantic Versioning, phiên bản có cấu trúc `MAJOR.MINOR.PATCH`:
- `MAJOR`: tăng khi có thay đổi không tương thích ngược.
- `MINOR`: tăng khi bổ sung chức năng mới nhưng vẫn tương thích ngược.
- `PATCH`: tăng khi sửa lỗi nhưng không làm thay đổi tính tương thích.

Trong giai đoạn phát triển ban đầu, dự án sử dụng các phiên bản `0.1.0`, `0.2.0` và `0.3.0`. Theo quy ước SemVer, các phiên bản `0.y.z` thể hiện phần mềm vẫn đang trong giai đoạn phát triển ban đầu và chưa cam kết đầy đủ về tính ổn định của giao diện hoặc hành vi.

Sau ba bài thực hành đầu tiên, dự án đã tích lũy được các chức năng nền tảng như quản lý giỏ hàng, tìm kiếm DVD, tính toán giảm giá và xử lý các lỗi quan trọng. Vì vậy, Lab 04 sử dụng phiên bản `1.0.0` để đánh dấu một baseline phát hành chính thức đầu tiên, thay vì tiếp tục đánh số `0.4.0`.

Việc chuyển từ `0.3.0` lên `1.0.0` thể hiện sự chuyển đổi từ giai đoạn phát triển ban đầu sang một phiên bản được xem là baseline ổn định. Đây không đơn thuần là việc tăng số phiên bản theo số lượng bài thực hành.