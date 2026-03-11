"""ClawForge UI — Premium Trading Terminal with animations."""
import streamlit as st
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
try:
    from core.icons import ICONS
except ImportError:
    ICONS = {}

THEME = {
    "bg": "#050608",
    "bg_surface": "#0d1117",
    "bg_elevated": "#161b22",
    "accent": "#22d3ee",
    "accent_soft": "rgba(34, 211, 238, 0.15)",
    "success": "#10b981",
    "danger": "#f43f5e",
    "warning": "#f59e0b",
    "text": "#f0f6fc",
    "text_muted": "#8b949e",
    "border": "rgba(34, 211, 238, 0.12)",
    "font_display": "Syne",
    "font_body": "DM Sans",
    "font_mono": "JetBrains Mono",
}


def inject_global_css():
    """Inject premium Trading Terminal theme with animations."""
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700&family=JetBrains+Mono:wght@400;500;600&display=swap');
    
    :root {{
        --cf-bg: {THEME["bg"]};
        --cf-surface: {THEME["bg_surface"]};
        --cf-elevated: {THEME["bg_elevated"]};
        --cf-accent: {THEME["accent"]};
        --cf-success: {THEME["success"]};
        --cf-danger: {THEME["danger"]};
        --cf-warning: {THEME["warning"]};
        --cf-text: {THEME["text"]};
        --cf-muted: {THEME["text_muted"]};
        --cf-border: {THEME["border"]};
    }}
    
    /* Keyframe animations */
    @keyframes cf-fadeIn {{
        from {{ opacity: 0; transform: translateY(-8px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    @keyframes cf-slideIn {{
        from {{ opacity: 0; transform: translateX(-12px); }}
        to {{ opacity: 1; transform: translateX(0); }}
    }}
    @keyframes cf-pulse {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0.7; }}
    }}
    @keyframes cf-glow {{
        0%, 100% {{ box-shadow: 0 0 0 rgba(34, 211, 238, 0.3); }}
        50% {{ box-shadow: 0 0 20px rgba(34, 211, 238, 0.15); }}
    }}
    @keyframes cf-shimmer {{
        0% {{ background-position: -200% 0; }}
        100% {{ background-position: 200% 0; }}
    }}
    
    #MainMenu {{ visibility: hidden; }}
    footer {{ visibility: hidden; }}
    header {{ visibility: hidden; }}
    div[data-testid="stToolbar"] {{ display: none; }}
    /* Hide sidebar toggle (keyboard_double_arrow_left <<) — always show left panel */
    [data-testid="collapsedControl"],
    [data-testid="stSidebarCollapsedControl"],
    div[data-testid="stSidebarCollapsedControl"],
    [data-testid="stSidebar"] > button,
    [data-testid="stSidebar"] button,
    section[data-testid="stSidebar"] > button,
    section[data-testid="stSidebar"] button,
    [data-testid="stSidebar"] + button,
    [data-testid="stSidebar"] + div > button,
    section[data-testid="stSidebar"] + button,
    section[data-testid="stSidebar"] + div > button,
    button[aria-label*="Close sidebar"],
    button[aria-label*="Expand sidebar"],
    button[aria-label*="collapse"],
    button[aria-label*="Collapse"],
    [aria-label*="sidebar"][role="button"],
    button:has([class*="keyboard_double_arrow"]),
    button:has(span[class*="keyboard_double_arrow"]),
    button:has([class*="keyboard_double_arrow_left"]),
    [class*="keyboard_double_arrow_left"],
    [class*="keyboard_double_arrow"] {{
        display: none !important;
        visibility: hidden !important;
        pointer-events: none !important;
        width: 0 !important;
        height: 0 !important;
        overflow: hidden !important;
    }}
    div.block-container {{ padding: 1.5rem 2rem 3rem; max-width: 1400px; animation: cf-fadeIn 0.4s ease-out; }}
    </style>
    <script>
    (function() {{
        function hideSidebarToggle() {{
            var s = [
                '[data-testid="collapsedControl"]',
                '[data-testid="stSidebarCollapsedControl"]',
                'button[aria-label*="Close sidebar"]',
                'button[aria-label*="Expand sidebar"]',
                'button[aria-label*="collapse" i]',
                'button[aria-label*="Collapse" i]',
                '[data-testid="stSidebar"] > button',
                '[data-testid="stSidebar"] button',
                'section[data-testid="stSidebar"] > button',
                'section[data-testid="stSidebar"] button',
                '[data-testid="stSidebar"] + button',
                'section[data-testid="stSidebar"] + button',
                '[data-testid="stSidebar"] + div button',
                'section[data-testid="stSidebar"] + div button'
            ];
            s.forEach(function(sel) {{
                try {{
                    document.querySelectorAll(sel).forEach(function(el) {{
                        el.style.cssText = 'display:none!important;visibility:hidden!important;';
                    }});
                }} catch(e) {{}}
            }});
            document.querySelectorAll('button').forEach(function(btn) {{
                var l = (btn.getAttribute('aria-label') || '').toLowerCase();
                if (l.indexOf('sidebar') >= 0 && (l.indexOf('close') >= 0 || l.indexOf('expand') >= 0 || l.indexOf('collapse') >= 0)) {{
                    btn.style.cssText = 'display:none!important;visibility:hidden!important;width:0!important;height:0!important;overflow:hidden!important;';
                }}
            }});
            document.querySelectorAll('[class*="stSidebar"], [data-testid="stSidebar"]').forEach(function(sb) {{
                sb.querySelectorAll('button').forEach(function(btn) {{
                    btn.style.cssText = 'display:none!important;visibility:hidden!important;width:0!important;height:0!important;overflow:hidden!important;';
                }});
            }});
            document.querySelectorAll('[class*="keyboard_double_arrow"]').forEach(function(el) {{
                var par = el.closest('button');
                if (par) par.style.cssText = 'display:none!important;visibility:hidden!important;width:0!important;height:0!important;overflow:hidden!important;';
                else el.style.cssText = 'display:none!important;visibility:hidden!important;';
            }});
            document.querySelectorAll('button').forEach(function(btn) {{
                if (btn.innerHTML && btn.innerHTML.indexOf('keyboard_double_arrow') >= 0) {{
                    btn.style.cssText = 'display:none!important;visibility:hidden!important;width:0!important;height:0!important;overflow:hidden!important;';
                }}
            }});
            document.querySelectorAll('[class*="stIconMaterial"]').forEach(function(el) {{
                var html = el.outerHTML || '';
                if (html.indexOf('keyboard_double_arrow') >= 0) {{
                    var par = el.closest('button');
                    if (par) par.style.cssText = 'display:none!important;visibility:hidden!important;width:0!important;height:0!important;overflow:hidden!important;';
                }}
            }});
            var sidebar = document.querySelector('[data-testid="stSidebar"], section[data-testid="stSidebar"]');
            if (sidebar) {{
                var next = sidebar.nextElementSibling;
                if (next && next.tagName === 'BUTTON') {{
                    next.style.cssText = 'display:none!important;visibility:hidden!important;width:0!important;height:0!important;overflow:hidden!important;';
                }}
                if (next && next.offsetWidth > 0 && next.offsetWidth < 100 && next.querySelector && next.querySelector('button')) {{
                    next.style.cssText = 'display:none!important;visibility:hidden!important;width:0!important;height:0!important;overflow:hidden!important;';
                    next.querySelectorAll('button').forEach(function(b) {{ b.style.cssText = 'display:none!important;visibility:hidden!important;'; }});
                }}
            }}
        }}
        hideSidebarToggle();
        document.addEventListener('DOMContentLoaded', hideSidebarToggle);
        if (document.readyState !== 'loading') hideSidebarToggle();
        [50, 150, 300, 500, 1000, 2000, 3000, 5000].forEach(function(ms) {{ setTimeout(hideSidebarToggle, ms); }});
        var debounce = 0;
        var mo = new MutationObserver(function() {{
            if (debounce) return;
            debounce = setTimeout(function() {{ debounce = 0; hideSidebarToggle(); }}, 300);
        }});
        if (document.body) mo.observe(document.body, {{ childList: true, subtree: true }});
    }})();
    </script>
    <style>
    
    .stApp {{
        font-family: '{THEME["font_body"]}', system-ui, sans-serif;
        background: {THEME["bg"]};
    }}
    .stApp::before {{
        content: '';
        position: fixed;
        inset: 0;
        background: 
            radial-gradient(ellipse 120% 100% at 50% -30%, rgba(34, 211, 238, 0.05) 0%, transparent 55%),
            radial-gradient(ellipse 80% 60% at 100% 0%, rgba(16, 185, 129, 0.03) 0%, transparent 50%);
        pointer-events: none;
        z-index: -1;
    }}
    
    /* ═══════════════════════════════════════════════════════════════
       SIDEBAR — Left panel with nav list (force visible)
       ═══════════════════════════════════════════════════════════════ */
    section[data-testid="stSidebar"],
    [data-testid="stSidebar"] {{
        visibility: visible !important;
        display: block !important;
        transform: none !important;
        min-width: 280px !important;
        width: 280px !important;
        background: linear-gradient(180deg, #0a0c0f 0%, #050608 100%) !important;
        border-right: 1px solid {THEME["border"]} !important;
        box-shadow: 4px 0 32px rgba(0,0,0,0.5) !important;
    }}
    [data-testid="stSidebar"] [data-testid="stSidebarContent"] {{
        padding: 1.25rem 1rem 2rem !important;
        overflow-y: auto !important;
    }}
    [data-testid="stSidebar"] [data-testid="stMarkdown"] p {{
        color: {THEME["text"]} !important;
    }}
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {{
        font-family: '{THEME["font_display"]}' !important;
        font-size: 0.95rem !important;
        color: {THEME["accent"]} !important;
        font-weight: 600 !important;
        letter-spacing: -0.02em !important;
        margin-bottom: 0.75rem !important;
    }}
    [data-testid="stSidebar"] .cf-nav-section {{
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: {THEME["text_muted"]};
        margin: 1rem 0 0.5rem;
        padding-left: 0.5rem;
    }}
    [data-testid="stSidebar"] .cf-nav-item {{
        display: flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.6rem 0.75rem;
        margin: 0.2rem 0;
        border-radius: 10px;
        color: {THEME["text_muted"]} !important;
        text-decoration: none !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }}
    [data-testid="stSidebar"] .cf-nav-item:hover {{
        background: {THEME["accent_soft"]} !important;
        color: {THEME["accent"]} !important;
        transform: translateX(4px);
    }}
    [data-testid="stSidebar"] .cf-nav-item.active {{
        background: {THEME["accent_soft"]} !important;
        color: {THEME["accent"]} !important;
        border-left: 3px solid {THEME["accent"]};
    }}
    [data-testid="stSidebar"] .cf-nav-icon {{ font-size: 1.1rem; }}
    [data-testid="stSidebar"] a {{ color: inherit !important; }}
    
    /* Style Streamlit page_link in sidebar — ensure visible */
    [data-testid="stSidebar"] [data-testid="stPageLink"] {{
        margin: 0.35rem 0 !important;
        border-radius: 10px !important;
    }}
    [data-testid="stSidebar"] [data-testid="stPageLink"] a {{
        font-family: '{THEME["font_body"]}' !important;
        font-size: 0.9rem !important;
        color: {THEME["text"]} !important;
        background: rgba(34, 211, 238, 0.06) !important;
        border-radius: 10px !important;
        padding: 0.7rem 0.85rem !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        border: 1px solid transparent !important;
    }}
    [data-testid="stSidebar"] [data-testid="stPageLink"] a:hover {{
        background: {THEME["accent_soft"]} !important;
        color: {THEME["accent"]} !important;
        border-color: rgba(34, 211, 238, 0.2) !important;
        transform: translateX(6px) !important;
    }}
    [data-testid="stSidebar"] [data-testid="stPageLink"][data-selected="true"] a {{
        background: {THEME["accent_soft"]} !important;
        color: {THEME["accent"]} !important;
    }}
    
    /* Tool cards with animation */
    .cf-tool-card {{
        background: {THEME["bg_surface"]};
        border: 1px solid {THEME["border"]};
        border-radius: 14px;
        padding: 1.25rem 1.5rem;
        transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
        height: 100%;
        animation: cf-fadeIn 0.5s ease-out backwards;
    }}
    .cf-tool-card:hover {{
        border-color: rgba(34, 211, 238, 0.35);
        transform: translateY(-4px) scale(1.02);
        box-shadow: 0 16px 48px rgba(0,0,0,0.3), 0 0 0 1px rgba(34, 211, 238, 0.1);
    }}
    .cf-tool-card .icon {{ font-size: 1rem; margin-bottom: 0.75rem; }}
    .cf-tool-card .cf-icon-wrap {{
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 44px;
        height: 44px;
        border-radius: 12px;
        background: rgba(34, 211, 238, 0.08);
        color: {THEME["accent"]};
    }}
    .cf-tool-card .cf-icon-wrap svg {{ width: 24px; height: 24px; }}
    .cf-tool-card h3 {{
        font-family: '{THEME["font_display"]}' !important;
        font-size: 1.15rem !important;
        font-weight: 600 !important;
        letter-spacing: -0.01em !important;
        color: {THEME["text"]} !important;
        margin: 0 0 0.5rem !important;
    }}
    .cf-tool-card .desc {{
        font-family: '{THEME["font_body"]}' !important;
        font-size: 0.9rem !important;
        line-height: 1.55 !important;
        color: {THEME["text_muted"]};
    }}
    .cf-tool-card .badge {{
        display: inline-block;
        font-family: '{THEME["font_body"]}' !important;
        font-size: 0.7rem !important;
        font-weight: 500 !important;
        letter-spacing: 0.03em !important;
        padding: 0.25rem 0.6rem;
        border-radius: 6px;
        margin-top: 0.5rem;
        background: {THEME["accent_soft"]};
        color: {THEME["accent"]};
    }}
    /* Card with Open button contained inside */
    .cf-tool-card-wrap {{
        display: block;
        text-decoration: none !important;
        color: inherit !important;
        height: 100%;
    }}
    .cf-tool-card-wrap .cf-tool-card {{
        display: flex;
        flex-direction: column;
        height: 100%;
    }}
    .cf-tool-card-wrap .cf-tool-card .cf-card-body {{ flex: 0 1 auto; }}
    .cf-tool-card-wrap .cf-card-open-btn {{
        display: inline-flex;
        align-items: center;
        justify-content: center;
        margin-top: 1rem;
        padding: 0.65rem 1.15rem;
        font-size: 0.875rem !important;
        font-weight: 600 !important;
        font-family: '{THEME["font_body"]}', system-ui, sans-serif !important;
        letter-spacing: 0.02em;
        background: rgba(34, 211, 238, 0.12);
        border: 1px solid rgba(34, 211, 238, 0.35);
        border-radius: 10px;
        color: {THEME["accent"]};
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .cf-tool-card-wrap:hover .cf-card-open-btn {{
        background: {THEME["accent_soft"]};
        border-color: {THEME["accent"]};
        transform: translateY(-2px);
    }}
    .cf-tool-card-wrap .cf-card-open-btn::after {{
        content: ' →';
    }}
    
    .cf-hero {{
        background: linear-gradient(135deg, {THEME["bg_surface"]} 0%, {THEME["bg_elevated"]} 100%);
        border: 1px solid {THEME["border"]};
        border-radius: 20px;
        padding: 2.5rem 3rem;
        margin-bottom: 2.5rem;
        animation: cf-fadeIn 0.5s ease-out;
    }}
    .cf-hero h1 {{
        font-family: '{THEME["font_display"]}' !important;
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        letter-spacing: -0.03em !important;
        color: {THEME["text"]} !important;
        margin: 0 !important;
    }}
    .cf-hero .sub {{
        font-family: '{THEME["font_body"]}' !important;
        font-size: 1.05rem !important;
        line-height: 1.65 !important;
        color: {THEME["text_muted"]};
        margin-top: 0.6rem;
    }}
    .cf-hero .cf-hero-icon {{
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 2.25rem;
        height: 2.25rem;
        margin-right: 0.5rem;
        vertical-align: middle;
        color: {THEME["accent"]};
    }}
    .cf-hero .cf-hero-icon svg {{ width: 2rem; height: 2rem; }}
    
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {{
        font-family: '{THEME["font_display"]}' !important;
        font-weight: 600 !important;
        letter-spacing: -0.02em !important;
        color: {THEME["text"]} !important;
    }}
    .stMarkdown h4 {{ font-size: 1.1rem !important; margin: 1.75rem 0 1rem !important; opacity: 0.95; }}
    .stCaption {{ color: {THEME["text_muted"]} !important; }}
    hr {{ border-color: {THEME["border"]} !important; }}
    
    .stButton > button {{
        background: linear-gradient(135deg, rgba(34, 211, 238, 0.15) 0%, rgba(34, 211, 238, 0.08) 100%) !important;
        border: 1px solid rgba(34, 211, 238, 0.35) !important;
        color: {THEME["accent"]} !important;
        font-weight: 600 !important;
        border-radius: 10px !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }}
    .stButton > button:hover {{
        background: linear-gradient(135deg, rgba(34, 211, 238, 0.25) 0%, rgba(34, 211, 238, 0.15) 100%) !important;
        border-color: {THEME["accent"]} !important;
        box-shadow: 0 0 24px rgba(34, 211, 238, 0.2) !important;
        transform: translateY(-1px);
    }}
    
    div[data-testid="stExpander"] {{
        background: {THEME["bg_surface"]};
        border: 1px solid {THEME["border"]};
        border-radius: 12px;
    }}
    
    .cf-footer {{
        margin-top: 3rem;
        padding: 1.5rem 0;
        border-top: 1px solid {THEME["border"]};
        font-family: '{THEME["font_body"]}' !important;
        color: {THEME["text_muted"]};
        font-size: 0.85rem;
        text-align: center;
    }}
    .cf-footer a {{ color: {THEME["accent"]}; text-decoration: none; }}
    .cf-footer a:hover {{ text-decoration: underline; }}
    
    .cf-onboard {{
        background: {THEME["accent_soft"]};
        border: 1px dashed rgba(34, 211, 238, 0.4);
        border-radius: 12px;
        padding: 1.25rem;
        margin: 1rem 0;
    }}
    .cf-onboard h4 {{ color: {THEME["accent"]}; margin: 0 0 0.5rem; font-size: 1rem; }}
    .cf-onboard code {{
        background: rgba(0,0,0,0.3);
        padding: 0.2rem 0.5rem;
        border-radius: 6px;
        color: {THEME["accent"]};
    }}
    
    .cf-security {{
        background: rgba(245, 63, 94, 0.08);
        border: 1px solid rgba(245, 63, 94, 0.2);
        border-radius: 12px;
        padding: 1rem 1.25rem;
        margin: 1rem 0;
        font-size: 0.9rem;
    }}
    .cf-security strong {{ color: {THEME["danger"]}; }}
    .cf-security a {{ color: {THEME["accent"]} !important; }}
    </style>
    """, unsafe_allow_html=True)


def render_footer():
    st.markdown("""
    <div class="cf-footer">
        ClawForge · AI Trading Platform · 
        <a href="https://clawhub.ai" target="_blank">ClawHub</a> · 
        <a href="https://docs.openclaw.ai" target="_blank">OpenClaw Docs</a>
    </div>
    """, unsafe_allow_html=True)


def onboarding_gateway():
    st.markdown("""
    <div class="cf-onboard">
        <h4>🦾 OpenClaw Setup</h4>
        <p><strong>LLM:</strong> Add <code>GROQ_API_KEY</code> (free at console.groq.com) or <code>CHUTES_API_KEY</code> to .env</p>
        <p><strong>Gateway:</strong> <code>npm install -g openclaw</code> → <code>./scripts/setup_openclaw.sh</code></p>
        <p>Set <code>OPENCLAW_GATEWAY_TOKEN</code> in .env</p>
    </div>
    """, unsafe_allow_html=True)


def security_notice():
    st.markdown("""
    <div class="cf-security">
        <strong>⚠️ Security</strong> — Use a dedicated bot wallet. Never connect main wallet. 
        Run OpenClaw in a container. Audit skills before installing. <a href="https://docs.openclaw.ai/security" target="_blank">Learn more</a>
    </div>
    """, unsafe_allow_html=True)


def _icon_svg(key: str) -> str:
    """Return inline SVG icon or empty."""
    return ICONS.get(key, "")


def _page_to_href(page: str) -> str:
    """Convert pages/1_Skill_Forge.py to Streamlit URL path (e.g. Skill_Forge)."""
    import re
    base = page.split("/")[-1].replace(".py", "")
    return "/" + re.sub(r"^\d+_", "", base)


def project_card_html(name: str, desc: str, icon_key: str, badge: str = "", delay_ms: int = 0) -> str:
    """Card with Lucide-style icon. icon_key: zap, message, bot, trending-up, bar-chart, clipboard, activity, wallet, bell, folder, layout-dashboard."""
    svg = _icon_svg(icon_key)
    icon_html = f'<span class="cf-icon-wrap">{svg}</span>' if svg else ""
    badge_html = f'<span class="badge">{badge}</span>' if badge else ""
    return f"""
    <div class="cf-tool-card" style="animation-delay: {delay_ms}ms">
        <div class="icon">{icon_html}</div>
        <h3>{name}</h3>
        <p class="desc">{desc}</p>
        {badge_html}
    </div>
    """


def project_card_with_open_html(name: str, desc: str, icon_key: str, badge: str, page: str, delay_ms: int = 0) -> str:
    """Card with Open button contained inside — whole card is clickable. Used on homepage."""
    svg = _icon_svg(icon_key)
    icon_html = f'<span class="cf-icon-wrap">{svg}</span>' if svg else ""
    badge_html = f'<span class="badge">{badge}</span>' if badge else ""
    href = _page_to_href(page)
    return f"""
    <a href="{href}" class="cf-tool-card-wrap" style="animation-delay: {delay_ms}ms">
        <div class="cf-tool-card">
            <div class="cf-card-body">
                <div class="icon">{icon_html}</div>
                <h3>{name}</h3>
                <p class="desc">{desc}</p>
                {badge_html}
            </div>
            <span class="cf-card-open-btn">Open</span>
        </div>
    </a>
    """


def project_card_html_emoji(name: str, desc: str, emoji: str, badge: str = "", delay_ms: int = 0) -> str:
    """Fallback: card with emoji icon."""
    badge_html = f'<span class="badge">{badge}</span>' if badge else ""
    return f"""
    <div class="cf-tool-card" style="animation-delay: {delay_ms}ms">
        <div class="icon">{emoji}</div>
        <h3>{name}</h3>
        <p class="desc">{desc}</p>
        {badge_html}
    </div>
    """


def page_hero(title: str, caption: str, icon: str = "") -> None:
    """Render page hero. icon: icon_key (zap, message, bot...) or emoji fallback."""
    try:
        from core.icons import ICONS
        svg = ICONS.get(icon, "")
        icon_html = f'<span class="cf-hero-icon">{svg}</span> ' if svg else (f"{icon} " if icon else "")
    except Exception:
        icon_html = f"{icon} " if icon else ""
    st.markdown(f"""
    <div class="cf-hero">
        <h1>{icon_html}{title}</h1>
        <p class="sub">{caption}</p>
    </div>
    """, unsafe_allow_html=True)


def sidebar_status():
    try:
        from core.openclaw_client import get_status
        from core.openclaw_gateway import is_gateway_ready
        s = get_status()
        gw = is_gateway_ready()
        cli = "✓" if s.get("installed") else "—"
        gw_str = "✓" if gw else "—"
        st.markdown(f"**CLI** {cli} · **Gateway** {gw_str}")
    except Exception:
        st.caption("Status: —")


def render_sidebar_nav():
    """Render full app navigation in sidebar — nav links only."""
    st.page_link("web_app.py", label="🏠 Home", icon=None, use_container_width=True)
    st.markdown(" ")
    nav_items = [
        ("🛠 Core", [
            ("Skill Forge", "pages/1_Skill_Forge.py", "⚡"),
            ("Chat", "pages/2_Chat_with_OpenClaw.py", "💬"),
            ("BankrBot", "pages/3_BankrBot.py", "🦾"),
        ]),
        ("📊 Trading", [
            ("Polyclaw", "pages/7_Polyclaw.py", "📈"),
            ("Alpaca", "pages/8_Alpaca.py", "📉"),
            ("Kalshi", "pages/9_Kalshi.py", "📋"),
            ("Whale Tracking", "pages/10_Whale_Tracking.py", "🐋"),
        ]),
        ("💰 Strategies", [
            ("DCA", "pages/4_DCA.py", "📊"),
            ("Price Alerts", "pages/5_Price_Alerts.py", "🔔"),
            ("Portfolio", "pages/11_Portfolio.py", "📁"),
        ]),
        ("📊 System", [
            ("Status", "pages/6_Status.py", "📊"),
        ]),
    ]
    for section, items in nav_items:
        st.markdown(f'**{section}**')
        for name, page, icon_key in items:
            lab = name
            st.page_link(page, label=lab, icon=None, use_container_width=True)
        st.markdown(" ")
