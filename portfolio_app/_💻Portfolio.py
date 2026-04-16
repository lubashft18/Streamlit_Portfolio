import streamlit as st
from datetime import datetime
import time
from pathlib import Path
import base64

st.set_page_config(
    page_title="Antonio Luba | Cyber Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================== ADVANCED CSS WITH ENHANCED ANIMATIONS ==================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');

/* Global Styles */
.stApp {
    background: linear-gradient(135deg, #0a0a0a 0%, #0a0f1a 25%, #0a0a0f 50%, #001a1a 100%);
}

/* Animated Grid Background */
.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: 
        linear-gradient(rgba(0, 255, 255, 0.05) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0, 255, 255, 0.05) 1px, transparent 1px);
    background-size: 50px 50px;
    pointer-events: none;
    z-index: 0;
    animation: gridMove 15s linear infinite;
}

@keyframes gridMove {
    0% { transform: translate(0, 0); }
    100% { transform: translate(50px, 50px); }
}

/* Glowing Orb Effect */
.stApp::after {
    content: "";
    position: fixed;
    top: 50%;
    left: 50%;
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, rgba(0,255,255,0.1), rgba(255,0,255,0.05), transparent);
    border-radius: 50%;
    transform: translate(-50%, -50%);
    animation: pulse 6s ease-in-out infinite;
    pointer-events: none;
    z-index: 0;
}

@keyframes pulse {
    0%, 100% { transform: translate(-50%, -50%) scale(1); opacity: 0.3; }
    50% { transform: translate(-50%, -50%) scale(1.8); opacity: 0.1; }
}

/* Main Content */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    position: relative;
    z-index: 1;
}

/* ================== ENHANCED SIDEBAR STYLES ================== */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(8, 8, 16, 0.98) 0%, rgba(12, 12, 24, 0.98) 100%);
    backdrop-filter: blur(20px);
    border-right: 2px solid rgba(0, 255, 255, 0.3);
    box-shadow: 5px 0 30px rgba(0, 255, 255, 0.1);
    transition: all 0.3s ease;
}

[data-testid="stSidebar"]:hover {
    border-right-color: rgba(0, 255, 255, 0.6);
    box-shadow: 5px 0 40px rgba(0, 255, 255, 0.2);
}

/* Sidebar Profile Section */
.sidebar-profile {
    text-align: center;
    padding: 20px;
    border-bottom: 2px solid rgba(0, 255, 255, 0.3);
    margin-bottom: 20px;
    position: relative;
    animation: slideIn 0.5s ease-out;
}

.sidebar-profile::after {
    content: '';
    position: absolute;
    bottom: -2px;
    left: 20%;
    width: 60%;
    height: 2px;
    background: linear-gradient(90deg, transparent, #00ffff, #ff00ff, transparent);
    animation: borderGlow 2s ease-in-out infinite;
}

@keyframes borderGlow {
    0%, 100% { opacity: 0.5; }
    50% { opacity: 1; }
}

.sidebar-avatar {
    margin-bottom: 15px;
    animation: float 3s ease-in-out infinite;
    display: inline-block;
}

.sidebar-avatar img {
    width: 150px;
    height: 150px;
    border-radius: 20px;
    border: 3px solid #00ffff;
    box-shadow: 0 0 20px rgba(0, 255, 255, 0.5);
    object-fit: cover;
    transition: all 0.3s ease;
}

.sidebar-avatar img:hover {
    transform: scale(1.05);
    box-shadow: 0 0 30px rgba(0, 255, 255, 0.8);
}

@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-5px); }
}

.sidebar-name {
    font-size: 1.2rem;
    font-weight: 700;
    background: linear-gradient(135deg, #00ffff, #ff00ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: 1px;
}

.sidebar-title {
    font-size: 0.8rem;
    color: #888;
    margin-top: 5px;
    font-family: 'Share Tech Mono', monospace;
}

/* Sidebar Navigation Items */
.sidebar-nav-item {
    padding: 12px 15px;
    margin: 8px 0;
    border-radius: 10px;
    transition: all 0.3s ease;
    cursor: pointer;
    position: relative;
    overflow: hidden;
}

.sidebar-nav-item:hover {
    background: linear-gradient(90deg, rgba(0, 255, 255, 0.2), rgba(255, 0, 255, 0.05));
    transform: translateX(5px);
}

.sidebar-nav-item.active {
    background: linear-gradient(90deg, rgba(0, 255, 255, 0.3), rgba(255, 0, 255, 0.1));
    border-left: 3px solid #00ffff;
}

/* Sidebar Stats */
.sidebar-stats {
    background: rgba(0, 255, 255, 0.05);
    border: 1px solid rgba(0, 255, 255, 0.2);
    border-radius: 10px;
    padding: 12px;
    margin: 15px 0;
    text-align: center;
    transition: all 0.3s ease;
}

.sidebar-stats:hover {
    border-color: #00ffff;
    transform: scale(1.02);
}

.sidebar-stat-number {
    font-size: 1.3rem;
    font-weight: 700;
    color: #00ffff;
    font-family: 'Share Tech Mono', monospace;
}

.sidebar-stat-label {
    font-size: 0.7rem;
    color: #888;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Sidebar Status Indicator */
.status-indicator {
    display: inline-block;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background-color: #00ff00;
    box-shadow: 0 0 8px #00ff00;
    animation: pulse 2s infinite;
    margin-right: 8px;
}

/* Social Links in Sidebar */
.social-links {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin: 15px 0;
}

.social-badge {
    transition: all 0.3s ease;
}

.social-badge:hover {
    transform: translateY(-3px);
    filter: drop-shadow(0 0 10px rgba(0, 255, 255, 0.5));
}

/* Cyber Title with Enhanced Animation */
.cyber-title {
    font-family: 'Space Grotesk', monospace;
    font-size: 5.5rem;
    font-weight: 800;
    text-align: center;
    background: linear-gradient(135deg, #00ffff 0%, #ff00ff 30%, #00ffff 60%, #ff00ff 100%);
    background-size: 300% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shimmer 4s linear infinite, glowPulse 2s ease-in-out infinite;
    letter-spacing: -3px;
    margin-bottom: 0.5rem;
}

@keyframes shimmer {
    0% { background-position: 0% 50%; }
    100% { background-position: 300% 50%; }
}

@keyframes glowPulse {
    0%, 100% { filter: drop-shadow(0 0 20px rgba(0, 255, 255, 0.3)); }
    50% { filter: drop-shadow(0 0 50px rgba(0, 255, 255, 0.6)); }
}

/* Enhanced Typewriter Effect */
.typewriter-container {
    display: flex;
    justify-content: center;
    margin-top: 1rem;
}

.typewriter {
    font-family: 'Share Tech Mono', monospace;
    font-size: 1.2rem;
    color: #00ffff;
    text-align: center;
    overflow: hidden;
    border-right: 2px solid #00ffff;
    white-space: nowrap;
    margin: 0 auto;
    letter-spacing: 2px;
    animation: typing 4s steps(50, end), blink-caret 0.75s step-end infinite;
    display: inline-block;
    width: fit-content;
}

@keyframes typing {
    from { width: 0; }
    to { width: 100%; }
}

@keyframes blink-caret {
    from, to { border-color: transparent; }
    50% { border-color: #00ffff; }
}

/* Hero Container with Glassmorphism */
.hero-container {
    background: linear-gradient(135deg, rgba(10, 20, 30, 0.5), rgba(0, 255, 255, 0.05));
    backdrop-filter: blur(20px);
    border-radius: 30px;
    padding: 3rem;
    margin: 3rem 0;
    border: 1px solid rgba(0, 255, 255, 0.3);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
    animation: fadeInUp 1s ease-out;
    text-align: center;
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(50px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Welcome Text Styles */
.welcome-badge {
    display: inline-block;
    background: rgba(0, 255, 255, 0.1);
    border: 1px solid rgba(0, 255, 255, 0.3);
    border-radius: 50px;
    padding: 0.5rem 1.5rem;
    margin-bottom: 1.5rem;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.9rem;
    color: #00ffff;
    letter-spacing: 2px;
}

.glow-text {
    color: #00ffff;
    font-size: 2rem;
    margin-bottom: 1rem;
    font-family: 'Share Tech Mono', monospace;
    animation: glowText 2s ease-in-out infinite;
}

@keyframes glowText {
    0%, 100% { text-shadow: 0 0 5px rgba(0, 255, 255, 0.5); }
    50% { text-shadow: 0 0 20px rgba(0, 255, 255, 0.8); }
}

.welcome-description {
    color: #ccc;
    line-height: 1.8;
    font-size: 1.1rem;
    max-width: 800px;
    margin: 0 auto;
}

/* Enhanced Navigation Cards */
.nav-card {
    background: linear-gradient(135deg, rgba(10, 20, 30, 0.8), rgba(0, 50, 50, 0.6));
    backdrop-filter: blur(10px);
    border: 1px solid rgba(0, 255, 255, 0.2);
    border-radius: 20px;
    padding: 2rem 1rem;
    text-align: center;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    cursor: pointer;
    position: relative;
    overflow: hidden;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.nav-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(0, 255, 255, 0.15), transparent);
    transition: left 0.5s ease;
}

.nav-card:hover::before {
    left: 100%;
}

.nav-card:hover {
    transform: translateY(-10px) scale(1.05);
    border-color: #00ffff;
    box-shadow: 0 20px 40px rgba(0, 255, 255, 0.3);
    background: rgba(0, 255, 255, 0.15);
}

.nav-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
    transition: all 0.3s ease;
    display: inline-block;
}

.nav-card:hover .nav-icon {
    transform: scale(1.2) rotate(5deg);
    filter: drop-shadow(0 0 10px #00ffff);
}

.nav-title {
    font-size: 1.3rem;
    font-weight: bold;
    color: #00ffff;
    margin: 0.5rem 0;
    letter-spacing: 2px;
}

.nav-desc {
    font-size: 0.85rem;
    color: #ccc;
    line-height: 1.4;
}

/* Skills Preview */
.skills-preview {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    justify-content: center;
    margin-top: 15px;
}

.skill-tag {
    background: rgba(0, 255, 255, 0.1);
    border: 1px solid rgba(0, 255, 255, 0.3);
    border-radius: 20px;
    padding: 4px 12px;
    font-size: 0.7rem;
    color: #00ffff;
    font-family: 'Share Tech Mono', monospace;
}

/* About Preview */
.about-preview {
    font-size: 0.8rem;
    color: #ccc;
    line-height: 1.5;
    margin-top: 10px;
}

/* CTA Button with Pulse Animation */
.cta-container {
    text-align: center;
    margin: 3rem 0;
    animation: fadeInUp 1s ease-out 0.5s backwards;
}

/* Particle Effects */
.particle {
    position: fixed;
    width: 2px;
    height: 2px;
    background: linear-gradient(135deg, #00ffff, #ff00ff);
    border-radius: 50%;
    pointer-events: none;
    animation: floatUp 10s linear infinite;
    opacity: 0;
}

@keyframes floatUp {
    0% {
        transform: translateY(100vh);
        opacity: 0;
    }
    10% {
        opacity: 0.8;
    }
    90% {
        opacity: 0.8;
    }
    100% {
        transform: translateY(-100vh);
        opacity: 0;
    }
}

/* Responsive Design */
@media (max-width: 768px) {
    .cyber-title {
        font-size: 2.5rem;
    }
    .typewriter {
        font-size: 0.8rem;
        white-space: normal;
    }
    .glow-text {
        font-size: 1.2rem;
    }
}
            
</style>
""", unsafe_allow_html=True)

# Create images directory if it doesn't exist
Path("image").mkdir(exist_ok=True)

# ================== IMAGE LOADER FUNCTION ==================
@st.cache_data
def get_image_base64(image_path):
    """Convert image to base64 for HTML embedding"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

@st.cache_data
def load_image_path():
    """Load profile image from multiple possible locations"""
    possible_paths = [
        Path("images/profile.png"),
        Path("image/profile.png"),
        Path("profile.png"),
        Path.cwd() / "images" / "profile.png",
        Path.cwd() / "image" / "profile.png",
        Path(__file__).parent / "images" / "profile.png",
        Path(__file__).parent / "image" / "profile.png",
    ]
    
    for path in possible_paths:
        if path.exists():
            return path
    return None

# Get image path
image_path = load_image_path()
img_base64 = get_image_base64(image_path) if image_path else None

# ================== PARTICLES BACKGROUND ==================
particles_html = ""
for i in range(80):
    left = (i * 1.25) % 100
    delay = i * 0.1
    duration = 8 + (i % 12)
    size = 2 + (i % 3)
    particles_html += f"""
    <div class="particle" style="
        left: {left}%;
        animation-duration: {duration}s;
        animation-delay: {delay}s;
        width: {size}px;
        height: {size}px;
    "></div>
    """
st.markdown(particles_html, unsafe_allow_html=True)

# ================== ENHANCED SIDEBAR ==================
with st.sidebar:
    # Profile Section with Image
    if img_base64:
        st.markdown(f"""
        <div class="sidebar-profile">
            <div class="sidebar-avatar">
                <img src="data:image/png;base64,{img_base64}" alt="Antonio Luba">
            </div>
            <div class="sidebar-name">ANTONIO LUBA</div>
            <div class="sidebar-title">Computer Science Student</div>
            <div class="sidebar-title" style="font-size: 0.7rem; color: #00ffff; margin-top: 8px;">
                <span class="status-indicator"></span> SYSTEM ONLINE
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="sidebar-profile">
            <div class="sidebar-avatar">
                <div style="font-size: 3rem;">👨‍💻</div>
            </div>
            <div class="sidebar-name">ANTONIO LUBA</div>
            <div class="sidebar-title">Computer Science Student</div>
            <div class="sidebar-title" style="font-size: 0.7rem; color: #00ffff; margin-top: 8px;">
                <span class="status-indicator"></span> SYSTEM ONLINE
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick Stats
    st.markdown("""
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin: 15px 0;">
        <div class="sidebar-stats">
            <div class="sidebar-stat-number">10+</div>
            <div class="sidebar-stat-label">PROJECTS</div>
        </div>
        <div class="sidebar-stats">
            <div class="sidebar-stat-number">2+</div>
            <div class="sidebar-stat-label">YEARS</div>
        </div>
        <div class="sidebar-stats">
            <div class="sidebar-stat-number">5+</div>
            <div class="sidebar-stat-label">CERTIFICATIONS</div>
        </div>
        <div class="sidebar-stats">
            <div class="sidebar-stat-number">15+</div>
            <div class="sidebar-stat-label">TECHNOLOGIES</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Contact Info
    st.markdown("""
    <div style="margin: 15px 0;">
        <div style="color: #00ffff; font-size: 0.75rem; letter-spacing: 2px; margin-bottom: 10px;">
            📡 CONTACT
        </div>
        <div style="font-size: 0.8rem; color: #ccc; margin: 8px 0;">
            📧 antonioluba285@gmail.com
        </div>
        <div style="font-size: 0.8rem; color: #ccc; margin: 8px 0;">
            📞 +63 985 3165 737
        </div>
        <div style="font-size: 0.8rem; color: #ccc; margin: 8px 0;">
            📍 Masbate, Philippines
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Social Links
    st.markdown("""
    <div style="margin: 15px 0;">
        <div style="color: #00ffff; font-size: 0.75rem; letter-spacing: 2px; margin-bottom: 10px;">
            🔗 CONNECT
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lubashft18)")
    with col2:
        st.markdown("[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:antonioluba285@gmail.com)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://web.facebook.com/antonio.luba.18)")
    with col2:
        st.markdown("")
    
    st.markdown("---")
# ================== WELCOME PAGE ==================

# Hero Title
st.markdown("""
<div style="text-align: center;">
    <div class="cyber-title">ANTONIO LUBA</div>
    <div class="typewriter-container">
        <div class="typewriter"> COMPUTER SCIENCE STUDENT * DEVELOPER * CYBERSECURITY</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Welcome Section
st.markdown("""
<div class="hero-container">
    <div class="welcome-badge">
        ⚡ WELCOME TO MY DIGITAL REALM ⚡
    </div>
    <div class="glow-text">
         Hello, I'm Antonio Luba
    </div>
    <div class="welcome-description">
        I'm a passionate Computer Science student dedicated to crafting innovative digital solutions. 
        I specialize in building robust web applications, exploring cybersecurity frontiers, 
        and pushing the boundaries of what's possible with technology.
    </div>
    <div style="margin-top: 2rem;">
        <div style="display: inline-block; background: rgba(0, 255, 0, 0.1); border: 1px solid #00ff00; border-radius: 5px; padding: 0.5rem 1rem;">
            <span style="color: #00ff00;">●</span> STATUS: <span style="color: #00ff00;">ACTIVE & AVAILABLE FOR WORK</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Enhanced Navigation Cards Section
st.markdown('<h2 style="text-align: center; color: #00ffff; margin: 2rem 0 1rem 0; font-family: monospace;">⚡ EXPLORE MY PORTFOLIO</h2>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

# Enhanced About Me Card
with col1:
    st.markdown("""
    <div class="nav-card" onclick="window.location.href='pages/2_👤_About.py'">
        <div class="nav-icon">👤</div>
        <div class="nav-title">ABOUT ME</div>
        <div class="nav-desc">Learn my story & background</div>
        <div class="about-preview">
            Computer Science student with passion for tech innovation and problem-solving.
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("📖 Read More", key="about_btn", use_container_width=True):
        st.switch_page("pages/2_👤_About.py")

# Enhanced Skills Card
with col2:
    st.markdown("""
    <div class="nav-card" onclick="window.location.href='pages/3_💪_Skills.py'">
        <div class="nav-icon">💪</div>
        <div class="nav-title">SKILLS</div>
        <div class="nav-desc">Discover my expertise</div>
        <div class="skills-preview">
            <span class="skill-tag">Python</span>
            <span class="skill-tag">JavaScript</span>
            <span class="skill-tag">PHP</span>
            <span class="skill-tag">SQL</span>
            <span class="skill-tag">HTML </span>
            <span class="skill-tag">CSS </span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🚀 View Skills", key="skills_btn", use_container_width=True):
        st.switch_page("pages/3_💪_Skills.py")

# Enhanced Projects Card
with col3:
    st.markdown("""
    <div class="nav-card" onclick="window.location.href='pages/4_📁_Projects.py'">
        <div class="nav-icon">📁</div>
        <div class="nav-title">PROJECTS</div>
        <div class="nav-desc">View my work</div>
        <div class="about-preview" style="font-size: 0.7rem;">
            🔥 10+ completed projects<br>
            💡 Innovative solutions<br>
            🚀 Real-world applications
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("📂 Browse Projects", key="projects_btn", use_container_width=True):
        st.switch_page("pages/4_📁_Projects.py")

# Enhanced Contact Card
with col4:
    st.markdown("""
    <div class="nav-card" onclick="window.location.href='pages/5_📧_Contact.py'">
        <div class="nav-icon">📧</div>
        <div class="nav-title">CONTACT</div>
        <div class="nav-desc">Get in touch</div>
        <div class="about-preview" style="font-size: 0.7rem;">
            ✉️ Email me<br>
            💬 Quick response<br>
            🤝 Let's collaborate
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("💬 Send Message", key="contact_btn", use_container_width=True):
        st.switch_page("pages/5_📧_Contact.py")

# Call to Action
st.markdown("""
<div class="cta-container">
    <div style="
        background: linear-gradient(135deg, rgba(0,255,255,0.08), rgba(255,0,255,0.08));
        border-radius: 30px;
        padding: 3rem 2rem;
        margin: 2rem 0;
        border: 1px solid rgba(0,255,255,0.2);
    ">
        <div style="font-size: 1.8rem; margin-bottom: 1rem; color: #fff; font-weight: bold;">✨ Let's Create Something Amazing</div>
        <div style="color: #aaa; margin-bottom: 2rem; font-size: 1rem;">Ready to bring your ideas to life? I'm just a message away.</div>
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("⚡ START A CONVERSATION", use_container_width=True):
        with st.spinner("Initializing secure connection..."):
            time.sleep(0.8)
            st.success("✅ Connection established!")
            st.balloons()
            time.sleep(0.5)
            st.switch_page("pages/5_📧_Contact.py")

# Footer
st.markdown("""
<div style="text-align: center; padding: 2rem; margin-top: 1rem;">
    <div style="color: #00ffff; font-family: monospace; font-size: 0.8rem; letter-spacing: 2px;">
        ═══════════════════════════════════════<br>
        ⚡ SYSTEM READY | EXPLORE USING THE CARDS ABOVE ⚡<br>
        ═══════════════════════════════════════
    </div>
</div>
""", unsafe_allow_html=True)