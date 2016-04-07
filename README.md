Here's how I render the site:

	./lib/poole/poole.py --build --base-url /sketch/

or

	./lib/poole/poole.py --build


For install info see [INSTALL.md](INSTALL.md).

To view the website locally use

	./lib/poole/poole.py --serve

and browse to [http://localhost:8080](http://localhost:8080)


##Editing publications

We store publications data as BibTeX in the folder `input/publications_bibtex`. Since our server doesn't have the `bibtex2html` command we manually create the corresponding HTML files using a linux shell command like this:

	cd input
	for year in 2008 2009 2010 2011 2012 2013 2014 2015 2016; do
		bibtex2html -nodoc -dl -a -noabstract -nokeywords -o pubs${year}_raw publications_bibtex/pubs${year}.bib;
	done

Then store the generated HTML files back into the git repository.
