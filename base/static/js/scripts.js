/*
  TO-DO:
 
  ao acrescentar item <li> à <ul>, colocá-lo em posicao alfabetica em relacao aos outros
  itens proximos.

  UTIL:

  foo = document.getElementById("#"+k[2]+"-list");
  f =  foo.children;

  for (x in f) {
    c = f[x];
    b = (c.children);
    a = b.item(0).firstChild.data // <- este é o InnerHTML da tag <a>
}


*/

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
	var cookies = document.cookie.split(';');
	for (var i = 0; i < cookies.length; i++) {
	    var cookie = jQuery.trim(cookies[i]);
	    // Does this cookie string begin with the name we want?
	    if (cookie.substring(0, name.length + 1) == (name + '=')) {
		cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
		break;
	    }
	}
    }
    return cookieValue;
}


var csrftoken = getCookie('csrftoken');

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
	xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
});

function create_post() {
    $.ajax({
	url: "/manager/",
	type : "POST",
	data: { name: $("#id_name").val(), url: $("#id_url").val(), category: $("#id_category").val() },
	success : function(json) {
	    j = JSON.stringify(json);
	    k = Object.values(JSON.parse(JSON.parse(j)));

	    $("#id_name").val("");
	    $("#id_url").val("");
	    $("#id_category").val("");

	    $("#"+k[2]+"-list").prepend("<li class=\"resource-item\"><a target=\"_blank\" href=\""+k[1]+"\">"+k[0]+"</a></li>");
	},

	    error: function(xhr, errmsg, err) {
		$("#results").html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>");
		console.log(xhr.status + ": " + xhr.responseText);
	    }
	});
};

$( "#post-form" ).submit(function( event ) {
    event.preventDefault();
    create_post();
});


