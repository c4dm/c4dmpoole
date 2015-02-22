

The website is made with a **static site generator** called **Poole**.
Poole is included here inside the "lib" folder, but you'll need to install
its dependencies (i.e. Python and python-markdown)
in order to refresh the content.
You do NOT need to install Poole on the webserver. However, we do indeed do that
since we run a cron script to automatically refresh the website.
Here's how that works:

* Wherever the web content is kept, let's call it `/path/to/www`
* We check out the git repository as a SUBfolder of that, `/path/to/www/sitecontent`
* We install a cron command to invoke `/path/to/www/sitecontent/scripts/cronscript` on a regular basis. This simply pulls the latest content in.
* We install a *git hook* to invoke `/path/to/www/sitecontent/scripts/git-hook-post-merge so that whenever there's new content, it will render the site and copy new things into the PARENT folder. This process might seem a bit confusing but here's what happens: Poole takes the content in the `input` subfolder and processes it into `output`. Then we copy everything from `output` into the "main" site folder. This means that we can automatically overwrite refreshed files, and also it means that in case of error the site doesn't disappear, and also it means that we can maintain some big media files etc outside of Poole.


