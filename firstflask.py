from flask import Flask, render_template, request, render_template_string
import random
import json

app = Flask(__name__)

@app.route("/") 
def helloworld():
    return "Hello, World!"

@app.route("/stat") 
def helloSTAT():
    return "Hello, STAT KKU!"


@app.route("/research")
def research_page():
    faculty_research = {
    "Dr. Alice Smith": [
        "สภาพอากาศ Statistical Modeling of Climate Change Impacts",
        "อนุกรมเวลา Advanced Methods in Time Series Analysis",
        "การเรียนรู้ของเครื่อง Machine Learning Applications in Biostatistics",
    ],
    "Dr. Bob Johnson": [
        "เบเบ Bayesian Inference in Social Sciences",
        "เศรษฐกิจ Quantitative Analysis of Economic Trends",
        "Development of Robust Statistical Software",
    ],
    "Dr. Carol Davis": [
        "Optimization Techniques in Big Data Analytics",
        "Statistical Approaches to Epidemiology",
        "Survey Data Analysis for Policy Decisions",
    ],
    }

    random_faculty, random_research_projects = random.choice(list(faculty_research.items()))
    
    return render_template("research.html", faculty=random_faculty, research_projects=random_research_projects)

@app.route("/contact",methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        user_email = request.form.get("email")
        with open("email.txt", "a") as myfile:
            myfile.write(f"{user_email}\n")
        return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Admin Contact</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f9;
                color: #333;
            }
            header {
                background-color: #0078d7;
                color: white;
                padding: 1rem 0;
                text-align: center;
            }
            nav {
                background-color: #005ea6;
                display: flex;
                justify-content: center;
                padding: 0.5rem 0;
            }
            nav a {
                color: white;
                text-decoration: none;
                margin: 0 1rem;
            }
            nav a:hover {
                text-decoration: underline;
            }
            main {
                padding: 2rem;
                text-align: center;
            }
            footer {
                background-color: #0078d7;
                color: white;
                text-align: center;
                padding: 1rem 0;
                position: fixed;
                bottom: 0;
                width: 100%;
            }
        </style> 
    </head>
    <body>
        <header>
            <h1>Admin Contact</h1>
            <p>Only accessible by administrators.</p>
        </header>
        <nav>
            <a href="/statHTML">Home</a>
            <a href="/statHTML#about">About Us</a>
            <a href="/statHTML#programs">Programs</a>
            <a href="/statHTML#research">Research</a>
            <a href="/statHTML#contact">Contact</a>
            <a href="/contact">Contact admin</a>
        </nav>
        
        <section>
            <h2>Administrator Contact Details</h2>
            <p>For any administrative inquiries, you can reach us via the following contact details:</p>

            <ul>
                <li><strong>Email:</strong> admin@example.com</li>
                <li><strong>Phone:</strong> +1-800-555-1234</li>
            </ul>

            <p>If you have any further questions, feel free to email us directly or contact our support team.</p>
            
            <h2>Submit Your Email So We Can Contact You Back</h2>
            <h2>Thank you {{user}}</h2>

            <p></p>
        </section>
        <a href="/statHTML">
            <button>Home</button>
        </a>
    
        <footer>
            <p>&copy; 2025 Your Company. All rights reserved.</p>
        </footer>
    </body>
   
    </html>

    """,user=user_email)
    else:
        return """
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Admin Contact</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f9;
                color: #333;
            }
            header {
                background-color: #0078d7;
                color: white;
                padding: 1rem 0;
                text-align: center;
            }
            nav {
                background-color: #005ea6;
                display: flex;
                justify-content: center;
                padding: 0.5rem 0;
            }
            nav a {
                color: white;
                text-decoration: none;
                margin: 0 1rem;
            }
            nav a:hover {
                text-decoration: underline;
            }
            main {
                padding: 2rem;
                text-align: center;
            }
            footer {
                background-color: #0078d7;
                color: white;
                text-align: center;
                padding: 1rem 0;
                position: fixed;
                bottom: 0;
                width: 100%;
            }
        </style> 
    </head>
    <body>
        <header>
            <h1>Admin Contact</h1>
            <p>Only accessible by administrators.</p>
        </header>
        <nav>
            <a href="/statHTML">Home</a>
            <a href="/statHTML#about">About Us</a>
            <a href="/statHTML#programs">Programs</a>
            <a href="/statHTML#research">Research</a>
            <a href="/statHTML#contact">Contact</a>
            <a href="/contact">Contact admin</a>
        </nav>
        
        <section>
            <h2>Administrator Contact Details</h2>
            <p>For any administrative inquiries, you can reach us via the following contact details:</p>

            <ul>
                <li><strong>Email:</strong> admin@example.com</li>
                <li><strong>Phone:</strong> +1-800-555-1234</li>
            </ul>

            <p>If you have any further questions, feel free to email us directly or contact our support team.</p>
            
            <h2>Submit Your Email So We Can Contact You Back</h2>
            <form method="POST">
            <label for="email">Your Email:</label>
            <input type="email" id="email" name="email" required placeholder="Enter your email">
            <button type="submit">Submit</button>
            </form>

            <p></p>
        </section>
        <a href="/statHTML">
            <button>Home</button>
        </a>
    
        <footer>
            <p>&copy; 2025 Your Company. All rights reserved.</p>
        </footer>
    </body>
   
    </html>

    """

@app.route("/statHTML") 
def helloSTAThtml():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Stat KKU - Homepage</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f9;
                color: #333;
            }
            header {
                background-color: #0078d7;
                color: white;
                padding: 1rem 0;
                text-align: center;
            }
            nav {
                background-color: #005ea6;
                display: flex;
                justify-content: center;
                padding: 0.5rem 0;
            }
            nav a {
                color: white;
                text-decoration: none;
                margin: 0 1rem;
            }
            nav a:hover {
                text-decoration: underline;
            }
            main {
                padding: 2rem;
                text-align: center;
            }
            footer {
                background-color: #0078d7;
                color: white;
                text-align: center;
                padding: 1rem 0;
                position: fixed;
                bottom: 0;
                width: 100%;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Welcome to Stat KKU</h1>
            <p>Department of Statistics, Khon Kaen University</p>
        </header>
        <nav>
            <a href="#about">About Us</a>
            <a href="#programs">Programs</a>
            <a href="/research">Research</a>
            <a href="#contact">Contact</a>
            <a href="/contact">Contact admin</a>
        </nav>
        <main>
            <section id="cookiesclicking">
                <h2>cookiesclicking</h2>
                <p>In the world of <strong>Cookie Clicker</strong>, there was once a peaceful kingdom where the inhabitants spent their days baking cookies. The aroma of freshly baked treats filled the air, bringing joy to all who lived there. This kingdom, known as <strong>The Cookie Kingdom</strong>, was ruled by a wise and benevolent king, <strong>Cookie King</strong>, who had a secret: he had discovered the power of the mystical <strong>Cookie</strong>.</p>
    
                <p>One day, a dark figure named <strong>The Grandmapocalypse</strong> appeared, claiming to be the rightful ruler of the Cookie Kingdom. With his arrival, the kingdom's cookies began to disappear mysteriously. The inhabitants grew desperate, as the once-bountiful cookie supply started dwindling. No one knew how to stop him, and the kingdom fell into chaos.</p>
                
                <p>But not all hope was lost. A <strong>Baker</strong>, an ordinary citizen with a love for baking, stood up to the threat. The Baker, armed with nothing but a rolling pin and an unyielding spirit, set off on an epic journey to reclaim the lost cookies and stop The Grandmapocalypse.</p>
                
                <p>Along the way, the Baker discovered <strong>Ancient Relics</strong>, each one imbued with the power to make cookies faster, to summon magical helpers, and even to control time itself. These relics were hidden in long-forgotten realms, some of which were ruled by creatures known as <strong>Wrinklers</strong>, mysterious entities who seemed to feed off the cookies produced by the kingdom.</p>
                
                <p>The Baker wasn't alone. Alongside him were other legendary heroes, such as the <strong>Cookie Production Wizards</strong>, who had the ability to cast powerful spells that turned ingredients into cookies at unimaginable speeds. There were also the <strong>Angry Grandmas</strong>, whose strength increased with each cookie the kingdom produced, and they were just as fierce as they were sweet.</p>
                
                <p>As the Baker ventured deeper into the Cookie Kingdom’s history, he uncovered the <strong>Furnaces of Fate</strong>, enormous ovens that could bake cookies in the blink of an eye. But these were not ordinary ovens—they were linked to the ancient <strong>Cookie Gods</strong>, powerful beings who had long since retreated into the <strong>Cookie Dimension</strong>, leaving behind only cryptic messages about the true nature of cookies and their significance to the universe.</p>
                
                <p>In a climactic battle at the <strong>Cookie Castle</strong>, the Baker faced off against The Grandmapocalypse. With the help of the mystical relics and the <strong>Cookie Gods</strong>, he was able to reverse the curse that had gripped the kingdom. But in doing so, the Baker learned that the cookies were not just a source of sustenance—they were the key to unlocking the very fabric of reality itself.</p>
                
                <p>As the kingdom rejoiced and the cookies flowed freely once more, the Baker realized that the true journey had just begun. The realm of cookies was far more expansive than anyone could have imagined. And somewhere, deep within the layers of dough and frosting, new adventures awaited those brave enough to keep clicking.</p>
                
            <section id="about">
                <h2>About Us</h2>
                <p>The Department of Statistics at Khon Kaen University is dedicated to excellence in teaching and research in the field of statistics.</p>
            </section>
            <section id="programs">
                <h2>Programs</h2>
                <p>We offer undergraduate and postgraduate programs in statistics to prepare students for successful careers.</p>
            </section>
            <section id="research">
                <h2>Research</h2>
                <p>Our faculty members are engaged in cutting-edge research to address real-world challenges using statistical methods.</p>
            </section>
            <section id="contact">
                <h2>Contact</h2>
                <p>Email: info@statkku.ac.th</p>
                <p>Phone: +66-1234-5678</p>
            </section>
        </main>
        <footer>
            <p>&copy; 2025 Stat KKU. All rights reserved.</p>
        </footer>
    </body>
    </html>
    """

##api
# @app.route('/simpleAPI',methods=['POST']) 
# def web_service_API():

#     payload = request.data.decode("utf-8")
#     inmessage = json.loads(payload) # ทำ json

#     print(inmessage)
    
    
#     json_data = json.dumps({'y': 'received!'}) # ส่งกลับไปว่าได้รับเเล้ววว
#     return json_data

# @app.route('/simpleAPI',methods=['POST']) 
# def web_service_API():
#     # รับข้อมูล JSON จาก request
#     payload = request.data.decode("utf-8")
#     inmessage = json.loads(payload)
    
#     # ดึง IP ของผู้เรียกใช้งาน
#     client_ip = request.remote_addr  # หรือจะใช้ request.headers.get('X-Forwarded-For', request.remote_addr) ก็ได้

#     # ลองพิมพ์ข้อมูลพร้อม IP ลง console
#     print("Received from IP:", client_ip)
#     print("Message:", inmessage['msg'])

#     # ส่งกลับ JSON ที่มี IP ด้วย
#     json_data = json.dumps({
#         'client_ip': client_ip,
#         'y': 'received!'
#     })
#     return json_data

@app.route('/simpleAPI', methods=['POST'])
def web_service_API():
    # ดึงข้อมูลจาก request
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent')
    referrer = request.referrer
    request_method = request.method
    request_url = request.url
    headers = dict(request.headers)
    body_data = request.get_json(silent=True)  # JSON payload ถ้ามี
    cookies = request.cookies  # Cookie ที่แนบมา
    
    # รวมข้อมูลทั้งหมดใน response
    response_data = {
        "client_ip": client_ip,
        "user_agent": user_agent,
        "referrer": referrer,
        "request_method": request_method,
        "request_url": request_url,
        "headers": headers,
        "body_data": body_data,
        "cookies": cookies
    }

    # แสดงข้อมูลใน console
    print(json.dumps(response_data, indent=4))

    return json.dumps(response_data, indent=4)



if __name__ == "__main__":   # run code
    # app.run(host='0.0.0.0',debug=True,port=5001) #host='0.0.0.0' = run on internet ,port=5001 
    app.run()