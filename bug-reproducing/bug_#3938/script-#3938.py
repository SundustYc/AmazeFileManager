import uiautomator2 as u2

d = u2.connect('7d5caacf') # connect to device
d.xpath('//*[@resource-id="com.amaze.filemanager.debug:id/listView"]/android.widget.RelativeLayout[7]').click()
d.xpath('//android.widget.RelativeLayout').click()
d.xpath('//*[@resource-id="com.amaze.filemanager.debug:id/listView"]/android.widget.RelativeLayout[2]/android.widget.ImageButton[1]').click()
d.xpath('//android.widget.ListView/android.widget.LinearLayout[2]').click()
d(resourceId="com.amaze.filemanager.debug:id/pathbar").click()
d(resourceId="com.amaze.filemanager.debug:id/properties").click()
d.xpath('//android.widget.ListView/android.widget.LinearLayout[4]').click()
d.click(0.118, 0.791)
d(resourceId="com.amaze.filemanager.debug:id/md_buttonDefaultPositive").click()
d.xpath('//*[@resource-id="com.amaze.filemanager.debug:id/scroll1"]/android.widget.LinearLayout[1]').click()
d(text="ATESTFILE").click()
d.xpath('//*[@resource-id="com.amaze.filemanager.debug:id/listView"]/android.widget.RelativeLayout[3]').click()
d(resourceId="com.amaze.filemanager.debug:id/snackBarActionButton").click()
d.xpath('//*[@resource-id="com.amaze.filemanager.debug:id/listView"]/android.widget.RelativeLayout[2]').click()
