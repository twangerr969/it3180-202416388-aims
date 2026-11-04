1. Merge base là gì?

Merge base là commit tổ tiên chung gần nhất của hai nhánh Git. Git sử dụng commit này làm cơ sở để so sánh và xác định những thay đổi được thực hiện trên mỗi nhánh khi tiến hành merge.

Ví dụ, hai nhánh `feature/A` và `feature/B` được phát triển từ cùng một commit `C`. Khi đó, `C` là merge base của hai nhánh.

Khi thực hiện merge, Git so sánh nội dung tại merge base với những thay đổi trên hai nhánh để xác định cách kết hợp chúng. Nếu hai nhánh cùng chỉnh sửa một đoạn mã theo những cách không thể tự động kết hợp, Git sẽ phát sinh merge conflict và yêu cầu lập trình viên giải quyết thủ công.

Trong Lab 03, hai nhánh `feature/vietnamese-messages` và `feature/show-added-title` cùng chỉnh sửa dòng lệnh trong `aims/cart.py`. Khi tích hợp nhánh thứ hai sau nhánh thứ nhất, Git phát hiện xung đột tại vị trí này. Đây là ví dụ về tình huống cần xử lý conflict khi kết hợp những thay đổi phát triển song song.

2. Vì sao master/release/* phải dùng revert thay vì reset?

`master` và `release/*` là những nhánh quan trọng, được sử dụng để tích hợp thay đổi hoặc lưu trữ phiên bản ổn định. Các commit trên những nhánh này thường đã được chia sẻ với nhiều thành viên hoặc được sử dụng làm cơ sở cho những công việc tiếp theo. Vì vậy, việc hoàn tác cần đảm bảo lịch sử thay đổi không bị viết lại.

Hai phương pháp hoàn tác phổ biến là `git reset` và `git revert`:

- `git reset`: Di chuyển con trỏ nhánh về một commit trước đó. Tùy chọn được sử dụng, các thay đổi có thể được giữ trong staging, working directory hoặc bị loại bỏ. Thao tác này có thể viết lại lịch sử commit.
- `git revert`: Tạo một commit mới có nội dung đảo ngược những thay đổi của commit được chỉ định. Các commit cũ vẫn được giữ nguyên trong lịch sử.

Nếu sử dụng `git reset` trên nhánh đã chia sẻ, lịch sử giữa máy cá nhân và remote có thể không còn đồng nhất, gây khó khăn khi các thành viên đồng bộ mã nguồn.

Ngược lại, `git revert` bảo toàn lịch sử đã chia sẻ, đồng thời ghi nhận rõ ràng cả thay đổi ban đầu và thao tác hoàn tác. Vì vậy, đây là phương pháp phù hợp hơn đối với các nhánh dùng chung như `master` và `release/*`.

Trong Lab 03, lệnh sau được sử dụng để hoàn tác merge commit `d9d2c6a`:

```bash
git revert -m 1 d9d2c6a
```

Tham số `-m 1` chỉ định parent thứ nhất làm mainline khi hoàn tác merge commit. Kết quả là Git tạo commit mới `59da714` để đảo ngược thay đổi được đưa vào từ PR #12 mà không xóa commit cũ khỏi lịch sử.

Thay đổi sau đó được đưa vào `master` thông qua Pull Request.