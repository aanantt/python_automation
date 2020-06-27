from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Firefox(executable_path="/home/anant/PycharmProjects/script/geckodriver")
driver.get("https://trainings.internshala.com/isp/talk_attendance/?utm_medium=ISP18VISH6263")
print(driver.title)
phone_list = ['9976466052', '9030835640', '9285392789', '9687144252', '9299398823', '8180675800', '9070488466', '8255246403',
         '9687746436', '9744258535', '9953347462', '9340809851', '8195203844', '9027833369', '9362644277', '9673070477',
         '9949763237', '9921536228', '9040559374', '8251415505', '8597689559', '9678352278', '9027923237', '8237073446',
         '9166953067', '9955894535', '9630670335', '8576716783', '9029258152', '9831175344', '9953704702', '8543537810',
         '9175642507', '9955379245', '8896544666', '8839093164', '9878620073', '9039498667', '8555970199', '8549859537',
         '8215176958', '9716567067', '9295505096', '8117304561', '8836007168', '9070244768', '9660073040', '9137647106',
         '9899613671', '9321564371', '9521482602', '8581502351', '8273462328', '9725062200', '9967670594', '8584897481',
         '9735417274', '8237577068', '9531872110', '9586112099', '9223641451', '8551820729', '8840587085', '8258789011',
         '9727974506', '8586761811', '8155576558', '8836613720', '9125446830', '9886653411', '8863943204', '9855005576',
         '8263549416', '9126783218', '9944217205', '9958284140', '9269765330', '9886452069', '8175117082', '9794957572',
         '9822458839', '9118429056', '8583615466', '8812500320', '9351980681', '8277442323', '9025336323', '9334752874',
         '9715349602', '9368554167', '9017871015', '9029070898', '9618492777', '8263588104', '8148240600', '8587912899',
         '9293856807', '9875618297', '9021686070', '9833416345']

last = [
    'sharma', 'singh', 'rajput', 'gupta', 'choudhary', 'kumar', 'madhwal', 'rawat', 'jha', 'kejriwal', 'shah',
    'gambhir', 'kohli', 'pratap', 'jatt', 'jaiswal', 'khatoliya', 'gautam', 'kain', 'meena', 'maurya', 'gupta', 'yadav',
    'samrat', 'chauhan', 'mishra', 'govind', 'doloy', 'bharti', 'idrisi', 'goswami', "senger", 'maheshwari', 'bahuguna',
    'jindal', 'goyal', 'pal', 'shukla', 'maheshwari']

name_list = ['Aaradhya', 'Adah', 'Adhira', 'Alisha', 'Amoli', 'Anaisha', 'Ananya', 'Anika', 'Anushka', 'Asmee', 'Avni',
        'Carina', 'Drishti', 'Hiya', 'Ira', 'Ishana', 'Ishita', 'Kaia', 'Kashvi', 'Keya', 'Kimaya', 'Krisha', 'Larisa',
        'Mahika', 'Mayra', 'Mehar', 'Mirai', 'Mishka', 'Naitee', 'Navya', 'Nehrika', 'Neysa', 'Pavati', 'Prisha',
        'Ryka',
        'Rebecca', 'Saanvi', 'Sahana', 'Sai', 'Saisha', 'Saloni', 'Shanaya', 'Shrishti', 'Sneha', 'Taahira', 'Taara',
        'Tanvi', 'Viti', 'Zara', 'Aahva', 'Aadiv', 'Aarav', 'Akanksh', 'Alex', 'Anant', 'Atiksh', 'Ayaan', 'Bhuv',
        'Dasya',
        'Gian', 'Hem', 'Idhant', 'Ishank', 'Jash', 'Jay', 'Joseph', 'Kabir', 'Kahaan', 'Kairav', 'Kevin', 'Laksh',
        'Luv',
        'Manan', 'Mohammad', 'Naksh', 'Nimit', 'Nirav', 'Pahal', 'Parv', 'Pranay', 'Rachit', 'Raj', 'Ranbir', 'Raunak',
        'Reyansh', 'Rishaan', 'Rishit', 'Rohan', 'Rudra', 'Rushil', 'Sadhil', 'Sarthak', 'Taarush', 'Taksh', 'Ved',
        'Vihaan', 'Vivaan', 'Yash', 'Yug', 'Anant']

email_list = ['aaradhya61@gmail.com', 'adah7@gmail.com', 'adhira915@gmail.com', 'alis70ha6308@gmail.com',
              'amoli96@gmail.com', 'anaisha8@gmail.com', 'ananya478@gmail.com', 'anik70a3586@gmail.com',
              'anushka26@gmail.com', 'asmee9@gmail.com', 'avni876@gmail.com', 'carina706109@gmail.com',
              'drishti61@gmail.com', 'hiya9@gmail.com', 'ira836@gmail.com', 'ishana1700542@gmail.com',
              'ishita92@gmail.com', 'kaia7@gmail.com', 'kashvi0409@gmail.com', 'key70a5670@gmail.com',
              'kimaya35@gmail.com', 'krisha7@gmail.com', 'larisa500@gmail.com', 'mahi70ka7312@gmail.com',
              'mayra23@gmail.com', 'mehar4@gmail.com', 'mirai516@gmail.com', 'mishk70a3912@gmail.com',
              'naitee101@gmail.com', 'navya9@gmail.com', 'nehrik6137@gmail.com', 'ney70sa8589@gmail.com',
              'pavati57@gmail.com', 'prisha8@gmail.com', 'ryka252@gmail.com', 'rebecc70a7749@gmail.com',
              'saanvi101@gmail.com', 'sahana9@gmail.com', 'sai337@gmail.com', 'saisha1700630@gmail.com',
              'saloni104@gmail.com', 'shanaya5@gmail.com', 'shrishi4076@gmail.com', 'sn70eha2552@gmail.com',
              'taahira101@gmail.com', 'taara8@gmail.com', 'tanvi406@gmail.com', 'viti270525@gmail.com',
              'zara40@gmail.com', 'aahva10@gmail.com', 'aadiv723@gmail.com', 'aarav701074@gmail.com',
              'akanksh67@gmail.com', 'alex8@gmail.com', 'anant264@gmail.com', 'atiks70h3145@gmail.com',
              'ayaan9@gmail.com', 'bhuv0@gmail.com', 'dasya0127@gmail.com', 'gia70n5699@gmail.com',
              'hem87@gmail.com', 'idhant5@gmail.com', 'ishank510@gmail.com', 'jash705638@gmail.com',
              'jay18@gmail.com', 'joseph1@gmail.com', 'kabir323@gmail.com', 'kahaa70n4245@gmail.com',
              'kairav26@gmail.com', 'kevin5@gmail.com', 'laksh947@gmail.com', 'luv567030@gmail.com',
              'manan62@gmail.com', 'mohammad23gmail.com', 'naksh241@gmail.com', 'nimit270798@gmail.com',
              'nirav3@gmail.com', 'pahal54gmail.com', 'parv944@gmail.com', 'pranay870729@gmail.com',
              'rachit47@gmail.com', 'raj12gmail.com', 'ranbir1953@gmail.com', 'raun70ak3432@gmail.com',
              'reyansh40@gmail.com', 'rishaan6@gmail.com', 'rishit876@gmail.com', 'roha70n5992@gmail.com',
              'rudra85@gmail.com', 'rushil4@gmail.com', 'sadhil079@gmail.com', 'sart70hak4629@gmail.com',
              'taarush53@gmail.com', 'taksh1@gmail.com', 'ved628@gmail.com', 'vihaan1700315@gmail.com',
              'vivaan55@gmail.com', 'yash@gmail.com', 'yug604@gmail.com', 'anant227078@gmail.com']



wait = WebDriverWait(driver, 15)
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="last_name"]')))
for i in range(2):
    email = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/form/div[1]/input")
    email.send_keys(str(email_list[i]))
    name = driver.find_element_by_xpath('//*[@id="first_name"]')
    name.send_keys(str(name_list[i]))
    last_name = driver.find_element_by_xpath('//*[@id="last_name"]')
    last_name.send_keys(str(last[i]))
    phone = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/form/div[3]/input")
    phone.send_keys(str(phone_list[i]))
    checked = driver.find_element_by_xpath('//*[@id="to_register"]').click()
    time.sleep(2)
    button = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div/form/div[5]/button').click()
    time.sleep(2)
driver.close()

 