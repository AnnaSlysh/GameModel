import streamlit as st
import pages.utils as utils

def app():
    utils.load_css("style.css")

    if 'language' not in st.session_state:
        st.session_state.language = 'uk'

    st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)

    col_empty, col1, col2, col_empty2 = st.columns([2, 1, 1, 2])
    with col1:
        if st.button("Українська", use_container_width=True, key="ua_btn_help"):
            st.session_state.language = 'uk'
    with col2:
        if st.button("English", use_container_width=True, key="en_btn_help"):
            st.session_state.language = 'en'


    texts = {
        'uk': {
            'help_project': "Допомогти проєкту",
            'join_us': ("Приєднуйтесь до нас і допоможіть будувати інклюзивне майбутнє!<br>"
                        "Станьте частиною нашої спільноти – разом ми можемо змінити світ!<br><br>"
                        "Якщо у вас виникають питання чи якісь проблеми, ви можете звернутися до нас за електронною адресою:<br>"
                        "hartingestures@gmail.com"),
            'feedback_title': "Ваші відгуки - важливі для нас ☺️!",
            'feedback_text': ("<strong>Нам важлива ваша думка!</strong><br>"
                              "Якщо у вас є ідеї щодо покращення гри або ви хочете поділитися своїми враженнями — напишіть нам!<br><br>"
                              "<a href='https://docs.google.com/forms/d/e/1FAIpQLScAlVmTQe6wKm4U7bqtnEbU8pravDP0XuGnP7ZlMWWw9SPSHA/viewform?usp=header' target='_blank'>Надіслати відгук</a>"),
            'spread_info_title': "Розповсюдження інформації 🤳",
            'spread_info_text': ("Розкажіть про наш проєкт друзям, у соцмережах чи на заходах."
                                 " Це допомагає нам знайти нову аудиторію та потенційних партнерів.<br><br>"
                                "Посилання: "
                                 "<a href='https://www.instagram.com/heartingestures_/profilecard/?igsh=bHd2bGJnaWg4Ynp4' target='_blank'>Наш Інстаграм</a>"),
            'partnership_title': "Партнерство 🤝",
            'partnership_text': ("Ми відкриті для співпраці з організаціями, які поділяють наші цінності!<br>"
                                 "Напишіть нам, якщо хочете стати частиною змін:<br>"
                                 "hartingestures@gmail.com"),
            'respect': "З повагою, команда Grlpwr!"
        },
        'en': {
            'help_project': "Support the Project",
            'join_us': ("Join us and help build an inclusive future!<br>"
                        "Become part of our community — together we can change the world!<br><br>"
                        "If you have any questions or problems, you can contact us at:<br>"
                        "hartingestures@gmail.com"),
            'feedback_title': "Your feedback is important to us ☺️!",
            'feedback_text': ("<strong>Your opinion matters!</strong><br>"
                              "If you have ideas for improving the game or want to share your impressions — write to us!<br><br>"
                              "<a href='https://docs.google.com/forms/d/e/1FAIpQLScAlVmTQe6wKm4U7bqtnEbU8pravDP0XuGnP7ZlMWWw9SPSHA/viewform?usp=header' target='_blank'>Send feedback</a>"),
            'spread_info_title': "Spreading Information 🤳",
            'spread_info_text': ("Tell your friends about our project, share it on social media or at events."
                                 " This helps us find a new audience and potential partners.<br><br>"
                                 "<a href='https://www.instagram.com/heartingestures_/profilecard/?igsh=bHd2bGJnaWg4Ynp4' target='_blank'>Our Instagram</a>"),
            'partnership_title': "Partnership 🤝",
            'partnership_text': ("We are open to cooperation with organizations that share our values!<br>"
                                 "Write to us if you want to become part of the changes:<br>"
                                 "hartingestures@gmail.com"),
            'respect': "Respectfully, Grlpwr Team!"
        }
    }

    lang = st.session_state.language

    st.markdown(f'<div class="title_header">{texts[lang]["help_project"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="text">{texts[lang]["join_us"]}</div>', unsafe_allow_html=True)

    st.markdown(f'<div class="title_subheader">{texts[lang]["feedback_title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="text" style="margin-top: 30px;">{texts[lang]["feedback_text"]}</div>', unsafe_allow_html=True)

    st.markdown(f'<div class="title_subheader">{texts[lang]["spread_info_title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="text">{texts[lang]["spread_info_text"]}</div>', unsafe_allow_html=True)

    st.markdown(f'<div class="title_subheader">{texts[lang]["partnership_title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="text">{texts[lang]["partnership_text"]}</div>', unsafe_allow_html=True)

    st.markdown(f'<div class="title_subheader">{texts[lang]["respect"]}</div>', unsafe_allow_html=True)




