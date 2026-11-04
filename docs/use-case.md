# AIMS-mini Use Case Diagram

## Actors
- Customer: Người sử dụng hệ thống.

## Use Cases
- Add DVD to cart: Thêm DVD vào giỏ hàng.
- Remove DVD from cart: Xóa DVD khỏi giỏ hàng.
- View cart: Xem danh sách DVD trong giỏ hàng.
- Calculate total cost: Tính tổng tiền giỏ hàng.
- Search DVD by title: Tìm kiếm DVD theo tiêu đề.

## Use Case Diagram

```mermaid
flowchart TD
    Customer([Customer])

    AddDVD((Add DVD to cart))
    RemoveDVD((Remove DVD from cart))
    ViewCart((View cart))
    Calculate((Calculate total cost))
    Search((Search DVD by title))

    Customer --> AddDVD
    Customer --> RemoveDVD
    Customer --> ViewCart
    Customer --> Calculate
    Customer --> Search