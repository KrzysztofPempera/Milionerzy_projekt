##tomorrow, I will add comments and do little changes
import random
import sys
class mechanizm():
    ## answers must be sorted from a to d, so questions too.
    question_base_easy = [
        "Jaka jest nazwa słodkiej substancji, które wiele owadów uzyskuje z kwiatów?\n A) nektar\n B) syrop klonowy\n C) pyłek\n D) syrop kwiatowy\n",
        "Helsinki są stolicą jakiego kraju?\n A) Finlandii\n B) Islandii\n C) Estonii\n D) Rumunii",
        "Jak nazywa się stolica Madagaskaru?\n A) Antananarywa\n B) Madagaskar\n C) Lemir\n D) Berno",
        "Jak nazywa się mikroskopijny organizm wodny, który zawiera tylko jedną komórkę?\n A) ameba\n B) amfibia\n C) skrzek\n D) cellulit",
        "Jak poprawnie brzmi nazwa rockowego zespołu z Anglii?\n A) Radiobed\n B) Radiohell\n C) Radiohead\n D) Radiohide",
        "Ten owoc podzielony jest na sekcje, wewnątrz których jest masa wypełnionych sokiem pęcherzyków:\n A) wiśnia\n B) czereśnia\n C) nektarynka\n D) mandarynka",

    ]
    answer_base_easy = ["a", "a", "a", "a", "c", "d"]


    question_base_medium = [
        "Jaka siła spowalnia toczenie się piłki?\n A) tarcie\n B) dynamiczna\n C) funkcyjna\n D) odśrodkowa",
        "Jaki instrument znajduje się w meksykańskich zespołach mariachi?\n A) fortepian\n B) trąbka\n C) wiolonczela\n D) tuba",
        "Co bada się za pomocą tablicy Snellena?\n A) pojemność płuc\n B) masa ciała\n C) wzrok\n D) słuch",
        "Jak nazywa się kraj, którego epopeja narodowa nosi tytuł “Mobinogion?”\n A) Holandia\n B) Irlandia\n C) Walia\n D) Niemcy",
        "Co utrzymuje się z surówki w procesie świeżenia?\n A) zdrowy dodatek do schabowego\n B) tkaninę w kolorze czerwonym\n C) stal\n D) materiał filmowy do montażu",
        "W czym tradycyjnie mieszkają ludy koczownicze w środkowej Azji?\n A) duryt\n B) kurta\n C) foliał\n D) jurta",
    ]
    answer_base_medium = ["a", "b", "c", "c", "c", "d"]


    question_base_hard = [
        "Jak Shakespear nazywa pierwszy akt w “Cały Świat to Scena?\n A) Podeszły wiek\n B) Dzieciństwo\n C) Dojrzałość\n D) Dorosłość",
        "Monet, Renior i Degas, wszyscy należeli do którego ruchu artystycznego?\n A) Minimalizm\n B) Impresjonizm\n C) Dadaizm\n D) Ekspresjonizm",
        "Co szczególnie przeraża Indianę Jonesa?\n A) łodzie\n B) węże\n C) pająki\n D) krokodyle",
        "Do czego służy akwalung?\n A) do latania\n B) szybszego wypijania płynów\n C) oddychania pod wodą\n D) nawoływania kaczek",
        "W którym roku wybuchła wojna koreańska?\n A) 1948\n B) 1969\n C) 1950\n D) 1958",
        "Wadery to nieprzemakalne buty:\n A) połączone z kapeluszem\n B) z wilczej skóry\n C) połączone ze spodniami\n D) na koturnach",
        "W jakim mieście toczy się akcja filmu “Ghostbusters”?\n A) w San Francisco\n B) w Chicago\n C) w Londynie\n D) w Nowym Jorku",
    ]
    answer_base_hard = ["b", "b", "b", "c", "c", "c", "d"]

    ##K: I will add more sentence.
    small_talk = ["Cieszę się, że mamy możliwość gościć Cię w naszym programie", "Bardzo dobrze Ci idzie.",
                  "Zbliżamy się do miliona", "Oby tak dalej."]

    print("Witamy w milionerach!")

    ## I'm going to add music and dynamic logo.



    ##K: Basic variables
    def __init__(self):
        self.stan_konta = 0
        self.odp = ""
        self.number_question = 0
        self.score = 0
        self.guaranted_cash = 0


    ##K: This def draw question and choose correct answer from list

    def random_question(self):
        ##K: stage easy
        if self.score == 0 or self.score == 1 or self.score == 2 or self.score ==3:
            self.random = random.choice(self.question_base_easy)
            self.position = self.question_base_easy.index(self.random)
            self.question_ans = self.question_base_easy[self.position]
            self.answer_ans = self.answer_base_easy[self.position]
        ##K: stage med
        if self.score == 4 or self.score == 5 or self.score == 6 or self.score == 7:
            self.random = random.choice(self.question_base_medium)
            self.position = self.question_base_medium.index(self.random)
            self.question_ans = self.question_base_medium[self.position]
            self.answer_ans = self.answer_base_medium[self.position]
        ##K: stage_hard
        if self.score == 8 or self.score == 9 or self.score == 10 or self.score == 11:
            self.random = random.choice(self.question_base_hard)
            self.position = self.question_base_hard.index(self.random)
            self.question_ans = self.question_base_hard[self.position]
            self.answer_ans = self.answer_base_hard[self.position]

    ##K: Introduction to the game
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
        self.odp = input("Podaj odpowiedź: \n").lower()
        print("Czy jesteś pewny swojej odpowiedzi, jest ona definitywna?")
        self.response = input()
        ##K: I must change this IF.
        if self.response == "tak":
            print("")



    def check_answer(self):
        if self.answer_ans == self.odp:
            self.score += 1
            print("Znakomicie,",self.number_question,"pytanie za nami.")
        if self.answer_ans != self.odp:
            print("To nie była prawidłowa odpowiedź, gdybyś wybrał/a odpowiedź:",self.answer_ans.upper(),"- To nasz przygoda trwałaby dłużej. ")
            print("Niestety to koniec naszej gry, spróbuj ponownie!")
            print("Twoja wygrana wynosi:", self.guaranted_cash)
            sys.exit(0)

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
            print("Gratulacje!", self.name.upper(), "jesteś MILIONEREM!")
        print("Obecnia na swoim koncie masz", self.stan_konta,"zł.")



    def question_remove(self):
        if self.score == 0 or self.score == 1 or self.score == 2 or self.score == 3:
            self.question_base_easy.remove(self.question_base_easy[self.position])
            self.answer_base_easy.remove(self.answer_base_easy[self.position])

        if self.score == 4 or self.score == 5 or self.score == 6 or self.score == 7:
            self.question_base_medium.remove(self.question_base_medium[self.position])
            self.answer_base_medium.remove(self.answer_base_medium[self.position])

        if self.score == 8 or self.score == 9 or self.score == 10 or self.score == 11:
            self.question_base_hard.remove(self.question_base_hard[self.position])
            self.answer_base_hard.remove(self.answer_base_hard[self.position])


    def audience(self):
        self.results = []
        self.base = ("a", "b", "c", "d")
        self.o = 0
        self.percent = 50
        self.part1 = random.randrange(self.percent)
        self.percent -= self.part1
        self.results.append(self.part1)
        self.results.append(self.percent)

        self.percent2 = 50
        self.part2 = random.randrange(self.percent2)
        self.percent2 -= self.part2
        self.results.append(self.part2)
        self.results.append(self.percent2)
        self.results.sort()

        for i in self.results:

            if i == max(self.results):
                print("Odpowiedź",self.answer_ans.upper(),"-", i, "%")
                self.base = list(self.base)
                self.base.remove(self.answer_ans)
                self.results.remove(i)
                self.base = tuple(self.base)
                for i in range (len(self.base)):
                    print("Odpowiedź",self.base[i].upper(),"-", self.results[self.o], "%")
                    self.o += 1




class player_menu(mechanizm):


    def menu_player(self):
        print("")

    def user_decision(self):
        print("")
        print(" Aby kontynuować i podać odpowiedź kliknij 'x'\n",  "Aby zakończyć klinij 'e'\n", "Jeśli chcesz z korzystać z kół ratunkowych kliknij 'o")
        button = input()
        if button == "e":
            print("Dziękujemy za udział w naszym teleturnieju twoja wygrana wynosi:", self.guaranted_cash,"zł.")
            sys.exit(0)
        if button == "o":
            print("Aby spytać publiczność o ich intuicję kliknij '1'")
            self.byb = int(input())
            if self.byb == 1:
                gracz.audience()








gracz = mechanizm()
gracz = player_menu()
gracz.interview()



while True:
    gracz.random_question()
    gracz.question()
    gracz.user_decision()
    gracz.answer()
    gracz.check_answer()
    gracz.bank()
    gracz.question_remove()




