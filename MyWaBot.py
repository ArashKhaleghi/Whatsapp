#Ican Do This

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://web.whatsapp.com')

names = input('Enter Users Name with cama (name1,name2,...): ')

a = names.split(',')
names = list(a)

msg = input('your Message : ')
count = int(input('How Many Times ??'))

input('Click Any thing ...')

for name in names:

    user = driver.find_element_by_xpath(f'//span[@title="{name}"]')
    user.click()

    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

    for i in range(count):
        msg_box.send_keys(msg)
        btn_send = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
        btn_send.click()

