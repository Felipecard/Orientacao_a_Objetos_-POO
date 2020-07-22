
// this = se refere ao objeto em que esta sendo chamado


// Classe
function Pessoa(nome, ida) {
    this.nome = nome;
    this.idade = ida;
}
Pessoa.prototype.mudaridade = function(ida) {
    this.idade = ida;
}

// Objetos
var pessoa1 = new Pessoa('Joao', 25)
var pessoa2 = new Pessoa('Tetulho', 55)

// -----------------------------------------------------------------------

console.log(`Pessoa 1 = ${pessoa1.nome} tem ${pessoa1.idade}`)
console.log(`Pessoa 2 = ${pessoa2.nome} tem ${pessoa2.idade}`)

pessoa1.mudaridade(70);
console.log(`Pessoa 1 = ${pessoa1.nome} tem ${pessoa1.idade}`)
