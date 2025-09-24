import time
import requests
import datetime as dt
import pytz
import os
import pandas as pd
import streamlit as st
from streamlit.components.v1 import iframe

import streamlit as st
import streamlit.components.v1 as components

# ==== Ohara Miniapps ====
OHARA_APPS = {
    "Python 101": {
        "url": "https://ohara.ai/mini-apps/be992dff-155e-4182-a55a-923ac2b3a2ca?utm_source=learnpy",
        "title": "📖 Python 101"
    },
    "Control Flow & Logic": {
        "url": "https://ohara.ai/mini-apps/8ed157b1-9d51-44fa-bafd-405b7e99ff8e?utm_source=learnpy",
        "title": "🔀 Control Flow & Logic"
    },
    "Data Structures": {
        "url": "https://ohara.ai/mini-apps/miniapp_cmffptu29011cb3lkcmx6h3co?utm_source=learnpy",
        "title": "📦 Data Structures"
    },
    "Functions & Modules": {
        "url": "https://ohara.ai/mini-apps/miniapp_cmffqhjpu0173b3lkbvhh7arq?utm_source=learnpy",
        "title": "🛠️ Functions & Modules"
    },
    "Object-Oriented Programming (OOP)": {
        "url": "https://ohara.ai/mini-apps/miniapp_cmffs5rj50oz18nlk6ogi2lmp?utm_source=learnpy",
        "title": "🧱 Object-Oriented Programming (OOP)"
    },
    "Python for Data": {
        "url": "https://ohara.ai/mini-apps/e33686f2-bdec-4043-b683-0fd4507979b2?utm_source=learnpy",
        "title": "📊 Python for Data"
    },
    "Python for Web & API": {
        "url": "https://ohara.ai/mini-apps/0c47e8dd-0310-4bf6-8e02-c97612856385?utm_source=learnpy",
        "title": "🌐 Python for Web & API"
    },
    "Python for AI/ML": {
        "url": "https://ohara.ai/mini-apps/6a9f756b-573c-442c-9544-792660d7a86a?utm_source=learnpy",
        "title": "🤖 Python for AI/ML"
    },
    "Final Project": {
        "url": "https://ohara.ai/mini-apps/e86a5136-f96f-4d52-af61-8de234ed7686?utm_source=learnpy",
        "title": "🎓 Final Project"
    }
}

import streamlit as st
import streamlit.components.v1 as components

def iframe(src, height=720, width="100%", hide_top=0, hide_bottom=0, title=None):
    if title:
        st.markdown(f"<h3>{title}</h3>", unsafe_allow_html=True)

    # Hitung tinggi iframe yang sebenarnya
    iframe_height = height + hide_top + hide_bottom
    # Hitung posisi top iframe
    top_offset = -hide_top

    st.markdown(f"""
        <div style="height:{height}px; 
                    overflow:hidden; 
                    position:relative;">
            <iframe src="{src}" 
                    width="{width}" 
                    height="{iframe_height}px" 
                    frameborder="0"
                    style="position:relative; top:{top_offset}px;">
            </iframe>
        </div>
    """, unsafe_allow_html=True)

def embed_lab(url: str, title: str = "", hide_top: int = 72, hide_bottom: int = 0, height: int = 720):
    if title:
        st.markdown(f"### {title}", unsafe_allow_html=True)

    # Tinggi iframe yang sebenarnya
    iframe_height = height + hide_top + hide_bottom
    # Offset untuk menyembunyikan bagian atas
    top_offset = -hide_top
    
    # Menggunakan components.html dengan logika yang sudah diperbaiki
    components.html(f"""
      <div style="position:relative;width:100%;height:{height}px;overflow:hidden;border-radius:12px;">
        <div id="loader"
             style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
                    font-weight:600;opacity:.6;transition:opacity .3s ease">
          Loading module…
        </div>

        <iframe id="ohara" src="{url}"
          style="position:absolute; top:{top_offset}px; left:0;
                 width:100%; height:{iframe_height}px;
                 border:0; border-radius:12px; overflow:hidden"></iframe>
      </div>

      <script>
        const ifr = document.getElementById('ohara');
        ifr.addEventListener('load', () => {{
          const l = document.getElementById('loader');
          if (l) {{
            l.style.opacity = 0;
            setTimeout(() => l.style.display = 'none', 300);
          }}
        }});
      </script>
    """, height=height)
    
def embed_cropped(
    url: str,
    hide_px: int = 56,
    height: int = 720,
    hide_bottom: int = 100,
    title: str | None = None
):
    """
    Embed iframe dengan crop atas (hide_px) dan crop bawah (hide_bottom).
    """
    if title:
        st.markdown(f"### {escape(title)}", unsafe_allow_html=True)

    iframe_height = height + hide_px + hide_bottom
    top_offset = -hide_px if hide_px else 0

    components.html(
        f"""
        <div style="position:relative;width:100%;height:{height}px;overflow:hidden;border-radius:12px;">
          <iframe
            src="{escape(url, quote=True)}"
            style="position:absolute;top:{top_offset}px;left:0;width:100%;height:{iframe_height}px;
                   border:0;border-radius:12px;"
            scrolling="yes"
          ></iframe>
        </div>
        """,
        height=height + 16,
    )

if st.query_params.get("ping") == "1":
    st.write("ok"); st.stop()

# Quick CSS theme (dark + teal accents)
st.markdown("""
<style>
:root { --accent:#20c997; --accent2:#7c4dff; }
.block-container { padding-top: 1rem; }
section[data-testid="stSidebar"] .st-expander { border:1px solid #313131; border-radius:12px; }
div[data-testid="stMetric"]{
  background: linear-gradient(135deg, rgba(32,201,151,.08), rgba(124,77,255,.06));
  border: 1px solid rgba(128,128,128,.15);
  padding: 12px; border-radius: 12px;
}
.stButton>button, .stDownloadButton>button{
  border-radius:10px; border:1px solid rgba(255,255,255,.15);
}
.stTabs [data-baseweb="tab-list"] { gap: 6px; }
.stTabs [data-baseweb="tab"]{
  background: rgba(255,255,255,.03); border: 1px solid rgba(255,255,255,.08);
  border-radius: 10px; padding: 6px 12px;
}
[data-testid="stHeader"] { background: transparent; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.sidebar.image(
        "https://i.imgur.com/E5LaGaa.png",
        use_container_width=True
    )
    st.sidebar.markdown("📘 **About**")
    st.sidebar.markdown("""
    Learn3 adalah platform edukasi Web3 interaktif yang dikemas seperti game petualangan. Memadukan AI bot dan mentor, gamifikasi, serta real-world tools dari ekosistem blockchain.
    Kami percaya belajar Web3 bukan sekadar membaca teori, tapi perjalanan interaktif:

    - mulai dari dasar,
    
    - naik level lewat simulasi,
    
    - eksplorasi frontier research,
    
    - dan menutup perjalanan dengan reward on-chain sebagai bukti pencapaian.

    Showcase dan dokumentasi ada disini [Doc](https://learn3showcase.vercel.app)
    
    ---
    #### 🔮 Vision Statement
    User belajar lewat chatbot AI, latihan simulasi DeFi & DAO, eksperimen smart contract, hingga riset cutting-edge seperti zkML.
    Setiap langkah terhubung dengan ekosistem STC (GasVision, Bench, Converter, Analytics) untuk pengalaman nyata.
    Di akhir perjalanan, user mendapatkan sertifikat Soul Bound Token (SBT) eksklusif — bukti abadi di blockchain bahwa mereka adalah bagian dari pionir Web3.

    ---
    ### 🧩 STC Ecosystem
    1. [STC Analytics](https://stc-analytics.streamlit.app/)
    2. [STC GasVision](https://stc-gasvision.streamlit.app/)
    3. [STC Converter](https://stc-converter.streamlit.app/)
    4. [STC Bench](https://stc-bench.streamlit.app/)
    5. [STC Insight](https://stc-insight.streamlit.app/)
    6. [STC Plugin](https://smartourism.elpeef.com/)
    7. [STC GasX](https://stc-gasx.streamlit.app/)
    8. [STC CarbonPrint](https://stc-carbonprint.streamlit.app/)
    9. [STC ImpactViz](https://stc-impactviz.streamlit.app/)
    10. [DataHub](https://stc-data.streamlit.app/)

    ---
    ### ⛓ RANTAI Communities

    > 💡 RANTAI Communities adalah ekosistem apps eksperimental berbasis Web3 & AI untuk riset, kolaborasi, dan inovasi. Dibangun di atas 3 core: Dev → Build, Net → Connect, Lab → Grow.
    
    🔧 Dev → “Build the chain”
    1. [Numerical Methods Lab](https://metnumlab.streamlit.app/)
    2. [Computational Analytics Studio](https://komnumlab.streamlit.app/)
    3. [BlockPedia](https://blockpedia.streamlit.app/)
    4. [Learn3](https://learn3.streamlit.app/)
    5. [LearnPy](https://learnpy.streamlit.app/)

    🌐 Net → “Connect the chain”
    1. [SmartFaith](https://smartfaith.streamlit.app/)
    2. [Nexus](https://rantai-nexus.streamlit.app/)
    3. [Decentralized Supply Chain](https://rantai-trace.streamlit.app/)
    4. [ESG Compliance Manager](https://rantai-sentinel.streamlit.app/)
    5. [Decentralized Storage Optimizer](https://rantai-greenstorage.streamlit.app/)
    6. [Cloud Carbon Footprint Tracker](https://rantai-greencloud.streamlit.app/)
    7. [Cloud.Climate.Chain](https://rantai-3c.streamlit.app/)
    
    🌱 Lab → “Grow the chain”
    1. [BlockBook](https://blockbook.streamlit.app/)
    2. [Data Insights & Visualization Assistant](https://rantai-diva.streamlit.app/)
    3. [Exploratory Data Analysis](https://rantai-exploda.streamlit.app/)
    4. [Business Intelligence](https://rantai-busi.streamlit.app/)
    5. [Predictive Modelling](https://rantai-model-predi.streamlit.app/)
    6. [Ethic & Bias Checker](https://rantai-ethika.streamlit.app/)
    7. [Smart Atlas For Environment](https://rantai-safe.streamlit.app/)
    8. [Blockchain Healthcare Revolution](https://healthchain.streamlit.app/)
    9. [Academic Flow Diagram Generator](https://mermaind.streamlit.app/)
    10. [Decentralized Agriculture](https://agroviz.streamlit.app/)
    
    ---
    #### 🙌 Dukungan & kontributor
    - ⭐ **Star / Fork**: [GitHub repo](https://github.com/mrbrightsides/learnpy)
    - Built with 💙 by [Khudri](https://s.id/khudri)
    - Dukung pengembangan proyek ini melalui: 
      [💖 GitHub Sponsors](https://github.com/sponsors/mrbrightsides) • 
      [☕ Ko-fi](https://ko-fi.com/khudri) • 
      [💵 PayPal](https://www.paypal.com/paypalme/akhmadkhudri) • 
      [🍵 Trakteer](https://trakteer.id/akhmad_khudri)

    Versi UI: v1.0 • Streamlit • Theme Dark
    """)

# ===== Page setup =====
st.set_page_config(
    page_title="LearnPy",
    page_icon="🐍",
    layout="wide"
)

col1, col2 = st.columns([2, 2])
with col1:
    st.markdown("""
        # Learn Python with LearnPy 🐍
    """)
with col2:
    st.markdown("""
        ## Code. Think. Automate. Innovate — Your Python Journey Starts Here
    """)
st.markdown("""
        > 💡 Untuk tampilan dan pengalaman belajar yang optimal, disarankan menggunakan browser pada laptop atau PC untuk mengakses Learn3
    """)

# ===== Tab utama =====
tabs = st.tabs([
    "🤖 AI Playground", 
    "📖 Python 101",
    "🔀 Control Flow & Logic",
    "📦 Data Structures",
    "🛠️ Functions & Modules",
    "🧱 Object-Oriented Programming (OOP)",
    "📊 Python for Data",
    "🤖 Python for AI/ML",
    "🎓 Final Project"
])

# ===== Tab: Chatbot =====
with tabs[0]:
    st.subheader("🤖 Chatbot AI-powered Playground")
    st.markdown("""
        Tanya jawab interaktif tentang Python. Pilih sesuai kebutuhan kamu.
    """)
    
    # --- Persist pilihan widget
    if "chat_widget" not in st.session_state:
        st.session_state.chat_widget = "AI Gateway"  # default
    
    widget_opt = st.radio(
        " ",
        ["AI Gateway"],
        horizontal=True, label_visibility="collapsed",
        index=["AI Gateway"].index(st.session_state.chat_widget),
        key="chat_widget"
    )
    
    URLS = {
        "AI Gateway": "https://learn3ai.vercel.app/"
    }
    chosen_url = URLS[widget_opt]
    
    cache_bust = st.toggle("Force refresh chat (cache-bust)", value=False)
    final_url = f"{chosen_url}?t={int(time.time())}" if cache_bust else chosen_url
    
    st.write(f"💬 Chat aktif: **{widget_opt}**")
    st.caption("Jika area kosong, kemungkinan dibatasi oleh CSP/X-Frame-Options dari penyedia.")
    
    if st.button(f"🔗 Klik disini jika ingin menampilkan halaman chat {widget_opt} dengan lebih baik"):
        st.markdown(f"""<meta http-equiv="refresh" content="0; url={chosen_url}">""", unsafe_allow_html=True)

# === Tab 1: Python 101 (iframe ke Ohara) ===
with tabs[1]:
    app = OHARA_APPS["Python 101"]
    embed_lab(app["url"], app["title"], hide_top=110, hide_bottom = 15)
    
# === Tab 2: Control Flow & Logic (iframe ke Ohara) ===
with tabs[2]:
    app = OHARA_APPS["Control Flow & Logic"]
    embed_lab(app["url"], app["title"], hide_top=110, hide_bottom = 15)

# === Tab 3: Data Structures (iframe ke Ohara) ===
with tabs[3]:
    app = OHARA_APPS["Data Structures"]
    embed_lab(app["url"], app["title"], hide_top=110, hide_bottom = 15)
    
# === Tab 4: Functions & Modules (iframe ke Ohara) ===
with tabs[4]:
    app = OHARA_APPS["Functions & Modules"]
    embed_lab(app["url"], app["title"], hide_top=110, hide_bottom = 15)

# === Tab 5: Object-Oriented Programming (OOP) (iframe ke Ohara) ===
with tabs[5]:
    app = OHARA_APPS["Object-Oriented Programming (OOP)"]
    embed_lab(app["url"], app["title"], hide_top=110, hide_bottom = 15)
    
# === Tab 6: Python for Data (iframe ke Ohara) ===
with tabs[6]:
    app = OHARA_APPS["Python for Data"]
    embed_lab(app["url"], app["title"], hide_top=110, hide_bottom = 15)
    
# === Tab 7: Python for Web & API (iframe ke Ohara) ===
with tabs[7]:
    app = OHARA_APPS["Python for Web & API"]
    embed_lab(app["url"], app["title"], hide_top=110, hide_bottom = 15)

# === Tab 8: Python for AI/ML (iframe ke Ohara) ===
with tabs[8]:
    app = OHARA_APPS["Python for AI/ML"]
    embed_lab(app["url"], app["title"], hide_top=110, hide_bottom = 15)

# === Tab 9: Certification (iframe ke Ohara) ===
with tabs[9]:
    app = OHARA_APPS["Certification"]
    embed_lab(app["url"], app["title"], hide_top=110, hide_bottom = 15)
