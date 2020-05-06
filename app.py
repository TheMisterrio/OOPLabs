from flask import Flask, render_template, redirect, url_for, request, abort, flash
from Fractions import Fraction
from Money import Money
from List import List
from Trapezoid import Trapezoid
from String import String, ComplexNum

app = Flask(__name__)
app.secret_key = '123456789'


@app.route('/')
def hello_world():
    return redirect(url_for('lab1'))


@app.route('/lab1', methods=['GET', 'POST'])
def lab1():
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        operation = request.form.get('operation')
        try:
            num1_formatted = Fraction(num1.split('.')[0], num1.split('.')[1])
            num2_formatted = Fraction(num2.split('.')[0], num2.split('.')[1])
            if operation == '+':
                result_formatted = num1_formatted + num2_formatted
            if operation == '-':
                result_formatted = num1_formatted - num2_formatted
            if operation == '*':
                result_formatted = num1_formatted * num2_formatted
            if operation == '=':
                result_formatted = num1_formatted == num2_formatted
            if operation == '>':
                result_formatted = num1_formatted > num2_formatted
            if operation == '<':
                result_formatted = num1_formatted < num2_formatted
            result = str(result_formatted)
        except:
            abort(404)
        return render_template('lab1.html', num1=num1, num2=num2, operation=operation, result=result)
    return render_template('lab1.html')


@app.route('/lab2', methods=['GET', 'POST'])
def lab2():
    if request.method=='POST':
        try:
            num1 = Money(int(request.form.get('num1_value')), int(request.form.get('num1_coins')))
            num2 = Money(int(request.form.get('num2_value')), int(request.form.get('num2_coins')))
            operation = request.form.get('operation')
            if operation == '+':
                result = num1+num2
            if operation == '-':
                result = num1-num2
            if operation == '=':
                result = num1 == num2
            if operation == '>':
                result = num1 > num2
            if operation == '<':
                result = num1 < num2
        except:
            abort(404)
        return render_template('lab2.html', num1=num1, num2=num2, operation=operation, result=result)
    return render_template('lab2.html', num1=Money(0, 0), num2=Money(0, 0))


@app.route('/lab3', methods=['GET', 'POST'])
def lab3():
    if request.method == 'POST':
        cor1 = request.form.get('cor1').split(';')
        cor2 = request.form.get('cor2').split(';')
        cor3 = request.form.get('cor3').split(';')
        cor4 = request.form.get('cor4').split(';')
        trapezoid = Trapezoid(cor1, cor2, cor3, cor4)
        cors = [';'.join(cor1), ';'.join(cor2), ';'.join(cor3), ';'.join(cor4)]
        if trapezoid.isEquilateral():
            flash('Фігура є рівнобічною трапецією. Інформація про неї виведена', 'success')
            info = {'sides': trapezoid.side_length(),
                    'perimeter': trapezoid.perimeter(),
                    'square': trapezoid.square()}
            return render_template('lab3.html', info=info, cors=cors)
        else:
            flash('Фігура не є рівнобічною трапецією', 'danger')
            return render_template('lab3.html', cors=cors)
    return render_template('lab3.html', cors=['', '', '', ''])


@app.route('/lab4', methods=['GET', 'POST'])
def lab4():
    num1_1, num1_2, num2_1, num2_2 = '0', '0', '0', '0'
    s, result = 'lol', ''
    if request.method == 'POST':
        try:
            if request.form['submit'] == 'Довжина рядка':
                s = request.form.get('string')
                st = String(s)
                result = st.get_length()
            if request.form['submit'] == 'Додавання':
                num1_1 = request.form.get('num1_1')
                num1_2 = request.form.get('num1_2')
                num2_1 = request.form.get('num2_1')
                num2_2 = request.form.get('num2_2')
                num1 = ComplexNum(num1_1, num1_2)
                num2 = ComplexNum(num2_1, num2_2)
                result = num1+num2
            if request.form['submit'] == 'Множення':
                num1_1 = request.form.get('num1_1')
                num1_2 = request.form.get('num1_2')
                num2_1 = request.form.get('num2_1')
                num2_2 = request.form.get('num2_2')
                num1 = ComplexNum(num1_1, num1_2)
                num2 = ComplexNum(num2_1, num2_2)
                result = num1 * num2
            if request.form['submit'] == 'Порівняння':
                num1_1 = request.form.get('num1_1')
                num1_2 = request.form.get('num1_2')
                num2_1 = request.form.get('num2_1')
                num2_2 = request.form.get('num2_2')
                num1 = ComplexNum(num1_1, num1_2)
                num2 = ComplexNum(num2_1, num2_2)
                result = num1 == num2
            return render_template('lab4.html', result=result, string=s, num1_1=num1_1,
                                   num1_2=num1_2, num2_1=num2_1, num2_2=num2_2)
        except:
            pass
    return render_template('lab4.html', result=result, string=s, num1_1=num1_1, num1_2=num1_2,
                           num2_1=num2_1, num2_2=num2_2)


@app.route('/lab5', methods=['GET', 'POST'])
def lab5():
    if request.method == 'POST':
        try:
            if request.form['submit'] == 'Створити новий список':
                items = request.form.get('item').split(';')
                l = List(*items)
                flash('Список створено', 'success')
            if request.form['submit'] == 'Добавити елемент в початок':
                item = request.form.get('item').split(';')
                prev_l = '' if request.form.get('list') == '' else request.form.get('list').split(';')
                l = List(*prev_l)
                l.add_first(*item)
                flash(';'.join(item) + ' добавлено на початок', 'success')
            if request.form['submit'] == 'Добавити елемент в кінець':
                item = request.form.get('item').split(';')
                prev_l = '' if request.form.get('list') == '' else request.form.get('list').split(';')
                l = List(*prev_l)
                l.add_last(*item)
                flash(';'.join(item) + ' добавлено в кінець', 'success')
            if request.form['submit'] == 'Видалити елемент':
                item = request.form.get('item')
                prev_l = '' if request.form.get('list') == '' else request.form.get('list').split(';')
                l = List(*prev_l)
                if l.remove_item(item):
                    flash('Усі входження елемента ' + item + ' видалено успішно', 'success')
                else:
                    flash('Елемент не знайдено', 'danger')
            if request.form['submit'] == 'Кількість входжень елемента':
                item = request.form.get('item')
                prev_l = '' if request.form.get('list') == '' else request.form.get('list').split(';')
                l = List(*prev_l)
                count = l.count_item(item)
                if count == 0:
                    flash('Елемент не знайдено', 'danger')
                else:
                    flash('Елемент зустрічається у кількості: ' + str(count), 'success')
            str_list = ';'.join(l.l)
            return render_template('lab5.html', list=str_list)
        except:
            abort(404)
    return render_template('lab5.html')


if __name__ == '__main__':
    app.run(debug=True)
