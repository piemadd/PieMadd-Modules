@app.errorhandler(400)
def error_bad_request(e):
	global siteName
	fancyLog("Bad Request", "Error", "templates/error.html", 400)
	return render_template('error.html', siteName=siteName, code = "400", message = "Bad Request")

@app.errorhandler(401)
def error_unauthorized(e):
	global siteName
	fancyLog("Unauthorized", "Error", "templates/error.html", 401)
	return render_template('error.html', siteName=siteName, code = "401", message = "Unauthorized")

@app.errorhandler(403)
def error_forbidden(e):
	global siteName
	fancyLog("Forbidden", "Error", "templates/error.html", 403)
	return render_template('error.html', siteName=siteName, code = "403", message = "Forbidden")

@app.errorhandler(404)
def error_page_not_found(e):
	global siteName
	fancyLog("Page not Found", "Error", "templates/error.html", 404)
	return render_template('error.html', siteName=siteName, code = "404", message = "Page not Found")

@app.errorhandler(409)
def error_conflict(e):
	global siteName
	fancyLog("Conflict", "Error", "templates/error.html", 409)
	return render_template('error.html', siteName=siteName, code = "409", message = "Conflict")

@app.errorhandler(501)
def error_internal_server_error(e):
	global siteName
	fancyLog("Internal Server Error", "Error", "templates/error.html", 501)
	return render_template('error.html', siteName=siteName, code = "500", message = "Internal Server Error")

@app.errorhandler(501)
def error_not_implemented(e):
	global siteName
	fancyLog("Not Implemented", "Error", "templates/error.html", 501)
	return render_template('error.html', siteName=siteName, code = "501", message = "Not Implemented")

@app.errorhandler(502)
def error_bad_gateway(e):
	global siteName
	fancyLog("Bad Gateway", "Error", "templates/error.html", 502)
	return render_template('error.html', siteName=siteName, code = "502", message = "Bad Gateway")