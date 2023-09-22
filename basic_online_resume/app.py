from flask import Flask, render_template

app = Flask(__name__)


resume = {
        "name": "Your Name",
        "title": "Web Developer",
        "contact_info": {
            "email": "youremail@example.com",
            "phone": "123-456-7890",
            "linkedin": "https://www.linkedin.com/in/your-profile",
            "github": "https://github.com/yourusername",
        },
        "summary": "A passionate web developer with a strong foundation in front-end and back-end technologies.",
        "education": [
            {
                "degree": "Bachelor of Science in Computer Science",
                "school": "Your University",
                "year": "20XX",
            },
            {
                "degree": "Web Development Certification",
                "school": "Coding Bootcamp",
                "year": "20XX",
            },
        ],
        "work_experience": [
            {
                "title": "Software Engineer",
                "company": "Tech Company Inc.",
                "dates": "20XX - Present",
                "description": "Developed and maintained web applications using HTML, CSS, and JavaScript.",
            },
            {
                "title": "Web Developer",
                "company": "Web Design Studio",
                "dates": "20XX - 20XX",
                "description": "Designed and implemented responsive and user-friendly websites for clients.",
            },
        ],
        "skills": [
            "HTML5",
            "CSS3",
            "JavaScript",
            "Python",
            "React.js",
            "Node.js",
            "SQL",
        ],
    }
@app.route("/")
def index():
    return render_template('resume.html',resume=resume)

if __name__ == '__main__':
    app.run(host='localhost', port=5001)
