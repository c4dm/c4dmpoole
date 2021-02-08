
The c4dm site is automated as follows:

1. We maintain the code in the github repository (markdown files, with a static site generator whose name is Poole)
2. There's a cron job in my personal user account which simply does a "git pull" regularly (you can see it in the github at scripts/cronscript)
3. There's a git "hook" in my local checkout which executes whenever the website changes: it runs the site generator, then copies the resulting output into the folder /import/elecpublicdept/legacysites/digitalmusic/ (you can see this hook at scripts/git-hook-post-merge)
    (I notice it hardcodes python 2.7, probably because of the Poole codebase. This hardcoded python versioning could be a source of breakage) 


Here's how you can render the site manually on your own computer:

	./lib/poole/poole.py --build

For install info see [INSTALL.md](INSTALL.md).

To view the website locally use

	./lib/poole/poole.py --serve

and browse to [http://localhost:8080](http://localhost:8080)


### Editing publications

We store publications data as BibTeX in the folder `input/publications_bibtex`. Since our server doesn't have the `bibtex2html` command we manually create the corresponding HTML files using a linux shell command like this:

	cd input
	for year in 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017; do
		bibtex2html -nodoc -dl -a -noabstract -nokeywords -o pubs${year}_raw publications_bibtex/pubs${year}.bib;
	done

Then store the generated HTML files back into the git repository.
