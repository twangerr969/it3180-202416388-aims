1. Cấu hình --global được lưu ở đâu? Khác gì so với --local?
- Cấu hình --global được lưu trong file ~/.gitconfig và áp dụng mặc định cho tất cả repository của người dùng hiện tại. Trong khi đó, --local được lưu tại .git/config của từng repository và chỉ có hiệu lực trong repository đó. Khi cùng một thuộc tính được cấu hình ở cả hai cấp, Git ưu tiên giá trị --local.
2. Vì sao dùng git mv?
- Sử dụng git mv giúp thao tác di chuyển hoặc đổi tên file rõ ràng, thuận tiện và tự động đưa thay đổi vào Staging Area. Điều này giúp hạn chế việc quên stage file cũ hoặc file mới, đồng thời thuận tiện cho việc theo dõi lịch sử thay đổi trong quá trình refactor.
3. release/lab01 có phải baseline?
- Có. Nhánh release/lab01 đóng vai trò baseline, đánh dấu trạng thái mã nguồn đã hoàn thành và được kiểm tra tại thời điểm kết thúc Lab 01. Nhánh này giúp lưu giữ một mốc phiên bản ổn định để phục vụ việc đối chiếu, kiểm tra và quản lý cấu hình phần mềm.
4. Vì sao không commit thẳng master dù làm một mình?
- Dù làm việc một mình, không nên commit trực tiếp vào master đối với những thay đổi lớn như refactor. Việc phát triển trên nhánh riêng và tích hợp thông qua Pull Request giúp bảo vệ tính ổn định của nhánh chính, tạo cơ hội kiểm tra mã nguồn trước khi merge và lưu lại lịch sử thay đổi rõ ràng. Đồng thời, quy trình này giúp hình thành thói quen quản lý cấu hình chuyên nghiệp.
