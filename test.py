##wersja niedokończona
import random
import sys
class mechanizm():
    question_base_easy = ["Jaka jest nazwa słodkiej substancji, które wiele owadów uzyskuje z kwiatów?\n A) nektar\n B) syrop klonowy\n C) pyłek\n D) syrop kwiatowy\n",
                          "Helsinki są stolicą jakiego kraju?\n A) Finlandii\n B) Islandii\n C) Estonii\n D) Rumunii",
                          "Jak poprawnie brzmi nazwa rockowego zespołu z Anglii?\n A) Radiobed\n B) Radiohell\n C) Radiohead\n D) Radiohide",
                          "Który z motoryzacyjnych skrótów dotyczy układu hamulcowego?\n A) ABC\n B) RWD\n C) ABS\n D) 4WD",
                          "Który organ jest odpowiedzialny za przechowywanie żółci?\n A) wątroba\n B) pęcherzyk żółciowy\n C) śledziona \n D) nerki ",
                          "Nadworny błazen Zygmunta Starego to:\n A) Michał\n B) Lisowczyk\n C) Sebastian\n D) Stańczyk"
                          ]
    answer_base_easy = ["a", "a", "c", "c", "b", "d"  ]
    question_base_medium = ["abc", "adk"]
    answer_base_medium = ["lol", "lep"]
    small_talk = ["Cieszę się, że mamy możliwość gościć Cię w naszym programie", "Bardzo dobrze Ci idzie.",
"Zbliżamy się do miliona",
                "Oby tak dalej."]

    print("Witamy w milionerach!")




    def __init__(self):
        self.stan_konta = 0
        self.odp = ""
        self.number_question = 0
        self.score = 0
        self.guaranted_cash = 0



    def random_question(self):
        self.random = random.choice(self.question_base_easy)
        self.position = self.question_base_easy.index(self.random)
        self.question_ans = self.question_base_easy[self.position]
        self.answer_ans = self.answer_base_easy[self.position]


    def interview(self):
        print("Proszę przedstaw nam się!")
        self.name = input("Mam na imię: ")
        print("Miło Cię poznać", self.name)
        print("Czy jesteś gotowy rozpoczać grę o MILION złotych?")
        com = input()
        print("Jeśli",com,", to zaczynajmy!")


    def question(self):
        self.number_question += 1
        print("Oto", self.number_question,"pytanie.")
        return print(self.question_ans)


    def answer(self):
        self.odp = input("Podaj odpowiedź: \n")



    def check_answer(self):
        if self.answer_ans == self.odp:
            self.score += 1
            print(self.score)
            print("Znakomicie,",self.number_question,"pytanie za nami.")
        if self.answer_ans != self.odp:
            print("Niestety to koniec naszej gry, do zobaczenia!")
            print("Twoja wygrana wynosi:", self.guaranted_cash)

        small_talk_random = random.randint(0,2)
        if small_talk_random == 1:
            print(random.choice(self.small_talk))

    def bank(self):
        if self.score == 1:
            self.stan_konta = "500"
        if self.score == 2:
            self.stan_konta = "1000"
            self.guaranted_cash = 1000
            print("Masz już zagwarantowane 1000 zł, oby tak dalej!")
        if self.score == 3:
            self.stan_konta = "2000"
        if self.score == 4:
            self.stan_konta = "5000"
        if self.score == 5:
            self.stan_konta = "10 000"
        if self.score == 6:
            self.stan_konta = "20 000"
        if self.score == 7:
            self.stan_konta = "40 000"
            self.guaranted_cash = 40000
            print("Zagwarantowane 40000 zł, stało się właśnie Twoją własnością!")
        if self.score == 8:
            self.stan_konta = "75 000"
        if self.score == 9:
            self.stan_konta = "125 000"
        if self.score == 10:
            self.stan_konta = "250 000"
        if self.score == 11:
            self.stan_konta = "500 000"
        if self.score == 12:
            self.stan_konta = "1 000 000"
            self.guaranted_cash = 1000000
        print("Obecnia na swoim koncie masz", self.stan_konta,"zł.")


    def question_remove(self):
        self.question_base_easy.remove(self.question_base_easy[self.position])
        self.answer_base_easy.remove(self.answer_base_easy[self.position])






class player_menu(mechanizm):
    '''Przeniesc, by kolo bylo przy podawaniu odpowiedzi'''
    def menu_player(self):
        print("telefon do przyjaciela, kliknij 'p'")
        phone_friend = input()
        if phone_friend == "p":
            print("Myślę, że poprawna odpowiedź to odpowiedź", self.mechanizm.random_question(answer_ans))

    def user_decision(self):
        print("Aby kontynuować kliknij 'x'\n",
              "Aby zakończyć klinij 'e'\n"
              "Jeśli chcesz z korzystać z kół ratunkowych kliknij 'o")
        button = input()
        if button == "e":
            print("Dziękujemy za udział w naszym teleturnieju twoja wygrana wynosi:", self.guaranted_cash,"zł.")
            sys.exit(0)
        if button == "o":
            gracz2.menu_player()








gracz = mechanizm()
gracz = player_menu()
gracz.interview()


while True:
    gracz.random_question()
    gracz.question()
    gracz.answer()
    gracz.check_answer()
    gracz.bank()
    gracz.user_decision()
    gracz.question_remove()





