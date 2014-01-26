# This file will prepare everything for writing a blog.
# Including: Article title, Creat Time, Tags, and prepare the directory


# Import pinyin for translate the chinese title into pinyin
import pinyin
# Import re for regex expression
import re
# Import datetime
import datetime
# Import date and time for writing the create timestamp
from time import gmtime, strftime
# Using main()
import sys
import getopt
# Import os for detecting the directory
import os
# Disable Warnings
import warnings

# ignore all of the warnings
warnings.filterwarnings("ignore")

# function for creating the blog directory and begin to edit: 
def create_blog(article_name):
    ### Get the gm time
    # The result will be like '2014-01-22 11:07:31'
    create_gm_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    # Local time, the same format as gm_time
    create_local_time_orig = datetime.datetime.now()
    # The blog_Date will be Date: 2014-01-22 18:20
    blog_Date = create_local_time_orig.strftime('%Y-%m-%d %H:%M')
    
    #create_local_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    ### Create the directory, according to the create_local_time
    # For example, if the time is 2014-01-22, the directory will be
    blog_Dir = 'content/' + 'posts/' + create_local_time_orig.strftime('%Y') + '/' + create_local_time_orig.strftime('%m') + '/'
    # Detect if we have create the blog_Dir already, if not, create one
    if not os.path.exists(blog_Dir):
        # Not exists, then create this directory
        os.makedirs(blog_Dir)

    ### Analyse the article_name, from chinese to english, thus we could use english for creating the file
    # Markdown: 2014_01_22_XXX.md
    blog_post_name = blog_Date[:10].replace("-", "_") + "_" + re.sub(r'[^\w]', '_', pinyin.get_pinyin(article_name)) + ".md"
    # Notice the - will be replaced for the existing spaces. 
    blog_post_Slug = re.sub(r'[^\w]', '-', pinyin.get_pinyin(article_name))
    # Now we have got the filename, will create this file for writing
    blog_whole_path = os.path.join(blog_Dir, blog_post_name)
    print blog_whole_path
    with open(os.path.join(blog_Dir, blog_post_name), 'wb') as temp_file:
        # Here we will write into the pre-defined template content:
        temp_file.write("Title: " + article_name + "\n")
        temp_file.write("Date: " + blog_Date + "\n")
        temp_file.write("Tags: " + "\n")
        temp_file.write("Category: " + "Qzone" + "\n")
        temp_file.write("Slug: " + blog_post_Slug + "\n")
        temp_file.write("Author: " + "Dash" + "\n")
        temp_file.write("Summary: " + "To fill something here(Default)" + "\n")
        temp_file.write("\n This is the Content of my blogs, writing in Markdown\n")
    # The following will be left to the author to write something. 
    # Now close the temp_file
    temp_file.close()
        


def main():
    # parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)
    # process arguments
    create_blog(args[0])
    for arg in args:
        pass
        # process(arg) # process() is defined elsewhere
        # It will print out all of the arguments. 
        # print arg

if __name__ == "__main__":
    main()
