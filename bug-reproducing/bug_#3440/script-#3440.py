import uiautomator2 as u2

d = u2.connect('7d5caacf') # connect to device
d.xpath('//*[@resource-id="com.amaze.filemanager.debug:id/listView"]/android.widget.RelativeLayout[7]').click()
d.xpath('//*[@resource-id="com.amaze.filemanager.debug:id/listView"]/android.widget.RelativeLayout[4]').click()
d.xpath('//*[@resource-id="com.amaze.filemanager.debug:id/listView"]/android.widget.RelativeLayout[2]').click()
d(resourceId="com.amaze.filemanager.debug:id/just_once_button").click()