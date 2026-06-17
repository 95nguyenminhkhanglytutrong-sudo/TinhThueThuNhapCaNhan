import streamlit as st

# Tiêu đề ứng dụng
st.title("💰 Ứng dụng tính Thuế Thu Nhập Cá Nhân")

# Nhập dữ liệu
thu_nhap = st.number_input(
    "Nhập thu nhập chịu thuế hàng tháng (triệu đồng)",
    min_value=0.0,
    value=20.0
)

# Nút tính toán
if st.button("Tính thuế"):

    tax = 0

    # Tính thuế theo biểu thuế lũy tiến từng phần
    if thu_nhap <= 5:
        tax = thu_nhap * 0.05

    elif thu_nhap <= 10:
        tax = 5 * 0.05 + (thu_nhap - 5) * 0.10

    elif thu_nhap <= 18:
        tax = 5 * 0.05 + 5 * 0.10 + (thu_nhap - 10) * 0.15

    elif thu_nhap <= 32:
        tax = 5 * 0.05 + 5 * 0.10 + 8 * 0.15 + (thu_nhap - 18) * 0.20

    elif thu_nhap <= 52:
        tax = (
            5 * 0.05 +
            5 * 0.10 +
            8 * 0.15 +
            14 * 0.20 +
            (thu_nhap - 32) * 0.25
        )

    elif thu_nhap <= 80:
        tax = (
            5 * 0.05 +
            5 * 0.10 +
            8 * 0.15 +
            14 * 0.20 +
            20 * 0.25 +
            (thu_nhap - 52) * 0.30
        )

    else:
        tax = (
            5 * 0.05 +
            5 * 0.10 +
            8 * 0.15 +
            14 * 0.20 +
            20 * 0.25 +
            28 * 0.30 +
            (thu_nhap - 80) * 0.35
        )

    thu_nhap_sau_thue = thu_nhap - tax

    st.success("Kết quả tính toán")

    st.write(f"📌 Thu nhập chịu thuế: **{thu_nhap:,.2f} triệu đồng**")
    st.write(f"📌 Thuế TNCN phải nộp: **{tax:,.2f} triệu đồng**")
    st.write(f"📌 Thu nhập sau thuế: **{thu_nhap_sau_thue:,.2f} triệu đồng**")
