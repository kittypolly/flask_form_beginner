from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                    RadioField, SelectField,TextField,
                    TextAreaField, SubmitField)
#데이터의 유효성을 검사합니다. DataRequired를 이용하면 form의 그 항목의 데이터가 없을때 오류메세지를 보냅니다.
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'AOA'

class InfoForm(FlaskForm):

    #choice의 앞에 것이 세션을 통해 submission으로 넘어간다. 뒤에꺼는 label로 활용된다.
    #즉, 뒤는 보여주는 값 앞이 넘어가는 값이다.
    #형식은 동일하다 .무엇.필드(.묻는내용., .함수명.=[])
    
    group_name = StringField("당신은 어떤 그룹을 좋아하시나요?", validators = [DataRequired()])
    debut_year = RadioField("몇 년도에 데뷔한 그룹인가요?", 
                        choices=[('1990','1990년'), ('2000','2000년'), ('2010','2010년'), ('2020','2020년')])
    buy_album = BooleanField("앨범을 구매하신 적이 있나요?")
    service = SelectField(u"다음 중 가장 좋아하는 행사를 골라주세요.", choices = [('팬미팅','팬미팅'),('콘서트','콘서트'),('팬사인회','팬사인회')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')
    
@app.route('/', methods=['GET','POST'])
def index():

    form = InfoForm()

    if form.validate_on_submit():
        session['group_name'] = form.group_name.data
        session['debut_year'] = form.debut_year.data
        session['buy_album'] = form.buy_album.data
        session['service'] = form.service.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('submission'))

    return render_template('home.html', form=form)

@app.route('/submission')
def submission():
    return render_template('submission.html')


if __name__ == '__main__':
    app.run(debug=True)
        
    