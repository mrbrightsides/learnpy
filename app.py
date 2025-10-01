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
        "url": "https://ohara.ai/mini-apps/be992dff-155e-4182-a55a-923ac2b3a2ca?utm_source=rantai-learnpy",
        "title": "📖 Python 101"
    },
    "Control Flow & Logic": {
        "url": "https://ohara.ai/mini-apps/491b5f00-9103-434e-8e35-620de7b9ab2b?utm_source=rantai-learnpy",
        "title": "🔀 Control Flow & Logic"
    },
    "Data Structures": {
        "url": "https://ohara.ai/mini-apps/833244b7-4a17-41ad-88fc-a22780bed324?utm_source=rantai-learnpy",
        "title": "📦 Data Structures"
    },
    "Functions & Modules": {
        "url": "https://ohara.ai/mini-apps/4a7f4d66-8217-4c85-a7a7-ad7cc0eee882?utm_source=rantai-learnpy",
        "title": "🛠️ Functions & Modules"
    },
    "OOP": {
        "url": "https://ohara.ai/mini-apps/35beb150-e2e2-4ce4-9274-96e9b8cb85ad?utm_source=rantai-learnpy",
        "title": "🧱 OOP"
    },
    "Py for Data": {
        "url": "https://ohara.ai/mini-apps/927ae816-a46c-43ca-ab6e-2889dd6a472b?utm_source=rantai-learnpy",
        "title": "📊 Py for Data"
    },
    "Py for Web & API": {
        "url": "https://ohara.ai/mini-apps/12df8624-3bab-4ace-9cb8-51dceae49177?utm_source=rantai-learnpy",
        "title": "🌐 Py for Web & API"
    },
    "Py for AI/ML": {
        "url": "https://ohara.ai/mini-apps/2b644af0-018c-481a-80e0-792dc7427d16?utm_source=rantai-learnpy",
        "title": "🤖 Py for AI/ML"
    },
    "Final Project": {
        "url": "https://ohara.ai/mini-apps/dfae20e7-edef-4845-8556-f06515f8373d?utm_source=rantai-learnpy",
        "title": "🎓 Final Project"
    }
}

import streamlit as st
import streamlit.components.v1 as components

def iframe_with_mobile_notice(content_html, height):
    style = """
    <style>
      @media (max-width: 768px) {
          .hide-on-mobile { display:none!important; }
          .show-on-mobile {
              display:block!important;
              padding:24px 12px;
              background:#ffecec;
              color:#d10000;
              font-weight:bold;
              text-align:center;
              border-radius:12px;
              font-size:1.2em;
              margin-top:24px;
          }
      }
      @media (min-width: 769px) {
          .show-on-mobile { display:none!important; }
      }
    </style>
    """
    notice = '''
      <div class="show-on-mobile">
        📱 Tampilan ini tidak tersedia di perangkat seluler.<br>
        Silakan buka lewat laptop atau desktop untuk pengalaman penuh 💻
      </div>
    '''
    components.html(
        style +
        f'<div class="hide-on-mobile">{content_html}</div>' +
        notice,
        height=height
    )

def iframe(src, height=720, width="100%", hide_top=0, hide_bottom=0, title=None):
    if title:
        st.markdown(f"<h3>{title}</h3>", unsafe_allow_html=True)
    iframe_height = height + hide_top + hide_bottom
    top_offset = -hide_top
    content_html = f'''
        <div style="height:{height}px; overflow:hidden; position:relative;">
            <iframe src="{src}" width="{width}" height="{iframe_height}px"
                    frameborder="0"
                    style="position:relative; top:{top_offset}px;">
            </iframe>
        </div>
    '''
    iframe_with_mobile_notice(content_html, height)

def embed_lab(url, title="", hide_top=72, hide_bottom=0, height=720):
    if title:
        st.markdown(f"### {title}", unsafe_allow_html=True)
    iframe_height = height + hide_top + hide_bottom
    top_offset = -hide_top
    content_html = f'''
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
    '''
    iframe_with_mobile_notice(content_html, height)

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
        "https://i.imgur.com/pwYe3ox.png",
        use_container_width=True
    )
    st.sidebar.markdown("📘 **About**")
    st.sidebar.markdown("""
    LearnPy adalah ruang belajar Python step-by-step, mulai dari dasar hingga pengenalan ke Data, Web/API, dan AI/ML.
    Konsepnya mirip Learn3 (simple, modular, interaktif), tapi khusus difokuskan untuk bahasa Python.
    
    Tujuannya: bikin Python gampang dipelajari, fun, tapi tetap serius sampai siap dipakai di project nyata.
    
    ---
    #### 🔮 Vision Statement
    Visi LearnPy adalah membekali siapa saja dengan kemampuan Python yang aplikatif, bisa dipakai untuk kuliah, riset, sampai proyek industri.
    > Learning Python should feel simple, structured, and sustainable.

    ---
    ### 🧩 Apps Showcase
    Lihat disini untuk semua tools yang kami kembangkan:
    [ELPEEF](https://showcase.elpeef.com/)
    
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
        > 💡 Untuk tampilan dan pengalaman belajar yang optimal, disarankan menggunakan browser pada laptop atau PC untuk mengakses LearnPy
    """)

# ===== Tab utama =====
tabs = st.tabs([
    "🤖 PyPlayground with AI", 
    "📖 Python 101",
    "🔀 Control Flow & Logic",
    "📦 Data Structures",
    "🛠️ Functions & Modules",
    "🧱 OOP",
    "📊 Py for Data",
    "🌐 Py for Web & API",
    "🤖 Py for AI/ML",
    "🎓 Final Project"
])

# ===== Tab: Chatbot =====
with tabs[0]:
    st.subheader("🤖 Chatbot AI-powered Playground")
    st.markdown("""
        Tanya AI seputar Python dengan vibes yang friendly.
    """)
        
    # --- Persist pilihan widget
    if "chat_widget" not in st.session_state:
        st.session_state.chat_widget = "PyTutor"  # default
    
    widget_opt = st.radio(
        " ",
        ["PyTutor", "PyGateway"],
        horizontal=True, label_visibility="collapsed",
        index=["PyTutor","PyGateway"].index(st.session_state.chat_widget),
        key="chat_widget"
    )
    
    URLS = {
        "PyTutor": "https://www.chatbase.co/chatbot-iframe/2JHRFT7U1mqvZHoHrJqeH",
        "PyGateway":"https://learnpy-ai.vercel.app/"
    }
    chosen_url = URLS[widget_opt]
    
    cache_bust = st.toggle("Force refresh chat (cache-bust)", value=False)
    final_url = f"{chosen_url}?t={int(time.time())}" if cache_bust else chosen_url
    
    st.write(f"💬 Chat aktif: **{widget_opt}**")
    st.caption("Jika area kosong, kemungkinan dibatasi oleh CSP/X-Frame-Options dari penyedia.")
    
    iframe(src=final_url, height=720)
    
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

# === Tab 5: OOP (iframe ke Ohara) ===
with tabs[5]:
    app = OHARA_APPS["OOP"]
    embed_lab(app["url"], app["title"], hide_top=110, hide_bottom = 15)
    
# === Tab 6: Py for Data (iframe ke Ohara) ===
with tabs[6]:
    app = OHARA_APPS["Py for Data"]
    embed_lab(app["url"], app["title"], hide_top=110, hide_bottom = 15)
    
# === Tab 7: Py for Web & API (iframe ke Ohara) ===
with tabs[7]:
    app = OHARA_APPS["Py for Web & API"]
    embed_lab(app["url"], app["title"], hide_top=110, hide_bottom = 15)

# === Tab 8: Py for AI/ML (iframe ke Ohara) ===
with tabs[8]:
    app = OHARA_APPS["Py for AI/ML"]
    embed_lab(app["url"], app["title"], hide_top=110, hide_bottom = 15)

# === Tab 9: Final Project (iframe ke Ohara) ===
with tabs[9]:
    app = OHARA_APPS["Final Project"]
    embed_lab(app["url"], app["title"], hide_top=110, hide_bottom = 15)
