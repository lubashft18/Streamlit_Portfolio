import streamlit as st
from pathlib import Path
from datetime import datetime
import base64
import pandas as pd
import os

st.set_page_config(
    page_title="Antonio Luba | Skills & Certificates",
    page_icon="💪",
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
    width: 120px;
    height: 120px;
    border-radius: 15px;
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

/* Cyber Title */
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

/* Cyber Subtitle */
.cyber-subtitle {
    text-align: center;
    color: #00ffff;
    letter-spacing: 3px;
    margin-bottom: 2rem;
    font-size: 0.9rem;
    text-transform: uppercase;
    font-family: monospace;
}

/* Cyber Card */
.cyber-card {
    background: rgba(10, 20, 30, 0.7);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(0, 255, 255, 0.3);
    border-radius: 15px;
    padding: 25px;
    transition: all 0.3s ease;
    height: 100%;
}

.cyber-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 30px rgba(0, 255, 255, 0.2);
    border-color: #00ffff;
}

/* Section Headers */
.section-header {
    color: #00ffff;
    font-size: 1.5rem;
    margin: 2rem 0 1.5rem 0;
    border-left: 3px solid #00ffff;
    padding-left: 15px;
    font-family: monospace;
}

/* ================== CERTIFICATES STYLES ================== */
.certificates-container {
    margin: 2rem 0;
}

.certificates-container h3 {
    color: #00ffff;
    font-size: 1.8rem;
    margin: 2rem 0 1.5rem 0;
    font-family: 'Share Tech Mono', monospace;
    border-bottom: 1px solid rgba(0, 255, 255, 0.3);
    display: inline-block;
    padding-bottom: 5px;
}

.certificates-grid {
    text-align: center;
    margin: 1.5rem 0;
}

.certificate-card {
    display: inline-block;
    width: 500px;
    margin: 15px;
    vertical-align: top;
    background: linear-gradient(135deg, rgba(10, 20, 30, 0.8), rgba(0, 50, 50, 0.6));
    backdrop-filter: blur(10px);
    border: 1px solid rgba(0, 255, 255, 0.2);
    border-radius: 15px;
    overflow: hidden;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    position: relative;
    text-align: left;
}

.certificate-card:hover {
    transform: translateY(-10px);
    border-color: #00ffff;
    box-shadow: 0 20px 40px rgba(0, 255, 255, 0.3);
}

.certificate-image {
    position: relative;
    overflow: hidden;
    background: rgba(0, 0, 0, 0.3);
    display: flex;
    align-items: center;
    justify-content: center;
    height: 180px;
    flex-shrink: 0;
}

.certificate-image img {
    width: 100%;
    height: auto;
    object-fit: contain;
    transition: transform 0.5s ease;
}

.certificate-card:hover .certificate-image img {
    transform: scale(1.02);
}

.certificate-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.7);
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transition: opacity 0.3s ease;
}

.certificate-card:hover .certificate-overlay {
    opacity: 1;
}

.btn-view {
    background: linear-gradient(90deg, #00ffff, #ff00ff);
    color: #0a0a0a;
    padding: 10px 25px;
    border-radius: 30px;
    text-decoration: none;
    font-weight: bold;
    font-family: monospace;
    transition: all 0.3s ease;
}

.btn-view:hover {
    background: linear-gradient(90deg, #00ffff, #ff00ff);
    color: #000000 !important;
    transform: scale(1.05);
    box-shadow: 0 0 20px rgba(0, 255, 255, 0.5);
}

.certificate-content {
    padding: 20px;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
}

.certificate-content h4 {
    color: #00ffff;
    font-size: 1.2rem;
    margin-bottom: 10px;
    font-family: 'Space Grotesk', monospace;
}

.certificate-content p {
    color: #ccc;
    font-size: 0.85rem;
    line-height: 1.5;
    margin-bottom: 15px;
    flex-grow: 1;
}

.certificate-date {
    color: #ff00ff;
    font-size: 0.75rem;
    font-family: 'Share Tech Mono', monospace;
    display: block;
    margin-top: 10px;
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

/* Status Bar */
.status-bar {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: rgba(0, 0, 0, 0.9);
    backdrop-filter: blur(5px);
    color: #00ff00;
    text-align: center;
    padding: 10px;
    font-family: monospace;
    font-size: 0.8rem;
    border-top: 1px solid #00ffff;
    z-index: 999;
    letter-spacing: 1px;
}

/* Responsive Design */
@media (max-width: 768px) {
    .cyber-title {
        font-size: 2.5rem;
    }
    .certificate-card {
        width: calc(100% - 30px);
    }
}
</style>
""", unsafe_allow_html=True)

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

# ================== FIXED IMAGE LOADER FOR CORRECT PATH ==================
@st.cache_data
def get_image_base64(image_path):
    """Convert image to base64 for HTML embedding"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception as e:
        return None

def get_cert_image(filename):
    """Load certificate image from the correct image folder"""
    # Get the current file's directory (pages folder)
    current_dir = Path(__file__).parent
    
    # Go up one level to the main portfolio_app folder
    main_dir = current_dir.parent
    
    # Possible paths for the image
    possible_paths = [
        main_dir / "image" / filename,                    # portfolio_app/image/filename
        main_dir / "images" / filename,                   # portfolio_app/images/filename
        current_dir / "image" / filename,                 # pages/image/filename
        current_dir / "images" / filename,                # pages/images/filename
        Path.cwd() / "image" / filename,                  # current working directory/image/filename
        Path.cwd() / "images" / filename,                 # current working directory/images/filename
        Path("/mount/src/your-repo-name/porfolio_app/image") / filename,  # Streamlit Cloud path
        Path("/mount/src/your-repo-name/porfolio_app/images") / filename, # Streamlit Cloud path
        Path("/mount/src/your-repo-name/image") / filename,  # Alternative Streamlit Cloud path
    ]
    
    for path in possible_paths:
        if path.exists():
            return get_image_base64(path)
    
    return None

def load_profile_image():
    """Load profile image from the correct location"""
    current_dir = Path(__file__).parent
    main_dir = current_dir.parent
    
    possible_paths = [
        main_dir / "image" / "profile.png",
        main_dir / "images" / "profile.png",
        current_dir / "image" / "profile.png",
        current_dir / "images" / "profile.png",
        Path.cwd() / "image" / "profile.png",
        Path.cwd() / "images" / "profile.png",
    ]
    
    for path in possible_paths:
        if path.exists():
            return get_image_base64(path)
    
    return None

# ================== SIDEBAR ==================
with st.sidebar:
    # Profile Section with Image
    img_base64 = load_profile_image()
    
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
            <div class="sidebar-stat-number">5+</div>
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
            <div class="sidebar-stat-number">6+</div>
            <div class="sidebar-stat-label">TECHNOLOGIES</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    
    # Navigation
    st.markdown("## 🧭 Navigation")
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")
    if st.button("👤 About Me", use_container_width=True):
        st.switch_page("pages/2_👤_About.py")
    if st.button("📁 Projects", use_container_width=True):
        st.switch_page("pages/4_📁_Projects.py")
    if st.button("📧 Contact", use_container_width=True):
        st.switch_page("pages/5_📧_Contact.py")
    
    st.markdown("---")
    
    # Social Links
    st.markdown("### 🔗 Connect")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lubashft18)")
    with col2:
        st.markdown("[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:antonioluba285@gmail.com)")
    
    st.markdown("---")

# ================== MAIN CONTENT ==================

# Header Section
st.markdown('<h1 class="cyber-title">TECHNICAL SKILLS</h1>', unsafe_allow_html=True)
st.markdown('<p class="cyber-subtitle">PROGRAMMING LANGUAGES * WEB TECHNOLOGIES * CERTIFICATIONS</p>', unsafe_allow_html=True)

# ================== SKILLS DATA ==================
# Programming Languages
st.markdown('<div class="section-header">💻 PROGRAMMING LANGUAGES</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.markdown("**🐍 Python**")
    st.progress(70)
    st.markdown("**🌐 HTML**")
    st.progress(80)
    st.markdown("**🎨 CSS**")
    st.progress(80)
    st.markdown("**⚡ JavaScript**")
    st.progress(70)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.markdown("**🐘 PHP**")
    st.progress(75)
    st.markdown("**⚙️ C**")
    st.progress(40)
    st.markdown("**🔧 C++**")
    st.progress(50)
    st.markdown("**🗄️ MySQL**")
    st.progress(50)
    st.markdown('</div>', unsafe_allow_html=True)

# ================== WEB TECHNOLOGIES ==================
st.markdown('<div class="section-header">🌐 WEB TECHNOLOGIES</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.markdown("**📱 Frontend Development**")
    st.write("• HTML5 & CSS3 - 80%")
    st.write("• JavaScript (ES6+) - 70%")
    st.write("• Responsive Design - 75%")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.markdown("**⚙️ Backend Development**")
    st.write("• PHP - 75%")
    st.write("• Python - 70%")
    st.write("• MySQL - 50%")
    st.markdown('</div>', unsafe_allow_html=True)

# ================== SKILLS MATRIX ==================
st.markdown('<div class="section-header">📊 SKILLS MATRIX</div>', unsafe_allow_html=True)

skills_data = {
    'Skill': ['HTML', 'CSS', 'JavaScript', 'PHP', 'Python', 'MySQL', 'C', 'C++'],
    'Proficiency (%)': [80, 80, 70, 75, 70, 50, 40, 50]
}
df_skills = pd.DataFrame(skills_data).set_index('Skill')

st.bar_chart(df_skills, height=400, use_container_width=True)

# ================== DATABASES & SECURITY ==================
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section-header">🗄️ DATABASES</div>', unsafe_allow_html=True)
    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.markdown("**MySQL**")
    st.progress(50)
    st.markdown("**Learning & Improving**")
    st.write("• Basic queries and operations")
    st.write("• Database design fundamentals")
    st.write("• CRUD operations")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="section-header">🔒 CYBERSECURITY</div>', unsafe_allow_html=True)
    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.markdown("**Security Knowledge**")
    st.write("• Network Security Basics")
    st.write("• Security Best Practices")
    st.write("• CTF Participation")
    st.write("• Bug Bounty Hunting")
    st.markdown('</div>', unsafe_allow_html=True)

# ================== LEARNING JOURNEY ==================
st.markdown('<div class="section-header">📈 LEARNING JOURNEY</div>', unsafe_allow_html=True)

st.markdown("""
<div class="cyber-card">
    <strong style="color: #00ffff;">&gt; CURRENT FOCUS</strong><br><br>
    • Improving Python skills for automation and AI/ML<br>
    • Deepening MySQL and database management knowledge<br>
    • Enhancing JavaScript and modern web frameworks<br>
    • Building full-stack web applications<br>
    <br>
    <strong style="color: #00ffff;">&gt; NEXT MILESTONES</strong><br><br>
    • Master advanced Python concepts<br>
    • Complete certification in cybersecurity<br>
    • Build 10+ portfolio projects<br>
    • Contribute to open-source projects<br>
    • Learn React and modern frameworks
</div>
""", unsafe_allow_html=True)

# ================== CERTIFICATES SECTION ==================
st.markdown('<div class="section-header">🏆 CERTIFICATES & AWARDS</div>', unsafe_allow_html=True)

# Helper function to display certificate with fallback
def display_certificate(title, img_filename, pdf_filename, description, issue_date):
    cert_img = get_cert_image(img_filename)
    
    if cert_img:
        img_src = f"data:image/png;base64,{cert_img}"
    else:
        # Use a styled placeholder
        img_src = f"https://via.placeholder.com/350x200/0a0f1a/00ffff?text={title.replace(' ', '+')}"
    
    # Fix PDF path - go up one level from pages folder
    current_dir = Path(__file__).parent
    main_dir = current_dir.parent
    pdf_path = main_dir / "pdf" / pdf_filename
    
    # Use relative path for PDF link
    if pdf_path.exists():
        pdf_link = f"../pdf/{pdf_filename}"
    else:
        pdf_link = f"pdf/{pdf_filename}"
    
    st.markdown(f"""
    <div class="certificate-card">
        <div class="certificate-image">
            <img src="{img_src}" alt="{title}">
            <div class="certificate-overlay">
                <a href="{pdf_link}" class="btn-view" target="_blank">View Certificate</a>
            </div>
        </div>
        <div class="certificate-content">
            <h4>{title}</h4>
            <p>{description}</p>
            <span class="certificate-date">Issued: {issue_date}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Cisco Certificates
st.markdown('<h3 style="color: #00ffff; font-size: 1.8rem; margin: 2rem 0 1.5rem 0; font-family: monospace;">CISCO NetAcad Certification</h3>', unsafe_allow_html=True)
st.markdown('<div class="certificates-grid">', unsafe_allow_html=True)

display_certificate(
    "HTML Essentials",
    "html_cert.png",
    "_certificate_antonioluba285-gmail-com_64e236ca-3935-460e-9f0d-c066538326e7 (1).pdf",
    "Completed Cisco Networking Academy's HTML Essentials course, gaining foundational skills in HTML structure, semantic markup, and website content organization.",
    "March 18, 2025"
)

display_certificate(
    "CSS Essentials",
    "css_cert.png",
    "_certificate_antonioluba285-gmail-com_aa55d699-17e9-437e-aedb-be53c80042c0.pdf",
    "Completed Cisco Networking Academy's CSS Essentials course, covering responsive design, Flexbox, Grid layouts, and modern styling techniques.",
    "April 22, 2025"
)

st.markdown('</div>', unsafe_allow_html=True)

# HackerRank Certificates
st.markdown('<h3 style="color: #00ffff; font-size: 1.8rem; margin: 2rem 0 1.5rem 0; font-family: monospace;">HackerRank Certification</h3>', unsafe_allow_html=True)
st.markdown('<div class="certificates-grid">', unsafe_allow_html=True)

display_certificate(
    "Python (Basic)",
    "python_cert.png",
    "python_basic certificate.pdf",
    "Earned HackerRank's Python (Basic) Certification, demonstrating core Python programming skills including data structures, control flow, and functions.",
    "May 6, 2025"
)

display_certificate(
    "Problem Solving (Basic)",
    "problemsolve_cert.png",
    "problem_solving_basic certificate.pdf",
    "Achieved HackerRank's Problem Solving (Basic) Certification, validating fundamental algorithmic thinking and logical reasoning skills.",
    "May 5, 2025"
)

display_certificate(
    "CSS (Basic)",
    "cssbasic_cert.png",
    "css certificate.pdf",
    "Completed CSS Basic Certification, demonstrating essential web styling and layout skills including selectors, box model, and responsive design.",
    "May 5, 2025"
)

st.markdown('</div>', unsafe_allow_html=True)

# ================== CALL TO ACTION ==================
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 40px; background: linear-gradient(135deg, rgba(0,255,255,0.05), rgba(255,0,255,0.05)); border-radius: 15px; margin: 20px 0;">
    <div style="font-size: 1.5rem; margin-bottom: 10px;">🚀 Ready to See My Work?</div>
    <div style="color: #888; margin-bottom: 20px;">Check out my projects and see these skills in action</div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("📁 VIEW MY PROJECTS", use_container_width=True):
        st.switch_page("pages/4_📁_Projects.py")

# ================== STATUS BAR ==================
current_time = datetime.now().strftime("%H:%M:%S")
st.markdown(f"""
<div class="status-bar">
    <span class="status-indicator"></span> SYSTEM: ONLINE | 
    TIME: {current_time} | 
    CONNECTION: SECURE | 
    READY FOR INPUT
</div>
""", unsafe_allow_html=True)

# Add padding for status bar
st.markdown("<br><br>", unsafe_allow_html=True)