import streamlit as st
from pathlib import Path
from datetime import datetime
import base64

st.set_page_config(
    page_title="Antonio Luba | Projects",
    page_icon="📁",
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

/* Section Headers */
.section-header {
    color: #00ffff;
    font-size: 1.5rem;
    margin: 2rem 0 1.5rem 0;
    border-left: 3px solid #00ffff;
    padding-left: 15px;
    font-family: monospace;
}

/* ================== PROJECT CARDS STYLES ================== */
.projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 25px;
    margin: 2rem 0;
}

.project-card {
    background: linear-gradient(135deg, rgba(10, 20, 30, 0.8), rgba(0, 50, 50, 0.6));
    backdrop-filter: blur(10px);
    border: 1px solid rgba(0, 255, 255, 0.2);
    border-radius: 15px;
    overflow: hidden;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    position: relative;
}

.project-card:hover {
    transform: translateY(-10px);
    border-color: #00ffff;
    box-shadow: 0 20px 40px rgba(0, 255, 255, 0.3);
}

.project-image {
    position: relative;
    overflow: hidden;
    height: 200px;
}

.project-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
}

.project-card:hover .project-image img {
    transform: scale(1.1);
}

.project-overlay {
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

.project-card:hover .project-overlay {
    opacity: 1;
}

.btn-view {
    background: linear-gradient(90deg, #00ffff, #ff00ff);
   color: #000000 !important;
    padding: 10px 25px;
    border-radius: 30px;
    text-decoration: none;
    font-weight: bold;
    font-family: monospace;
    transition: all 0.3s ease;
}

.btn-view:hover {
    transform: scale(1.05);
    box-shadow: 0 0 20px rgba(0, 255, 255, 0.5);
            color: #000000 !important;
}

.project-content {
    padding: 20px;
}

.project-content h4 {
    color: #00ffff;
    font-size: 1.3rem;
    margin-bottom: 10px;
    font-family: 'Space Grotesk', monospace;
}

.project-tech {
    margin: 10px 0;
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.tech-tag {
    background: rgba(0, 255, 255, 0.1);
    border: 1px solid rgba(0, 255, 255, 0.3);
    border-radius: 20px;
    padding: 4px 12px;
    font-size: 0.7rem;
    color: #00ffff;
    font-family: 'Share Tech Mono', monospace;
}

.project-content p {
    color: #ccc;
    font-size: 0.9rem;
    line-height: 1.5;
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

/* Responsive */
@media (max-width: 768px) {
    .cyber-title {
        font-size: 2.5rem;
    }
    .projects-grid {
        grid-template-columns: 1fr;
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

# ================== IMAGE LOADER ==================
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

# ================== SIDEBAR ==================
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
            <div class="sidebar-stat-number">6+</div>
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

# ================== MAIN CONTENT ==================

# Header Section
st.markdown('<h1 class="cyber-title">MY PROJECTS</h1>', unsafe_allow_html=True)
st.markdown('<p class="cyber-subtitle">REAL-WORLD APPLICATIONS * INNOVATIVE SOLUTIONS</p>', unsafe_allow_html=True)

# Projects Data
projects = [
    {
        "title": "Enrollment System",
        "img": "image/SNHS logo.jpg",
        "link": "https://simawanhsenrollment.42web.io",
        "tech": ["PHP", "MySQL", "Bootstrap"],
        "description": "Full-featured student enrollment system with database management, file upload capabilities, and comprehensive admin panel for efficient student data processing."
    },
    {
        "title": "SNHS Reading Hub",
        "img": "image/book.png",
        "link": "https://simawanhsreadinghub.free.nf",
        "tech": ["HTML5", "CSS3", "JavaScript"],
        "description": "A modern, student-friendly reading platform featuring organized content, responsive design, and an engaging collection of educational and inspiring reads."
    },
    {
        "title": "Cafe'Han Coffee Website",
        "img": "image/logo.png",
        "link": "https://coffeewebsite.github.io/cafehan",
        "tech": ["HTML5", "CSS3", "JavaScript"],
        "description": "A visually stunning coffee website with smooth animations, responsive layout, and a warm café-inspired user experience showcasing menu items and brand story."
    },
    {
        "title": "Love Surprise Gallery",
        "img": "image/love_logo.png",
        "link": "https://lovesurprise.lovestoblog.com",
        "tech": ["HTML5", "CSS3", "JavaScript"],
        "description": "A special romantic birthday gift website designed as a digital surprise gallery, featuring interactive elements and heartfelt animations to celebrate love."
    },
    {
        "title": "Code Breaker Algebra System",
        "img": "image/codebreaker.png",
        "link": "https://codebreakeralgebra.gamer.gd/",
        "tech": ["HTML5", "CSS3", "JavaScript", "Gamification", "MySQL", "PHP"],
        "description": "An interactive algebra learning platform developed for Cataingan National High School, featuring equation solving, code-breaking puzzles, and step-by-step problem solving to help students master mathematical concepts."
    },
    {
        "title": "Panique NHS Attendance System",
        "img": "image/panique_logo.jpg",
        "link": "https://attendancesystem.web1337.net/",
        "tech": ["HTML5", "CSS3", "JavaScript", "Face Recognition", "MySQL", "PHP"],
        "description": "A smart and automated attendance monitoring system developed for Panique National High School. This system utilizes face recognition technology to accurately record student attendance in real-time. It features a secure admin dashboard, student database management, attendance reports, and analytics to improve efficiency, accuracy, and transparency in daily attendance tracking."
    }
]

# Helper function to get image base64 from local file
def get_project_image_base64(img_path):
    """Load project image and return base64 string"""
    # Try multiple possible locations
    possible_paths = [
        Path(img_path),
        Path("pages") / img_path,
        Path(__file__).parent / img_path,
        Path(__file__).parent.parent / img_path,
    ]
    for path in possible_paths:
        if path.exists():
            try:
                with open(path, "rb") as f:
                    return base64.b64encode(f.read()).decode()
            except:
                pass
    return None

# Display projects in grid using columns
st.markdown('<div class="projects-grid">', unsafe_allow_html=True)

# Create rows of 3 columns
for i in range(0, len(projects), 3):
    cols = st.columns(3)
    for j in range(3):
        idx = i + j
        if idx < len(projects):
            project = projects[idx]
            # Get image base64
            img_b64 = get_project_image_base64(project["img"])
            if img_b64:
                img_src = f"data:image/png;base64,{img_b64}"
            else:
                # Fallback to placeholder
                img_src = "https://via.placeholder.com/350x200?text=Project+Image"
            
            # Create tech tags HTML
            tech_tags = "".join([f'<span class="tech-tag">{tech}</span>' for tech in project["tech"]])
            
            with cols[j]:
                st.markdown(f"""
                <div class="project-card">
                    <div class="project-image">
                        <img src="{img_src}" alt="{project['title']}">
                        <div class="project-overlay">
                            <a href="{project['link']}" class="btn-view" target="_blank">Live Demo</a>
                        </div>
                    </div>
                    <div class="project-content">
                        <h4>{project['title']}</h4>
                        <div class="project-tech">
                            {tech_tags}
                        </div>
                        <p>{project['description']}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ================== CALL TO ACTION ==================
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 40px; background: linear-gradient(135deg, rgba(0,255,255,0.05), rgba(255,0,255,0.05)); border-radius: 15px; margin: 20px 0;">
    <div style="font-size: 1.5rem; margin-bottom: 10px;">💡 Have a Project in Mind?</div>
    <div style="color: #888; margin-bottom: 20px;">Let's collaborate and bring your ideas to life</div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("📧 CONTACT ME", use_container_width=True):
        st.switch_page("pages/5_📧_Contact.py")

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