function validar(field) {
  str = field.value;
  if (str.length > 10) {
    field.value = str.substring(0, str.length - 1);
  }
}
function validarano(field) {
  str = field.value;
  if (str.length > 4) {
    field.value = str.substring(0, str.length - 1);
  }
}
function validarsemestre(field) {
  str = field.value;
  if (str.length > 0) {
    field.value = str.substring(0, str.length - 1);
  }
}
function numerico(evt) {
  var key_code = evt.keyCode ? evt.keyCode : evt.charCode ? evt.charCode : evt.which ? evt.which : void 0;
  if (key_code == 8 || key_code == 9 || key_code == 13 || key_code == 27 || key_code == 46) {
    return true;
  } else if ((key_code >= 35) && (key_code <= 40)) {
    return true
  } else if ((key_code >= 48) && (key_code <= 57)) {
    return true
  }
  return false;
}

function validarano(field) {
  str = field.value;
  if (str.length > 4) {
    field.value = str.substring(0, str.length - 1);
  }
}

function somenteletra(e)
	{
		var expressao;
		expressao = /[a-zA-Z]/;
		if(expressao.test(String.fromCharCode(e.keyCode)))
		{
			return true;
		}
		else
		{
			return false;
		}
	}

  function somenteletraacento(e)
  	{
  		var expressao;
  		expressao = /^[a-zA-ZãÃáÁàÀêÊéÉèÈíÍìÌôÔõÕóÓòÒúÚùÙûÛçÇºª' ']+$/;
  		if(expressao.test(String.fromCharCode(e.keyCode)))
  		{
  			return true;
  		}
  		else
  		{
  			return false;
  		}
  	}
