function Request(endpoint)
{
	this.url = "http://127.0.0.1:5000/" + endpoint;
	
	this.xhr = new XMLHttpRequest();
	this.response = false;//Until called

	//Get Request
	this.get = function(endpoint)
	{
		this.xhr.open("GET", this.url+endpoint, false);
		this.xhr.send(this.payload);
		
		var response = this.xhr.responseText;
		this.response = response;
	}

	//Post request
	this.post = function(endpoint)
	{
		this.xhr.open("POST", this.url+endpoint, false);
		this.xhr.send(this.payload.formData);
		
		var response = this.xhr.responseText;
		this.response = response;
	}
	
	//Used in almost all api calls, atleast for token
	this.Payload = function()
	{
		this.formData = new FormData();
		this.add = function(key, value)
		{
			this.formData.append(key, value)
		}
		this.remove = function(key)
		{
			this.formData.delete(key);
		}
		this.init = function(formId)
		{
			var form = document.getElementById(formId);
			this.formData = new FormData(form);
		}
	}
	//Data to send
	this.payload = new this.Payload();
}
function checkDayInput()
{
	var elem = document.getElementById("days");
	var days = document.getElementById("nrOfDays").value;
	days = parseInt(days);
	if(isNaN(days))
	{
		elem.innerHTML = "days";
	}
	else
	{
		if(days == 1)
		{
			elem.innerHTML = "day";
		}
		else
		{
			elem.innerHTML = "days";
		}
	}
}

function start()
{
	var elem = document.getElementById("msgInput");
	elem.focus();
	document.getElementById("form").addEventListener("submit", function(event)
	{
		event.preventDefault();
		console.log("Pressed");
		
		document.getElementById("main").className = "fadeout";
		setTimeout(function()
			{
				document.getElementById("main").className = "faded";
			}, 3000);
	});
	//Init eventlistener
	document.getElementById("nrOfDays").addEventListener("input", checkDayInput);
}