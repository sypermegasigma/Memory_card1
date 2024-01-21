#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,QHBoxLayout,QRadioButton,QGroupBox
from random import shuffle,randint
#создание приложения и главного окна
app = QApplication([])
main_win = QWidget()

main_win.resize(400,200)

#создание виджетов главного окна
main_win.setWindowTitle('Конкурс от Crazy People')


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


question = QLabel('Какой национальности не существует?')
layout_main = QVBoxLayout()
btn_ok = QPushButton('Ответить')

RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1) 


AnsGroup = QGroupBox("прав ответ")
ib_result = QLabel("f")
ib_Correct = QLabel("ответ будет тут")

layout_res = QVBoxLayout()
layout_res.addWidget(ib_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(ib_Correct, alignment=Qt.AlignHCenter, stretch=2)

#layout_ans1.addWidget(RadioGroupBox,stretch=8)
AnsGroup.setLayout(layout_res) 
AnsGroup.hide()

layouth1 = QHBoxLayout()
layouth2 = QHBoxLayout()
layouth3 = QHBoxLayout()

layouth1.addWidget(question, alignment = Qt.AlignCenter)
layouth2.addStretch(1)
layouth2.addWidget(RadioGroupBox,stretch=8)
layouth2.addWidget(AnsGroup,stretch=8)
layouth2.addStretch(1)
layouth3.addStretch(1)
layouth3.addWidget(btn_ok, stretch=2)
layouth3.addStretch(1)


layout_main.addLayout(layouth1)
layout_main.addLayout(layouth2)
layout_main.setSpacing(50)
layout_main.addLayout(layouth3)
layout_main.setSpacing(50)

main_win.setLayout(layout_main)
def show_result():
    '''показать панель ответа'''
    RadioGroupBox.hide()
    AnsGroup.show()
    btn_ok.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroup.hide()
    btn_ok.setText('Ответить')
    '''RadioGroupBox.setExclusive(False)'''


answers = [rbtn_1, rbtn_2,rbtn_3, rbtn_4]
def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    ib_Correct.setText(q.right_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов: ', main_win.score)
    else:
        if answers[1].isChecked or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
        #window = QWidget()

def show_correct(res):
    ib_result.setText(res)
    show_result()


question_list = []
q1 = Question("кто я?",'python-ист', 'архитектор','не знаю', 'игрок') 
question_list.append(q1)

question_list.append(Question("сколько скинов на io в дота 2?",'2', '1','3', '4'))

question_list.append(Question("сколько надо с4 на мвк дверь?",'4', '3','2', '5'))
question_list.append(Question("когда вышел стим?", "22 марта 2002 года" , "24 марта 2004 года" , '15 мая 1998 года' , "22 апреля 2001 года"))
question_list.append(Question("Максимальная скорость, с которой игрок может лететь, выпрыгнув из самолета? ", "230 km/h" , "234km/h" , "324km/h" , "124 km/h") )
question_list.append(Question("Сколько надо хаешек чтоб убить игрока в кс? " , "1", "2", "3", "5"))
question_list.append(Question("Сколько видов гранат есть в кс го? " , "5", "2", "3", "1"))


def next_question():
    main_win.total += 1
    print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов: ', main_win.score)
    cur_question = randint (0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)

def click_OK():
    if btn_ok.text() == 'Ответить':
        check_answer()
    else:
        next_question()


print(question_list)


main_win.total =0
main_win.score = 0
next_question()

btn_ok.clicked.connect(click_OK)

#отображение окна приложения 
main_win.show()
app.exec_()
