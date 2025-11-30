"""
Namakkal Logistics India (P) Ltd (NLIPL) - Website
A Flask-based website for transport and logistics company
"""

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Company Information
COMPANY_INFO = {
    "name": "Namakkal Logistics India (P) Ltd",
    "short_name": "NLIPL",
    "tagline": "We Carry With Care",
    "phone": "+91 44 XXXX XXXX",
    "email": "info@namakkallogistics.com",
    "address": "Dr. T.K. Murthy Street, New Kuberan Nagar, 4 - Ground Floor, Chennai, Tamil Nadu 600091",
    "website": "www.namakkallogistics.com",
    "linkedin": "https://www.linkedin.com/company/namakkal-logistics-india-p-ltd/"
}

# Services offered
SERVICES = [
    {
        "title": "Project Logistics",
        "description": "End-to-end project cargo solutions for heavy and oversized shipments across India.",
        "icon": "🏗️"
    },
    {
        "title": "General Transportation",
        "description": "Reliable road freight services with a comprehensive fleet for all cargo types.",
        "icon": "🚛"
    },
    {
        "title": "Warehousing & 3PL",
        "description": "State-of-the-art warehousing facilities with complete supply chain management.",
        "icon": "🏭"
    },
    {
        "title": "Freight Forwarding",
        "description": "Seamless international freight forwarding with multimodal transport solutions.",
        "icon": "✈️"
    },
    {
        "title": "Custom Clearance",
        "description": "Expert customs brokerage services ensuring smooth cross-border shipments.",
        "icon": "📋"
    },
    {
        "title": "ODC Transportation",
        "description": "Specialized over-dimensional cargo movement with precision and safety.",
        "icon": "⚙️"
    }
]

# Industries served
INDUSTRIES = [
    "Renewable Energy",
    "Oil & Gas",
    "Power & Transmission",
    "Manufacturing",
    "Automotive",
    "FMCG",
    "Pharmaceuticals",
    "E-Commerce",
    "Construction",
    "Steel & Metals"
]

# Stats
STATS = [
    {"number": "17+", "label": "Years of Excellence"},
    {"number": "20+", "label": "Dedicated Employees"},
    {"number": "Pan-India", "label": "Network Coverage"},
    {"number": "Bank", "label": "Approved Operator"}
]

# About content from LinkedIn
ABOUT_CONTENT = {
    "intro": "Welcome to NLIPL – a trailblazer in the transport and logistics industry since 2007.",
    "description": "With a robust foundation established in 2011, we have evolved into a dynamic force with over 20 dedicated employees. NLIPL is not just a logistics company; we are the architects of seamless connectivity across diverse topographies.",
    "mission": "Our journey began with a commitment to excellence, and over the years, we've mastered the art of navigating complexities with precision and reliability.",
    "highlight": "As a bank-approved transport operator, NLIPL operates on a nationwide scale, with branches strategically positioned across India. From serving FMCG giants to collaborating with ISRO, our versatile portfolio showcases our ability to cater to a broad spectrum of clientele.",
    "closing": "Join us on this journey as we continue to redefine logistics, connect businesses, and contribute to the growth and success of enterprises across India.",
    "motto": "Where Logistics Meets Excellence"
}

# Leadership Team
LEADERSHIP = [
    {
        "name": "G V Barathwaaj",
        "role": "Managing Director",
        "bio": "A visionary leader in transport and logistics, Barathwaaj has been the driving force behind NLIPL's remarkable growth since its inception. With deep expertise in supply chain management and operations, he has built NLIPL from the ground up into a trusted pan-India logistics partner. His strategic vision and hands-on approach have enabled the company to serve prestigious clients including FMCG giants and collaborate with ISRO, establishing NLIPL as a leader in specialized transportation.",
        "linkedin": "https://www.linkedin.com/in/gv-barathwaaj-832120294/",
        "image": None
    }
]

# Team Members
TEAM_MEMBERS = [
    {
        "name": "Coming Soon",
        "role": "Traffic Manager",
        "bio": "Oversees daily transportation operations and route optimization.",
        "image": None
    },
    {
        "name": "Coming Soon",
        "role": "Marketing Manager",
        "bio": "Drives brand growth and client acquisition strategies.",
        "image": None
    },
    {
        "name": "Coming Soon",
        "role": "Accounts Manager",
        "bio": "Manages financial operations and client relationships.",
        "image": None
    },
    {
        "name": "Coming Soon",
        "role": "Vehicle Fleet Co-ordinator",
        "bio": "Coordinates fleet management and vehicle maintenance.",
        "image": None
    }
]


@app.route('/')
def home():
    return render_template('index.html', 
                         company=COMPANY_INFO,
                         services=SERVICES,
                         industries=INDUSTRIES,
                         stats=STATS,
                         about=ABOUT_CONTENT,
                         leadership=LEADERSHIP,
                         team=TEAM_MEMBERS)


@app.route('/contact', methods=['POST'])
def contact():
    """Handle contact form submissions"""
    data = request.form
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    message = data.get('message')
    
    # In production, you would save this to a database or send an email
    print(f"Contact Form Submission:")
    print(f"Name: {name}, Email: {email}, Phone: {phone}")
    print(f"Message: {message}")
    
    return jsonify({"status": "success", "message": "Thank you for your inquiry. We will contact you soon!"})


if __name__ == '__main__':
    app.run(debug=True, port=5000)

