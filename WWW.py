# -*- coding: utf-8 -*-
# quiz/quiz.py

from flask import Flask,request
from flask import render_template

app = Flask(__name__)


app.config.update(dict(
    SECRET_KEY='bradzosekretnawartosc',
))

# lista pytań 1


DANE2  = [{
    'pytanie': 'Czy jesteś studentem WETI:',  # pytanie
    'odpowiedzi': ['Tak', 'Nie'],  # możliwe odpowiedzi
    },  # poprawna odpowiedź
    {
    'pytanie': 'Jestem:',
    'odpowiedzi': ['Mężczyzną', 'Kobietą'],
    },
    {
    'pytanie': 'Jestem na semestrze:',
    'odpowiedzi': ['II', 'IV', 'VI','VIII'],
    },
    {
    'pytanie': 'Mieszkam :',
    'odpowiedzi': ['Sam', 'Z rodzicami', 'Z partnerem','Ze współlokatorami'],
    },
    {
    'pytanie': 'Czy przyłapałeś się na " posiedzę jeszcze pare minut i wyłączam?',
    'odpowiedzi': ['1', '2', '3', '4', '5'],
    },
    {
    'pytanie': 'Czy obawiasz się tego, że gdyby odcięto Internet życie byłoby nudne, puste i bez radości?',
    'odpowiedzi': ['1', '2', '3', '4', '5'],
    },
{
    'pytanie': 'Czy próbujesz ograniczyć swój czas spędzony w sieci?',
    'odpowiedzi': ['1', '2', '3', '4', '5'],
    },
{
    'pytanie': 'Czy zdarzyło Ci się naskoczyć na kogoś, wrzasnąć lub być poirytowanym, gdy ktoś ci przeszkadza podczas "surfowania" po sieci?',
    'odpowiedzi': ['1', '2', '3', '4', '5'],
    },
{
    'pytanie': 'Czy nie możesz doczekać się, aby znów być online? (lub włączyć dane komórkowe)',
    'odpowiedzi': ['1', '2', '3', '4', '5'],
    },
{
    'pytanie': 'Czy przeglądanie Internetu absorbuje cię do tego stopnia, iż nie możesz przestać o nim myśleć?',
    'odpowiedzi': ['1', '2', '3', '4', '5'],
    },
{
    'pytanie': 'Czy przygnębienie i wahania nastroju mijają podczas przeglądania Internetu?',
    'odpowiedzi': ['1', '2', '3', '4', '5'],
    },
{
    'pytanie': 'Czy zarywasz noce surfując po sieci?',
    'odpowiedzi': ['1', '2', '3', '4', '5'],
    },
{
    'pytanie': 'Czy ukrywasz czas spędzony w sieci?',
    'odpowiedzi': ['1', '2', '3', '4', '5'],
    },
{
    'pytanie': 'Czy wolisz siedzieć na Facebooku zamiast wyjść ze znajomymi?',
    'odpowiedzi': ['1', '2', '3', '4', '5'],
    },
{
    'pytanie': 'Zawierasz kontakty online?',
    'odpowiedzi': ['1', '2', '3', '4', '5'],
    },
{
    'pytanie': 'Czy bardziej cenisz sobie rozgłos w Internecie niż prywatność partnera/bliskiej osoby?',
    'odpowiedzi': ['1', '2', '3', '4', '5'],
    },
{
    'pytanie': 'Zaniedbujesz obowiązki domowe jak odkurzanie, aby spędzić trochę czasu online?',
    'odpowiedzi': ['1', '2', '3', '4', '5'],
    },
{
    'pytanie': 'Czy przyłapujesz się na tym, że spędzasz więcej czasu w sieci niż planowałeś?',
    'odpowiedzi': ['1', '2', '3', '4', '5'],
    },
{
    'pytanie': 'Czy ktoś wypomina ci ilość czasu spędzonego w sieci?',
    'odpowiedzi': ['1', '2', '3', '4', '5'],
    },
{
    'pytanie': 'Czy twoje wyniki w pracy i efektywność spadła, pogorszyła się?',
    'odpowiedzi': ['1', '2', '3', '4', '5'],
    },
{
    'pytanie': 'Czy twoje osiągi w nauce zmalały przez czas spędzony w sieci?',
    'odpowiedzi': ['1', '2', '3', '4', '5'],
    },
{
    'pytanie': 'Czy zastępujesz dręczące myśli o otaczającym świecie myśleniem o świecie online?',
    'odpowiedzi': ['1', '2', '3', '4', '5'],
    },
{
    'pytanie': 'Czy sprawdzanie wiadomości to pierwsze co robisz po przebudzeniu?',
    'odpowiedzi': ['1', '2', '3', '4', '5'],
    },
{
    'pytanie': 'Czy wypierasz i bronisz się przed tym co robisz w sieci?',
    'odpowiedzi': ['1', '2', '3', '4', '5'],
    },
]


DANE4 = [
    {
    'pytanie': 'Posiadam konto na (pytanie wielokrotnego wyboru): ',
    'odpowiedzi4': ['facebook', 'instagram','wykop','tinder','twitter','pornhub','tumblr']
    }
]


@app.route('/')
def index():

    return render_template('strona2.html')


@app.route('/walidacja', methods=['POST'])
def index2():

   odp = request.form.get("sprawdzenie")
   if odp=='4':

       return render_template('index.html', pytania2=DANE2, pytania4=DANE4)
   else:
       return render_template('strona2.html')


if __name__ == '__main__':
    app.run(debug=True)