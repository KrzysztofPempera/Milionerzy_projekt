##tomorrow, I will add comments and do little changes
import random
import sys

class mechanizm():
    ## answers must be sorted from a to d, so questions too.
    question_base_easy = [
        "Jaka jest nazwa słodkiej substancji, które wiele owadów uzyskuje z kwiatów?",
        "Helsinki są stolicą jakiego kraju?",
        "Jak nazywa się stolica Madagaskaru?",
        "Jak nazywa się mikroskopijny organizm wodny, który zawiera tylko jedną komórkę?",
        "Jak poprawnie brzmi nazwa rockowego zespołu z Anglii?",
        "Ten owoc podzielony jest na sekcje, wewnątrz których jest masa wypełnionych sokiem pęcherzyków:",

    ]
    question_answer_base_easy = [
        ["A) nektar","B) syrop klonowy","C) pyłek","D) syrop kwiatowy"],
        ["A) Finlandii","B) Islandii", "C) Estonii", "D) Rumunii"],
        ["A) Antananarywa","B) Madagaskar", "C) Lemir", "D) Berno"],
        ["A) ameba", "B) amfibia", "C) skrzek", "D) cellulit"],
        ["A) Radiobed", "B) Radiohell", "C) Radiohead", "D) Radiohide"],
        ["A) wiśnia", "B) czereśnia", "C) nektarynka", "D) mandarynka"]]

    answer_base_easy = [0, 0, 0, 0, 2, 3]

    question_base_medium = [
        "Jaka siła spowalnia toczenie się piłki?",
        "Jaki instrument znajduje się w meksykańskich zespołach mariachi?",
        "Co bada się za pomocą tablicy Snellena?",
        "Jak nazywa się kraj, którego epopeja narodowa nosi tytuł “Mobinogion?”",
        "Co utrzymuje się z surówki w procesie świeżenia?",
        "W czym tradycyjnie mieszkają ludy koczownicze w środkowej Azji?",
    ]
    question_answer_base_medium = [
        ["A) tarcie", "B) dynamiczna", "C) funkcyjna", "D) odśrodkowa"],
        ["A) fortepian", "B) trąbka", "C) wiolonczela", "D) tuba"],
        ["A) pojemność płuc", "B) masa ciała", "C) wzrok", "D) słuch"],
        ["A) Holandia", "B) Irlandia", "C) Walia", "D) Niemcy"],
        ["A) zdrowy dodatek do schabowego", "B) tkaninę w kolorze czerwonym", "C) stal", "D) materiał filmowy do montażu"],
        ["A) duryt", "B) kurta", "C) foliał", "D) jurta"]]

    answer_base_medium = [0, 1, 2, 2, 2, 3]

    question_base_hard = [
        "Jak Shakespear nazywa pierwszy akt w “Cały Świat to Scena?",
        "Monet, Renior i Degas, wszyscy należeli do którego ruchu artystycznego?",
        "Co szczególnie przeraża Indianę Jonesa?",
        "Do czego służy akwalung?",
        "W którym roku wybuchła wojna koreańska?",
        "Wadery to nieprzemakalne buty:",
        "W jakim mieście toczy się akcja filmu “Ghostbusters”?",
    ]
    question_answer_base_hard = [
        ["A) Podeszły wiek", "B) Dzieciństwo", "C) Dojrzałość", "D) Dorosłość"],
        ["A) Minimalizm", "B) Impresjonizm", "C) Dadaizm", "D) Ekspresjonizm"],
        ["A) łodzie", "B) węże", "C) pająki", "D) krokodyle"],
        ["A) do latania", "B) szybszego wypijania płynów", "C) oddychania pod wodą", "D) nawoływania kaczek"],
        ["A) 1948", "B) 1969", "C) 1950", "D) 1958"],
        ["A) połączone z kapeluszem", "B) z wilczej skóry", "C) połączone ze spodniami", "D) na koturnach"],
        ["A) w San Francisco", "B) w Chicago", "C) w Londynie", "D) w Nowym Jorku"]]

    answer_base_hard = [1, 1, 1, 2, 2, 2, 3]

    ##K: Basic variables
    def __init__(self):
        self.nagrody = ["500$","1000$","2000$","5000$","10 000$","20 000$","40 000$","75 000$","125 000$","250 000$","500 000$","1 000 000$"]
        self.stan_konta = "500$"
        self.number_question = 0
        self.score = 0
        self.guaranted_cash = "0$"
        self.loss = False
        self.last_score = self.score 
    ##K: This def draw question and choose correct answer from list

    def random_question(self):
        ##K: stage easy
        if self.score >= 0  and self.score <= 3:
            self.question = random.choice(self.question_base_easy)
            self.position = self.question_base_easy.index(self.question)
            self.answer_ans = self.answer_base_easy[self.position]
        ##K: stage med
        elif self.score >= 4  and self.score <= 7:
            self.question = random.choice(self.question_base_medium)
            self.position = self.question_base_medium.index(self.question)
            self.answer_ans = self.answer_base_medium[self.position]
        ##K: stage_hard
        elif self.score >= 8  and self.score <= 11:
            self.question = random.choice(self.question_base_hard)
            self.position = self.question_base_hard.index(self.question)
            self.answer_ans = self.answer_base_hard[self.position]

    def questionFunction(self):
        self.number_question = self.number_question + 1

    def check_answer(self,ans):
        if self.answer_ans == ans:
            self.last_score = self.score
            self.score = self.score + 1
        elif self.answer_ans != ans:
            self.loss = True

    def bank(self):
        self.stan_konta = self.nagrody[self.score]
        if self.score == 2:
            self.guaranted_cash = "1000$"
        elif self.score == 7:
            self.guaranted_cash = "40 000$"
        elif self.score == 12:
            self.guaranted_cash = "1 000 000$"

    def question_remove(self):
        if self.last_score >= 0  and self.last_score <= 3:
            self.question_base_easy.remove(self.question_base_easy[self.position])
            del self.question_answer_base_easy[self.position]
            self.answer_base_easy.remove(self.answer_base_easy[self.position])

        if self.last_score >= 4  and self.last_score <= 7:
            self.question_base_medium.remove(self.question_base_medium[self.position])
            del self.question_answer_base_medium[self.position]
            self.answer_base_medium.remove(self.answer_base_medium[self.position])

        if self.last_score >= 8  and self.last_score <= 11:
            self.question_base_hard.remove(self.question_base_hard[self.position])
            del self.question_answer_base_hard[self.position]
            self.answer_base_hard.remove(self.answer_base_hard[self.position])

    def scoreCheck(self):
        return self.score
    def stan_kontaCheck(self):
        return self.stan_konta
    def number_questionChcek(self):
        return self.number_question
    def guaranted_cashCheck(self):
        return self.guaranted_cash
    def answerCheck(self):
        return self.answer_ans


