from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import random
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=options)
scale = [[92,8],[85,75,60,70,50,40],[60,30,8,1,1],[70,65,55,10],[47,30,15,8],[50,30,15,4,1],[10,30,50,10],[60,50,40,30],[70,60,50],[80,60,50,70,5]]
temp = 0
for i in scale:
    pos = temp + 1
    if pos == 2  or pos == 4  or pos == 8 or pos == 9 or pos == 10:
        temp+=1
        continue
    for k in range(1,len(i)):
        scale[temp][k] += scale[temp][k-1]
    temp+=1
i = 0
while i <= 140:
    try:
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSc6kB9VG-cCf9mgzHRe1a2QeDxwtwFW59ZHM0FH-18vqz9kVA/viewform")
        time.sleep(1)
        # Tìm các phần tử con (role="listitem") bên trong danh sách
        list_items = driver.find_elements(By.CLASS_NAME, 'Qr7Oae')
        count = 1
        for item in list_items:
            # answer positive
            # if count == len(list_items):
            #     list_radiogroup = item.find_elements(By.XPATH,".//div[@role = 'radiogroup']")
            #     for it in list_radiogroup:
            #         answers = it.find_elements(By.XPATH,".//div[@role = 'radio']")
            #         random_number = random.randint(1, 100)
            #         for k in range (0,len(scale[count-1])):
            #             if random_number <= scale[count-1][k]:
            #                 answers[k].click()
            #                 count += 1
            #                 break
            # else:
                answers = item.find_elements(By.XPATH,".//div[@role = 'radio' or @role = 'checkbox']")
                role = answers[0].get_attribute("role")
                if role == "checkbox":
                    random_number = random.randint(1, 100)
                    click = False
                    for k in range (0,len(scale[count-1])):
                        if random_number <= scale[count-1][k]:
                            answers[k].click()
                            click = True
                            # time.sleep(0.05)
                    if click == False:
                        random_number = random.randint(0, len(scale[count-1])-1)
                        answers[random_number].click()
                    count += 1
                # print(len(answers))
                else:
                    random_number = random.randint(1, 100)
                    for k in range (0,len(scale[count-1])):
                        if random_number <= scale[count-1][k]:
                            answers[k].click()
                            # time.sleep(0.05)
                            count += 1
                            break 
                
        try:
            driver.find_element(By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div[3]/div/div[1]/div/span").click()
        except:                            
            try:
                driver.find_element(By.XPATH,"/html/body/div/div[3]/form/div[2]/div/div[3]/div/div[1]/div/span").click()
            except Exception as e:
                print(e)
        time.sleep(0.1)
    except Exception as e:
        print(e)
    i+=1
    
    print("Done ", i)
    
