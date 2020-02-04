from flask import Flask, render_template
app = Flask(__name__)

frettir = [[0,"Anakin solves world overpopulation.","Anakins new solution to world overpopulation is showing great reasuts, but some people thing it is to crude","Darth Sidius","anakinCK.jpg"],
		   [1,"Chemtrails.","InfoWars advocates New World Order conspiracy theories, 9/11 conspiracy theories, chemtrails, conspiracy theories involving Bill Gates, supposed covert government weather control programs, claims of rampant domestic false flag operations by the US Government (including 9/11) and the unsupported claim that millions voted illegally in the 2016 US presidential election. Jones frequently uses InfoWars to assert that mass shootings are conspiracies or false flag operations, claims which are often then spread. This has been characterized as Second Amendment fan fiction","alex jones","chemtrails.jpg"],
		   [2,"Jeffrey Epstein didn't kill him self.","On August 10, 2019, American financier and convicted sex offender Jeffrey Epstein was found unresponsive in his Metropolitan Correctional Center jail cell, where he was awaiting trial on new sex trafficking charges.On August 10, 2019, American financier and convicted sex offender Jeffrey Epstein was found unresponsive in his Metropolitan Correctional Center jail cell, where he was awaiting trial on new sex trafficking charges. Epstein's brother, Mark, hired Michael Baden to oversee the autopsy. In late October, Baden announced that autopsy evidence was more indicative of homicidal strangulation than suicidal hanging.","Gloria Borger","jeffreydidnt.jpg"]]

@app.route('/')
def index():
	return '<h1>Verkefni 2</h1> <h4><a href="/lidura">Liður a</a><br> <a href="/lidurb">Liður b</a></h4>'
	

@app.route('/lidura')
def sida1():
	return render_template("lidura.html")

@app.route('/kt/<kt>')
def kt(kt):
	summa = 0
	kennit = []
	for i in kt:
		i = int(i)
		kennit.append(i)
	summa = sum(kennit)
	return "Þversumma kennitölunnar " + kt + " er " + str(summa)

@app.route('/lidurb')
def sida2():
	return render_template("index.html", frettir=frettir)

@app.route('/frett/<int:id>')
def frett(id):
	frett = frettir[id]
	return render_template("frett.html",frett=frett)

if __name__ == "__main__":
	app.run(debug=True)
