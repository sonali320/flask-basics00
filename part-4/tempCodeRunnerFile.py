from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

# ---------------- HOME ----------------
@app.route('/')
def home():
    return render_template('index.html')

# ---------------- USER PROFILE ----------------
@app.route('/user/<username>')
def user_profile(username):
    return render_template('user.html', username=username)

# ---------------- POST ----------------
@app.route('/post/<int:post_id>')
def show_post(post_id):
    posts = {
        1: {'title': 'Getting Started with Flask', 'content': 'Flask is a micro-framework...'},
        2: {'title': 'Understanding Routes', 'content': 'Routes map URLs to functions...'},
        3: {'title': 'Working with Templates', 'content': 'Jinja2 makes HTML dynamic...'},
    }
    post = posts.get(post_id)
    return render_template('post.html', post_id=post_id, post=post)

# ---------------- USER POST ----------------
@app.route('/user/<username>/post/<int:post_id>')
def user_post(username, post_id):
    return render_template('user_post.html', username=username, post_id=post_id)

# ---------------- ABOUT ----------------
@app.route('/about/')
def about():
    return render_template('about.html')

# ---------------- LINKS ----------------
@app.route('/links')
def show_links():
    links = {
        'home': url_for('home'),
        'about': url_for('about'),
        'user_alice': url_for('user_profile', username='Alice'),
        'user_bob': url_for('user_profile', username='Bob'),
        'post_1': url_for('show_post', post_id=1),
        'post_2': url_for('show_post', post_id=2),
    }
    return render_template('links.html', links=links)

# ==============================
# Exercise 4.1: Product Page
# ==============================
@app.route('/product/<int:product_id>')
def product(product_id):
    products = {
        1: {'name': 'Laptop', 'price': 75000},
        2: {'name': 'Smartphone', 'price': 25000},
        3: {'name': 'Headphones', 'price': 1500},
    }
    product = products.get(product_id)
    return render_template('product.html', product=product, product_id=product_id)

# ==============================
# Exercise 4.2: Category & Product
# ==============================
@app.route('/category/<category_name>/product/<int:product_id>')
def category_product(category_name, product_id):
    products = {
        1: {'name': 'Laptop', 'price': 75000},
        2: {'name': 'Smartphone', 'price': 25000},
        3: {'name': 'Headphones', 'price': 1500},
    }
    product = products.get(product_id)
    return render_template('category_product.html', category=category_name, product=product)

# ==============================
# Exercise 4.3: Search
# ==============================
@app.route('/search/<query>')
def search(query):
    return render_template('search.html', query=query)

# Optional search form redirect
@app.route('/search', methods=['GET', 'POST'])
def search_form():
    if request.method == 'POST':
        query = request.form.get('query')
        return redirect(url_for('search', query=query))
    return render_template('search_form.html')

# ==============================
if __name__ == '__main__':
    app.run(debug=True)