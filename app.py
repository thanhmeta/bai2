import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cấu hình ứng dụng
st.set_page_config(page_title="Báo cáo Doanh Thu", page_icon="📊", layout="wide")

# Tiêu đề ứng dụng
st.title("📊 Báo cáo Doanh Thu Hàng Tháng")

# Đọc dữ liệu
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("sales_data.csv")  # Đảm bảo file có trong thư mục
        return df
    except FileNotFoundError:
        st.error("⚠️ Không tìm thấy file `sales_data.csv`. Hãy chắc chắn rằng file nằm trong thư mục chạy ứng dụng!")
        return None

df = load_data()

# Nếu dữ liệu hợp lệ, tiếp tục hiển thị
if df is not None:
    # Hiển thị dữ liệu
    st.subheader("📋 Dữ liệu doanh thu")
    st.dataframe(df)

    # Biểu đồ doanh thu theo tháng
    st.subheader("📈 Biểu đồ Doanh Thu")

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df["Month"], df["Revenue"], marker="o", linestyle="-", color="blue", label="Doanh thu")
    ax.set_xlabel("Tháng")
    ax.set_ylabel("Doanh thu ($)")
    ax.set_title("Biểu đồ Doanh Thu Theo Tháng")
    ax.grid(True)
    ax.legend()

    # Hiển thị biểu đồ trên Streamlit
    st.pyplot(fig)

    # Tính tổng doanh thu và doanh thu trung bình
    total_revenue = df["Revenue"].sum()
    avg_revenue = df["Revenue"].mean()

    # Hiển thị thông tin thống kê
    st.subheader("📊 Tổng Quan Doanh Thu")
    col1, col2 = st.columns(2)

    with col1:
        st.metric("📌 Tổng doanh thu", f"${total_revenue:,}")

    with col2:
        st.metric("📌 Doanh thu trung bình", f"${avg_revenue:,.2f}")

    # Sidebar chọn tháng để xem chi tiết
    selected_month = st.sidebar.selectbox("🔍 Chọn tháng để xem chi tiết", df["Month"])
    selected_revenue = df[df["Month"] == selected_month]["Revenue"].values[0]
    st.sidebar.write(f"💰 Doanh thu tháng {selected_month}: **${selected_revenue:,}**")

    st.success("✅ Phân tích doanh thu hoàn tất! 🎉")

