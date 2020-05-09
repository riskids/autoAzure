from selenium import webdriver 
from time import sleep 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import colorama
from colorama import Fore, Style
from colorama import init
init()

usr = "emailmu"
pwd = "passwordmu"

vm_name8 = ["r1","r2","r3","r4","r5","r6","r7","r8","r9","r10","r11","r12","r13","r14"]
vm_name2 = ["mini1","mini2","mini3","mini4","mini5","mini6","mini7","mini8","mini9","mini10","mini11","mini12","mini13","mini14"]
vm_size2 = ["Standard_F2","Standard_F2s","Standard_F2s_v2"]
vm_size8 = ["Standard_F8","Standard_F8s","Standard_F8s_v2"]
region_isi = ["EastUS","EastUS2","SouthCentralUS","WestUS2","AustraliaEast","NorthEurope","UKSouth","WestEurope","CentralUS","WestUS","EastAsia","JapanEast","KoreaCentral","CanadaCentral"]
delay_get_ip = 200

print(Fore.CYAN+"                          .                   .o.                                                ")
print(Fore.CYAN+"                        .o8                  .888.                                               ")
print(Fore.CYAN+" .oooo.   oooo  oooo  .o888oo  .ooooo.      .8*888.       oooooooo oooo  oooo  oooo d8b  .ooooo. ")
print(Fore.CYAN+"^P  )88b  ^888  ^888    888   d88^ ^88b    .8^ ^888.     d^**7d8P  ^888  ^888  ^888**8P d88^ ^88b")
print(Fore.CYAN+" .oP*888   888   888    888   888   888   .88ooo8888.      .d8P^    888   888   888     888ooo888")
print(Fore.CYAN+"d8(  888   888   888    888 . 888   888  .8^     ^888.   .d8P^  .P  888   888   888     888    .o")
print(Fore.CYAN+"*Y888**8o  *V88V*V8P    *888*  Y8bod8P  o88o     o8888o d8888888P   ^V88V*V8P^ d888b    ^Y8bod8P^")
print(Fore.GREEN+"                                                                                 coded by riskids")
print("")
print(Style.RESET_ALL)
print("Mulai dari vm keberapa bos? ")
inputanvm = int(input())
i = inputanvm - 1

sleep(1)
print("Berapa Core Bos?")
print("1. Dual Core")
print("2. Hexa Core")
sleep(1)
tanyacore = int(input())

if tanyacore == 1:
    vmSize = vm_size2
    vmName = vm_name2
    print("membuat vm dual core")
else:
    vmSize = vm_size8
    vmName = vm_name8
    print("membuat vm hexa core")

driver = webdriver.Firefox(executable_path='c:\\Python38\\geckodriver') 
driver.get('https://portal.azure.com') 
print ("Opened Azure....") 

username_box = driver.find_element_by_id('i0116') 
username_box.send_keys(usr) 
print ("Email Id entered") 
next_button = driver.find_element_by_id('idSIButton9') 
next_button.click() 
sleep(7) 

#mengisi password
password_box = driver.find_element_by_id('i0118') 
password_box.send_keys(pwd) 
print ("Password entered") 

sleep(2)
#klik login
login_button = driver.find_element_by_id('idSIButton9')
login_button.click()

def createVM(urutan, vm_name, vm_size, region_isi, delay_get_ip):
    F_vmName = vm_name
    F_vm_size = vm_size

    sleep(7) 
    driver.get('https://portal.azure.com/#create/Microsoft.Template')

    #klik create vm template
    sleep(7)
    actions = ActionChains(driver) 
    actions.send_keys(Keys.TAB * 2)
    actions.send_keys(Keys.ENTER)
    actions.perform()

    #mengisi form vm template
    sleep(6)
    actions2 = ActionChains(driver) 
    actions2.send_keys(Keys.TAB * 2)
    actions2.perform()

    sleep(1)
    actions3 = ActionChains(driver) 
    actions3.send_keys(Keys.TAB * 3)
    actions3.perform()

    sleep(2)
    actions4 = ActionChains(driver) 
    actions4.send_keys(Keys.ARROW_DOWN * 2)
    actions4.send_keys(Keys.ENTER)
    actions4.perform()
    print("memlih resource grup...")

    sleep(2)
    actions5 = ActionChains(driver) 
    actions5.send_keys(Keys.TAB * 2)
    actions5.send_keys(F_vmName[urutan])
    actions5.perform()
    print("memasukan nama vm")

    sleep(2)
    actions6 = ActionChains(driver) 
    actions6.send_keys(Keys.TAB)
    actions6.send_keys("roots")
    actions6.perform() 
    print("memasukan username")

    sleep(2)
    actions7 = ActionChains(driver) 
    actions7.send_keys(Keys.TAB  * 2)
    actions7.send_keys("pepengkolan1!")
    actions7.perform()
    print("memeasukan password...") 

    sleep(2)
    actions8 = ActionChains(driver) 
    actions8.send_keys(Keys.TAB  * 3)
    actions8.send_keys(region_isi)
    actions8.perform()
    print("memilih lokasi server...") 

    sleep(2)
    actions8 = ActionChains(driver) 
    actions8.send_keys(Keys.TAB)
    actions8.send_keys(F_vm_size[0])
    actions8.perform()
    print("memilih size server...") 

    sleep(1)
    actions9 = ActionChains(driver) 
    actions9.send_keys(Keys.TAB)
    actions9.send_keys("vNet"+F_vmName[urutan])
    actions9.perform()

    sleep(1)
    actions9 = ActionChains(driver) 
    actions9.send_keys(Keys.TAB*2)
    actions9.send_keys(F_vmName[urutan]+"-sgn")
    actions9.perform()

    sleep(1)
    actions10 = ActionChains(driver) 
    actions10.send_keys(Keys.TAB*3)
    actions10.perform()

    sleep(1)
    actions11 = ActionChains(driver) 
    actions11.send_keys(Keys.TAB*2)
    actions11.perform()

    #menclik tombol agree
    sleep(1)
    actions12 = ActionChains(driver) 
    actions12.send_keys(Keys.TAB*2)
    actions12.perform()
    sleep(1)
    centang_agree = driver.switch_to.active_element
    centang_agree.click()
    print("berhasil agree!")

    #submitting
    sleep(1)
    actions12b = ActionChains(driver) 
    actions12b.send_keys(Keys.TAB)
    actions12b.send_keys(Keys.ENTER)
    actions12b.perform()
    sleep(1)
    print("berhasil submitting....")

    #pengulangan pengecekan vm size, available atau tidak
    vm_i = 1
    while True:
        try:
            #mencari simbol error, jika tidak ada, menjalankan exeption
            sleep(7)
            warning = driver.find_element_by_id('FxSymbol0-01c')

            print("ditemukan simbol tidak valid! perlu revisi....")
            #jika ada simbol eror, revisi vm size menjadi f2s
            sleep(2)
            revisi = driver.find_element_by_xpath("//label[contains(.//text(), 'Vm Size')]")
            revisi.click()
            rivisi_tab = driver.switch_to.active_element
            sleep(1)
            rivisi_tab.send_keys(F_vm_size[vm_i])
            print("mengganti vm dengan "+F_vm_size[vm_i])
            
            #submitting
            sleep(2)
            submit = driver.find_element_by_xpath("//span[contains(.//text(), 'Purchase')]")
            submit.click()
            print("berhasil submitting....")
            vm_i += 1
            continue
        except NoSuchElementException:
            #jika tidak ada simbol error, menjalan kan ini
            print("buat vm berhasil! menunggu deploy...")
            break

    sleep(delay_get_ip)
    #mengambil ip vm
    driver.get('https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Compute%2FVirtualMachines')
    sleep(15)
    vm_jadi = driver.find_element_by_xpath("//a[@class='fxc-gcflink-link'][contains(.//text(), '"+F_vmName[urutan]+"')]")
    vm_jadi.click()
    sleep(10)
    klik_ip = driver.find_element_by_xpath("//label[contains(.//text(), 'Public IP address')]")
    klik_ip.click()
    sleep(1)
    actions15 = ActionChains(driver) 
    actions15.send_keys(Keys.TAB)
    actions15.perform()

    sleep(1)
    ip = driver.switch_to.active_element.text 

    with open('ip.txt', 'a+') as filehandle:
            filehandle.write('%s ' + F_vmName[urutan] + '\n' % ip)
    print("menyimpan ip dalam text "+ip)


################################ perintah utama ##########################

total_region = len(region_isi)
while i <= total_region:
    #urutan(integer), vmName[array], vm_size[array], region_isi(integer array), delay_get_ip(integer)
    createVM(i,vmName,vmSize,region_isi[i],delay_get_ip)
    i += 1

