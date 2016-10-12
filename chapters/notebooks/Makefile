
localhost:
	PYTHONPATH=~/Developer/working-copies/programming-contests/competitive-programming/python-libs/ jupyter-notebook

presentation-make:
	jupyter-nbconvert presentation-first-year.ipynb --to slides

publish: presentation-make
	cp presentation-first-year.slides.html ~/Developer/working-copies/massimo-nocentini.github.io/PhD/first-year-summary/talk.html

presentation:
	jupyter-nbconvert presentation-first-year.ipynb --to slides --post serve

serve-fatberry.disia.unifi.it:
	PYTHONPATH=../../../programming-contests/competitive-programming/python-libs/ jupyter-notebook --no-browser --port=5900 --ip=150.217.37.116

