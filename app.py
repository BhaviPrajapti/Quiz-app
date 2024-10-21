from flask import Flask, render_template, request,redirect, url_for,flash,session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key= 'quiz_All_data'
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'adm_quiz_question'

mysql = MySQL(app)
# Quiz data
# quiz_data = [
#     {"question": "What does CPU stand for?", "answer": "central processing unit"},
#     {"question": "What does GPU stand for?", "answer": "graphics processing unit"},
#     {"question": "What does RAM stand for?", "answer": "random access memory"},
#     {"question": "What does PSU stand for?", "answer": "power supply"},
# ]
# ----Client Route ----

# defult Route user question write answer
@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT question,option1,option2,option3,option4,correct_answer FROM adm_question")
    fetchdata = cur.fetchall()
    cur.close()
    quiz_data = [{'question': row[0],'option1': row[1],'option2': row[2],'option3': row[3],'option4':row[4],'correct_answer': row[5]} for row in fetchdata]
    session['quiz_data'] = quiz_data
    return render_template('quiz.html', quiz_data=quiz_data)




# user submit answer 
@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    quiz_data = session.get('quiz_data') 
    total_questions = len(quiz_data)
    user_answers = request.form.to_dict()
    feedback = {}
    for  i,item in enumerate(quiz_data):
        user_answer = request.form.get(f'user_answer{i}', "")
        correct_answer = item['correct_answer']
        if user_answer == correct_answer:
            feedback[item['question']] = {'message': 'Your answer is correct!', 'correct': True}
            score += 1
        else:
            feedback[item['question']] = {'message': 'Your answer is incorrect.', 'correct': False, 'correct_answer': correct_answer}

    percentage = (score / total_questions) * 100
    # Pass both the score and user's answers to the result page
    return render_template('result.html', user_answers=user_answers, score=score, total_questions=total_questions, percentage=percentage, feedback=feedback)

# ----admin Route ----

# admin route displayed question/answer
@app.route('/admin')
def admin():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM adm_question")
    fetchdata = cur.fetchall()
    cur.close()
    fetchdata = [{'id': row[0], 'question': row[1], 'option1': row[2],'option2': row[3],'option3': row[4],'option4':row[5],'correct_answer': row[6]} for row in fetchdata]
    return render_template('/admin/question.html', quiz_data=fetchdata)


# Admin add question and answer Route
@app.route('/add_question', methods=['POST'])
def add_question():
    question = request.form['question']
    option1 = request.form['firstotn']
    option2 = request.form['sendoptn']
    option3 = request.form['thirdotn']
    option4 = request.form['fourotn']
    correct_answer = request.form['rightans']

    # Insert the new question and answer into the database
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO adm_question (question, option1,option2,option3,option4,correct_answer) VALUES (%s, %s,%s, %s,%s, %s)", (question, option1,option2,option3,option4,correct_answer))
    mysql.connection.commit()
    cur.close()
    #flash("Question added successfully!", "success")
    return redirect(url_for('admin'))  # Redirect to the admin page

# Admin edit  question and answer Route
@app.route('/update_question', methods=['POST'])
def update_question():
    question_id = request.form['id']
    question_text = request.form['question']
    option1_text = request.form['option1']
    option2_text = request.form['option2']
    option3_text = request.form['option3']
    option4_text = request.form['option4']
    correct_answer_text = request.form['correct_answer']

    # Update the database logic here
    cur = mysql.connection.cursor()
    cur.execute("UPDATE adm_question SET question=%s, answer=%s WHERE id=%s", (question_id ,question_text, option1_text, option2_text,option3_text,option4_text,correct_answer_text))
    mysql.connection.commit()
    cur.close()

    return redirect(url_for('admin')) # Redirect back to the admin page

#Admin Delete question and answer Route
@app.route('/delete_question', methods=['POST'])
def delete_question():
    question_id = request.form['id']

    # Execute the delete query
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM adm_question WHERE id = %s", [question_id])
    mysql.connection.commit()
    cur.close()

    return redirect(url_for('admin'))  # Redirect back to the admin page

if __name__ == "__main__":
    app.run(debug=True)
