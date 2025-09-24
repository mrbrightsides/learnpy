# external_module.py
import streamlit as st
import streamlit.components.v1 as components

def render_external_module(url: str, title: str, note: str = "", height: int = 740):
    st.markdown(f"## {title}")
    if note:
        st.caption(note)

    fallback = st.toggle(
        "Buka fullscreen di halaman ini (fallback jika embed diblokir CSP)", value=False
    )

    if not fallback:
        st.info("Jika area di bawah kosong, kemungkinan diblokir CSP/X-Frame-Options. Aktifkan toggle di atas untuk buka fullscreen.")
        components.html(
            f"""
            <iframe
              src="{url}"
              style="width:100%;height:85vh;border:0;border-radius:12px;overflow:hidden"
              referrerpolicy="no-referrer-when-downgrade"
            ></iframe>
            """,
            height=height,
        )
    else:
        components.html(
            f"""
            <div style="display:flex;gap:12px;align-items:center">
              <button id="launch"
                      style="padding:10px 16px;border-radius:10px;border:0;background:#3b82f6;color:white;font-weight:600;cursor:pointer">
                🚀 Launch Module (fullscreen)
              </button>
              <span style="opacity:.7;">Kembali ke Learn3: tombol back aplikasi/browser</span>
            </div>
            <script>
              document.getElementById('launch').onclick = () => {{
                window.location.href = "{url}";
              }};
            </script>
            """,
            height=80,
        )
