function verificar() {
    var nome = document.getElementById("nome").value;
    var sexo = document.getElementById("sexo").value;
    var idade = document.getElementById("idade").value;
  
    var resultado = document.getElementById("resultado");
  
    if (sexo === "feminino" && idade < 25) {
      resultado.innerHTML = "Nome: " + nome + "<br>Mensagem: ACEITA";
    } else {
      resultado.innerHTML = "Nome: " + nome + "<br>Mensagem: NÃO ACEITA";
    }
  }
  
  function limpar() {
    document.getElementById("meuFormulario").reset(); 
    document.getElementById("resultado").innerHTML = "";
  }