import streamlit as st

# Tiêu đề ứng dụng
st.title("App tính Thuế Thu Nhập Cá Nhân Việt Nam đề tài 6 Nguyễn Minh Khang")

# Nhập dữ liệu
thu_nhap = st.number_input(
    "Nhập thu nhập chịu thuế hàng tháng (triệu đồng)",
    min_value=0.0,
    value=20.0
)

# Nút tính toán
if st.button("Tính thuế"):

    tax = 0

   # Tính thuế theo biểu thuế mới
if thu_nhap <= 5:
    tax = thu_nhap * 0.02

elif thu_nhap <= 10:
    tax = 5 * 0.02 + (thu_nhap - 5) * 0.04

elif thu_nhap <= 18:
    tax = 5 * 0.02 + 5 * 0.04 + (thu_nhap - 10) * 0.06

elif thu_nhap <= 32:
    tax = 5 * 0.02 + 5 * 0.04 + 8 * 0.06 + (thu_nhap - 18) * 0.08

elif thu_nhap <= 52:
    tax = (
        5 * 0.02 +
        5 * 0.04 +
        8 * 0.06 +
        14 * 0.08 +
        (thu_nhap - 32) * 0.10
    )

elif thu_nhap <= 80:
    tax = (
        5 * 0.02 +
        5 * 0.04 +
        8 * 0.06 +
        14 * 0.08 +
        20 * 0.10 +
        (thu_nhap - 52) * 0.12
    )

else:
    tax = (
        5 * 0.02 +
        5 * 0.04 +
        8 * 0.06 +
        14 * 0.08 +
        20 * 0.10 +
        28 * 0.12 +
        (thu_nhap - 80) * 0.15
    )

    thu_nhap_sau_thue = thu_nhap - tax

    st.success("Kết quả tính toán")

    st.write(f"📌 Thu nhập chịu thuế: **{thu_nhap:,.2f} triệu đồng**")
    st.write(f"📌 Thuế TNCN phải nộp: **{tax:,.2f} triệu đồng**")
    st.write(f"📌 Thu nhập sau thuế: **{thu_nhap_sau_thue:,.2f} triệu đồng**")
