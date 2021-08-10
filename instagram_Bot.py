from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

class instabot:
    def __init__(self,username,password):
        self.username=username
        self.password=password

        self.driver =webdriver.Chrome("./chromedriver.exe")
        self.login()

    def login(self):
        self.driver.get("https://www.instagram.com/?hl=en")
        enter_username = WebDriverWait(self.driver, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)

        enter_password = WebDriverWait(self.driver, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        login=self.driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]/button/div')
        login.click()
        try:
            time.sleep(4)
            '''after login it will ask about to save the password we have to click on Not Now to continue testing
            '''

            not_save_password=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
            time.sleep(1)
            ''' again it will ask to turn on desktop notification we have to click on not now
            '''
            turn_on_notification=self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        except:
            pass
    time.sleep(2)
    def crawl(self):
        #user name button
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a').click()
        time.sleep(4)

        self.open_users('followers')
        followers = self.scroll_and_get()
        print(followers)

        self.open_users('following')
        following=self.scroll_and_get()
        print(following)
        time.sleep(2)
        not_following_back = [f for f in following if f not in followers]
        print('USERS NOT FOLLOWING BACK', not_following_back)
        print("total followers ->",len(followers))
        print("total following ->",len(following))
        print("total not following ->",len(not_following_back))

    # def unfollow(self):
    #     l=['vikashrbhaskar', 'yeshwant__singh', 'md_hussainnn', 'rajnikantkumarsachin', 'afaque_siddiqui3867', 'insanesaurabh', 'surpatil728', 'henrynadodaiki', 'the_voiceofhearts', 'bodybuilding', 'abhinav.dangerous7', 'axshivam', 'ksenng_chow', 'chirag.shukla_', '__anuragmishra', 'ashishkohke', 'arpitshukla2928', 'arvind.sharma0792', 'aryangarg3125', 'omprakash9100', 'iamharish01', 'chandrachandanprince', 'ankur.saurikh', 'lucky_love_077', 'aryangarg1999', 'pushpad_30', 'mellow_vibe12', 'sanket_um_agrawal', 'sajal31392', 'the_beast_ujjwal', 'maneesh5483', 't_u_s_h_a_r_s_a_c_h_a_n', 'r.k.rajora', 'harshit2266', 'anup2916', 'pranshup45', 'fitbull_anish', 'dhruveeljain', 'prasoon10', 'vivekpal2688', 'priyesh.dixit.921', 'nikka_zimidar', '0tanishqmishra', 'bg___9', 'minion893', 'atultiwaridkt', 'shobhit.upadhyay', 'me_rishabh2307', 'chandel_sraghav', 'fin.lew', 'kazmi_armaan', 'amar_dwivedi_', 'deepakzgupta', 'prem.k03', 'be_aware_in_business', 'i_am_aswinn', 'joychatter165', 'aashu1710', 'kumargupta.saurabh', 'shagunrana09', 'aham_shivam', 'born_loserr', 'theskinnymonk', 'shubham_2017', 'divyanshu_nigam_', 'd_gajendra_', 'chetan_bhaskar1', 'naveen_arya_prajapati', 'katiyar.sandeep', 'gaurangggupta', 'madaninsta', 'antonio_8400', 'amit_deep_singh_', 'aman_a_paragon', 'sanjog_yadav', '_manish_dixit', 'suyashraj_bajpai007', 'vairaagiiii' ]
    #
    #     i=0
    #     while i<len(l):
    #         searchbox = WebDriverWait(self.driver, 10).until(
    #             expected_conditions.visibility_of_element_located(
    #                 (By.XPATH, "//input[@placeholder='Search']")
    #             )
    #         )
    #
    #         # send search into input
    #
    #         searchbox.send_keys(l[i])
    #         time.sleep(2)
    #         # searchbox.submit()
    #
    #         searchbox.send_keys(Keys.ENTER)
    #         time.sleep(1)
    #         searchbox.send_keys(Keys.ENTER)
    #         time.sleep(4)
    #         self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[2]/div[2]/div/span/span[1]/button/div/span').click()


    def open_users(self, user_type):
        driver = self.driver
        driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(user_type)).click()
        time.sleep(2)

    def scroll_and_get(self):
        driver = self.driver
        scroll_box = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')

        time.sleep(2)
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(1)
            ht = driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;', scroll_box)

        names = scroll_box.find_elements_by_tag_name('a')
        users = [name.text for name in names if name != ''][:]

        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button').click()
        #/html/body/div[5]/div/div/div[1]/div/div[2]/button/div/svg/path
        #/html/body/div[5]/div/div/div[1]/div/div[2]/button/div/svg
        users=list(filter(None,users))
        return users

if __name__== '__main__':
    ig_bot=instabot('Instagram id ','Password')
    ig_bot.crawl()

