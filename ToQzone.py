# This script will send the latest markdown based blog to the QZone, 
# Update via email. xxxx@qzone.qq.com

# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.

# This script will also read the generate html for pelican, and create the 
# MIME formated letter from the article and send it to xxxxxx@qzone.qq.com

# This script will find the newest markdown based article, then find 
# the corresponding html file, use this html file to generate the email.

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

# Import BeautifulSoup for analyse the html files
from BeautifulSoup import BeautifulSoup
# For Regex Expression
import re
# For make directories
import os

# Using glob to find the latest file in the directory:
import glob
# Recursively walk through the directory
import fnmatch

# Using ini file for protecting the username and password
import ConfigParser

#########################################################################
# Module 0: Read out the configuration informations
#########################################################################
def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

Config = ConfigParser.ConfigParser()
Config.read("/home/qzone/qq.ini")
Name = ConfigSectionMap("SectionOne")['username']
Password = ConfigSectionMap("SectionOne")['password']


#########################################################################
# Module1:  Find the latest article
#########################################################################
### Example
# The first 2 examples are only works for single directory
# newest = max(glob.iglob('*.py'), key=os.path.getctime)
# print max([f for f in os.listdir('.') if f.lower().endswith('.mp3')], key=os.path.getctime)

#print max([f for f in os.listdir('./') if f.lower().endswith('.py')], key=os.path.getctime)
# print newest

### Recursively walk through the directory
#matches = []
#for root, dirnames, filenames in os.walk('./content'):
#    for filename in fnmatch.filter(filenames, '*.md'):
#        matches.append(os.path.join(root, filename))
#
#for item in matches:
#    print item
#    print os.path.getmtime(item)
#    print os.path.getctime(item)

# The oldest file in the tree
def oldest_file_in_tree(rootfolder, extension=".md"):
    return min(
        (os.path.join(dirname, filename)
        for dirname, dirnames, filenames in os.walk(rootfolder)
        for filename in filenames
        if filename.endswith(extension)),
        key=lambda fn: os.stat(fn).st_mtime)

def newest_file_in_tree(rootfolder, extension=".md"):
    return max(
        (os.path.join(dirname, filename)
        for dirname, dirnames, filenames in os.walk(rootfolder)
        for filename in filenames
        if filename.endswith(extension)),
        key=lambda fn: os.stat(fn).st_mtime)

# print oldest_file_in_tree('./content')
# print newest_file_in_tree('./content')

# Get the corresponding html file via md file
def get_html_from_md(mdfile):
    f = open(mdfile, 'r')
    mdfile_content = f.read()
    f.close()
    htmlfile_name_group = re.search('Slug: (.*?)\n', mdfile_content)
    htmlfile_name = htmlfile_name_group.group(0).split(':')[1][1:-1]
    # print htmlfile_name
    #print htmlfile_name.group(0).split(':')[1]
    return './output/' + htmlfile_name + '.html'

# get_html_from_md(newest_file_in_tree('./content'))
whole_html_file = get_html_from_md(newest_file_in_tree('./content'))
print whole_html_file

#########################################################################
# Module2: Use the html file to generate the email
#########################################################################

# Open the files and read it into the cache
# f = open('./shifou.html', 'r')
f = open(whole_html_file, 'r')
htmlContent = f.read()
# Close f after reading
f.close()
# Cook the soup and print it out
htmlSoup = BeautifulSoup(htmlContent)
#print htmlSoup.prettify()
# Get the elements from the Soup

# Letter name
html_title = htmlSoup.title.string

# Get the content from the html
html_div_content = htmlSoup.find("div", {"class" : "entry-content"}).renderContents()
#print html_content
html_pure_content = html_div_content.split("-->")[-1]
#print html_pure_content
# <h3>shifou,woshi zhen de </h3>
#<p>following is the picture<br />
#<img alt="/images/shifou.jpg" src="/images/shifou.jpg" /></p>
# Get the source of the images, store it into image_addr
image_addr=[]
for match in re.finditer('src="(.*?)"', html_pure_content, re.S):
    image_addr.append(match.group(0).split('"')[1])
# List all of the items in image_addr
# for item in image_addr:
#     print item

# Now we have to replace the image url info
count = 0
# Use an iter for doing this
#for match in re.finditer('http://[\w]*.photo.store.qq.com/(.*?)"', qzoneContent, re.S):
# msgText = MIMEText('Important graphic here!<br><img src="cid:image1"><br>Another important graphic here!<br><img src="cid:image2"><br>', 'html')
for match in re.finditer('<img alt=(.*?)/>', html_pure_content, re.S):
    count += 1
    #### Now we have to replace
    html_pure_content = re.sub(r'<img alt=(.*?)/>', '<img src="cid:image' + str(count) + '">', html_pure_content, 1, 2)
# print count
# print html_pure_content

# Base path for image files
# basepath = './'
basedir = './content/'
 
# Define these once; use them twice!
strFrom = '971477@qq.com'
#strTo = ['971477@qzone.qq.com', '971477@qzone.qq.com']
# strTo = ['971477@qq.com', '971477@qq.com']
strTo = '971477@qq.com'
#strSubject = 'Your Important Message'
strSubject = html_title
 
# Create the root message and fill in the from, to, and subject headers
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = strSubject
msgRoot['From'] = strFrom
msgRoot['To'] = ''.join(strTo)
msgRoot.preamble = 'This is a multi-part message in MIME format.'
 
# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)
 
msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)
 
# We reference the image in the IMG SRC attribute by the ID we give it below
# msgText = MIMEText('Important graphic here!<br><img src="cid:image1"><br>Another important graphic here!<br><img src="cid:image2"><br>', 'html')
msgText = MIMEText(html_pure_content, 'html')
msgAlternative.attach(msgText)

# Global variable for storing the msgImages
msgImages = []
# Now we will add the pictures 
count = 0
for item in image_addr:
    #with open(os.path.join(blog_post_directory, webpage_name), 'wb') as temp_file: 
    count += 1
    item = item[1:]
    # print item
    # print os.path.join(basedir, item)
    fp = open(os.path.join(basedir, item), 'rb')
    #fp = open('%s/%s' % basedir, % item, 'rb')
    msgImage_mine = MIMEImage(fp.read())
    fp.close()
    header2 = '<image' + str(count) + '>'
    # print header2
    msgImage_mine.add_header('Content-ID', '<image' + str(count) +'>',) 
    msgRoot.attach(msgImage_mine)
    #msgImages.append(MIMEImage(fp.read()))
    #fp.close()

# Now we add the image's ID as referenced above
#count = 0
#for item in msgImages:
#    count += 1
#    item.add_header('Content-ID', '<image' + str(count) + '>',)
#    msgRoot.attach(item)
 
# print msgText 
# 
 
#########################################################################
# Module 3: For sending out the email via smtp
#########################################################################
# Use the basepath directory to find the gif files
#fp = open('%s/image1.gif' % basepath, 'rb')
#msgImage1 = MIMEImage(fp.read())
#fp.close()
#fp = open('%s/image2.gif' % basepath, 'rb')
#msgImage2 = MIMEImage(fp.read())
#fp.close()
## Define the image's ID as referenced above
#msgImage1.add_header('Content-ID', '<image1>',)
#msgRoot.attach(msgImage1)
#msgImage2.add_header('Content-ID', '<image2>',)
#msgRoot.attach(msgImage2)
 
# Send the email (this example assumes SMTP authentication is required)
### For testing purpose, don't update currently
smtp = smtplib.SMTP('smtp.exmail.qq.com')
smtp.login(Name, Password) 
smtp.sendmail(strFrom, strTo, msgRoot.as_string())
smtp.quit()
