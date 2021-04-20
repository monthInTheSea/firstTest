from appium import webdriver
desire_cap = {
    "platformName": "Android",
    "deviceName": "127.0.0.1:7555",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".main.view.MainActivity",
    "noReset": True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
driver.implicitly_wait(30)
el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.ViewFlipper/android.widget.LinearLayout/android.widget.TextView")
el1.click()
el1.send_keys("alibaba")
el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]")
el2.click()
