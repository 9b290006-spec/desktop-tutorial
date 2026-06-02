import streamlit as st

# ==========================================================================
# 1. Streamlit 頁面核心設定 (必須是第一個 Streamlit 命令)
# ==========================================================================
st.set_page_config(
    page_title="Peter Tsai | 南台資訊有限公司",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================================================
# 2. Vibe Styling: 強行注入高質感黑金美學 CSS
# ==========================================================================
st.markdown("""
    <style>
        /* 載入奢華感英文字型 */
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600&family=Montserrat:wght@300;400&display=swap');

        /* 全域樣式覆蓋：底色全黑 */
        .stApp {
            background-color: #0A0A0A !important;
            color: #F5F5F7 !important;
            font-family: 'Montserrat', 'Noto Sans TC', sans-serif;
        }

        /* 隱藏 Streamlit 預設頂部裝飾線與選單 */
        #MainMenu, header, footer {visibility: hidden;}
        
        /* 高級黑金文字漸層效果 */
        .gold-text {
            background: linear-gradient(135deg, #F3E5AB 0%, #D4AF37 50%, #AA7C11 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-family: 'Cinzel', serif;
        }
        
        /* 標題區塊調整 */
        .hero-title {
            font-size: 3.8rem;
            letter-spacing: 6px;
            text-align: center;
            margin-top: 50px;
            margin-bottom: 10px;
        }
        
        .hero-subtitle {
            font-size: 1.3rem;
            letter-spacing: 5px;
            text-align: center;
            color: #8E8E93;
            margin-bottom: 40px;
            font-weight: 300;
        }

        .hero-slogan {
            font-size: 1.6rem;
            letter-spacing: 3px;
            text-align: center;
            color: #F5F5F7;
            font-style: italic;
            margin-bottom: 80px;
            font-family: 'Cinzel', serif;
        }

        /* 高級感框線卡片 */
        .luxury-card {
            background-color: #121212;
            border: 1px solid rgba(214, 175, 87, 0.2);
            padding: 35px;
            border-radius: 4px;
            margin-bottom: 25px;
            transition: all 0.4s ease;
        }
        
        .luxury-card:hover {
            border-color: rgba(214, 175, 87, 0.6);
            box-shadow: 0 10px 25px rgba(214, 175, 87, 0.05);
            transform: translateY(-3px);
        }

        .card-number {
            font-family: 'Cinzel', serif;
            color: #D4AF37;
            font-size: 1.1rem;
            margin-bottom: 10px;
            letter-spacing: 2px;
        }

        .card-title {
            font-size: 1.25rem;
            color: #F5F5F7;
            margin-bottom: 12px;
            letter-spacing: 1px;
            font-weight: 600;
        }

        .card-desc {
            color: #8E8E93;
            font-size: 0.95rem;
            line-height: 1.6;
            font-weight: 300;
        }

        /* 聯絡資訊元件 */
        .contact-label {
            font-size: 0.8rem;
            color: #8E8E93;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 2px;
        }
        .contact-value {
            font-size: 1.15rem;
            color: #F5F5F7;
            margin-bottom: 20px;
            letter-spacing: 1px;
        }

        /* 高級感客製化按鈕 */
        .fb-button-container {
            text-align: center;
            margin-top: 40px;
            margin-bottom: 80px;
        }
        
        .fb-gold-btn {
            display: inline-block;
            padding: 14px 45px;
            background: transparent;
            color: #D4AF37 !important;
            border: 1px solid #AA7C11;
            text-decoration: none !important;
            letter-spacing: 3px;
            font-size: 0.9rem;
            font-weight: 500;
            transition: all 0.4s ease;
        }
        
        .fb-gold-btn:hover {
            background: linear-gradient(135deg, #AA7C11, #D4AF37);
            color: #0A0A0A !important;
            box-shadow: 0 0 25px rgba(214, 175, 87, 0.35);
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================================================
# 3. Web Content 排版架構
# ==========================================================================

# --- HERO 主視覺區 ---
st.markdown('<h1 class="hero-title gold-text">Peter Tsai</h1>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">南台資訊有限公司 · 執行長</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-slogan">「以極致技術，淬鍊企業數位轉型的無限可能」</div>', unsafe_allow_html=True)

# 使用 Streamlit 的欄位切分大區塊
left_space, main_content, right_space = st.columns([1, 5, 1])

with main_content:
    
    # --- SECTION: 核心理念 ---
    st.markdown('<h2 class="gold-text" style="font-size:1.8rem; letter-spacing:3px; margin-bottom:25px;">領航者理念 / Executive Profile</h2>', unsafe_allow_html=True)
    st.markdown("""
        <div style="color: #A0A0A5; font-size: 1.05rem; line-height: 1.8; text-align: justify; margin-bottom: 60px; font-weight: 300;">
            作為南台資訊有限公司的執行長，Peter Tsai 帶領團隊專注於頂級網路資訊技術與企業數位轉型布局。
            我們打破傳統資訊外包的冰冷框架，將商業策略與前沿技術（雲端架構、資安防禦、大數據優化）完美融合，
            為每一家渴望跨越世代的企業，打造無懈可擊的數位資產護城河。
        </div>
    """, unsafe_allow_html=True)

    # --- SECTION: 專業服務項目 ---
    st.markdown('<h2 class="gold-text" style="font-size:1.8rem; letter-spacing:3px; margin-bottom:35px;">專業服務項目 / Corporate Services</h2>', unsafe_allow_html=True)
    
    # 建立 2x2 的網格服務卡片
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class="luxury-card">
                <div class="card-number">01 / ARCHITECTURE</div>
                <div class="card-title">企業級雲端架構設計</div>
                <div class="card-desc">客製化高可用性、彈性擴展的頂級雲端環境，協助企業流暢跨越傳統架構瓶頸，全面擁抱新世代算力。</div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class="luxury-card">
                <div class="card-number">02 / SECURITY</div>
                <div class="card-title">網路安全防禦與資安審計</div>
                <div class="card-desc">建構全方位主動式防護網，深度進行系統漏洞掃描、威脅情報分析與防禦部署，死守企業核心商業機密。</div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="luxury-card">
                <div class="card-number">03 / DEVELOPMENT</div>
                <div class="card-title">關鍵業務軟體客製開發</div>
                <div class="card-desc">深入企業原生商業邏輯，拒絕套版，研發直覺、精準、高吞吐量的專屬軟體與自動化生態系統。</div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class="luxury-card">
                <div class="card-number">04 / DATA SCIENCE</div>
                <div class="card-title">大數據分析與系統維運顧問</div>
                <div class="card-desc">清洗並提煉沉睡的數據價值，提供 24/7 全天候黑匣子級系統監控與極致優化，確保商務運作永不中斷。</div>
            </div>
        """, unsafe_allow_html=True)

    # --- SECTION: 聯絡資訊 ---
    st.markdown('<h2 class="gold-text" style="font-size:1.8rem; letter-spacing:3px; margin-top:50px; margin-bottom:35px; text-align:center;">聯絡事務所 / Contact Suite</h2>', unsafe_allow_html=True)
    
    c_col1, c_col2, c_col3 = st.columns(3)
    with c_col1:
        st.markdown('<div class="contact-label">Corporate Office</div><div class="contact-value">南台資訊有限公司</div>', unsafe_allow_html=True)
    with c_col2:
        st.markdown('<div class="contact-label">Direct Line</div><div class="contact-value">06-253-3131</div>', unsafe_allow_html=True)
    with c_col3:
        st.markdown('<div class="contact-label">Secure Email</div><div class="contact-value">chtsai@stust.edu.tw</div>', unsafe_allow_html=True)

    # 社交連結按鈕
    st.markdown("""
        <div class="fb-button-container">
            <a href="https://www.facebook.com/keepbusytsai" target="_blank" class="fb-gold-btn">
                CONNECT VIA FACEBOOK
            </a>
        </div>
    """, unsafe_allow_html=True)

    # --- FOOTER ---
    st.markdown("""
        <div style="text-align:center; color:#444; font-size:0.8rem; letter-spacing:1px; border-top:1px solid rgba(214,175,87,0.05); padding-top:30px; margin-bottom:30px;">
            © 2026 SOUTHERN TAIWAN INFORMATION CO., LTD. ALL RIGHTS RESERVED. POWERED BY STREAMLIT & VIBE.
        </div>
    """, unsafe_allow_html=True)