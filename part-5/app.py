"""
Part 5: Mini Project - Personal Website with Flask
===================================================
A complete personal website using everything learned in Parts 1-4.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template

app = Flask(__name__)

# =============================================================================
# YOUR DATA - Customize this section with your own information!
# =============================================================================

PERSONAL_INFO = {
    'name': 'Sonali',
    'title': 'Web Developer',
    'bio': 'A passionate developer learning Flask and web development.',
    'email': 'sonalikadale197@gmail.com',
    'github': 'https://github.com/sonali320',
    'linkedin': 'https://linkedin.com/in/yourusername',
}

SKILLS = [
    {"name": "Python", "level": 78},
    {"name": "HTML & CSS", "level": 83},
    {"name": "SQL", "level": 89}
]

PROJECTS = [
    {'id': 1, 'name': 'Personal Website', 'description': 'A Flask-powered personal portfolio website.', 'tech': ['Python', 'Flask', 'HTML', 'CSS'], 'status': 'Completed'},
    {'id': 2, 'name': 'Inventory Management', 'description': 'A simple task management application.', 'tech': ['Python', 'Flask', 'SQLite'], 'status': 'Completed'},
    {'id': 3, 'name': 'Weather Dashboard', 'description': 'Display weather data from an API.', 'tech': ['Python', 'Flask', 'API'], 'status': 'Planned'},
]


# =============================================================================
# ROUTES
# =============================================================================

@app.route('/')
def home():
    return render_template('index.html', info=PERSONAL_INFO)


@app.route("/about")
def about():
    info = {
        "name": "Test User",
        
    }

    skills = [
        {"name": "Python", "level": 73},
        {"name":"HTML & CSS", "level":78},
        {"name": "SQL", "level": 89}
    ]

    return render_template("about.html", info=info, skills=skills)

    

@app.route('/projects')
def projects():
    return render_template('projects.html', info=PERSONAL_INFO, projects=PROJECTS)


@app.route('/project/<int:project_id>')  # Dynamic route for individual project
def project_detail(project_id):
    project = None
    for p in PROJECTS:
        if p['id'] == project_id:
            project = p
            break
    return render_template('project_detail.html', info=PERSONAL_INFO, project=project, project_id=project_id)

@app.route("/blog")
def blog():
    info = {
        "name": "Sonali Kadale"
    }

    posts = [
        {
            "title": "Getting Started with Flask",
            "date": "Jan 4, 2026",
            "category": "Flask",
            "summary": "A beginner-friendly introduction to Flask."
        },
        {
            "title": "Why I Love Python",
            "date": "Jan 2, 2026",
            "category": "Python",
            "summary": "My journey learning Python and why it’s amazing."
        }
    ]

    return render_template("blog.html", info=info, posts=posts)



@app.route('/contact')
def contact():
    return render_template('contact.html', info=PERSONAL_INFO)




if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# PROJECT STRUCTURE:
# =============================================================================
#
# part-5/
# ├── app.py              <- You are here
# ├── static/
# │   └── style.css       <- CSS styles
# └── templates/
#     ├── base.html       <- Base template (inherited by all pages)
#     ├── index.html      <- Home page
#     ├── about.html      <- About page
#     ├── projects.html   <- Projects list
#     ├── project_detail.html <- Single project view
#     └── contact.html    <- Contact page
#
# =============================================================================

# =============================================================================
# EXERCISES:
# =============================================================================
#
# Exercise 5.1: Personalize your website
#   - Update PERSONAL_INFO with your real information
#   - Add your actual skills and projects
#
# Exercise 5.2: Add a new page
#   - Create a /blog route
#   - Add blog posts data structure
#   - Create blog.html template
#
# Exercise 5.3: Enhance the styling
#   - Modify static/style.css
#   - Add your own color scheme
#   - Make it responsive for mobile
#
# Exercise 5.4: Add more dynamic features
#   - Create a /skill/<skill_name> route
#   - Show projects that use that skill
#
# =============================================================================
