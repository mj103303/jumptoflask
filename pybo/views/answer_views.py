from flask import Blueprint, render_template, redirect, url_for, request
from datetime import datetime

from pybo import db     
# migrate는 안가지고오네
from ..forms import AnswerForm
from pybo.models import Question, Answer

bp = Blueprint("answer", __name__, url_prefix="/answer")

@bp.route("/create/<int:question_id>", methods=["POST"])
def create(question_id):
    form = AnswerForm()    
    question = Question.query.get_or_404(question_id)
    
    if request.method == "POST" and form.validate_on_submit():
        content = request.form.get("content")
        answer = Answer(content=content, create_date=datetime.now())
        '''
            answer = Answer(question=question, content, create_date=datetime.now())
            db.session.add(answer)
            db.session.commit()
            이렇게 해도, 저장가능 >> 존나 불편하네
            question=릴레이션할 질문 적는겨
        '''
        question.answer_set.append(answer)
        db.session.commit()
        return redirect(url_for('question.detail', question_id=question_id))

    return render_template('question/question_detail.html', question=question, form=form)