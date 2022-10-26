title: Publications How-To
---

C4DM MEMBERS: here's how to contribute to [the list of C4DM publications](../publications.html):

We store our publications publicly as [Bibtex files](https://github.com/c4dm/c4dmpoole/tree/master/input/publications_bibtex).
Anyone can add publications just by submitting a github Pull Request to edit these files.
(The changes don't go through to the website immediately.)

**Instructions for the website maintainer:**
Here's how to update all of C4DM's publications in bulk.

* Using QMUL Elements, go through each of the main academics of C4DM, using the "impersonate" tool, and exporting their recent publications list as BibTex.
* Concatenate these Bibtex files into one big one. You may also wish to concatenate some previously-existing bib files (e.g. from the git repository).
* Open the file in a program such as JabRef, and run the "Find duplicates" tool. Also run "Resolve duplicate keys" to ensure there are no repeated keys.
* Now, from this merged+deduplicated file, export one year at a time to files named like "pubs2019.bib" in the correct folder inside the git repository. I do this simply by sorting the papers by year, selecting and then exporting the selection.

At this point, the `.bib` files are ready to push. But we also want to export them to HTML. So:

* Run bibtex2html on EACH of these per-year files. Here's the command I use:

         # run this from within the "input" directory
         for year in 2017 2018 2019 2020; do
         /usr/bin/bibtex2html -nodoc -dl -a -noabstract -nokeywords -o pubs${year}_raw publications_bibtex/pubs${year}.bib
         done

* Commit to github, BOTH the original bib files and the HTML files we've produced from them.
* The site-generation script (using "Poole") includes a customised hook that automatically pastes these HTML content into the final rendered site. The hook is defined in `macros.py`. Hopefully you don't need to edit that.

(Note, we currently use a cron job in Dan's account to perform the regular `git pull` on the site. That is what pulls+renders the site onto the public webserver.)
