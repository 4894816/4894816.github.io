1. How to write new article?
python  config_blog.py Your_title

2. How to make html? 
make html

3. How to preview your article?
make serve
then visit http://localhost:8000

4. How to push your pages into github?
Make modifications also available on github:   
```
make github
```

Make your website publish:   
```
make pushgit
```

5. How to push your code into remote code?
git push origin code

6. Prerequisites?    
You should manually install the dependencies for python libs:    

```
$ sudo pip install ghp-import
$ sudo pip install pinyin
$ sudo pip install Markdown
```

In ArchLinux, install pelican via `yaourt -S pelican`.   

7. Branches
Yes there are 3 branches for development:   
* code
* master
* gh-pages

Only the code branch holds the modifications of the code, so make sure you are
under the code branch for writing articles.   

```
$ git pull origin code
$ git push origin code
```
