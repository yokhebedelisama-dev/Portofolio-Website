from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    data = {
        "name": "Yokhebed Elisama",
        "title": "Computer Science Educator | Software Developer",
        "email": "yokhebedelisama2@gmail.com",
        "location": "Jember, East Java",
        "education": "Bachelor of Informatics Engineering - University of Muhammadiyah Jember",
        "gpa": "3.69/4.00",
        "summary": "A Computer Science professional and educator specializing in Data Structures, Algorithms, and Backend Systems. Skilled in architecting scalable solutions through Database Management and Cloud Computing, with a commitment to advancing technical literacy and mentoring future developers.",
      "skills": {
            "Programming": ["Python", "C++", "Java", "JavaScript"],
            "Database": ["PostgreSQL", "MySQL", "Relational Design"],
            "Cloud & DevOps": ["Google Cloud Platform", "Cloud Run", "Docker", "Git/GitHub"],
            "Networking": ["TCP/IP", "Cisco Packet Tracer", "Network Security"]
        },
        "experience": [
            {
                "year": "2024",
                "role": "Cloud Computing Graduate",
                "org": "Bangkit Academy 2024 (by Google, GoTo, Traveloka)",
                "desc": "Built and deployed scalable microservices on GCP. Handled API integration and containerization for a high-traffic Capstone Project."
            },
            {
                "year": "2024-2025",
                "role": "Computer Science Educator",
                "org": "MSCS Surabaya",
                "desc": "Designed a comprehensive curriculum for Python and Database Management. Mentored students in Computational Thinking and Data Structures."
            },
            {
                "year": "2023",
                "role": "Database Systems Lab Assistant",
                "org": "University of Muhammadiyah Jember",
                "desc": "Guided 50+ students in practical database implementation and query optimization."
            }
        ],
        "experience": [
            {
                "year": "2024",
                "role": "Cloud Computing Path",
                "org": "Bangkit Academy 2024",
                "desc": "Mastered cloud-native applications and networking using Google Cloud Run."
            },
            {
                "year": "2024-2025",
                "role": "Computer Science Teacher",
                "org": "MSCS Surabaya",
                "desc": "Taught core subjects including data analysis, databases, and Python."
            }
        ],
        "projects": [
            {
        "title": "Inventory & Asset Tracking", 
        "png": "P1.png", 
        "category": "web",
        "desc": "A robust asset management system designed to streamline resource allocation and tracking using relational database normalization."
    },
    {
        "title": "Payroll & Salary Slip Generator", 
        "png": "P2.png", 
        "category": "web",
        "desc": "Automated financial system for high-accuracy salary computation and dynamic PDF report generation."
    },
    {
        "title": "DP Divisi Purchasing", 
        "png": "P3.png", 
        "category": "web",
        "desc": "User interface analysis and prototyping for procurement workflows, focused on enhancing user experience and task efficiency."
    },
    {
        "title": "School Website", 
        "png": "P4.png", 
        "category": "web",
        "desc": "Full-stack educational platform deployed on Google Cloud, utilizing Cloud Run for scalable and high-availability performance."
    }
        ]
    }
    return render_template('index.html', d=data)

if __name__ == '__main__':
    app.run(debug=True)