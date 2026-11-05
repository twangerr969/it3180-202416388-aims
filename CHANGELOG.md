# Changelog

Tất cả những thay đổi đáng chú ý của dự án sẽ được ghi lại trong tệp này.

## [Unreleased]

## [1.1.0] - 2026-11-05

### Added
- Bổ sung chức năng sắp xếp DVD trong giỏ hàng theo tên.
- Bổ sung chức năng sắp xếp DVD trong giỏ hàng theo giá.
- Bổ sung chức năng tìm kiếm DVD theo thể loại.

## [1.0.0] - 2026-11-05

### Added
- Bổ sung chức năng tìm kiếm DVD theo tên.
- Bổ sung chức năng hiển thị thông tin giỏ hàng.
- Bổ sung thông báo tiếng Việt khi thêm DVD vào giỏ hàng.
- Bổ sung chức năng tính toán giá sau khi áp dụng giảm giá.
- Bổ sung sơ đồ Use Case vào tài liệu dự án.

### Fixed
- Sửa lỗi kiểm tra giới hạn số lượng DVD trong giỏ hàng, ngăn không cho thêm DVD vượt quá `MAX_NUMBERS_ORDERED`.
- Sửa lỗi tính tổng tiền sau giảm giá và kiểm tra tính hợp lệ của phần trăm giảm giá.
- Sửa lỗi xử lý trường hợp giỏ hàng rỗng khi hiển thị thông tin giỏ hàng.