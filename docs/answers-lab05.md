1. Ưu, nhược điểm của Upstream First so với Release First?

**Upstream First** là cách tiếp cận trong đó bản sửa lỗi được thực hiện và tích hợp vào nhánh phát triển chính (`master`) trước, sau đó mới được lan truyền sang các nhánh release cần thiết bằng `cherry-pick`.

Ưu điểm:
- Nhánh chính là nơi tập trung bản sửa gốc, giúp duy trì một nguồn thay đổi thống nhất.
- Lỗi được xử lý và kiểm thử trên phiên bản phát triển mới nhất trước khi lan truyền.
- Tránh tình trạng các nhánh release tự phát triển những bản sửa khác nhau cho cùng một lỗi.
- Phù hợp với dự án có nhiều nhánh release và quy trình phát triển liên tục.

Nhược điểm:
- Người dùng đang sử dụng phiên bản cũ có thể phải chờ bản sửa được chuyển sang nhánh release.
- Việc cherry-pick có thể phát sinh xung đột nếu mã nguồn giữa nhánh chính và nhánh release đã khác nhau nhiều.
- Bản sửa được kiểm thử trên phiên bản mới nhất chưa chắc tương thích hoàn toàn với phiên bản cũ.

**Release First** là cách tiếp cận trong đó bản sửa được thực hiện trên nhánh release bị ảnh hưởng trước, sau đó được lan truyền về `master` và các nhánh release khác bằng `cherry-pick`.

Ưu điểm:
- Có thể ưu tiên khắc phục nhanh lỗi trên phiên bản đang được sử dụng hoặc đã phát hành.
- Bản sửa được phát triển và kiểm thử trực tiếp trong môi trường mã nguồn có lỗi.
- Phù hợp với quy trình bảo trì nhiều phiên bản đã phát hành song song.

Nhược điểm:
- Phải chủ động lan truyền bản sửa sang các nhánh khác, dễ bỏ sót nếu không kiểm toán.
- Có thể phát sinh xung đột khi cherry-pick do các nhánh đã phát triển khác nhau.
- Nếu không kiểm soát tốt, các nhánh có thể chứa những phiên bản sửa lỗi không đồng nhất.

**Kết luận:** Upstream First phù hợp khi ưu tiên duy trì một nguồn phát triển chính thống và sau đó phân phối bản sửa xuống các phiên bản cũ. Release First phù hợp khi cần ưu tiên khắc phục lỗi trên một phiên bản đã phát hành. Với bài thực hành này, Release Flow của học phần sử dụng Release First: tạo nhánh hotfix từ `release/*`, sau đó lan truyền bản sửa sang `master` và các nhánh release bị ảnh hưởng.

2. Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F sẽ phát hiện?

Có thể sử dụng lệnh:

```bash
git cherry -v origin/release/lab05 origin/master
```

Lệnh này so sánh các commit trên `origin/master` với `origin/release/lab05`, dựa trên nội dung thay đổi (patch), chứ không chỉ dựa vào mã SHA của commit.

- Dấu `+`: Commit trên `master` chưa có bản thay đổi tương đương trên `release/lab05`.
- Dấu `-`: Đã tìm thấy một commit có nội dung thay đổi tương đương trên `release/lab05`, dù mã SHA có thể khác.

Nếu bản sửa hotfix đã được đưa vào `master` nhưng bị bỏ quên trên `release/lab05`, commit sửa lỗi sẽ xuất hiện với dấu `+`. Đây là dấu hiệu cần kiểm tra và lan truyền bản sửa sang nhánh release còn thiếu.

Trước khi kiểm tra, nên cập nhật thông tin từ remote:

```bash
git fetch origin
git cherry -v origin/release/lab05 origin/master
```

**Lưu ý:** Lệnh này chỉ phát hiện sự khác biệt về patch giữa hai nhánh; cần đối chiếu nội dung commit để xác định chính xác đó có phải bản sửa hotfix bị thiếu hay không.