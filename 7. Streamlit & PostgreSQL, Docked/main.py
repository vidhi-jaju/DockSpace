import streamlit as st
import psycopg2

# Custom CSS for a professional look
st.markdown("""
    <style>
        body {
            background-color: #f4f6f9;
            font-family: 'Arial', sans-serif;
        }
        .title {
            color: #333;
            font-size: 36px;
            font-weight: bold;
        }
        .subtitle {
            color: #555;
            font-size: 24px;
            margin-bottom: 20px;
        }
        .card {
            background-color: #ffffff;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .data {
            font-size: 18px;
            line-height: 1.6;
            color: #444;
        }
        .data span {
            color: #0073e6;
        }
        .error {
            color: #e74c3c;
        }
        .success {
            color: #2ecc71;
        }
        .warning {
            color: #f39c12;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 PostgreSQL Connection with Streamlit through Docker")

DB_HOST = "my_postgres_container"
DB_NAME = "testdb"
DB_USER = "tarak"
DB_PASSWORD = "secret"

def fetch_data():
    try:
        st.write("🔄 Connecting to database...")
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        st.write("<p class='success'>✅ Connected to PostgreSQL!</p>", unsafe_allow_html=True)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM passengers;")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    except Exception as e:
        st.write(f"<p class='error'>❌ Database connection error: {str(e)}</p>", unsafe_allow_html=True)
        return []

data = fetch_data()

if data:
    st.subheader("📊 Data Retrieved:")
    for row in data:
        st.markdown(f"""
            <div class="card">
                <p class="data"><strong>🆔 ID:</strong> {row[0]} <strong>🏷 Name:</strong> {row[1]} <strong>📍 Location:</strong> {row[2]}</p>
            </div>
        """, unsafe_allow_html=True)
else:
    st.markdown("<p class='warning'>⚠️ No data found in the `passengers` table.</p>", unsafe_allow_html=True)


