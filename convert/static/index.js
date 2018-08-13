document.addEventListener('DOMContentLoaded', () => {

		document.querySelector('#form').onsubmit = () => {

	 			// creating new obj in js. allow to make a ajax or http request for info.
				const request = new XMLHttpRequest();
				const currency = document.querySelector('#currency').value;		// value in input field.
				// initialize a new request.
				request.open('POST', '/convert');	// url path. in app.py line 11.

				request.onload = () => {

						// extract json data found from request.
						const data = JSON.parse(request.responseText);	// result as text
													// ^parsing the text as json obj. like base, value etc.

						if (data.success) {
								const contents = `1 EUR = ${data.rate} ${currency}.`	// contents in result div.
								document.querySelector('#result').innerHTML = contents;	// showing result to html.
							}
							else {
								document.querySelector('#result').innerHTML = 'There was an error. Try again.';
							}
					}

				// add data to send with request.
				const data = new FormData();	// new obj. holds the form data.
				data.append('currency', currency);	// adding to the data, currency.

				// send request.
				request.send(data);
				return false;	// stops the page from reloading.
		};
});
