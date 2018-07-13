from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException as Nosuch
from bs4 import BeautifulSoup
from random import randint
import time
import csv
import ast


def login():
    opts = Options()
    opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
    driver = webdriver.Chrome("C:/Users/alexel_t91/Downloads/chromedriver_win32/chromedriver.exe", chrome_options=opts)
    driver.get("https://linkedin.com")  # opens up chrome - okcupid
    agent = driver.execute_script("return navigator.userAgent")
    print(agent)
    user_name = "evich_blah@mail.com"  # give username
    password = "1234567890As!"  # give password
    n = randint(0, 10)
    time.sleep(n)

    driver.find_element_by_xpath('//*[@id="login-email"]').send_keys(user_name)
    driver.find_element_by_xpath('//*[@id="login-password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="login-submit"]').click()
    time.sleep(n)

def scrape():
    with open('C:/Users/alexel_t91/Desktop/users/csvusers11.csv', 'r') as userfile:
        userfilereader = csv.reader(userfile)
        for col in userfilereader:
            userlist.append(col)

    user_list = ast.literal_eval(str(userlist[0]))
    user_list = list(set(user_list))
    userfile.close()
    exp_list = []

    for user in user_list:
        k = randint(80, 120)
        n = randint(70, k)
        time.sleep(n)
        driver.get('https://www.linkedin.com/in/'+user)
        html = driver.page_source
        source = BeautifulSoup(html, 'html.parser')

        sections = source.find_all('section')
        skills = []

        name = None
        headline = None
        location = None
        connections = None
        first_text = None
        work_name = None
        school_name = None

        for section in sections:

            section_class = section.get('class')
            if section_class == 'pv-profile-section pv-top-card-section artdeco-container-card ember-view':  # Name
                print('name')

                try:
                    driver.find_element_by_css_selector('.pv-top-card-section__summary-toggle-button.pv-profile-section__card-action-bar.artdeco-container-card-action-bar.mt4').click()
                except Nosuch:
                    pass
                n = randint(4, 14)
                time.sleep(n)

                name = section.find('h1', {'class': 'pv-top-card-section__name Sans-26px-black-85%'}).text
                headline = section.find('h2', {'class': 'pv-top-card-section__headline mt1 Sans-19px-black-85%'}).text
                location = section.find('h3', {'class': 'pv-top-card-section__location Sans-17px-black-55%-dense mt1 inline-block'}).text
                connections = section.find('span', {'class': 'pv-top-card-v2-section__entity-name pv-top-card-v2-section__connections ml2 Sans-15px-black-85%'}).text

                first_text = section.find('p', {'class': 'pv-top-card-section__summary-text text-align-left mt4 ember-view'}).text

            elif section_class == 'pv-profile-section experience-section ember-view':
                print('experience')

                try:
                    driver.find_element_by_css_selector('.pv-profile-section__see-more-inline.pv-profile-section__text-truncate-toggle.link').click()
                except Nosuch:
                    pass
                n = randint(4, 14)
                time.sleep(n)
                exp_divs = section.find_all('div', {'class': 'pv-entity__summary-info'})
                for exp_div in exp_divs:
                    work_name = exp_div.find('h3', {'class': 'Sans-17px-black-85%-semibold'}).text
                    exp_div_h4 = exp_div.find_all('h4')
                    print(work_name)
                    for exp_div1 in exp_div_h4:
                        print(exp_div1.text)



            elif section_class == 'pv-profile-section education-section ember-view':
                print('education')

                try:
                    driver.find_element_by_css_selector('.pv-profile-section__see-more-inline.pv-profile-section__text-truncate-toggle.link').click()
                except Nosuch:
                    pass
                n = randint(4, 14)
                time.sleep(n)
                edu_divs = section.find_all('div', {'class': 'pv-entity__summary-info'})
                for edu_div in edu_divs:
                    school_name = edu_div.find('h3', {'class': 'pv-entity__school-name Sans-17px-black-85%-semibold'}).text
                    edu_div_h4s = edu_div.find_all('span', {'class': 'pv-entity__comma-item'})
                    print(school_name)
                    for edu_div_h4 in edu_div_h4s:
                        print(edu_div_h4.text)



            elif section_class == 'pv-profile-section volunteering-section ember-view':
                print('volunteer')

                try:
                    driver.find_element_by_css_selector('.pv-profile-section__see-more-inline.pv-profile-section__text-truncate-toggle.link').click()
                except Nosuch:
                    pass
                n = randint(4, 14)
                time.sleep(n)
                vol_uls = section.find_all('ul', {'class': 'pv-profile-section__section-info section-info pv-profile-section__section-info--has-no-more ember-view'})
                for vol_ul in vol_uls:
                    vol_name = vol_ul.find('h3', {'class': 'Sans-17px-black-85%-semibold'}).text
                    print(vol_name)
                    vol_div_h4 = vol_ul.find_all('h4')
                    for vol_div1 in vol_div_h4:
                        print(vol_div1.text)


            elif section_class == 'pv-profile-section pv-skill-categories-section artdeco-container-card ember-view':
                print('Skills')

                try:
                    driver.find_element_by_css_selector('.pv-profile-section__card-action-bar.pv-skills-section__additional-skills.artdeco-container-card-action-bar').click()
                except Nosuch:
                    pass
                n = randint(4, 14)
                time.sleep(n)
                header = section.find('h2', {'class': 'pv-profile-section__card-heading Sans-21px-black-85%'})
                if header == 'Skills & Endorsements':
                    spans = section.find_all('span', {'class': 'Sans-17px-black-100%-semibold'})
                    for span in spans:
                        skills.append(span.text)
                    print(*skills)
                elif header == 'Skills':
                    ps = section.find_all('p', {'class': 'pv-skill-category-entity__name  Sans-17px-black-100%-semibold'})
                    for par in ps:
                        skills.append(par.text)
                    print(*skills)

            elif section_class == 'pv-profile-section pv-accomplishments-section artdeco-container-card ember-view':
                print('accomplishments')

                acc_h3s = list(section.find_all('h3', {'class': 'pv-entity__summary-info'}))
                acc_h3s_no = list(section.find_all('h3', {'class': 'pv-accomplishments-block__count Sans-34px-black-100% pr3'}))
                ul_list = list(section.find('ul', {'class': 'pv-accomplishments-block__summary-list Sans-15px-black-70% pv-accomplishments-block__summary-list-more'}))
                for i in range(0, len(acc_h3s)):
                    print(acc_h3s[i].text)
                    print(acc_h3s_no[i].text)
                    print(ul_list[i].text)




            elif section_class == 'pv-profile-section pv-interests-section artdeco-container-card ember-view':
                print('asdf')
                spans_interests = section_class.find_all('span', {'class': 'pv-entity__summary-title-text'})
                for span_interest in spans_interests:
                    span_interest.text


            elif section_class == 'pv-profile-section pv-recommendations-section artdeco-container-card ember-view':
                print('recommendations')
                try:
                    driver.find_element_by_css_selector('.pv-profile-section__see-more-inline.pv-profile-section__text-truncate-toggle.link').click()
                except Nosuch:
                    pass
                n = randint(4, 14)
                time.sleep(n)
                rec_lis = section.find_all('li', {'class': 'pv-recommendation-entity ember-view'})
                for rec_li in rec_lis:
                    person = rec_li.find('div', {'class': 'pv-recommendation-entity__header'})
                    letter = rec_li.find('div', {'class': 'pv-recommendation-entity__highlights'})
                    print(person)
                    print(letter)





opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
driver = webdriver.Chrome("C:/Users/alexel_t91/Downloads/chromedriver_win32/chromedriver.exe", chrome_options=opts)
userlist = []
scrape()