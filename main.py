from selenium import webdriver
import sys
import os

inputs = ["이상균", "20163248", "A1101", "36.7"]

if getattr(sys, "frozen", False):
    driver_path = os.path.join(sys._MEIPASS, "msedgedriver.exe")
    driver = webdriver.Edge(driver_path)
else:
    driver = webdriver.Edge("msedgedriver.exe")

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdka3B7OA0l1aj7H26bPkNynKzHaH2PahuRNdbqGpyEepCX3w/viewform")

export_inputs = driver.find_elements_by_xpath("//input[@class=\"quantumWizTextinputPaperinputInput exportInput\"]")
boxes = driver.find_elements_by_xpath("//div[@class=\"quantumWizTogglePapercheckboxInnerBox exportInnerBox\"]")
label = driver.find_element_by_xpath(
    "//span[@class=\"appsMaterialWizButtonPaperbuttonLabel quantumWizButtonPaperbuttonLabel exportLabel\"]")

chains = webdriver.ActionChains(driver)
for i in range(len(export_inputs)):
    chains = chains.send_keys_to_element(export_inputs[i], inputs[i])
chains = chains.click(boxes[0])
#chains = chains.click(label)
chains.perform()

driver.quit()
