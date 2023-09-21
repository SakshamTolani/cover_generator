import os


# if __name__=='__main__':
#     company = input("Enter Company Name: ")
#     position = input("Enter Position you want to apply: ")
#     generator(company=company, position=position)


from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        # main_layout = BoxLayout(padding=10, orientation="vertical")
        self.cols = 1

        self.add_widget(Label(text="Company Name*"))

        self.company_name = TextInput(
            hint_text="Company name*",
            multiline=False,
        )
        self.add_widget(self.company_name)

        self.add_widget(Label(text="Role or Position*"))

        self.position = TextInput(
            hint_text="Role or Position*",
            multiline=False,
        )
        self.add_widget(self.position)
        self.submit = Button(
            text="Submit Application",
            size=(20, 10),
            background_color="green",
            color="black",
        )
        self.add_widget(self.submit)
        self.submit.bind(on_press=self.submit_clicked)

        self.popup = Popup(
            title="Company or Position Missing",
            content=Label(text="Please enter all the fields."),
            size_hint=(None, None),
            size=(500, 500),
        )

        # return main_layout

    def submit_clicked(self, instance):
        company = self.company_name.text
        role = self.position.text
        if company == "" or company is None or role=="" or role is None or company==" " or role==" ":
            self.popup.open()
        else:
            self.generator(company, role)

    def generator(self, company="Nagarro", position="SDE"):
        with open(f"{os.getcwd()}\cover_letter_{company}.txt", mode="w") as f:
            message = f"Dear Hiring Manager, \n\nI am excited to apply for the role of {position}, at {company}. With a background in {position} and a proven track record of success I am confident that I can make contributions to your teams achievements.\n\nHaving recently graduated with a Bachelor of Science in Computer Science from SGTB Khalsa College, University of Delhi I have gained a foundation in programming languages like Python, Java and C++. My passion for development has driven me to excel in frameworks such as Django and ReactJS enabling me to create solutions.\n\nDuring my internship at Newton School as an MIS Analyst & BA Support Intern I utilized my skills to improve team productivity by analyzing MS Excel trackers. Additionally I designed appealing dashboards that enhanced the readability of statistics by 20%. Furthermore, I. Implemented growth strategies that resulted in a 10% expansion acceleration for the company.\n\nMy experience as a Django Developer Intern at IIT Bombay further refined my skills. Through creating REST APIs using Python and Django I achieved a 30% reduction in response time, for a collaboration tool.\n\nI have also created an reliable database using MySQL, which effectively manages the storage and retrieval of data ensuring that the platform operates smoothly.\n\nI'd like to highlight a few of the projects I've worked on. One of them is MILAN, a video chat app that I developed using Django, HTML, CSS and MongoDB. It allowed people, from over the world to connect easily and saved them 40% on travel expenses for meetings. Another project I'm proud of's QRATOR a QR code generator that I built using Flask, HTML, CSS and SQLite. It not improved efficiency by 30%. Also had a user friendly interface that led to a 25% increase in QR code usage.\n\nIn addition to my skills I'm also a team player with communication and problem solving abilities. During my time in college I actively participated in coding societies and physics societies, which helped me collaborate effectively on projects and initiatives.\n\nI am genuinely excited about the opportunity to join {company} and contribute to its success. With my skills, enthusiasm and dedication I believe I would be an asset to your team.\n\nThank you for considering my application. You can find my resume attached for details about my qualifications and experiences. I would appreciate the chance to discuss how my skills align with the {position} role, in depth.\n\nI am excited, about the opportunity to become a part of your team and contribute to the growth of {company}.\n\nSincerely,\nSaksham Tolani"
            f.write(message)
            print(f"Written Successfully to cover_letter_{company}.txt")
            f.close()


class MyApp(App):
    #     company = input("Enter Company Name: ")
    #     position = input("Enter Position you want to apply: ")
    #     generator(company=company, position=position)
    def build(self):
        return MyGridLayout()


MyApp().run()
